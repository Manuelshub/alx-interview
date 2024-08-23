#!/usr/bin/python3
"""
This module contains a function hat checks for UTF-8 encoding.
"""


def validUTF8(data):
    """
    Checks if the given data is a valid UTF-8 encoded byte sequence.

    Args:
        data (bytes): The input byte sequence to be checked.

    Returns:
        True if the data is a valid UTF-8 encoded byte sequence.
        False otherwise.
    """
    num_bytes = 0
    for byte in data:
        mask = 1 << 7
        if not num_bytes:
            while byte & mask:
                num_bytes += 1
                mask >>= 1
            if not num_bytes:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
        num_bytes -= 1
    return num_bytes == 0
