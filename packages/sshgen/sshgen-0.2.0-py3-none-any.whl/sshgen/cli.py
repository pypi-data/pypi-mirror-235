#!/usr/bin/env python
from typing import Annotated, Optional

import typer

from sshgen import __app_name__, __version__
from sshgen.utils.app import AppUtils
from sshgen.utils.file import FileUtils

app = typer.Typer(no_args_is_help=True)


@app.command('generate')
def generate_hosts_file(hosts_file: Annotated[str, typer.Option('--hosts-file', '-h')] = './hosts.yml',
                        output: Annotated[str, typer.Option('--output', '-o')] = './config') -> None:
    """
    Command to generate SSH configuration file.
    By default, it uses hosts.yml file placed in your working directory and outputs to file named as "config"

    Example usage: sshconf generate -o my_ssh_config
    """

    hosts_file = FileUtils.as_file(file_path=hosts_file)
    output_file = FileUtils.as_file(file_path=output)

    AppUtils(hosts_file, output_file).generate_ssh_config()


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f'{__app_name__} v{__version__}')
        raise typer.Exit()


# noinspection PyUnusedLocal
@app.callback()
def callback(
        version: Annotated[Optional[bool],  # noqa: ARG001, UP007
        typer.Option('-v', '--version', callback=_version_callback, is_eager=True)] = None,
) -> None:
    """
    sshgen generates SSH configuration file based on an Ansible hosts file.
    """
    return


if __name__ == '__main__':
    app()
