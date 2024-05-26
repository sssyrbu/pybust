from .custom_types import UrlInfo
from .exceptions import CantWriteFile


def write_file(output_file: str, url_info: UrlInfo) -> None:
    try:
        with open(output_file, "a+") as file:
            file.write(f"{url_info.url} >>> {url_info.code}\n")
    except Exception:
        raise CantWriteFile
