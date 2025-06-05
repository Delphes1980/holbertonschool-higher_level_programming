#!/usr/bin/python3
"""
This module defines a method that serialize and deserialize using XML
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """ Serializes a Python dictionary into XML and saves it to the given
    filename

    Args:
    dictionary: the dictionary to serialize
    filename: the file to save the XML to
    """
    root = ET.Element("data")
    # Iteration through dictionary items
    for key, value in dictionary.items:
        # Each item is a child element to the root
        # key becomes the tag name of the child element
        # value becomes the text content of the child element
        child = ET.SubElement(root, key)
        # Converts the value to a string
        child.text = str(value)
    # ElementTree object creation from the root element
    tree = ET.ElementTree(root)
    with open(filename, 'wb') as f:  # Writes the XML tree in the filename
        tree.write(f, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """ Reads XML data from a file and returns a deserialized Python
    dictionary

    Args:
    filename: the XML file to read from

    Returns:
    A deserialized Python dictionary
    """
    # Parses the XML file to get the ElementTree object
    tree = ET.parse(filename)
    # Gets the root element from the parsed tree
    root = tree.getroot()
    my_dict = {}
    for child in root:  # Iteration through the child elements of the root
        key = child.tag  # Tag of the XML element is the dictionary key
        value_str = child.text  # Text content of the XML element is the value
        my_dict[key] = value_str
    return my_dict
