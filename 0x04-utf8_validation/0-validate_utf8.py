#!/usr/bin/python3
""" validUTF8` function """


def validUTF8(data):
    """
    validate UTF-8 data.
    it relies on recognizing the correct patterns
    for starting byte and continuation bytes in a UTF-8 character.
    Args:
        data(List[int]) - list of integers representing bytes.
    Return:
        True if data is valid `UTF-8`, False otherwise.
    """
    cont_bytes = 0
    for num in data:
        byte = format(num, "08b")
        if cont_bytes == 0:
            if byte.startswith('0'):
                continue
            elif byte.startswith('110'):
                cont_bytes = 1
            elif byte.startswith('1110'):
                cont_bytes = 2
            elif byte.startswith('11110'):
                cont_bytes = 3
            else:
                return False
        else:
            if not byte.startswith('10'):
                return False
            cont_bytes -= 1
    return cont_bytes == 0
