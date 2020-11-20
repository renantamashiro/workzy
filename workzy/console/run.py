import os
import json

import click

from workzy.console.create import create_file
from workzy.core.workspace import Workspace
from workzy.console import io_workspace


@click.command()
@click.argument("workspace_name")
def run(workspace_name: str) -> None:
    """Run all commands associated with the workspace."""
    print(f"Loading {workspace_name}...")
    try:
        data = io_workspace.load()
        workspace = Workspace(workspace_name)
        workspace.jobs = data[workspace_name]
        workspace.initialize()
    except FileNotFoundError:
        print("No workspace's file found...\n")
        print(
            "Do you want to create a new workspace? Type `workzy create WORKSPACE_NAME`"
        )
