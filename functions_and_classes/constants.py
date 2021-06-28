"""
File: constants.py

This file is the compilation of all the constants that the game uses.
"""

BOSS_NAME = '⊑⟒⍀?'

# TODO: Change the constants later after debugging: enemy possibility, break defense chance
# ======================= POSSIBILITY CONSTANTS ======================= #
FLEE_POSSIBILITY = 3  # constant for flee function based from 1 to an integer for the possibility of the character
# fleeing. 3 is original
NUMBER_OF_MOVES = 10  # used to determine the number of steps possible for the player to do. 10 is original
BREAK_DEFENSE_CHANCE = 2  # constant used in the .do_damage function in which there is a one in an integer possibility
# that an attack can break a defense. 2 is the original

# ====================== CHARACTER STATS CONSTANTS ====================== #
DOUBLE_DAMAGE_LIMIT = 50  # constant to determine the limit that a character can have the double damage percentage
# to prevent godlike skills

# =================== CHARACTER LEVELUP STATS CONSTANTS =================== #
# these are constants to determine the upper limit of the random integer upgrade when a player level up
HEALTH_MAX_UPGRADE_LIMIT = 10  # up to 10 health only per level up
ATTACK_UPGRADE_LIMIT = 10  # up to 10 attack per level up
DOUBLE_DAMAGE_UPGRADE_LIMIT = 1.0  # up to 10% double damage chance per level up
LEECHING_UPGRADE_LIMIT = 5  # up to 5 leech per level up
DEFENSE_UPGRADE_LIMIT = 5  # up to 5 defense per level up
SHIELD_BUBBLE_MAX_UPGRADE_LIMIT = 5  # up to 10 shield bubble per level up

UPGRADE_ROSTER_LIMIT = 6  # constant to determine the number of upgrades that are available for the
# player to upgrade.
NUMBER_OF_UPGRADES_AVAILABLE = 3  # based on the number of stats that the player can upgrade for the level up section
# in which there are only 3 upgrades choices that a player can do each time they level up

# ======================= RANDOM ENEMY CONSTANTS ======================= #
# constants used for the random enemy function
ENEMY_POSSIBILITY = 1  # constant for random_enemy_occurance based from 1 to an integer for the possibility of an enemy
# spawning. each number represents a particular enemy. 3 is original value
RANDOM_ENEMY_INTEGER = 1  # used for DEBUGGING in the random_enemy_occurance. Each integer represents the
# particular enemy to showup. 4 is the original value to represent chaser

DEFORMED_MUTATED_HUMAN = 1  # dedicated number for the monster deformed mutated human
MUTATED_HUMAN = 2  # dedicated number for the monster mutated human
LOST_WANDERER = 3  # dedicated number for the lost wanderer
CHASER = 4  # dedicated number for the chaser

# ======================= TEXT EFFECT CONSTANTS ======================= #
NEXT_TEXT_DURATION = 0.1  # constant used for having a gap in between text that have the typing effect
INPUT_AND_TEXT_EFFECT_DURATION = 0.001  # 0.05 normal speed
HELP_BACKSTORY_NEXT_TEXT = 0.2  # similar with NEXT_TEXT_DURATION difference however is this is used
# Used when the player attacks

# ========================== BANNER CONSTANTS ======================== #
NUMBER_OF_DASHES = 25  # used for the breakers found in the terminal when the user plays
PLAYER_TURN_BANNER = '=' * NUMBER_OF_DASHES + " PLAYER'S TURN " + '=' * NUMBER_OF_DASHES
ENEMY_TURN_BANNER = '=' * NUMBER_OF_DASHES + " ENEMY'S TURN " + '=' * NUMBER_OF_DASHES

PLAYER_DEFEAT_BANNER = '=' * NUMBER_OF_DASHES + " PLAYER DEFEAT " + '=' * NUMBER_OF_DASHES
ENEMY_DEFEAT_BANNER = '=' * NUMBER_OF_DASHES + " ENEMY DEFEAT " + '=' * NUMBER_OF_DASHES

# for leeching effect
LEECH_BANNER = '=' * NUMBER_OF_DASHES + " LEECH EFFECT " + '=' * NUMBER_OF_DASHES

# for double damage effect
DOUBLE_DAMAGE_BANNER = '=' * NUMBER_OF_DASHES + " DOUBLE DAMAGE " + '=' * NUMBER_OF_DASHES

# in the help menu
HELP_END_BANNER = '=' * NUMBER_OF_DASHES + " END OF HELP SECTION " + '=' * NUMBER_OF_DASHES

# in the help command menu
COMMAND_DESCRIPTION_HELP_BANNER = '=' * NUMBER_OF_DASHES + " COMMAND DESCRIPTION " + '=' * NUMBER_OF_DASHES
COMMAND_END_HELP_BANNER = '=' * NUMBER_OF_DASHES + " END OF COMMAND SECTION " + '=' * NUMBER_OF_DASHES

# in the help enemy menu
ENEMY_STATS_BANNER = '=' * NUMBER_OF_DASHES + " ENEMY STATS " + '=' * NUMBER_OF_DASHES
ENEMY_BACK_STORY_BANNER = '=' * NUMBER_OF_DASHES + " BACK STORY " + '=' * NUMBER_OF_DASHES
ENEMY_END_HELP_SECTION = '=' * NUMBER_OF_DASHES + " END OF ENEMY SECTION " + '=' * NUMBER_OF_DASHES