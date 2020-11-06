import click
import json

from workzy.core.workspace import Workspace


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
            workspace.append(command)
            print(f"{command} saved! Ctrl+C to close\n")
    except KeyboardInterrupt:
        if workspace.jobs:
            create_file(workspace)
            print(f"\nTo run it, type `workzy run {workspace.name}`")
        else:
            print(f"{workspace.name} is not saved: Empty processes list")


def create_file(workspace):
    """Create a json file to save workspaces config."""
    try:
        with open(".jobs.json", "r") as file:
            data = json.loads(file.read())

        data[workspace.name] = workspace.jobs
        data = json.dumps(data)

        with open(".jobs.json", "w") as file:
            file.write(data)
    except (IOError, TypeError) as err:
        print(err)


def basic_usage_help():
    help_message = """
    Open a web page:
        - just type 'web' follows by the url
                Example: (web www.google.com)

    Open a folder in the default file manager:
        - just type 'folder' follows by the directory
                Example: (folder /home/user/Documents)

    Another commands or programs just enter the name\n
    """
    print(help_message)
