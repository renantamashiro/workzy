import click
import json

from workzy.console import io_workspace


@click.command()
def show():
    """List all workspaces."""
    data = io_workspace.load()
    print(f"{'WORKSPACE'.ljust(15)}COMMANDS")

    for workspace, commands in data.items():
        commands = ", ".join(commands)
        print(f"{workspace.ljust(15)}{commands}")
