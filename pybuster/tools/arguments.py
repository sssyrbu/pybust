import argparse
from .custom_types import UserArgs


def parse_args() -> UserArgs:
    parser = argparse.ArgumentParser(prog="PyBust", description="Find website's hidden directories.")
    parser.add_argument("path", help="Path to the file or directory")
    parser.add_argument("link", help="Link to the website")
    parser.add_argument("-o", "--output", required=False, help="Path to the output file")
    args = parser.parse_args()

    return UserArgs(args)

