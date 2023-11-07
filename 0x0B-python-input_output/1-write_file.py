#!/usr/bin/python3
""" These defins a file writing function"""


def write_file(filename="", text=""):
    """Write a string to a utf8 text file.

        Args:
            filename (str): The nmae of the file to write.
            text (str): The text to write to the file.
        Returns:
            The number os characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
