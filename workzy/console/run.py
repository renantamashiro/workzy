import os
import json

import click

from workzy.core.workspace import Workspace


@click.command()
@click.argument("workspace_name")
def run(workspace_name: str) -> None:
    """Run all commands associated with the workspace.
    """
    print(f"Loading {workspace_name}...")
    with open(os.getcwd() + "/.jobs.json", "r") as file:
        data = file.read()

    data = json.loads(data)
    workspace = Workspace(workspace_name)
    workspace.jobs = data[workspace_name]
    workspace.initialize()
