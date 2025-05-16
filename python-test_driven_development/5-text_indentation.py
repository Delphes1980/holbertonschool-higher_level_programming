#!/usr/bin/python3
"""
    Module description: module that contains a function
    called text_indentation that prints a text with 2 new lines
    after each of these characters: ., ? and :

    Functions: text_indentation(text):
    prints a text with 2 lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Description: prints a text with 2 lines after each of
    these characters: ., ? and :
    text must be a string
    There should be no space at the beginning or at the end of
    each printed line

    Parameters:
    text: the text to print

    Returns: the text printed

    Raises:
    TypeError if text is not a string
    """

    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text_to_print = ""
    for i in range(len((text))):
        text_to_print += text[i]
        if text[i] in ['.', '?', ':']:
            text_to_print = text_to_print.rstrip().lstrip()
            print(text_to_print, end='\n\n')
            text_to_print = ""
    text_to_print = text_to_print.lstrip()
    print(text_to_print, end='')