import os
import re

class Utilities(object):
    @classmethod
    def clean_special_characters(cls, string) -> str:
        """
        The function `clean_special_characters` removes special characters such as
        tabs and newlines from a given string and returns the cleaned string.

        :param cls: The parameter `cls` in the `split_string_to_number_and_text`
        method is a convention in Python to refer to the class itself. It is used
        when defining class methods
        :param string: The `string` parameter is a string that may contain special
        characters such as tabs (`\t`) and newlines (`\n`)
        :return: a string.
        """
        return re.sub('\\t|\\n', '', string).strip()

    @classmethod
    def modify_special_characters(cls, string) -> str:
        """
        The function `modify_special_characters` replaces the special character `\xa0`
        with a space and removes any leading or trailing whitespace from the input
        string.

        :param cls
        :param string: The `string` parameter is a string that may contain special
        characters
        :return: a modified version of the input string with special characters replaced
        by spaces and any leading or trailing whitespace removed.
        """
        return re.sub('\\xa0', ' ', string).strip()

    @classmethod
    def split_string_to_number_and_text(cls, str_val) -> dict:
        """
        The function `split_string_to_number_and_text` takes a string as input and
        returns a dictionary containing the numbers and strings found in the input
        string.

        :param cls
        :param str_val: The `str_val` parameter is a string value that contains a
        combination of numbers and text
        :return: a dictionary with two keys: "nums" and "chars". The value of "nums"
        is a list of numbers extracted from the input string, and the value of
        "chars" is a list of strings extracted from the input string.
        """
        numbers = re.findall(r"([0-9]+)", str_val, re.I)
        strings = re.findall(r"[a-zA-Z]+", str_val, re.I)
        return{
            "nums": numbers,
            "chars": strings
        }
