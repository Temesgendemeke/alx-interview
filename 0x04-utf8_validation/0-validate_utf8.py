#!/usr/bin/env python3
"""_summary_"""


def validUTF8(data):
    """_summary_

    Args:
        data (_type_): _description_

    Returns:
        _type_: _description_
    """
    number_of_bytes = 0
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        mask = 1 << 7
        if number_of_bytes == 0:
            while mask & num:
                number_of_bytes += 1
                mask = mask >> 1
            if number_of_bytes == 0:
                continue
            if number_of_bytes == 1 or number_of_bytes > 4:
                return False
        else:
            if not (num & mask1 and not (num & mask2)):
                return False
        number_of_bytes -= 1
    return number_of_bytes == 0
