"""
This module provides functions for creating, reading, and editing JSON files in a specified folder.
"""

import os
import json


def create(folder, jsonfile, template):
    """
    Create a JSON file with the given content in the specified folder.

    Args:
        folder (str): The folder where the JSON file will be created.
        jsonfile (str): The name of the JSON file to be created.
        template (dict): The JSON content to be written to the file.

    Returns:
        None
    """
    jsonfile = str(jsonfile)
    template = dict(template)

    file_path = os.path.join(folder, jsonfile)

    if os.path.exists(file_path):
        print("File already exists.")
        return

    if folder is not None:
        os.makedirs(folder, exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(template, f)
        print("File created.")


def read(folder, jsonfile):
    """
    Read the content of a JSON file in the specified folder.

    Args:
        folder (str): The folder where the JSON file is located.
        jsonfile (str): The name of the JSON file to be read.

    Returns:
        dict: The JSON data read from the file, or None if the file does not exist.
    """
    jsonfile = str(jsonfile)
    file_path = os.path.join(folder, jsonfile)

    if not os.path.exists(file_path):
        print("File does not exist.")
        return None

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def edit(folder, jsonfile, update):
    """
    Edit a JSON file in the specified folder by updating its content with new data.

    Args:
        folder (str): The folder where the JSON file is located.
        jsonfile (str): The name of the JSON file to be edited.
        update (dict): The JSON data to be merged into the existing data.

    Returns:
        None
    """
    update = dict(update)
    file_path = os.path.join(folder, jsonfile)

    if not os.path.exists(file_path):
        print("File does not exist.")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        unloadf = json.load(f)
        unloadf.update(update)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(unloadf, f)
        print("File edited.")
