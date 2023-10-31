class BadConnectionError(Exception):
    """When client is unable to connect"""


class CantWriteFile(Exception):
    """When couldn't write to a file"""
