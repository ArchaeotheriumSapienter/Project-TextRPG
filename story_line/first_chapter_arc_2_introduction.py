"""
File: first_chapter_arc_1_welcome_message.py
----------------------------------------------------------------------

This is the first story line in which it is a welcome message for the player
"""
from functions_and_classes import constants, text_effect_and_exit_function

# putting the effects into a variable for easier readability
type_print_effect = text_effect_and_exit_function.type_print_effect
input_print_effect = text_effect_and_exit_function.input_print_effect
text_delay_via_time_sleep = text_effect_and_exit_function.text_delay_via_time_sleep


#  TODO: kulang pa dito YUNG WEAPONS LAGYAN MO MAMAYA
def introduction(user_name):
    """
    Opening dialogue with Alicia, the first character that the player saw, she will guide the player to the dojo
    Pre-condition: Player starts the game
    Post-condition: Player has a name and is headed for the dojo
    """
    print('')  # For spacing from the start menu
    type_print_effect("Hey, wake up! Are you okay? Who are you? And what are you doing near my home!\n")
    text_delay_via_time_sleep(constants.NEXT_TEXT_DURATION)
    type_print_effect("Oh my, you have so many bruises! Let me tend your wounds and then let's talk.\n")
    text_delay_via_time_sleep(constants.NEXT_TEXT_DURATION)
    type_print_effect("I'm Alicia by the way, its a good thing I found you here,\n")
    text_delay_via_time_sleep(constants.NEXT_TEXT_DURATION)
    type_print_effect("there isn't any hospitals or clinic here for hundreds of kilometers.\n")
    text_delay_via_time_sleep(constants.NEXT_TEXT_DURATION)
    type_print_effect("The best bet you have right now is me, good thing I have a first aid kit.\n")
    text_delay_via_time_sleep(constants.NEXT_TEXT_DURATION)
    type_print_effect("I forgot to even ask! What's your name?\n")

    text_delay_via_time_sleep(constants.NEXT_TEXT_DURATION)
    type_print_effect("That's a nice name, " + user_name + "\n")
    text_delay_via_time_sleep(constants.NEXT_TEXT_DURATION)
    type_print_effect("There we go, I patched your wounds. The problem now is where would you go?\n")
    text_delay_via_time_sleep(constants.NEXT_TEXT_DURATION)
    type_print_effect("And do you remember how you got here? Or who you are?\n")
    text_delay_via_time_sleep(constants.NEXT_TEXT_DURATION)
    type_print_effect("Hey! What's that in your shoulder, I guess I missed a wound.\n")
    text_delay_via_time_sleep(constants.NEXT_TEXT_DURATION)
    type_print_effect("...\n")
    text_delay_via_time_sleep(constants.NEXT_TEXT_DURATION)
    type_print_effect("You're one of them!!! I can't believe it. How did you wind up here? In the middle of nowhere?\n")
    text_delay_via_time_sleep(constants.NEXT_TEXT_DURATION)
    type_print_effect("You're here to defeat " + constants.BOSS_NAME + "\n")
    text_delay_via_time_sleep(constants.NEXT_TEXT_DURATION)
    type_print_effect("But you can't! You'll get yourself killed!\n")
    text_delay_via_time_sleep(constants.NEXT_TEXT_DURATION)
    type_print_effect("But if you're one of them, I guess you're destined towards that goal? Destiny is so weird\n")
    text_delay_via_time_sleep(constants.NEXT_TEXT_DURATION)
    type_print_effect("I mean, who gets to decide what you should do? Is it the player? I guess not...\n")
    text_delay_via_time_sleep(constants.NEXT_TEXT_DURATION)
    type_print_effect("The player is only looking at the screen right now, just watching our whole conversation.\n")
    text_delay_via_time_sleep(constants.NEXT_TEXT_DURATION)
    type_print_effect("Anyway, since I can see that you're one of them, I believe you can still remember how to "
                      "fight?\n")
    text_delay_via_time_sleep(constants.NEXT_TEXT_DURATION)
    type_print_effect("Or how to use your power? I want to see how you release your power!\n")
    text_delay_via_time_sleep(constants.NEXT_TEXT_DURATION)
    type_print_effect("...\n")
    text_delay_via_time_sleep(constants.NEXT_TEXT_DURATION)
    type_print_effect("Don't you rememeber anything? Come on, just one move!\n")
    text_delay_via_time_sleep(constants.NEXT_TEXT_DURATION)
    type_print_effect("...\n")
    text_delay_via_time_sleep(constants.NEXT_TEXT_DURATION)
    type_print_effect("Oh my, if that's the case, I think you should go to the nearby dojo.\n")
    text_delay_via_time_sleep(constants.NEXT_TEXT_DURATION)
    type_print_effect("The sensei there would help you remember the once you've lost\n")
    text_delay_via_time_sleep(constants.NEXT_TEXT_DURATION)
    type_print_effect("Before you go! I'll give you this to defend yourself.\n")
    text_delay_via_time_sleep(constants.NEXT_TEXT_DURATION)
    type_print_effect("You've acquired a KNIFE.\n")  # TODO: add weapons in the future
    text_delay_via_time_sleep(constants.NEXT_TEXT_DURATION)
    type_print_effect("It's no longer safe ever since we've left Earth.\n")
    text_delay_via_time_sleep(constants.NEXT_TEXT_DURATION)
    type_print_effect("Goodluck out there " + user_name + "\n")
    print('')  # for terminal
