import click
import json
import os

from workzy.core.workspace import Workspace
from workzy.console import io_workspace


@click.command()
@click.argument("workspace_name")
def create(workspace_name: str) -> None:
    """Create a new workspace with interaction.

    :param workspace_name: the workspace's name created.
    :type workspace_name: str.
    """
    workspace = Workspace(workspace_name)
    try:
        while True:
            basic_usage_help()
            command = input(f"Enter command to run with {workspace.name}: ")

            if len(command.split(" ")) > 1:
                command = transform_string(command)

            workspace.append(command)
            print(f"{command} saved! Ctrl+C to close\n")
    except KeyboardInterrupt:
        if workspace.jobs:
            create_file(workspace)
            print(f"\nTo run it, type `workzy run {workspace.name}`")
        else:
            print(f"\n{workspace.name} is not saved: Empty processes list")


def create_file(workspace: Workspace) -> str:
    """Create a json file to save workspaces config."""
    if os.path.exists(io_workspace.jobs):
        try:
            data = io_workspace.load()
            data[workspace.name] = workspace.jobs
            io_workspace.write(data)
        except (IOError, TypeError) as err:
            print(err)
    else:
        io_workspace.create()
        create_file(workspace)


def transform_string(command_input: str) -> str:
    tag, command = command_input.split(" ")
    tags = ["folder"]
    if tag not in tags:
        return command_input
    return f"xdg-open {command}"


def basic_usage_help() -> None:
    help_message = """
    Open a web page:
        - just type 'browser_name' follows by the url
                Example: (google-chrome http://www.google.com/)

    Open a folder in the default file manager:
        - just type 'folder' follows by the directory
                Example: (folder /home/user/Documents)

    Another commands or programs just enter the name\n
    """
    print(help_message)
