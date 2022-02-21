#!interpreter [optional-arg]
# -*- coding: utf-8 -*-

"""
Complex passworf generator using CPython 3.10.
Author: Arnaud Ralec
"""

import string
import random

from typing import Tuple


SPECIAL_CHARACTERS = ("@", "#", "_", "-", "!", "?", "&")


def get_ratios(size: int) -> Tuple[int, int, int]:
    """Sets a ratio of letters, digits and special caracters.

    Args:
        size (int): Size of the password.

    Returns:
        Tuple[int, int, int]: Ratios.
    """
    letters = int(size / 2)
    schar = digits = int(letters / 4) if letters % 2 == 0 else 1
    return letters, digits, schar


def password_generator(size: int = 12) -> str:
    """Generates a random password that includes capital letter,
    special characters and digits.

    Args:
        size (int, optional): Desired size of the password. Defaults to 10.

    Returns:
        str: _description_
    """
    letters, integers, scharacters = get_ratios(size)
    pwd = [random.choice(string.ascii_uppercase) for _ in range(letters)]
    pwd += [random.choice(string.digits) for _ in range(integers)]
    pwd += [random.choice(SPECIAL_CHARACTERS) for _ in range(scharacters)]
    random.shuffle(pwd)
    return "".join(pwd).lower()


if __name__ == "__main__":
    print(password_generator())
