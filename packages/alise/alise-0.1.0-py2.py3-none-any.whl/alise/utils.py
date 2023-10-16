# vim: tw=100 foldmethod=indent
# pylint: disable=logging-fstring-interpolation

import binascii
import base64
from alise.logsetup import logger


def base64url_decode(data):
    """Encode base64 encode data"""
    logger.debug(f"Len data: {len(data)}")
    size = len(data) % 4
    if size == 2:
        data += "=="
    elif size == 3:
        data += "="
    elif size != 0:
        raise ValueError("Invalid base64 string")
    logger.debug(f"Len data: {len(data)}")
    return base64.urlsafe_b64decode(data).decode()


def base64_decode(data):
    """Encode base64 encode data"""
    rv = []

    for chunk in data.split("."):
        # logger.debug(F"Len chunk before padding: {len(chunk)}")
        size = len(chunk) % 4
        if size == 2:
            chunk += "=="
        elif size == 3:
            chunk += "="
        elif size != 0:
            raise ValueError("Invalid base64 string")
        # logger.debug(F"Len chunk after padding: {len(chunk)}")
        chunk_dec = ""
        try:
            # logger.info(F"chunk: {chunk}")
            chunk_dec = base64.urlsafe_b64decode(chunk).decode()
            # logger.info(F" dec: {chunk_dec}")
        except binascii.Error:
            # logger.error(f"binascii.Error: {e}")
            pass
        except UnicodeDecodeError:
            chunk_dec = ""
        if chunk_dec:
            rv.append(chunk_dec)

    return rv
