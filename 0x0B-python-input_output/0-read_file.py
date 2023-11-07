#!/usr/bin/python3
"""These defines a text file reading a function"""


def read_file(filename=""):
    """This prints the content of a UTF-8 text file to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
