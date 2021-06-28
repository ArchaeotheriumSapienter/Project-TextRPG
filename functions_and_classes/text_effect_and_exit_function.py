"""
File: text_effect_and_exit_function.py
----------------------------------------------------------------------

File that holds the function used to have effects on the text when the user is engaged in the terminal.
It also has functions for system exit as well as delay of text.
"""

import sys  # used for flushing and system exit
import time  # used for sleep method
from functions_and_classes.constants import \
    INPUT_AND_TEXT_EFFECT_DURATION  # constant that is the duration of lag between text


# =========================================================
# TEXT EFFECT FUNCTIONS
# =========================================================

def type_print_effect(text):
    """
    This function takes print strings and change them to have a typing effect with the help of time
    sleep so that it has a delay, much like when someone is typing

    Parameter: text - the inputted text where it would be converted to a typing effect
    """

    for character in text:
        print(character, end='')
        sys.stdout.flush()
        time.sleep(INPUT_AND_TEXT_EFFECT_DURATION)


def input_print_effect(text):
    """
    This function is the same with text_print_effect, the difference is that this is used
    when a user inputs something and a message is prompted

    :param: text - the message with the input from the user
    :return: value - the answer that the user gave to be used by other functions
    """
    for character in text:
        print(character, end='')
        sys.stdout.flush()
        time.sleep(INPUT_AND_TEXT_EFFECT_DURATION)
    value = input()
    return value


def text_delay_via_time_sleep(constant):
    """
    Function used for buffering the text so there is a delay for text effect in the terminal
    :param constant: integer constant to determine how long will the delay be
    """
    time.sleep(constant)


# =========================================================
# SYSTEM FUNCTIONS
# =========================================================

def system_exit():
    """
    Function used to exit the game
    """
    sys.exit()
