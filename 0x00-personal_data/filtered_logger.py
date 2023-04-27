#!/usr/bin/env python3

"""
Module that implements some personal data obfuscation functionality.
"""

import re

from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    A function that a log message which obfuscates personal data.

    Arguments
    ---------
    fields: a list of strings representing all fields to obfuscate
    redaction: a string representing by what the field will be obfuscated
    message: a string representing the log line
    separator: a string representing by which character is separating all
    fields in the log line (message)
    """

    lst = message.split(separator)

    for f in fields:
        for i in range(len(lst)):
            if lst[i].startswith(f):
                subst = f + '=' + redaction
                lst[i] = re.sub(lst[i], '', lst[i])
                lst[i] = subst
    return separator.join(lst)
