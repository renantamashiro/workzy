import click

from workzy import __version__
from workzy.console.create import create
from workzy.console.run import run
from workzy.console.remove import remove
from workzy.console.show import show


@click.group()
@click.version_option(version=__version__)
def workzy_cli() -> None:
    """Click group commands for cli."""
    pass


def console() -> None:
    """Function for add commands for workzy_cli and call it."""
    workzy_cli.add_command(run, "run")
    workzy_cli.add_command(create, "create")
    workzy_cli.add_command(remove, "remove")
    workzy_cli.add_command(show, "show")
    workzy_cli()
