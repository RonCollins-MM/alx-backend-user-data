#!/usr/bin/env python3

"""
Module that implements some personal data obfuscation functionality.
"""

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

    split_mssg = [kv for kv in message.split(separator)]
    for key_val in split_mssg:
        for field in fields:
            if key_val.split('=')[0] == field:
                key = key_val.split('=')[0]
                index = split_mssg.index(key_val)
                split_mssg.remove(key_val)
                split_mssg.insert(index, f'{key}={redaction}')
    return f'{separator}'.join(split_mssg)
