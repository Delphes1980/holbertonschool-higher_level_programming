#!/usr/bin/python3
"""
This module defines a method that serialize and deserialize using XML
"""

import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
	data = ET.Element(dictionary)
	for elem in dictionary:
		ET.SubElement(data, elem)
	tree = ET.ElementTree(data)
	with open(filename, 'wb') as f:
		tree.write(f, encoding='utf-8', xml_declaration=True)

def deserialize_from_xml(filename):
	tree.ET.parse(filename)
	root = tree.getroot()
	dict = {}
	for item in root.findall:
		return dict[item]
