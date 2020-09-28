import click

from . import __version__


@click.command()
@click.version_option(version=__version__)
def main():
    """
    Workzy: manage your workspaces easily
    """
    click.echo("Hello, manager!")
