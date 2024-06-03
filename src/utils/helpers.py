import pandas as pd
import matplotlib.pyplot as plt

"""
Contains helper functions used across the project
"""


def read_file(file_path):
    """
    Reads a file and returns its content
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def plot_dataframe_simple(
    dataframe: pd.DataFrame, x: str, y: str, title: str, x_label: str, y_label: str
) -> None:
    """
    Plot a DataFrame using the specified columns and labels
    """
    dataframe.plot(x=x, y=y, title=title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()
