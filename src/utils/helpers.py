"""
Contains helper functions used across the project
"""


def read_file(file_path):
    """
    Reads a file and returns its content
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
