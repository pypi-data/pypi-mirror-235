from typing import List


def read_file(
        path: str,
) -> List[str]:
    """
    Read external file with path and return a list of strings/lines.
    Delete the final "\n" in all lines.

    :param str path: path
    :return: list of lines
    """
    with open(path, "r") as file:
        lines = file.readlines()
    return [line[:-1] for line in lines]
