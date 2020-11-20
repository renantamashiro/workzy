import click
import json

from workzy.console import io_workspace


@click.command()
@click.argument("workspace_name")
def remove(workspace_name: str) -> None:
    """Remove a workspace.

    :param workspace_name: the workspace's name created.
    :type workspace_name: str.
    """
    try:
        data = io_workspace.load()
        data.pop(workspace_name)
        data = json.dumps(data, skipkeys=True, indent=2)
        io_workspace.write(data)
    except (IOError, FileNotFoundError) as err:
        print(err)
    else:
        print(f"{workspace_name} removed!")
