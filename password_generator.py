#!interpreter [optional-arg]
# -*- coding: utf-8 -*-

"""
Complex password generator using CPython 3.10.
Author: Arnaud Ralec
"""

import random
import string
from typing import Tuple

SPECIAL_CHARACTERS = ("@", "#", "_", "-", "!", "?", "&")


class PasswordSizeError(Exception):
    pass


def get_ratios(size: int) -> Tuple[int, int, int]:
    """Sets a ratio of letters, digits and special caracters.

    Args:
        size (int): Size of the password.

    Returns:
        Tuple[int, int, int]: Ratios.
    """
    letters = int(size / 2)
    schars = digits = int(letters / 2)
    return letters, digits, schars


def password_generator(size: int = 12) -> str:
    """Generates a random password that includes capital letter,
    special characters and digits.

    Args:
        size (int, optional): Desired size of the password. Defaults to 10.

    Raises:
        PasswordSizeError: Error occuring when the selected size for
        the password is too short. A valid password must be at least 8
        characters long.

    Returns:
        str: Generated password
    """
    try:
        if size >= 8:
            letters, integers, scharacters = get_ratios(size)
            pwd = [random.choice(string.ascii_uppercase) for _ in range(letters)]
            for i in range(0, random.randint(0, len(pwd))):
                pwd[i] = pwd[i].lower()
            pwd += [random.choice(string.digits) for _ in range(integers)]
            pwd += [random.choice(SPECIAL_CHARACTERS) for _ in range(scharacters)]
            random.shuffle(pwd)
            return "".join(pwd)
        else:
            raise PasswordSizeError
    except PasswordSizeError:
        print("A valid password must contain at least 8 characters.")


if __name__ == "__main__":
    _ = password_generator()
    if _:
        print(_)
