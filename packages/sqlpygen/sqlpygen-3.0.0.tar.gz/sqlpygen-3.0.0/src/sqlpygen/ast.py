"""Create AST from parse_tree."""

import re
from pathlib import Path
from collections import Counter
from typing import Any, Callable, assert_never

import rich
import attrs
import click
from tree_sitter import Node

from .parse_tree import get_parser, make_rich_tree
from .errors import ErrorType, append_error


@attrs.define
class CodeStr:
    text: str
    node: Node

    def __str__(self):
        return self.text

    def __hash__(self):
        return hash(self.text)

    def __eq__(self, other):
        if isinstance(other, CodeStr):
            return self.text == other.text
        elif isinstance(other, str):
            return self.text == other
        else:
            raise TypeError("Invalid type for other")


def check_for_duplicates(
    items: list[Any],
    error_type: ErrorType,
    explanation: Callable[[Any], str],
):
    item_names = Counter(item.name for item in items)
    for name, count in item_names.items():
        if count > 1:
            for item in items:
                if item.name == name:
                    append_error(
                        type=error_type, explanation=explanation(item), node=item.node
                    )


@attrs.define
class Module:
    name: CodeStr
    node: Node


@attrs.define
class Dialect:
    name: CodeStr
    node: Node


@attrs.define
class Type:
    name: CodeStr
    nullable: bool
    node: Node

    def __attrs_post_init__(self):
        if self.name.text not in ["int", "float", "str", "bytes", "bool"]:
            append_error(
                ErrorType.UnknownType,
                f"{self.name.text} is not one of [int, float, str, bytes, bool]",
                self.node,
            )


@attrs.define
class Field:
    name: CodeStr
    type: Type
    node: Node


@attrs.define
class Table:
    name: CodeStr
    fields: list[Field]
    node: Node

    def __attrs_post_init__(self):
        check_for_duplicates(
            self.fields,
            error_type=ErrorType.DuplicateColumn,
            explanation=lambda x: f"Column {x.name} is multiply defined",
        )

        if not self.fields:
            append_error(
                type=ErrorType.EmptyTable,
                explanation=f"Table {self.name} has zero columns",
                node=self.node,
            )


@attrs.define
class AnonTable:
    fields: list[Field]
    node: Node

    def __attrs_post_init__(self):
        check_for_duplicates(
            self.fields,
            error_type=ErrorType.DuplicateColumn,
            explanation=lambda x: f"Column {x.name} is multiply defined",
        )

        if not self.fields:
            append_error(
                type=ErrorType.EmptyTable,
                explanation=f"Anonymous table has zero columns",
                node=self.node,
            )


@attrs.define
class SchemaFn:
    name: CodeStr
    sql: CodeStr
    node: Node


@attrs.define
class ParsedSQL:
    sql_template: str
    vars: list[str]
    node: Node


@attrs.define
class QueryFn:
    name: CodeStr
    params: list[Field]
    return_: CodeStr | AnonTable | None
    sql: ParsedSQL
    node: Node

    def __attrs_post_init__(self):
        check_for_duplicates(
            self.params,
            error_type=ErrorType.DuplicateParam,
            explanation=lambda x: f"Parameter {x.name} is multiply defined",
        )

        params = set(p.name.text for p in self.params)
        vars = set(self.sql.vars)
        if params != vars:
            unused_params = params - vars
            missing_params = vars - params

            explanation = f"Parameter mismatch"
            if unused_params:
                unused_params = ",".join(unused_params)
                explanation += f"\nunused_params={unused_params}"
            if missing_params:
                missing_params = ",".join(missing_params)
                explanation += f"\nmissing_params={missing_params}"

            append_error(
                type=ErrorType.QueryParamVarMismatch,
                explanation=explanation,
                node=self.node,
            )


@attrs.define
class Source:
    modules: list[Module]
    dialects: list[Dialect]
    schemas: list[SchemaFn]
    queries: list[QueryFn]
    tables: list[Table]
    node: Node

    def __attrs_post_init__(self):
        if len(self.modules) == 0:
            append_error(
                ErrorType.NoModule,
                f"No module name specified.",
                self.node,
            )

        for module in self.modules[1:]:
            append_error(
                ErrorType.MultipleModule,
                f"Multiple module statements",
                module.node,
            )

        if len(self.dialects) == 0:
            append_error(
                ErrorType.NoDialect,
                f"No module name specified.",
                self.node,
            )

        for dialect in self.dialects[1:]:
            append_error(
                ErrorType.MultipleDialect,
                f"Multiple dialects statements",
                dialect.node,
            )

        for dialect in self.dialects:
            if dialect.name.text not in ["sqlite3"]:
                append_error(
                    ErrorType.UnknownDialect,
                    f"{dialect.name.text} is not one of [sqlite3]",
                    dialect.node,
                )

        check_for_duplicates(
            self.schemas,
            error_type=ErrorType.DuplicateSchema,
            explanation=lambda x: f"Schema {x.name} is multiply defined",
        )

        check_for_duplicates(
            self.queries,
            error_type=ErrorType.DuplicateQuery,
            explanation=lambda x: f"Query {x.name} is multiply defined",
        )

        check_for_duplicates(
            self.tables,
            error_type=ErrorType.DuplicateTable,
            explanation=lambda x: f"Table {x.name} is multiply defined",
        )


class UnexpectedChildCount(ValueError):
    def __str__(self):
        return "unexpected child count"


class ASTConstructionError(ValueError):
    def __init__(self, node: Node, children: list[Any], e: Exception):
        self.node = node
        self.children = children
        self.e = e

    def __str__(self):
        return f"Failed to construct AST: {str(self.e)}"


