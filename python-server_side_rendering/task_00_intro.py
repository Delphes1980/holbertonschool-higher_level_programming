#!/usr/bin/python3
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def generate_invitations(template, attendees):
	""" Generates invitation files for each attendee based on a template
	Args:
		template (str): the template for the invitation
		attendees (list): a list of dictionaries
	"""
	if not isinstance(template, str):
		logging.error('Template must be a string.')
		return

	if not isinstance(attendees, list):
		logging.error('Attendees must be a list of dictionary.')
		return

	if template == "":
		logging.error('Template is empty, no output files generated')
		return

	if attendees == []:
		logging.error('No data provided, no output files generated')
		return

	# Iteration through the list of attendees starting to 1
	for index, attendee in enumerate(attendee, start = 1):
		current_message = template
		# Iteration through the dictionary items
		for key, value in attendee.items():
			placeholder = "{" + key + "}"
			if not value:
				current_message = current_message.replace(placeholder, 'N/A')
				continue
			else:
				current_message = current_message.replace(placeholder, str(value))

			# Write the output in a file
			output_filename = f"output_{index}.txt"
			with open(output_filename, 'w', encoding="utf-8") as f:
				f.write(current_message)
