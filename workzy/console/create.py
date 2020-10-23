import click

from workzy.core.workspace import Workspace


@click.command()
@click.argument("workspace_name")
def create(workspace_name):
    workspace = Workspace(workspace_name)

    try:
        while True:
            command = input(f"Enter command to run with {workspace.name}")
            workspace.append(command)
            print(f"{command} saved! Ctrl+C to close\n")
    except KeyboardInterrupt:
        print("\n\n")
    finally:
        if workspace.jobs:
            create_file(workspace)
            print(f"\nTo run it, type `workzy run {workspace.name}`")
        else:
            print(f"{workspace.name} is not saved> Empty processes list")


def create_file(workspace):
    try:
        with open(".jobs", "a") as file:
            string = ",".join(workspace.jobs)
            file.write(workspace.name + "," + string + "\n")
    except IOError as err:
        print(err)
