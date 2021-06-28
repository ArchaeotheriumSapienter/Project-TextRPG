"""
File: rpgameV3.py
----------------------------------------------------------------------
This is the main file. It contains the story of the game as well as the commands of the player


This is an RPG program where the player can fight various types of enemies. It has its own story line based
from the creator. The enemies also get harder as the player plays.

Milestone:
1. Prompt welcome message - done
2. Input Name - done
2. Finish introduction - done
3. Create character - done
4. Make character move, attack, defend - done
    a. make a set of moves that a player can do:
        - move done
        - attack - done
        - status - done
        - help - done
        - flee - done
        - leech - done
5. Make an enemy - done
6. Random occurence of enemy when player is walking - done
6. Make enemy fight the character - done
7. Do level up - done
8. Make a scripted enemy
9. continue storyline
"""
# character: for the players and enemies
# constants: for the various constants
# text_effect_and_exit_function: for effects

from functions_and_classes import character, text_effect_and_exit_function
from story_line import chapter_1_arc_1_welcome_message

# putting the effects into a variable for easier readability
type_print_effect = text_effect_and_exit_function.type_print_effect
input_print_effect = text_effect_and_exit_function.input_print_effect
text_delay_via_time_sleep = text_effect_and_exit_function.text_delay_via_time_sleep

# putting the storyline function into a variable for easier readability
welcome_message = chapter_1_arc_1_welcome_message.welcome_message

# =========================================================
# MAIN FUNCTION
# =========================================================


def main():
    """
    Main function used to execute the whole program of the rpgameV3
    """
    #  handler for the character parent class and the minimum value of each stats that a character can have
    p = character.Player()

    # name input to get the name of the player
    p.name = input_print_effect('Before we start, what is your name? ')

    # calling all of the common class enemy when the player walks with a one in third chance to encounter them
    # compiled into a dictionary for organization

    common_enemy_dict = {
        'deformed_mutated_human': character.DeformedMutatedHuman(),
        'mutated_human': character.MutatedHuman(),
        'lost_wanderer': character.LostWanderer(),
        'chaser': character.Chaser()
    }

    # the welcome message for the player
    welcome_message(p.name)

    # while loop to accomodate the half done program
    while True:
        #  p.level_up()
        # p.double_damage_and_damage_generator()
        p.player_commands(common_enemy_dict)

    # first_chapter()

# =========================================================
# NO NEED FOR EDITING
# =========================================================


if __name__ == '__main__':
    main()
