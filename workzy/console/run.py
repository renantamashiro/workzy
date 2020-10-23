import click

from workzy.core.workspace import Workspace


@click.command()
@click.argument("workspace")
def run(workspace):
    with open("/home/renan/Documents/projects/workzy/.jobs", "r") as file:
        data = file.read()
    data = data[data.find(workspace):]
    data = data[: data.find("\n")]
    data = data.split(",")
    data.remove(workspace)
    job = Workspace(workspace)
    job.jobs = data
    job.initialize()
