# ruff: noqa: D415, UP007, D103
"""CLI interface for kfactory.

Use `sea --help` for more info.
"""
from __future__ import annotations

import typer

from seali import __version__

from .typer.data import data
from .typer.project import project

message = f"GDataSea Command Line and Python API: {__version__}"

app = typer.Typer(help=message)


@app.callback(invoke_without_command=True)
def version_callback(
    version: bool = typer.Option(False, "--version", help="Show version of the CLI")
) -> None:
    """Show the version of the cli."""
    if version:
        print(message)
        raise typer.Exit()


app.add_typer(
    project, name="project", help="Commands to interact with a gdatasea project"
)
app.add_typer(
    data, name="data", help="Commands to interact with a gdatasea device data"
)
