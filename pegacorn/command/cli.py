import click

from pegacorn import __version__
from pegacorn.main import main


@click.version_option(version=__version__)
@click.command(no_args_is_help=True)
@click.option(
    "-f",
    "--target_file",
    is_flag=False,
    help="target file",
)
def entry_point(target_file):
    """PEGACORN"""
    if target_file:
        main(target_file=target_file)


if __name__ == "__main__":
    entry_point()
