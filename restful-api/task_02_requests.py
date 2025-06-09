#!/usr/bin/python3
"""
This module defines 2 functions that fetch datas from JSONPlaceholder
"""

import requests
import json
import csv


def fetch_and_print_posts():
    """ A function that fetches all post from JSONPlaceholder. """
    # Send a GET request to the JSONPlaceholder/posts endpoint
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {response.status_code}")
    # If the request was successful, parse the JSON response into a Python
    # list dictionary
    if response.status_code == 200:
        json_data = response.json()
        for i in json_data:
            print(i['title'])  # Print the title field of the current post


def fetch_and_save_posts():
    """ A function that fetches all post from JSONPlaceholder & save
    them to a CSV file"""
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        json_data = response.json()
        # Initialization of a new list to store the restructured data for CSV
        new_list = []
        for i in json_data:
            new_dict = {}  # New dictionary to store the desired fields only
            fields = ['id', 'title', 'body']  # The desired fields
            # Extract the desired fields from the original post
            new_dict['id'] = i['id']
            new_dict['title'] = i['title']
            new_dict['body'] = i['body']
            # Add the restructured dictionary to the list
            new_list.append(new_dict)
        with open('post.csv', 'w', newline='', encoding='utf-8') as f:
            # Create a DictWriter object to write dictionary keys to CSV
            # column headers
            writer_dict = csv.DictWriter(f, fieldnames=fields)
            # Write the header row (column names) to the CSV file
            writer_dict.writeheader()
            # Write all the restructured post data rows to the CSV file
            writer_dict.writerows(new_list)
