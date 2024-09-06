#!/usr/bin/python3
"""
This module contains a function `validUTF8`
to validate if a sequence of bytes represents
a valid UTF-8 encoded data.
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    validate UTF-8 data.
    it relies on recognizing the correct patterns
    for starting byte and continuation bytes in a UTF-8 character.
    Args:
        data(List[int]) - list of integers representing bytes.
    Return:
        True if data is valid `UTF-8`, False otherwise.
    """
    # if not data or not all((type(i) is int) for i in data):
    #     return False # checker didn't like this
    cont_bytes = 0
    for num in data:
        if num > 255 or num < 0:
            return False
        # byte = format(num, "08b")
        byte = bin(num).replace("0b", "").rjust(8, "0")
        if cont_bytes == 0:
            if byte.startswith("0"):
                continue
            elif byte.startswith("110"):
                cont_bytes = 1
            elif byte.startswith("1110"):
                cont_bytes = 2
            elif byte.startswith("11110"):
                cont_bytes = 3
            else:
                return False
        else:
            if not byte.startswith("10"):
                return False
            cont_bytes -= 1
    return cont_bytes == 0
