# Python Imports
import json
# Third-Party Imports
# Project Imports


def read_json_file_as_dict(filepath: str) -> dict:
    with open(filepath, "rb") as json_card_file:
        return json.load(json_card_file)
