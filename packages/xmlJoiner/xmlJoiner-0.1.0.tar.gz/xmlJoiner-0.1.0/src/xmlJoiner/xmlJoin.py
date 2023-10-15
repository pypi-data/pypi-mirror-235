#! /usr/bin/env python3

import glob
import xml.etree.ElementTree as ET
from pathlib import Path
from sys import exit

import rich_click as click

from rich.progress import Progress


from xmlJoiner.constants import (CONTEXT_SETTINGS, FMODE, MSG, progEpilog,
                                 progrSet)
from xmlJoiner.loginit import logInit
from xmlJoiner.version import version
from rich.console import Console

__version__ = version.full()
click.rich_click.USE_RICH_MARKUP = True
click.rich_click.FOOTER_TEXT = progEpilog
click.rich_click.HEADER_TEXT = f"ESA EDDS XML Telemetry joiner, version [blue]{__version__}[/blue]"


def xmlJoin(files, output: str, verbose: bool, logger, console:Console=None):
    first = None
    with Progress(*progrSet, console=console) as progr:

        task0 = progr.add_task("Processing files", total=len(files))
        for fileName in files:
            message = f"Processing file {fileName}"
            logger.info(message)
            if verbose:
                console.print(
                    f"{MSG.INFO} {message}")
            data = ET.parse(fileName)
            if first is None:
                first = data
            else:
                test = first.find(".//PktRawResponse")
                root = data.getroot()
                for packet in root.iter('PktRawResponseElement'):
                    test.append(packet)
            progr.update(task0, advance=1)
    if first is not None:
        message = f"Writing output file {output}"
        logger.info(message)
        if verbose:
            progr.console.print(f"{MSG.INFO}Writing output file {output}")
        first.write(output)
    # f1.close()


@click.command(context_settings=CONTEXT_SETTINGS,)
@click.argument('files', nargs=-1)
@click.option('-f', '--folder', metavar='FOLDER', help='Folder to scan', default=None)
@click.option('-o', '--output', metavar='FILE', help='Joined XML File', default=None)
@click.option('-s', '--show-list', 'show', is_flag=True, help="Show the list of files and exit.")
@click.option('-l', '--log-file', 'log', metavar='FILE', help="Set the name of the log file", default=None)
@click.option('-v', '--verbose', is_flag=True, help='Enable :point_right: [yellow]verbose mode[/yellow] :point_left:', default=False)
@click.version_option(__version__, '-V', '--version')
def action(files, folder, output, show, log,  verbose):
    """ESA EDDS XML Telemetry joiner """
    from xmlJoiner.console import console
    if len(files) == 0:
        if folder is None:
            console.print(
                f"{MSG.ERROR}must be specified a list of file or a folder\n{' '*len('[ERROR] ')}Run the command xmljoin -h for the help.")
            exit(1)
        else:
            files = sorted(glob.glob(folder+'/*.xml'))
    else:
        files = sorted(files)
    if show:
        console.print('\n'.join(files))
        exit(0)
    if output is None:
        output = 'joinedFile.xml'

    if log is None:
        logger = logInit('default.log', 'xmlJoiner',
                         0, FMODE.APPEND)
    else:
        logger = logInit(log, 'xmlJoiner', 20, FMODE.APPEND)

    xmlJoin(files, output, verbose, logger, console)
    pass


if __name__ == "__main__":
    action()