def make_parsed_sql(sql: str, node: Node) -> ParsedSQL:
    pattern = r"\$[_a-zA-Z][_a-zA-Z0-9]*"
    pattern = re.compile(pattern)

    vars = set()
    for match in pattern.finditer(sql):
        var = match.group(0).removeprefix("$")
        vars.add(var)

    vars = list(vars)
    sql_template = sql
    for var in vars:
        sql_template = sql_template.replace("$" + var, "{%s}" % var)

    return ParsedSQL(sql_template, vars, node)


def make_ast(node: Node) -> Any:
    children = [make_ast(child) for child in node.named_children]
    children = [c for c in children if c is not None]

    try:
        match node.type:
            case "source_file":
                modules, dialects = [], []
                schemas, queries, tables = [], [], []
                for c in children:
                    match c:
                        case Module():
                            modules.append(c)
                        case Dialect():
                            dialects.append(c)
                        case SchemaFn():
                            schemas.append(c)
                        case QueryFn():
                            queries.append(c)
                        case Table():
                            tables.append(c)
                        case _:
                            # This is for comments
                            pass
                return Source(modules, dialects, schemas, queries, tables, node)
            case "module_stmt":
                (name,) = children
                return Module(name, node)
            case "dialect_stmt":
                (name,) = children
                return Dialect(name, node)
            case "schema_fn":
                name, sql = children
                return SchemaFn(name, sql, node)
            case "query_fn":
                match children:
                    case [name, params, return_, sql]:
                        return QueryFn(name, params, return_, sql, node)
                    case [name, params, sql]:
                        return QueryFn(name, params, None, sql, node)
                    case _:
                        raise UnexpectedChildCount()
            case "table":
                name, fields = children
                return Table(name, fields, node)
            case "fields":
                return children
            case "field":
                name, type = children
                return Field(name, type, node)
            case "nullable_type":
                (name,) = children
                return Type(name, True, node)
            case "non_nullable_type":
                (name,) = children
                return Type(name, False, node)
            case "anon_table":
                (fields,) = children
                return AnonTable(fields, node)
            case "named_table":
                (name,) = children
                return name
            case "return_":
                (ret,) = children
                return ret
            case "query_sql":
                return make_parsed_sql(node.text.decode(), node)
            case "identifier" | "schema_sql":
                return CodeStr(node.text.decode(), node)
            case _:
                return None
    except Exception as e:
        raise ASTConstructionError(node, children, e)


@attrs.define
class ConcreteQueryFn:
    name: CodeStr
    params: list[Field]
    return_: CodeStr | None
    sql: ParsedSQL
    node: Node


def make_concrete_queryfn(query: QueryFn) -> tuple[ConcreteQueryFn, Table | None]:
    match query.return_:
        case None:
            return_ = None
            new_table = None
        case CodeStr():
            return_ = query.return_
            new_table = None
        case AnonTable(fields, node):
            table_name = query.name.text + "__ReturnType"
            table_name = CodeStr(table_name, node)

            return_ = table_name
            new_table = Table(table_name, fields, node)
        case _ as unexpected:
            assert_never(unexpected)

    concrete_query = ConcreteQueryFn(
        name=query.name,
        params=query.params,
        return_=return_,
        sql=query.sql,
        node=query.node,
    )

    return concrete_query, new_table


@attrs.define
class ConcreteSource:
    module: CodeStr
    dialect: CodeStr
    schemas: list[SchemaFn]
    queries: list[ConcreteQueryFn]
    tables: list[Table]
    node: Node

    schemas_dict: dict[str, SchemaFn]
    queries_dict: dict[str, ConcreteQueryFn]
    tables_dict: dict[str, Table]


def make_concrete_source(source: Source) -> ConcreteSource:
    tables = list(source.tables)
    queries = list()
    for query in source.queries:
        concrete_query, new_table = make_concrete_queryfn(query)
        queries.append(concrete_query)
        if new_table is not None:
            tables.append(new_table)

    schemas_dict = {s.name.text: s for s in source.schemas}
    queries_dict = {q.name.text: q for q in queries}
    tables_dict = {t.name.text: t for t in tables}

    return ConcreteSource(
        module=source.modules[0].name,
        dialect=source.dialects[0].name,
        schemas=source.schemas,
        queries=queries,
        tables=tables,
        node=source.node,
        schemas_dict=schemas_dict,
        queries_dict=queries_dict,
        tables_dict=tables_dict,
    )


@click.command()
@click.argument(
    "filename",
    type=click.Path(exists=True, file_okay=True, dir_okay=False, path_type=Path),
)
def print_initial_ast(filename: Path):
    """Print the initial abstract syntax tree."""

    file_bytes = filename.read_bytes()

    parser = get_parser()
    parse_tree = parser.parse(file_bytes)
    if parse_tree.root_node.has_error:
        print("Failed to parse input")
        return 1

    try:
        source = make_ast(parse_tree.root_node)
    except ASTConstructionError as e:
        print(e)
        rich_parse_tree = make_rich_tree(e.node, named_only=False)
        rich.print(rich_parse_tree)
        return
    rich.print(source)


@click.command()
@click.argument(
    "filename",
    type=click.Path(exists=True, file_okay=True, dir_okay=False, path_type=Path),
)
def print_final_ast(filename: Path):
    """Print the final abstract syntax tree."""

    file_bytes = filename.read_bytes()

    parser = get_parser()
    parse_tree = parser.parse(file_bytes)
    if parse_tree.root_node.has_error:
        print("Failed to parse input")
        return 1

    try:
        source = make_ast(parse_tree.root_node)
    except ASTConstructionError as e:
        print(e)
        rich_parse_tree = make_rich_tree(e.node, named_only=False)
        rich.print(rich_parse_tree)
        return

    source = make_concrete_source(source)
    rich.print(source)
