#!/usr/bin/python3
"""
This module defines a function to convert CSV data to JSON format
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """ Converts data from a CSV file to JSON format and write
    it to data.json

    Args:
    csv_filename (str): the path to the input CSV file
    Returns:
    bool: True if the conversion was successful, False otherwise"""
    try:
        data_to_serialize = []
        # Reads the CSV file et appends the data in a list of dictionary
        with open(csv_filename, 'r', newline='', encoding='utf-8') as f_csv:
            reader_dict = csv.DictReader(f_csv)
            for row in reader_dict:
                data_to_serialize.append(row)

        json_output_filename = "data.json"
        # Writes the list of dictionary serialized in JSON in data.json
        with open(json_output_filename, 'w', encoding='utf-8') as file_json:
            json.dump(data_to_serialize, file_json)
            return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
