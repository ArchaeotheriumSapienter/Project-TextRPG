"""
File: chapter_1_arc_1_welcome_message.py
----------------------------------------------------------------------

This is the first story line in which it is a welcome message for the player. Then it goes to the second arc
which is the introduction
"""
from functions_and_classes import constants, text_effect_and_exit_function
from story_line import chapter_1_arc_2_introduction

# putting the effects into a variable for easier readability
type_print_effect = text_effect_and_exit_function.type_print_effect
input_print_effect = text_effect_and_exit_function.input_print_effect
text_delay_via_time_sleep = text_effect_and_exit_function.text_delay_via_time_sleep

# putting the storyline into a variable for easier readability
introduction = chapter_1_arc_2_introduction.introduction


def welcome_message(user_name):
    """
    Welcome message for the user to see and asks the user whether to start the game or not
    Return: user_name
    """
    type_print_effect("Welcome to the Journey.\n")
    text_delay_via_time_sleep(constants.NEXT_TEXT_DURATION)
    type_print_effect('You are an individual that suddenly woke up without any recollection.\n')
    text_delay_via_time_sleep(constants.NEXT_TEXT_DURATION)
    type_print_effect('Now you must understand what happened before you came to this place.\n')
    text_delay_via_time_sleep(constants.NEXT_TEXT_DURATION)

    # Asks the user for an input and the input of the user is turned into a lowercase to clean data
    start_game = input_print_effect('Type y to start or n to end the game ').lower()

    # If argument with the user's choices, if n, it will exit the program, anything other than y or n will
    # be taken as a sign to end the game, and y will prompt to start the introduction function
    while start_game != '':
        if start_game == 'y':
            # starts the game by going into the introduction
            introduction(user_name)

            # to prevent looping of the while loop after introduction
            break

        elif start_game == 'n':
            print('')  # space for terminal
            type_print_effect('Thank you for taking the time to check out my first Python Project.\n')
            text_delay_via_time_sleep(constants.NEXT_TEXT_DURATION)
            type_print_effect('This means a lot to me. Have a great day! :)')

            # ends the code
            text_effect_and_exit_function.system_exit()

        else:
            print('')  # space for terminal
            print('Invalid input. Please press the appropriate letter.')

            # Fencepost solution
            start_game = input_print_effect('Type y to start or n to end the game ').lower()

# def first_chapter():


