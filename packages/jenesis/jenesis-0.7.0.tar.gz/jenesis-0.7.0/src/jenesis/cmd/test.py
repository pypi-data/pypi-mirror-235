import argparse
import os
import pytest
import sys


PROJECT_PATH = os.getcwd()


def run(args: argparse.Namespace):
    pytest_args = sys.argv[sys.argv.index("test") + 1 :]
    pytest.main(pytest_args)


def add_test_command(parser):
    run_cmd = parser.add_parser("test")
    run_cmd.add_argument(
        "-p", "--profile", default=None, help="The profile to use"
    )
    run_cmd.add_argument(
        "args", nargs= "*", help="The args to pass to pytest"
    )
    run_cmd.set_defaults(handler=run)
