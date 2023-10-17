"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following lines in the
``[options.entry_points]`` section in ``setup.cfg``::

    console_scripts =
         fibonacci = thetennisplay.skeleton:run

Then run ``pip install .`` (or ``pip install -e .`` for editable mode)
which will install the command ``fibonacci`` inside your current environment.

Besides console scripts, the header (i.e. until ``_logger``...) of this file can
also be used as template for Python modules.

Note:
    This file can be renamed depending on your needs or safely removed if not needed.

References:
    - https://setuptools.pypa.io/en/latest/userguide/entry_point.html
    - https://pip.pypa.io/en/stable/reference/pip_install
"""
# pylint: disable=unused-argument

import logging
import time
from typing import Dict, List

import chime
import schedule
import typer
from rich import print
from rich.logging import RichHandler
from rich.table import Table
from typing_extensions import Annotated

from thetennisplay import __version__

from .court import Court
from .driver import Driver
from .validators import *

__author__ = "Jay Cho"
__copyright__ = "Jay Cho"
__license__ = "MIT"

_logger = logging.getLogger(__name__)

_app = typer.Typer(
    invoke_without_command=True,
    no_args_is_help=True,
    context_settings={"help_option_names": ["-h", "--help"]},
)


# ---- Python API ----
def setup_logging(verbose: bool):
    """Set logging level"""
    logformat = "[%(name)s]: %(message)s"
    logging.basicConfig(
        level=10 if verbose else 20,
        handlers=[RichHandler()],
        format=logformat,
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    msg = "Set logging level to "
    msg += "DEBUG" if verbose else "INFO"
    _logger.info(msg)


def version_cb(value: bool):
    """Print version of the program"""
    if value:
        print(f"thetennisplay {__version__}")
        raise typer.Exit()


def print_table(data: Dict[str, List[int]]):
    """Print available courts in format"""
    table = Table()
    for keys in list(data.keys()):
        table.add_column(keys)
    if not data:
        return
    max_length = max(len(lst) for lst in data.values())
    for row in range(max_length):
        table.add_row(
            *list(
                map(
                    lambda d: f"{data[d][row]} 시" if row < len(data[d]) else "",
                    list(data.keys()),
                )
            )
        )
    print(table)


def notify(hour, data: Dict[str, List[int]]):
    """Notify users if available courts exist"""
    if not data:
        return
    if hour:
        hours = sum(data.values(), [])
        for h in hours:
            if hour[0] <= h <= hour[1]:
                chime.success()
    else:
        chime.success()


# ---- Shared Options ----
VerboseOption = Annotated[
    bool,
    typer.Option(
        "--verbose",
        "-V",
        callback=setup_logging,
    ),
]

HeadlessOption = Annotated[
    bool,
    typer.Option(
        help="크롬 Headless 모드",
    ),
]


# ---- Commands ----
@_app.command()
def watch(
    date: Annotated[
        str,
        typer.Option(
            "--date",
            "-d",
            help="코트를 사용하실 날짜 (YYYY-MM-DD)",
            callback=validate_date,
        ),
    ],
    court: Annotated[Court, typer.Option("--court", "-c", help="이용 계획중인 코트")],
    username: Annotated[
        str,
        typer.Option(
            "--username",
            help="thetennisplay 이메일",
            envvar="THETENNISPLAY_USERNAME",
            prompt=True,
        ),
    ],
    password: Annotated[
        str,
        typer.Option(
            "--password",
            help="thetennisplay 비밀번호",
            envvar="THETENNISPLAY_PASSWORD",
            prompt=True,
            hide_input=True,
        ),
    ],
    refresh_rate: Annotated[
        int,
        typer.Option(
            "--refresh_rate",
            help="몇초마다 데이터를 갱신할지 (최소 5초)",
            callback=validate_refresh_rate,
        ),
    ] = 60,
    hour: Annotated[
        str,
        typer.Option(
            "--hour",
            help="예약할려는 시간 (ex: 18 또는 15-22)",
            callback=validate_hour,
        ),
    ] = None,
    verbose: VerboseOption = False,
    headless: HeadlessOption = False,
):
    """Fetches data every interval and check if available courts exist"""
    _logger.info("로딩중...")
    driver = Driver(headless=headless, logger=_logger)
    driver.login(username, password)
    driver.pick_court(court)
    available_now = driver.pick_date(date)
    _logger.info("작업을 시작합니다")
    _logger.info("Press Ctrl-C to quit")
    if available_now:

        def fn():
            driver.refresh_available_courts()
            courts = driver.parse_courts()
            notify(hour, courts)
            print_table(courts)

        schedule.every(refresh_rate).seconds.do(fn)
    else:

        def fn():
            driver.refresh_page()
            driver.pick_date(date)
            courts = driver.parse_courts()
            notify(hour, courts)
            print_table(courts)

        schedule.every(refresh_rate).seconds.do(fn)
    while True:
        schedule.run_pending()
        time.sleep(1)


@_app.callback()
def common(
    ctx: typer.Context,
    version: Annotated[
        bool,
        typer.Option(
            "--version",
            "-v",
            help="Display current version",
            callback=version_cb,
            is_eager=True,
        ),
    ] = None,
):
    """Common Argument"""


def run():
    """Run the App"""
    _app()


if __name__ == "__main__":
    run()
