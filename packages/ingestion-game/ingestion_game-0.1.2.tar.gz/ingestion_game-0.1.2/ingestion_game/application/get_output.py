from typing import Dict
from typing import List

from ingestion_game.domain import Rules


def get_output(
        rules: Rules,
        results: List[Dict[str, str | int]],
) -> str:
    """
    Get the string output with rules and results from logic.

    :param rules: rules
    :param results: results
    :return: string in CSV format
    """
    result = ",".join([key for key in rules.important_keys.keys()]) + "\n"
    for object in results:
        result += ",".join([str(object[key]) for key in rules.important_keys.keys()]) + "\n"

    return result
