"""Helper functions to be used in the Small Programs Section of LS-PY110"""
from json import load
from typing import Callable


def load_messages(path: str) -> dict:
    """Loads a json file from the given path

    :path (string): the filepath to the location of the json file
    :returns (dict): the deserialized json data loaded in a dictionary"""
    with open(path, 'r', encoding="utf-8") as f:
        return load(f)


def get_message_dict(path: str, lang: str = 'en') -> dict:
    """Returns a dictionary with messages in the supported language
    from a given json file.

    :path (string): the path to the json file
    :lang (string): the selected language
    :returns (dict): the messages dictionary loaded in the given language
    """
    message_dict = dict(load_messages(path))
    return message_dict[lang]


def prompt(message: str) -> None:
    """Formats and prints a given message with ==>

    :message (str): the message to format and print
    :returns (NoneType): None
    """
    print(f"==> {message}")


def is_valid_choice(choice: str, valid_choices: list) -> bool:
    """Validates if a given choice (in string format) is in the
    given valid_choices (passed into kwargs).

    :choice (str): the player choice
    :valid_choices (list<int>): a list of valid choices
    :returns (bool): True / False
    """
    return choice in valid_choices


def get_valid_user_input(message: str, valid_choices: list = None,
                         validation_func: Callable = is_valid_choice) -> str:
    """Gets user input, validated by the given validation function.

    :message (str): The message to prompt the user
    :valid_choices (list): the list of valid choices for the validation func
    :validation_func (Callable): the function to validate the user input
    :returns user_input (str): The validated user input string
    """
    prompt(message)
    user_input = input()
    while not validation_func(user_input, valid_choices):
        prompt(f"Invalid entry. {message}")
        user_input = input()
    return user_input
