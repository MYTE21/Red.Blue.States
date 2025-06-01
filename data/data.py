import json
import platform
from typing import Literal


def get_dataset_path(
    project: str,
    category: Literal["raw", "external", "interim", "processed", "urls"],
    step: str,
    depth: int = 0,
) -> str:
    """
    Retrieves the file path to a specific dataset based on project, category, and processing step.

    This function reads a JSON file (`datasets.json`) that contains mappings of dataset locations
    for different projects and environments (Mac or Windows).
    It supports navigating to a parent directory based on a specified depth
    and returning the appropriate dataset path.

    Parameters:
        - project (str): The name of the data project.
        - category (Literal): The stage of the data pipeline.
          Must be one of:
                - "raw": Unprocessed original data.
                - "external": External data sources.
                - "interim": Intermediate cleaned or transformed data.
                - "processed": Final dataset ready for use.
                - "urls": Refers to URLs instead of file paths.
        - step (str): The specific step or sub-category within the chosen category.
        - depth (int, optional): Number of directory levels to go up when locating the datasets.json file.
    Returns:
        - str: The resolved dataset file path or URL based on the provided parameters.
    """
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
