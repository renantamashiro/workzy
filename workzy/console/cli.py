import click

from workzy import __version__
from workzy.console.create import create
from workzy.console.run import run


@click.group()
@click.version_option(version=__version__)
def workzy_cli():
    pass


def console():
    workzy_cli.add_command(run, "run")
    workzy_cli.add_command(create, "create")
    workzy_cli()
