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
        if num_bytes == 0:
            if byte >> 7 == 0b0:
                continue
            if byte >> 5 == 0b110:
                num_bytes = 1
                continue
            if byte >> 4 == 0b1110:
                num_bytes = 2
                continue
            if byte >> 3 == 0b11110:
                num_bytes = 3
                continue
            return False
        else:
            if byte >> 6 != 0b10:
                return False
            num_bytes -= 1
    return num_bytes == 0
