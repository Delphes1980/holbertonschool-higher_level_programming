#!/usr/bin/python3
"""
This module defines a method that serialize and deserialize an objet
using CSV
"""

import csv
import json

def convert_csv_to_json(csv_filename):
    with open(csv_filename, 'r', newline='', encoding='utf-8') as file_csv:
        reader_dict = csv.DictReader(file_csv)
    with open('reader_dict', 'w', encoding='utf-8') as file_json:
        data = json.dumps(file_json)
    if not csv_filename:
        return False
