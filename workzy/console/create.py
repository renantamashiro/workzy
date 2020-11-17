import click
import os
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


def create_file(workspace):
    """Create a json file to save workspaces config."""
    jobs_file = ".jobs.json"

    if os.path.exists(jobs_file):    
        try:
            with open(jobs_file, "w") as file:
                temp = {}
                temp[workspace.name] = workspace.jobs
                json.dump(temp, file)
        except (IOError, TypeError) as err:
            print(err)
    else:
        with open(jobs_file, "w+") as file:
           file.close() 
        create_file(workspace)

def transform_string(command: str):
    tag, command = command.split(" ")
    if tag == "web" and not command.startswith("http://www."):
        if command.startswith("http://"):
            command.replace("http://", "http://www.")
            return f"xdg-open {command}"
        else:
            return f"xdg-open http://www.{command}"
    return f"xdg-open {command}"


def basic_usage_help():
    help_message = """
    Open a web page:
        - just type 'web' follows by the url
                Example: (web http://www.google.com/)

    Open a folder in the default file manager:
        - just type 'folder' follows by the directory
                Example: (folder /home/user/Documents)

    Another commands or programs just enter the name\n
    """
    print(help_message)
