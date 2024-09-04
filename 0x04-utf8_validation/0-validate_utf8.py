#!/usr/bin/python3
""" comprises `validUTF8` function """

def validUTF8(data):
    """
    validate UTF-8 data.
    it relies on recognizing the correct patterns
    for starting bytes and continuation bytes in a UTF-8 character.
    Args:
        data - list of integers
    Return:
        True if data is a valid `UTF-8`, False otherwise.
    """
    cont_bytes = 0
    for num in data:
        bin_rep = format(num, '08b')
        if cont_bytes == 0:
            if bin_rep.startswith('0'):
                continue
            elif bin_rep.startswith('11'):
                cont_bytes = 1
            elif bin_rep.startswith('111'):
                           cont_bytes = 2
            elif bin_rep.startswith('1111'):
                           cont_bytes = 3
            else:
                return False
        else:
            if not bin_rep.startswith('10'):
                return False
            cont_bytes -= 1
    return cont_bytes == 0
