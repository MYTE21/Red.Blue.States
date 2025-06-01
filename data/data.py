import json
import platform
from typing import Literal


def get_dataset_path(
    project: str,
    category: Literal["raw", "external", "interim", "processed", "urls"],
    step: str,
    depth: int = 0,
) -> str:
    if depth:
        datasets_file_location = "../" * depth + "data/" + "datasets.json"
    else:
        datasets_file_location = "data/" + "datasets.json"

    with open(datasets_file_location) as file:
        datasets_path = json.load(file)

    device = "mac" if platform.system() == "Darwin" else "win"

    if category == "urls":
        exit_project_station = ""
    else:
        exit_project_station = datasets_path["data"][device]

    enter_data_station = datasets_path["data"][project]

    return exit_project_station + enter_data_station[category][step]


if __name__ == "__main__":
    pass
