from argparse import Namespace
from typing import NamedTuple, NewType


UserArgs = NewType("UserArgs", Namespace)


class UrlInfo(NamedTuple):
    url: str
    code: int
