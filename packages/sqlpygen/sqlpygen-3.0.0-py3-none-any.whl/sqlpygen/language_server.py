"""Start a language server."""

import logging
from pathlib import Path

import click
from lsprotocol.types import (
    DidOpenTextDocumentParams,
    DidSaveTextDocumentParams,
    TEXT_DOCUMENT_DID_OPEN,
    TEXT_DOCUMENT_DID_SAVE,
    Diagnostic,
    DiagnosticSeverity,
    Range,
    Position,
)
from pygls.server import LanguageServer
from platformdirs import user_log_dir

from .errors import Error
from .tree_sitter_bindings import get_parser, Parser
from .errors import Error, capture_errors
from .parse_tree import check_parse_errors
from .ast import make_ast, make_concrete_source
from .codegen import sql_test_sqlite3

server = LanguageServer("sqlpygen-server", "v0.1")
parser: Parser | None = None


def error_to_diagnostic(error: Error) -> Diagnostic:
    return Diagnostic(
        range=Range(
            start=Position(error.node.start_point[0], error.node.start_point[1]),
            end=Position(error.node.end_point[0], error.node.end_point[1]),
        ),
        severity=DiagnosticSeverity.Error,
        message=f"{error.type.value}: {error.explanation}",
        source="sqlpygen-server",
    )


@server.feature(TEXT_DOCUMENT_DID_OPEN)
@server.feature(TEXT_DOCUMENT_DID_SAVE)
async def did_open(
    ls: LanguageServer, params: DidOpenTextDocumentParams | DidSaveTextDocumentParams
):
    assert parser is not None
    ls.show_message_log("checking document")

    # Parse the file
    text_doc = ls.workspace.get_document(params.text_document.uri)
    file_bytes = text_doc.source.encode()

    with capture_errors() as errors:
        parse_tree = parser.parse(file_bytes)
        check_parse_errors(parse_tree.root_node)
        if errors:
            diagnostics = [error_to_diagnostic(e) for e in errors]
            ls.publish_diagnostics(params.text_document.uri, diagnostics)
            return

    with capture_errors() as errors:
        source = make_ast(parse_tree.root_node)

        if errors:
            diagnostics = [error_to_diagnostic(e) for e in errors]
            ls.publish_diagnostics(params.text_document.uri, diagnostics)
            return

    source = make_concrete_source(source)

    with capture_errors() as errors:
        sql_test_sqlite3(source, verbose=False)

        if errors:
            diagnostics = [error_to_diagnostic(e) for e in errors]
            ls.publish_diagnostics(params.text_document.uri, diagnostics)
            return

    # If we have no errors, remove all diagnostics
    ls.publish_diagnostics(params.text_document.uri, [])


@click.command()
def language_server_io():
    """Start the language server."""
    global parser

    log_dir = user_log_dir(appname="sqlpygen-language-server")
    log_dir = Path(log_dir)
    log_dir.mkdir(parents=True, exist_ok=True)

    log_file = log_dir / "language-server.log"

    logging.basicConfig(filename=str(log_file), filemode="a", level=logging.INFO)

    parser = get_parser()
    server.start_io()


@click.command()
@click.option(
    "--host", default="127.0.0.1", show_default=True, help="Hostname to bind to."
)
@click.option(
    "--port", default=2087, show_default=True, type=int, help="Port to bind to."
)
def language_server_tcp(host: str, port: int):
    """Start the language server."""
    global parser

    logging.basicConfig(filemode="a", level=logging.INFO)

    parser = get_parser()
    server.start_tcp(host, port)
