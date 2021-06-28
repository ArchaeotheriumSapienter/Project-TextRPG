"""
File: character.py

This file is the parent class of all the enemies and the player. It has all the functions that each character can do
with their initial stats via __init__ of the class Character. This also has all of the enemy instances as well as
the player commands
"""

import random  # used for the probability of enemies as well as the upgrading of stats and abilities
from functions_and_classes import constants  # used for the various constants such as the probability of
# enemies and text designs like banners
from functions_and_classes import common_enemies
from functions_and_classes import text_effect_and_exit_function  # used for the system exit and text delay

# putting the effects into a variable for easier readability
type_print_effect = text_effect_and_exit_function.type_print_effect
input_print_effect = text_effect_and_exit_function.input_print_effect


# =========================================================
# PARENT CLASS
# =========================================================

class Character:
    """
    Parent Class for all of the stats of each character, as well as the player.
    This also has all the functions that each character can do
    """

    def __init__(self):
        self.name = ''
        self.health = 1
        self.health_max = 1
        self.attack = 10
        self.double_damage = 0
        self.leeching = 0
        self.defense = 0
        self.shield_bubble = 0
        self.shield_bubble_max = 0

        # stats for levelling up to gain your ultimate
        self.ultimate_levelup_bar = 0
        self.ultimate_levelup_bar_per_attack = 0

        # stats for levelling up your character
        self.levelup_bar = 0
        self.levelup_bar_max = 0
        self.levelup_per_defeated_enemy = 0

    def double_damage_and_damage_generator(self):
        """
        This is a function used for getting the percentage that will determine if the damage dealt by the character
        will do a double damage plus the generating damage that the character will do

        :return: damage: so that it will be used by the characters
        """
        # damage of the character
        damage = random.randint(0, self.attack)
        #  print('DEBUGGING: DAMAGE IS ', damage, "OF", self.name)

        # percent chance that the character will get a
        double_damage_chance = random.uniform(0, constants.DOUBLE_DAMAGE_LIMIT)

        # if statement to determine if the player will have a double damage by computing if the double_damage_chance
        # is within the range of the double_damage attribute of the character
        if double_damage_chance <= self.double_damage:
            # the damage is multiplied to two as a double damage
            damage *= 2
            #  print('DEBUGGING: DOUBLE DAMAGE IS', damage)
            print(constants.DOUBLE_DAMAGE_BANNER)
            type_print_effect('DOUBLE DAMAGE HAS BEEN ACTIVATED!\n')
            print('')  # for terminal

        # returns damage to be used by the other functions
        return damage

    def do_damage_with_shield_bubble(self, enemy):
        """
        Function for when the player or enemy attacks, parent function of do_damage_player and do_damage_enemy.
        It first computes the shield bubble of the characters then if the shield bubble pops it will commence to
        the normal kinds of attacks with defense

        :param enemy: To lower the health of the enemy
        :return enemy.health: To be analyzed inside the attack function in an if statement
        """
        # damage of the character
        damage = self.double_damage_and_damage_generator()

        # computes the shield bubble of the enemy to the damage done by the character
        # to update damage to reflect shield bubble if the enemy has one
        damage = damage - enemy.shield_bubble

        # so it will not go negative and enemy shield bubble will increase due to it
        if damage <= 0:
            damage = 0

        # updating shield to input the damage
        enemy.shield_bubble = enemy.shield_bubble - damage

        # if statement if the shield bubble stat is non existent or if the shield bubble has broke
        if enemy.shield_bubble <= 0:
            # sets shield bubble to zero to avoid negative values
            enemy.shield_bubble = 0

            # it will go straight to attacking the character directly
            self.do_damage(enemy, damage)

        # if the shield bubble is still intact
        else:
            # checks the class of the caller for aesthetics
            if self.__class__ == Player:
                # for aesthetics purposes
                print(constants.PLAYER_TURN_BANNER)
            else:
                print(constants.ENEMY_TURN_BANNER)
                # for aesthetics purposes

            # message saying that the shield bubble is still intact
            type_print_effect(enemy.name + "'s Shield Bubble has withstand the attack of " + self.name + ".\n")
            type_print_effect("The remaining Shield Bubble of " + enemy.name + " is "
                              + str(enemy.shield_bubble) + ".\n")
            print('')  # for terminal

        # returns enemy health to be analyzed in an if statement inside the caller in attack function
        return enemy.health

    def do_damage(self, enemy, damage):
        """
        Function when the shield bubble burst, it will attack the health directly

        :param enemy: to determine which will give damage to
        :param damage: amount of damage that will be given
        :return enemy_health: to be analyzed in an if statement in the attack function in the Player class
        """
        # utilizing the defense, one in three chance that the defense will break
        break_defense_chance = random.randint(1, constants.BREAK_DEFENSE_CHANCE)

        # checks to see if the class that called the method is the player
        if self.__class__ == Player:
            # when the player does damage to the enemy, has messages for the terminal
            self.do_damage_player(enemy, damage, break_defense_chance)

        # if the caller are the common enemies
        elif self.__class__ == DeformedMutatedHuman or self.__class__ == MutatedHuman \
                or self.__class__ == LostWanderer or self.__class__ == Chaser:

            # when the enemy attacks, gives messages whether the player died and how many damage the enemy dealt
            self.do_damage_enemy(enemy, damage, break_defense_chance)

        # returns enemy health to be analyzed in an if statement inside the caller in attack function
        return enemy.health

    def do_damage_player(self, enemy, damage, break_defense_chance):
        """
        Subfunction of the do_damage, for cutting down code inside the do_damage function.
        This function gives the messages of damage to the user as the player

        :param enemy: for the enemy to lose health and give name in terminal
        :param damage: to determine damage given to the enemy
        :param break_defense_chance: to determine if the enemy will break its defense
        :return: self.health: so that it will check whether or not the enemy or player will die
        """
        # for aesthetics in terminal
        print(constants.PLAYER_TURN_BANNER)

        # if the defenses break
        if break_defense_chance == 1:
            # when the damage is equals to zero
            if damage == 0:
                type_print_effect(enemy.name + " felt a scratch! " +
                                  self.name + " dealt " + str(damage) + " damage!\n")

            else:
                # enemy losses health with no defense
                enemy.health = enemy.health - damage
                type_print_effect(enemy.name + "'s defense has broken! " +
                                  self.name + " dealt " + str(damage) + " damage!\n")
                type_print_effect("The " + enemy.name + "'s remaining health is " +
                                  str(enemy.health) + "!\n")
                # call upon leeching when there is damage from the enemy
                if self.leeching != 0 and self.health < self.health_max:
                    self.health = self.leeching_health(damage, enemy)

        # if it does not break
        else:
            # if the damage is lower than the defense of the enemy
            if damage <= enemy.defense:
                type_print_effect(enemy.name + " has defended all of your attack!\n")
                type_print_effect("The " + enemy.name + "'s remaining health is " +
                                  str(enemy.health) + "!\n")

            # if the damage exceeds the defense
            else:
                # used when the damage is larger than the defense
                damage_with_defense = damage - enemy.defense

                enemy.health = enemy.health - damage_with_defense

                type_print_effect(enemy.name + " defended a part of " + self.name + " attack!\n")
                type_print_effect(self.name + " dealt " + str(damage) + " damage!\n")
                type_print_effect("The " + enemy.name + "'s remaining health is " +
                                  str(enemy.health) + "!\n")
                # call upon leeching when there is damage from the enemy
                if self.leeching != 0 and self.health < self.health_max:
                    self.health = self.leeching_health(damage, enemy)

        # returns self.health to be used by the do_damage function
        return self.health

    def do_damage_enemy(self, enemy, damage, break_defense_chance):
        """
        Function just like the do_damage_player but it is used instead for the enemy and gives message to the player
        on what damage they dealt and if they defeat the player

        :param enemy: enemy is the player
        :param damage: damage given to the player
        :param break_defense_chance: if the defense of the player broke
        """
        print('')  # space for terminal
        # for aesthetics in terminal
        print(constants.ENEMY_TURN_BANNER)
        # if the defenses break
        if break_defense_chance == 1:
            # when the damage is equals to zero
            if damage == 0:
                type_print_effect(self.name + " barely scratched " +
                                  enemy.name + "!\n")
                type_print_effect(enemy.name + "'s Health is: " + str(enemy.health) + "\n")
                print('')  # space for terminal

            # when the defenses break but there is damage
            else:
                # enemy losses health with no defense
                enemy.health = enemy.health - damage
                type_print_effect(enemy.name + "'s defense has broken! " +
                                  self.name + " dealt " + str(damage) + " damage!\n")
                type_print_effect(enemy.name + "'s remaining health is " +
                                  str(enemy.health) + "!\n")
                print('')  # space for terminal

        # if the defenses did not break
        else:
            # if the damage is lower than the defense of the enemy
            if damage <= enemy.defense:
                type_print_effect(enemy.name + " defended all of " + self.name + " attacks!\n")
                type_print_effect(enemy.name + "'s remaining health is " +
                                  str(enemy.health) + "!\n")
                print('')  # space for terminal

            # if the damage exceeds the defense
            else:
                # damage is subtracted to defense, that is the updated damage
                damage_with_defense = damage - enemy.defense

                # enemy losses health with defense
                enemy.health = enemy.health - damage_with_defense

                type_print_effect(enemy.name + " defended a part of " + self.name + " attack!\n")
                type_print_effect(self.name + " dealt " + str(damage) + " damage!\n")
                type_print_effect(enemy.name + "'s remaining health is " +
                                  str(enemy.health) + "!\n")
                print('')  # space for terminal

    def leeching_health(self, damage, enemy):
        """
        Function for the leeching power in which the damage given by the character is transformed into the
        character's health. But if the leeching is higher than the damage, only the damage is transformed into the
        health

        :param: damage: to determine how much leeching the character will do
        :param: enemy: to determine where the character will get the health from
        :return: self.health: to check if the character will be alive after the attack
        """
        # calculates the missing health to prevent over health in a character
        health_missing = self.health_max - self.health

        # for aesthetics in terminal
        print('')
        print(constants.LEECH_BANNER)

        # executed if the health missing is less than the leech or damage
        if health_missing <= self.leeching <= damage or health_missing <= self.leeching > damage:
            self.health += health_missing
            type_print_effect(self.name + " successfully leeched " + str(health_missing) +
                              " health from " + enemy.name + " and gained full health!\n")
            type_print_effect(self.name + "'s health is currently at " + str(self.health) + ".\n")

        # executed when the health missing is greater than the leech or damage
        elif health_missing > self.leeching <= damage:
            self.health += self.leeching
            type_print_effect(self.name + " leeched " + str(self.leeching) +
                              " health from " + enemy.name + ".\n")
            type_print_effect(self.name + "'s health is currently at " + str(self.health) + ".\n")

        # executed when the health missing is greater than the leech but the leech is greater than the damage
        elif health_missing > self.leeching > damage or self.leeching > damage:
            self.health += damage
            type_print_effect(self.name + " leeched " + str(damage) +
                              " health from " + enemy.name + " with all possible damage given at this round.\n")
            type_print_effect(self.name + "'s health is currently at " + str(self.health) + ".\n")

        return self.health

    def character_death(self, enemy):
        """
        Function that gets two characters and determine if they die. If an enemy dies, the player gains additional stats
        If the player dies, game over

        :param enemy: for the function to get the enemy attributes
        :return self.levelup_bar: used to indicate when the player will level up
        """
        # if the enemy of the instance caller dies
        if enemy.health <= 0:
            # if the enemy dies
            if self.__class__ == Player:
                print('')  # space for terminal
                # for aesthetics in terminal
                print(constants.ENEMY_DEFEAT_BANNER)

                type_print_effect(enemy.name + " has been slain by " + self.name + '!\n')

                #  used to increase the level up bar by counting whenever the player defeats an enemy
                self.levelup_bar += self.levelup_per_defeated_enemy

                return self.levelup_bar

            # when the player dies by various enemies
            else:
                print('')  # space for terminal
                # for aesthetics in terminal
                print(constants.PLAYER_DEFEAT_BANNER)

                type_print_effect(enemy.name + " has been slain by " + self.name + " with no mercy!\n")
                type_print_effect("Game over! Thank you so much for playing The Journey\n")

                # end the game when the player dies
                text_effect_and_exit_function.system_exit()

    def level_up(self):
        """
        Function for the character to level up. It takes a random integer and let the character choose which
        upgrade to get. Parent function of level_up_assigning and level_up_choosing
        """
        # variables to determine the upgradable stats the player can have
        health_upgrade = random.randint(1, constants.HEALTH_MAX_UPGRADE_LIMIT)
        attack_upgrade = random.randint(1, constants.ATTACK_UPGRADE_LIMIT)

        # for floats
        double_damage_upgrade = random.uniform(0.1, constants.DOUBLE_DAMAGE_UPGRADE_LIMIT)

        leeching_upgrade = random.randint(1, constants.LEECHING_UPGRADE_LIMIT)
        defense_upgrade = random.randint(1, constants.DEFENSE_UPGRADE_LIMIT)
        shield_bubble_upgrade = random.randint(1, constants.SHIELD_BUBBLE_MAX_UPGRADE_LIMIT)

        # dictionary storing all of the upgrade
        player_upgrade = {
            1: health_upgrade,
            2: attack_upgrade,
            3: double_damage_upgrade,
            4: leeching_upgrade,
            5: defense_upgrade,
            6: shield_bubble_upgrade
        }

        # this dictionary will be used for the player to choose which upgrade they want to have
        upgrade_roster_choices = {}

        # this counter is used to check if the limit of how many upgrades presented to the player has been set
        counter = 0

        # key used for the roster of the random upgrades
        key_for_upgrade_roster_choices = (1, 2, 3)

        # while loop determined by the counter to check if the dictionary have the right amount of upgrades available
        # for the player
        while counter < constants.NUMBER_OF_UPGRADES_AVAILABLE:
            # iteration of the tuple variable to be used as keys
            for key in key_for_upgrade_roster_choices:
                # this will determine which upgrade will the player have based on the integers provided. Each integer
                # determines a unique upgrade based on the keys of player_upgrade. they will be the value for the
                # new dict
                upgrade_roster = random.randint(1, 6)

                # puts the value of the upgrade_roster to the empty dictionary
                upgrade_roster_choices[key] = upgrade_roster

                # counter add 1 to stop it when it reaches the limit
                counter += 1

        #  gets the values of the upgrade_roster_choices to be compared to the keys of the player_upgrade
        # to let the character choose which to upgrade
        value_of_roster = list(upgrade_roster_choices.values())

        # calling of the assigning to put the random variables into a new dictionary for the player
        # to ultimately choose in the end
        player_upgrade_choosing_time = self.level_up_assigning(value_of_roster)

        # gets the dictionary of compiled available upgrades and lets the player choose one from them
        self.level_up_choosing(player_upgrade_choosing_time, player_upgrade)

    @staticmethod
    def level_up_assigning(value_of_roster):
        """
        Function that takes the key from the player upgrades and the value from the randomized upgrade and puts it
        on a dictionary for the character to choose from. Subclass of level_up

        :param value_of_roster: value from the randomized player upgrades
        :return: player_upgrade_choosing_time: dictionary to let the player choose what they want ot upgrade
        """
        # final dictionary to be presented to the layer for them to choose from
        player_upgrade_choosing_time = {}

        # if the key corresponds to 1, upgrade health
        for key in value_of_roster:
            #  for health
            if key == 1:
                player_upgrade_choosing_time[key] = 'Health Upgrade'

            # for attack
            if key == 2:
                player_upgrade_choosing_time[key] = 'Attack Upgrade'

            # for double damage
            if key == 3:
                player_upgrade_choosing_time[key] = 'Double Damage Upgrade'

            # for leeching
            if key == 4:
                player_upgrade_choosing_time[key] = 'Leeching Upgrade'

            # for defense
            if key == 5:
                player_upgrade_choosing_time[key] = 'Defense Upgrade'

            # for shield bubble
            if key == 6:
                player_upgrade_choosing_time[key] = 'Shield Bubble Upgrade'

        return player_upgrade_choosing_time

    def level_up_choosing(self, player_upgrade_choosing_time, player_upgrade):
        """
        Function that takes the choice of the character to be finally upgraded and let them choose.
        Player will upgrade if they chose right and if it is within the choices. Subclass of level_up

        :param: player_upgrade_choosing_time: used to check if the choice of the player is within the selection
        :param: player_upgrade: used so the player can upgrade themselves
        """
        # to be seen by the player
        print(player_upgrade_choosing_time)

        # input for the user to let them choose what upgrade they want
        chosen_upgrade = (input_print_effect("You've levelled up! Choose the appropriate "
                                             "number in which you want to upgrade "))
        if chosen_upgrade != '':
            if chosen_upgrade == '1' and 1 in player_upgrade_choosing_time:
                self.health = self.health_max + player_upgrade[1]
                self.health_max = self.health_max + player_upgrade[1]
                print('')  # for terminal
                type_print_effect(str(player_upgrade[1]) + ' Health Points has been added. ' + self.name +
                                  "'s total health is: " + str(self.health_max) + '\n')
                print('')  # for terminal

            # for attacking
            elif chosen_upgrade == '2' and 2 in player_upgrade_choosing_time:
                self.attack += player_upgrade[2]
                print('')  # for terminal
                type_print_effect(self.name + " has attained " + str(player_upgrade[2]) + ' Attack Points!'
                                  + ' Total attack is ' + str(self.attack) + ' points!\n')
                print('')  # for terminal

            # for double damage
            elif chosen_upgrade == '3' and 3 in player_upgrade_choosing_time:
                self.double_damage += player_upgrade[3]
                print('')  # for terminal
                type_print_effect(self.name + ' upgraded their Double Damage with ' + str(player_upgrade[3]) +
                                  ' points. Its value is now: ' + "{:.1%}".format(self.double_damage / 100) + '.\n')
                print('')  # for terminal

            # for leeching
            elif chosen_upgrade == '4' and 4 in player_upgrade_choosing_time:
                self.leeching += player_upgrade[4]
                print('')  # for terminal
                type_print_effect(self.name + "'s Leeching is growing stronger with an additional "
                                  + str(player_upgrade[4]) + ' points!\n')
                print('')  # for terminal

            # for defense
            elif chosen_upgrade == '5' and 5 in player_upgrade_choosing_time:
                self.defense += player_upgrade[5]
                print('')  # for terminal
                type_print_effect(self.name + " can defend more with Defense upgraded to " + str(self.defense) + '!\n')
                print('')  # for terminal

            # for shield bubble
            elif chosen_upgrade == '6' and 6 in player_upgrade_choosing_time:
                self.shield_bubble = self.shield_bubble_max + player_upgrade[6]
                self.shield_bubble_max = self.shield_bubble_max + player_upgrade[6]
                print('')  # for terminal
                type_print_effect('Shield Bubble upgraded! ' + str(player_upgrade[6]) + ' points added!\n')
                print('')  # for terminal

            else:
                type_print_effect("Invalid Input. Please press the available upgrade shown.\n")
                print('')  # for terminal
                self.level_up_choosing(player_upgrade_choosing_time, player_upgrade)
                print('')  # for terminal

        else:
            type_print_effect("Invalid Input. Please press the available upgrade shown.\n")
            print('')  # for terminal
            self.level_up_choosing(player_upgrade_choosing_time, player_upgrade)

    def enemy_level_up(self):
        """
        Function specifically for levelling up the enemy. It will level up all of their necessary stats for
        a harder battle with the player
        """
        # for levelling up the enemy
        self.health = self.health_max + 1
        self.health_max = self.health_max + 1
        self.attack += 1
        self.leeching += 0.1
        self.defense += 0.2
        self.shield_bubble = self.shield_bubble_max + 0.2
        self.shield_bubble_max = self.shield_bubble_max + 0.2

        # debugging
        #  self.__repr__()

    def __repr__(self):
        """
        repr function to check each enemy mob as they upgrade through time
        """
        print("NAME:", self.name)
        print("health:", self.health)
        print("health_max:", self.health_max)
        print("attack:", self.attack)
        print("double_damage:", self.double_damage)
        print("leeching:", self.leeching)
        print("defense:", self.defense)
        print("shield_bubble:", self.shield_bubble)

        print('')  # for terminal
        print("ultimate_levelup_bar:", self.ultimate_levelup_bar)
        print("ultimate_levelup_bar_per_attack:", self.ultimate_levelup_bar_per_attack)

        print('')  # for terminal
        print("levelup_bar:", self.levelup_bar)
        print("levelup_per_defeated_enemy:", self.levelup_per_defeated_enemy)
        print('')  # for terminal


# =========================================================
# SUB-CLASS: COMMON ENEMY
# =========================================================

class DeformedMutatedHuman(common_enemies.DeformedMutatedHuman, Character):
    """
    Subclass of characters, a common enemy
    """

    def __init__(self):
        super().__init__()


class MutatedHuman(common_enemies.MutatedHuman, Character):
    """
    Subclass of character, a common enemy
    """

    def __init__(self):
        super().__init__()


class LostWanderer(common_enemies.LostWanderer, Character):
    """
    Subclass of character, a common enemy
    """

    def __init__(self):
        super().__init__()


class Chaser(common_enemies.Chaser, Character):
    """
    Subclass of character, a common enemy
    """

    def __init__(self):
        super().__init__()

# =========================================================
# SUB-CLASS: PLAYER
# =========================================================

class Player(Character):
    """
    Subclass of Character and it has all the commands that the player can do
    """

    # initial stats of the player
    def __init__(self):
        super().__init__()

        # for the p.name instance to overwrite the values of the parent class
        self.name = ''
        self.health = 50
        self.health_max = 50
        self.attack = 15
        self.double_damage = 0.0
        self.leeching = 0
        self.defense = 7
        self.shield_bubble = 0
        self.shield_bubble_max = 0
        self.ultimate_levelup_bar = 20
        self.ultimate_levelup_bar_per_attack = 4
        self.levelup_bar = 0
        self.levelup_bar_max = 30
        self.levelup_per_defeated_enemy = 10

    def random_enemy_encounter(self, common_enemy_dict):
        """
        Function for random enemies to fight the player

        :param: common_enemy_dict - used to determine what enemy the player will fight
        """

        # each integer is equivalent to one type of enemy
        random_enemy = random.randint(1, constants.RANDOM_ENEMY_INTEGER)

        # the if statement messages are here for organization so that these messages should appear first
        # before the player commands attack mode
        if random_enemy == constants.DEFORMED_MUTATED_HUMAN:
            type_print_effect("A " + 'Deformed Mutated Human' + " has spotted you!\n")
            print('')  # space for terminal

        elif random_enemy == constants.MUTATED_HUMAN:
            type_print_effect("A " + 'Mutated Human' + " screeched as it notices your movement!\n")
            print('')  # space for terminal

        elif random_enemy == constants.LOST_WANDERER:
            type_print_effect("The sound of a " + 'Lost Wanderer' + " echoed through the wind. And it has "
                                                                    "caught your attention!\n")
            print('')  # space for terminal

        elif random_enemy == constants.CHASER:
            type_print_effect("A vicious " + 'Chaser' + " has smelled your scent. It suddenly sprinted "
                                                        "towards your direction!\n")
            print('')  # space for terminal

        # automatically goes to attack mode after encounter with an enemy
        self.player_commands_attack_mode(random_enemy, common_enemy_dict)

    def attack(self, random_enemy, common_enemy_dict):
        """
        Player attack using the .do_damage then if the player has leeching, call upon .leeching

        :parameter - random_enemy = for the function to see what enemy the player will face
        :parameter - common_enemy_dict = for the function to get the enemy attributes
        """

        # if statement stating what enemy the player will encounter
        if random_enemy == constants.DEFORMED_MUTATED_HUMAN:

            # lets the player attack first and .do_damage returns health to be analyzed here
            enemy_health = self.do_damage_with_shield_bubble(common_enemy_dict['deformed_mutated_human'])

            # if the enemy dies when their health is zero
            if enemy_health <= 0:
                # count the added level up points to the player by the levelup_bar
                self.levelup_bar = self.character_death(common_enemy_dict['deformed_mutated_human'])

                # lets the enemy revive themselves and player to level up themselves
                self.revive_enemy_and_level_them_up_alongside_player(common_enemy_dict, self.levelup_bar)

                # to cut the loop of still going into attack mode when the enemy dies
                self.player_commands(common_enemy_dict)

            # if enemy is not yet death it will prompt the enemy to do revenge attack
            else:
                # the enemy will do counter revenge
                self.enemy_attack(random_enemy, common_enemy_dict)

        # same formula from above, just with different enemies
        elif random_enemy == constants.MUTATED_HUMAN:
            enemy_health = self.do_damage_with_shield_bubble(common_enemy_dict['mutated_human'])
            if enemy_health <= 0:
                self.levelup_bar = self.character_death(common_enemy_dict['mutated_human'])
                self.revive_enemy_and_level_them_up_alongside_player(common_enemy_dict, self.levelup_bar)
                self.player_commands(common_enemy_dict)
            else:
                self.enemy_attack(random_enemy, common_enemy_dict)

        elif random_enemy == constants.LOST_WANDERER:
            enemy_health = self.do_damage_with_shield_bubble(common_enemy_dict['lost_wanderer'])
            if enemy_health <= 0:
                self.levelup_bar = self.character_death(common_enemy_dict['lost_wanderer'])
                self.revive_enemy_and_level_them_up_alongside_player(common_enemy_dict, self.levelup_bar)
                self.player_commands(common_enemy_dict)
            else:
                self.enemy_attack(random_enemy, common_enemy_dict)

        elif random_enemy == constants.CHASER:
            enemy_health = self.do_damage_with_shield_bubble(common_enemy_dict['chaser'])
            if enemy_health <= 0:
                self.levelup_bar = self.character_death(common_enemy_dict['chaser'])
                self.revive_enemy_and_level_them_up_alongside_player(common_enemy_dict, self.levelup_bar)
                self.player_commands(common_enemy_dict)
            else:
                self.enemy_attack(random_enemy, common_enemy_dict)

    def enemy_attack(self, random_enemy, common_enemy_dict):
        """
        Function that activates when the player chose flee in the commands but failed to escape,
        the enemy will attack the player first as a punishment.

        This also activates after the player attacks the enemy but the enemy is still alive, it does revenge attack
        :param random_enemy: to see what enemy will face the player
        :param common_enemy_dict: to let the function access the attributes of each enemy
        """

        # if statement stating what enemy the player will encounter
        if random_enemy == constants.DEFORMED_MUTATED_HUMAN:
            # the enemy will do counter revenge
            common_enemy_dict['deformed_mutated_human'].do_damage_with_shield_bubble(self)
            # if the player died from the damage, it will end the game with a message
            common_enemy_dict['deformed_mutated_human'].character_death(self)
            # if the player did not die, let the player choose their next command in attack mode
            self.player_commands_attack_mode(random_enemy, common_enemy_dict)

        # same formula from above, just with different enemies
        elif random_enemy == constants.MUTATED_HUMAN:
            common_enemy_dict['mutated_human'].do_damage_with_shield_bubble(self)
            common_enemy_dict['mutated_human'].character_death(self)
            self.player_commands_attack_mode(random_enemy, common_enemy_dict)

        elif random_enemy == constants.LOST_WANDERER:
            common_enemy_dict['lost_wanderer'].do_damage_with_shield_bubble(self)
            common_enemy_dict['lost_wanderer'].character_death(self)
            self.player_commands_attack_mode(random_enemy, common_enemy_dict)

        elif random_enemy == constants.CHASER:
            common_enemy_dict['chaser'].do_damage_with_shield_bubble(self)
            common_enemy_dict['chaser'].character_death(self)
            self.player_commands_attack_mode(random_enemy, common_enemy_dict)

    def revive_enemy_and_level_them_up_alongside_player(self, common_enemy_dict, levelup_bar):
        """
        This activates when the player defeats a common enemy. It lets all of the enemies level up all of their stats
        for a harder game in the long run. It also levels up the player

        :param - common_enemy_dict: to let the enemies level up with their respectful stats
        :param - levelup_bar: to check if the levelup_bar is the right digit for levelup_bar_max to activate
        level up
        """
        # if the levelup_bar reaches the max levelup_bar it will level up the player alongside the enemies

        #  if levelup_bar >= self.levelup_bar_max: #  TODO: utilize level up bar in the future
        # let the user level up
        self.level_up()

        # let all common enemies level up
        common_enemy_dict['deformed_mutated_human'].enemy_level_up()
        common_enemy_dict['mutated_human'].enemy_level_up()
        common_enemy_dict['lost_wanderer'].enemy_level_up()
        common_enemy_dict['chaser'].enemy_level_up()

    def move(self, common_enemy_dict):
        """
        Function when a player moves, uses random integer to determine the number of steps the player takes
        One out of an integer chance that the player will encounter an enemy while moving

        :param common_enemy_dict: used for the random enemy encounter
        """
        # probablity for enemy to show up while moving based on the constant
        enemy_possibility = random.randint(1, constants.ENEMY_POSSIBILITY)

        # how many steps the player can take
        number_of_moves = random.randint(1, constants.NUMBER_OF_MOVES)

        # if the player encounters an enemy
        if enemy_possibility == 1:
            # call upon the random_enemy_encounter to see what enemy the player will face off
            self.random_enemy_encounter(common_enemy_dict)
        elif enemy_possibility == 2:
            type_print_effect(self.name + " has nearly missed an enemy, and has moved " + str(number_of_moves)
                              + " steps.\n")
        elif enemy_possibility == 3:
            type_print_effect(self.name + " sneakily moved " + str(number_of_moves)
                              + " steps away from a monster.\n")
        else:
            type_print_effect(self.name + " has moved " + str(number_of_moves) + " steps.\n")

        print('')  # for spacing in the terminal

    def flee(self, random_enemy, common_enemy_dict):
        """
        A function only found while attack mode is one, a one in integer chance for the character to flee to prevent
        them from dying

        :param random_enemy: used if the flee failed, the particular enemy will attack
        :param common_enemy_dict: for the usage of the commands as well as the fighting of the enemy
        """
        flee_chance = random.randint(1, constants.FLEE_POSSIBILITY)

        if flee_chance == 1:
            type_print_effect("You successfully escaped the enemy!\n")
            print('')
            self.player_commands(common_enemy_dict)
        else:
            type_print_effect('You failed to escape.\n')
            self.enemy_attack(random_enemy, common_enemy_dict)

    def status(self, random_enemy, common_enemy_dict, who_called_me):
        """
        Function that shows the current status (health, attack damage, etc) of the user's character

        :param random_enemy: for the player_attack_mode
        :param common_enemy_dict: for the player_attack_mode
        :param who_called_me: to check if status will execute attack mode or passive mode commands
        """
        print("Health: " + str(self.health) + "   |   " +
              "Attack: " + str(self.attack) + "   |   " +
              "Double Damage: " + "{:.1%}".format(self.double_damage / 100))

        print("Leeching: " + str(self.leeching) + "  |   " +
              "Defense: " + str(self.defense) + "   |   " +
              "Shield Bubble: " + str(self.shield_bubble))

        # TODO: utilize these stats in the future
        # print("Ultimate Level Up Bar: " + str(self.ultimate_levelup_bar))
        # print("Ultimate Level Up Bar Per Attack: " + str(self.ultimate_levelup_bar_per_attack))
        # print("Level Up Bar: " + str(self.levelup_bar))
        print('')  # space for terminal

        # used when the player is in the middle of fighting a mob and chose status, it will go automatically to
        # attack mode to not let the player escape the loop
        if who_called_me == 'attack_mode':
            self.player_commands_attack_mode(random_enemy, common_enemy_dict)
            print('')  # for spacing in the terminal

        print('')  # for spacing in the terminal

    # TODO: add player status
    def help_game(self, common_enemy_dict, random_enemy, who_called_me):
        """
        Function about all the information that the player wants to know

        :param common_enemy_dict: to determine the enemy stats as well as for the player_command and attack mode
        :param random_enemy: for the player command and attack mode
        :param who_called_me: for tjhe execution of attack mode or passive mode after utilizing the this function
        """
        # list for all the commands that the player can do
        commands = [
            'a = attack',
            'b = move',
            'c = status',
            'd = help',
            'e = quit',
            'f = flee'
        ]

        # to be used in the dictionary as grouping
        enemy = [
            'a = Common Enemies',
            'b = Uncommon Enemies',
            'c = Allies'
        ]

        common_enemy = [
            'a = Deformed Mutating Human',
            'b = Mutated Human',
            'c = Lost Wanderer',
            'd = Chaser'
        ]
        print("This is the help section. What do you want to know about?")
        print("Please press the appropriate letter of the information you want to know about.")
        print('')

        #  Dictionary of information that the player can access
        help_list = ["a = Commands", "b = Enemies"]

        # list for the user to see
        print(help_list)

        # asks the user which topic do they need help with and lowercase for sanitation
        print('')
        player_chosen_help_command = input_print_effect('Which criteria do you want to choose? ').lower()
        print('')

        # if statement to implement what the player has chosen from
        # a for the commands
        if player_chosen_help_command == 'a':
            print(commands)
            # space for terminal
            print('')
            # subset for the user to be asked what specific command they want to know plus lowercase for sanitation
            chosen_help_specific_command = input_print_effect('What command do you want to learn more? ').lower()

            # where the player will see all commands, below this code are just for looping through this function
            self.help_commands(chosen_help_specific_command, random_enemy, common_enemy_dict, who_called_me)

            # asked at the end of the submain commands section for the player to choose if they still want to know
            # more information on the commands subtopic or go back to the main topic
            print('')  # space terminal
            print(constants.COMMAND_END_HELP_BANNER)
            print('')  # space terminal

            # end statement for the user to see when they are inside the commands database
            type_print_effect("Do you want to dive further into knowing more about different commands?\n")
            type_print_effect("Or go back to the main help section?\n")
            type_print_effect("Press y to stick to commands and n for no.\n")
            type_print_effect("Or press b to go back to the main help section.\n")
            ask_commands_again = input_print_effect("Please press the appropriate letter. ").lower()
            print('')

            # while loop when the player is inside the command database for them to repeat over and over if they
            # like
            while True:
                # if they chose to learn more
                if ask_commands_again == 'y':
                    # shows the user the exact same thing earlier for them to choose what they want to learn more
                    # for the user to see all types of commands
                    print(commands)
                    # space for terminal
                    print('')
                    # subset for the user to be asked what specific command they want to know plus lowercase for
                    # sanitation
                    chosen_help_specific_command = input_print_effect(
                        'What command do you want to learn more? ').lower()

                    # where the player will see all commands, below this code are just for looping through this function
                    self.help_commands(chosen_help_specific_command, random_enemy, common_enemy_dict, who_called_me)

                    # asked at the end of the submain enemies section for the player to choose if they still want to
                    # know more information on the enemies subtopic or go back to the main topic
                    print('')  # space terminal
                    print(constants.COMMAND_END_HELP_BANNER)
                    print('')  # space terminal

                    # end statement for the user to see when they are inside the enemy database
                    type_print_effect("Press y to stick to commands and n for no.\n")
                    type_print_effect("Or press b to go back to the main help section.\n")
                    ask_commands_again = input_print_effect("Please press the appropriate letter. ").lower()
                    print('')

                # when the player choses no
                elif ask_commands_again == 'n':
                    # to end the help loop and let the player choose another command besides help

                    # used when the player is in the middle of fighting a mob and chose help,
                    # it will go automatically to
                    # attack mode to not let the player escape the loop
                    if who_called_me == 'attack_mode':
                        self.player_commands_attack_mode(random_enemy, common_enemy_dict)
                        print('')  # for spacing in the terminal
                    else:
                        self.player_commands(common_enemy_dict)

                # when the player wants to go back to the main section
                elif ask_commands_again == 'b':
                    self.help_game(common_enemy_dict, random_enemy, who_called_me)

                else:
                    # fencepost solution
                    type_print_effect("Invalid input. Please press the appropriate letter.\n")
                    print('')  # space terminal
                    type_print_effect("Press y to stick to commands and n for no.\n")
                    type_print_effect("Or press b to go back to the main help section.\n")
                    ask_commands_again = input_print_effect("Please press the appropriate letter. ").lower()
                    print('')

        # for when the player chooses enemies in the main help section
        elif player_chosen_help_command == 'b':
            # for the user to see all types of enemies
            print(enemy)
            # space for terminal
            print('')
            # subset for the user to be asked what specific enemy they want to know plus lowercase for sanitation
            chosen_enemy_help = input_print_effect('What enemy do you want to learn more? ').lower()
            print('')  # space for terminal

            # where the player will see the enemies, below this code are just for looping through this function
            self.help_enemies(chosen_enemy_help, common_enemy, random_enemy, common_enemy_dict, who_called_me)

            # asked at the end of the submain enemies section for the player to choose if they still want to know
            # more information on the enemies subtopic or go back to the main topic
            print('')  # space terminal
            print(constants.ENEMY_END_HELP_SECTION)
            print('')  # space terminal

            # end statement for the user to see when they are inside the enemy database
            type_print_effect("Do you want to dive further into knowing more about different enemies?\n")
            type_print_effect("Or go back to the main help section?\n")
            type_print_effect("Press y to stick to enemies and n for no.\n")
            type_print_effect("Or press b to go back to the main help section.\n")
            ask_enemies_again = input_print_effect("Please press the appropriate letter. ").lower()
            print('')

            # while loop when the player is inside the enemy database for them to repeat over and over if they
            # like
            while True:
                # if they chose to learn more
                if ask_enemies_again == 'y':
                    # shows the user the exact same thing earlier for them to choose what they want to learn more
                    # for the user to see all types of enemies
                    print(enemy)
                    print('')  # space for terminal
                    chosen_enemy_help = input_print_effect('What enemy do you want to learn more? ').lower()
                    print('')  # space for terminal

                    # chosen enemy help will go inside prompting a new if statement to be executed inside help_enemies
                    self.help_enemies(chosen_enemy_help, common_enemy, random_enemy, common_enemy_dict, who_called_me)

                    print('')  # space terminal
                    print(constants.ENEMY_END_HELP_SECTION)
                    print('')  # space terminal

                    # asks the user again if they still want to stick
                    type_print_effect("Press y to stick to enemies and n for no.\n")
                    type_print_effect("Or press b to go back to the main help section.\n")
                    ask_enemies_again = input_print_effect("Please press the appropriate letter. ").lower()
                    print('')

                # when the player choses no
                elif ask_enemies_again == 'n':
                    # to end the help loop and let the player choose another command besides help

                    # used when the player is in the middle of fighting a mob and chose help,
                    # it will go automatically to
                    # attack mode to not let the player escape the loop
                    if who_called_me == 'attack_mode':
                        self.player_commands_attack_mode(random_enemy, common_enemy_dict)
                        print('')  # for spacing in the terminal
                    else:
                        self.player_commands(common_enemy_dict)

                # when the player wants to go back to the main section
                elif ask_enemies_again == 'b':
                    self.help_game(common_enemy_dict, random_enemy, who_called_me)

                else:
                    # fencepost solution
                    type_print_effect("Invalid input. Please press the appropriate letter.\n")
                    print('')  # space terminal
                    type_print_effect("Press y to stick to enemies and n for no.\n")
                    type_print_effect("Or press b to go back to the main help section.\n")
                    ask_enemies_again = input_print_effect("Please press the appropriate letter. ").lower()
                    print('')

        # use for cleaner terminal reading at the end of each information given
        print('')  # space terminal
        print(constants.HELP_END_BANNER)
        print('')  # space terminal

    def help_commands(self, chosen_help_specific_command, random_enemy, common_enemy_dict, who_called_me):
        """
        Functions particular for the commands. used to determine what the commands do

        :param chosen_help_specific_command: to execute particular command chosen by the player
        :param random_enemy: for the player commands and attack mode
        :param common_enemy_dict: for the player commands and attack mode
        :param who_called_me: to determine if it will go to passive or attack mode after this function
        """
        # for attack
        if chosen_help_specific_command == 'a':
            print('')  # space terminal
            print(constants.COMMAND_DESCRIPTION_HELP_BANNER)
            print('')  # space terminal
            print("Command for the player to attack.")
            print("Damage is based on the current weapon that the player is holding.")

        # for move
        elif chosen_help_specific_command == 'b':
            print('')  # space terminal
            print(constants.COMMAND_DESCRIPTION_HELP_BANNER)
            print('')  # space terminal
            print("Command for the player to move.")
            print("There is a small percentage that the player will encounter an enemy while moving.")

        # for status
        elif chosen_help_specific_command == 'c':
            print('')  # space terminal
            print(constants.COMMAND_DESCRIPTION_HELP_BANNER)
            print('')  # space terminal
            print("Command for the player to see their character's status.")

        # for help section
        elif chosen_help_specific_command == 'd':
            print('')  # space terminal
            print(constants.COMMAND_DESCRIPTION_HELP_BANNER)
            print('')  # space terminal
            print("Command for the player to see the help section of the game.")

        # for quitting the game
        elif chosen_help_specific_command == 'e':
            print('')  # space terminal
            print(constants.COMMAND_DESCRIPTION_HELP_BANNER)
            print('')  # space terminal
            print("Command for the player to quit the game.")

        # for fleeing
        elif chosen_help_specific_command == 'f':
            print('')  # space terminal
            print(constants.COMMAND_DESCRIPTION_HELP_BANNER)
            print('')  # space terminal
            print("Only available when an enemy has approached the player.")
            print('There is a percentage that the flee will be successful, if it fails the enemy')
            print('will attack the player for that turn.')

        # when invalid input
        else:
            print('Invalid input. Please press the aproppriate letter.')
            print('')
            self.help_game(common_enemy_dict, random_enemy, who_called_me)

    def help_enemies(self, chosen_enemy_help, common_enemy, random_enemy, common_enemy_dict, who_called_me):
        """
        Sub function of help that has the information for all the enemies so the help function is not overcrowded
        with lines of code

        :param chosen_enemy_help: to execute particular enemy information chosen by the player
        :param common_enemy: to check the particular common enemy that the player wants to know
        :param random_enemy: for the player commands and attack mode
        :param common_enemy_dict: for the player commands and attack mode
        :param who_called_me: to determine if it will go to passive or attack mode after this function
        """
        # for the common enemies
        if chosen_enemy_help == 'a':
            # for the user to see all common enemies possible
            print(common_enemy)
            # space for terminal
            print('')
            # subset for the user to be asked what specific common enemy they want to know plus lowercase for
            # sanitation
            chosen_common_enemy_help = input_print_effect('What enemy do you want '
                                                          'to learn more? ').lower()
            print('')  # space for terminal

            # neverending loop if they want to keep finding out about enemies
            while True:
                # for deformed mutated human
                if chosen_common_enemy_help == 'a':
                    # Used for aesthetics in the terminal
                    print(constants.ENEMY_STATS_BANNER)
                    print('')
                    # for gap for the player to see the stats for a while before the backstory
                    text_effect_and_exit_function.text_delay_via_time_sleep(constants.HELP_BACKSTORY_NEXT_TEXT)
                    # prints the stats first
                    print("Health: " + str(common_enemy_dict['deformed_mutated_human'].health) + "    |   " +
                          "Attack: " + str(common_enemy_dict['deformed_mutated_human'].attack) + "   |   " +
                          "Double Damage: "
                          + "{:.1%}".format(common_enemy_dict['deformed_mutated_human'].double_damage / 100))

                    print("Leeching: " + str(common_enemy_dict['deformed_mutated_human'].leeching) + "  |   " +
                          "Defense: " + str(common_enemy_dict['deformed_mutated_human'].defense) + "   |   " +
                          "Shield Bubble: " + str(common_enemy_dict['deformed_mutated_human'].shield_bubble))

                    # then prints the backstory
                    # plus cleanliness in the terminal
                    print('')
                    print(constants.ENEMY_BACK_STORY_BANNER)
                    print('')
                    type_print_effect("Once a human that came from Earth, this "
                                      "abomination is the result of countless\n")
                    type_print_effect("experiments that failed, leaving him a husk of his former self.\n")
                    type_print_effect("They no longer have any sort of consciousness. "
                                      "Instead, what's left is their pure\n")
                    type_print_effect('rage for what has become of them. They have lower '
                                      'health due to them being the \n')
                    type_print_effect('later stage in decomposition than the Mutated Human. '
                                      'However, they make up for it\n')
                    type_print_effect('by their sheer strength.\n')
                    type_print_effect('')
                    break  # to break the while loop

                # for mutated human
                elif chosen_common_enemy_help == 'b':
                    # Used for aesthetics in the terminal
                    print(constants.ENEMY_STATS_BANNER)
                    print('')
                    # for gap for the player to see the stats for a while before the backstory
                    text_effect_and_exit_function.text_delay_via_time_sleep(constants.HELP_BACKSTORY_NEXT_TEXT)
                    print("Health: " + str(common_enemy_dict['mutated_human'].health) + "    |   " +
                          "Attack: " + str(common_enemy_dict['mutated_human'].attack) + "   |   " +
                          "Double Damage: " + "{:.1%}".format(common_enemy_dict['mutated_human'].double_damage / 100))

                    print("Leeching: " + str(common_enemy_dict['mutated_human'].leeching) + "  |   " +
                          "Defense: " + str(common_enemy_dict['mutated_human'].defense) + "   |   " +
                          "Shield Bubble: " + str(common_enemy_dict['mutated_human'].shield_bubble))

                    # then prints the backstory
                    # plus cleanliness in the terminal
                    print('')
                    print(constants.ENEMY_BACK_STORY_BANNER)
                    print('')
                    type_print_effect("It has the same sad fate as the Deformed Mutated Human.\n")
                    type_print_effect("The difference, however, is that the Mutated Human is a failed experiment,\n")
                    type_print_effect("that has been conducted quite recently. They have a small percentage\n")
                    type_print_effect('of their consciousness still intact, therefore making their suffering more\n')
                    type_print_effect('horrendous. They have higher health than the Deformed Mutated Human due to\n')
                    type_print_effect('them being recent test subjects. However, they have a higher defense than the\n')
                    type_print_effect('Deformed Mutated Human due to their intact body composition.\n')
                    type_print_effect('')
                    break  # to break the while loop

                # for lost wanderer
                elif chosen_common_enemy_help == 'c':
                    # Used for aesthetics in the terminal
                    print(constants.ENEMY_STATS_BANNER)
                    print('')
                    # for gap for the player to see the stats for a while before the backstory
                    text_effect_and_exit_function.text_delay_via_time_sleep(constants.HELP_BACKSTORY_NEXT_TEXT)
                    print("Health: " + str(common_enemy_dict['lost_wanderer'].health) + "    |   " +
                          "Attack: " + str(common_enemy_dict['lost_wanderer'].attack) + "   |   " +
                          "Double Damage: " + "{:.1%}".format(common_enemy_dict['lost_wanderer'].double_damage / 100))

                    print("Leeching: " + str(common_enemy_dict['lost_wanderer'].leeching) + "  |   " +
                          "Defense: " + str(common_enemy_dict['lost_wanderer'].defense) + "   |   " +
                          "Shield Bubble: " + str(common_enemy_dict['lost_wanderer'].shield_bubble))

                    # then prints the backstory
                    # plus cleanliness in the terminal
                    # TODO: add the history about the incident in the main story line that caused lost
                    #  wanderers to escape the experiments
                    print('')
                    print(constants.ENEMY_BACK_STORY_BANNER)
                    print('')
                    type_print_effect("These are individuals that have escaped the experiments but have failed to\n")
                    type_print_effect("mitigate the effects, therefore making their body worse than the Deformed\n")
                    type_print_effect("and Mutated Humans. They have drastically low health due to the effects but\n")
                    type_print_effect('they have gained the ability to restore their health '
                                      'when attacking individuals.\n')
                    type_print_effect('Unlike the Mutated Humans the Lost Wanderers have lost their\n')
                    type_print_effect('consciousness due to them escaping a long time ago after the incident.\n')
                    type_print_effect('')
                    break  # to break the while loop

                # for chaser
                elif chosen_common_enemy_help == 'd':
                    # Used for aesthetics in the terminal
                    print(constants.ENEMY_STATS_BANNER)
                    print('')
                    # for gap for the player to see the stats for a while before the backstory
                    text_effect_and_exit_function.text_delay_via_time_sleep(constants.HELP_BACKSTORY_NEXT_TEXT)
                    print("Health: " + str(common_enemy_dict['chaser'].health) + "    |   " +
                          "Attack: " + str(common_enemy_dict['chaser'].attack) + "   |   " +
                          "Double Damage: " + "{:.1%}".format(common_enemy_dict['chaser'].double_damage / 100))

                    print("Leeching: " + str(common_enemy_dict['chaser'].leeching) + "  |   " +
                          "Defense: " + str(common_enemy_dict['chaser'].defense) + "   |   " +
                          "Shield Bubble: " + str(common_enemy_dict['chaser'].shield_bubble))

                    # then prints the backstory
                    # plus cleanliness in the terminal
                    print('')
                    print(constants.ENEMY_BACK_STORY_BANNER)
                    print('')
                    type_print_effect("These are animals of different origins that have escaped the experiments.\n")
                    type_print_effect(
                        "They are similar to the lost wanderers. Their entire existence is solely based\n")
                    type_print_effect(" in finding nutrition to feed themselves as they decay faster than the\n")
                    type_print_effect('Deformed and Mutated Humans. Out of all the enemies that the player encounter\n')
                    type_print_effect('while walking, they have the most balanced stats and have also gained the\n')
                    type_print_effect('the leech ability as well as high defense from their tough exterior.\n')
                    type_print_effect('')
                    break  # to break the while loop

                else:
                    print('Invalid input. Please press the aproppriate letter.')
                    print('')

                    print(common_enemy)
                    # space for terminal
                    print('')
                    # subset for the user to be asked what specific common enemy they want to know plus lowercase for
                    # sanitation
                    chosen_common_enemy_help = input_print_effect('What enemy do you want '
                                                                  'to learn more? ').lower()
                    print('')  # space for terminal

        # TODO: add uncommon enemies and allies later
        elif chosen_enemy_help == 'b' or chosen_enemy_help == 'c':
            print('Coming Soon!')

        else:  #
            print('Invalid input. Please press the appropriate letter.')
            print('')
            self.help_game(common_enemy_dict, random_enemy, who_called_me)

    def quit_game(self, common_enemy_dict, random_enemy, who_called_me='attack_mode'):
        """
        Command that will quit the game when the player wants to

        :param common_enemy_dict: for the player commands or attack mode
        :param random_enemy: for the player command or attack mode
        :param who_called_me: used to determine if it will go to passive or attack mode after this function
        """

        #  Asks the player if they want to quit for a second time to make sure it was not a mistake and lowercase
        # for sanitation
        ask_player_again = input_print_effect("Are you sure you want to exit? (Type y for yes, n for no) ").lower()

        while ask_player_again != '':
            if ask_player_again == 'y':
                type_print_effect(
                    'Thank you for playing my game! I hope you enjoyed my first ever Programming Project.')
                text_effect_and_exit_function.system_exit()
            elif ask_player_again == 'n':
                # TODO: BUG HELP
                print('')  # for spacing in the terminal
                # used when the player is in the middle of fighting a mob and chose quit, it will go automatically to
                # attack mode to not let the player escape the loop
                if who_called_me == 'attack_mode':
                    self.player_commands_attack_mode(random_enemy, common_enemy_dict)
                    print('')  # for spacing in the terminal

                #  to prevent endless loop
                else:
                    self.player_commands(common_enemy_dict)

            else:
                type_print_effect("Invalid input\n")
                print('')  # for spacing in the terminal

                #  fencepost solution
                ask_player_again = input_print_effect(
                    "Are you sure you want to exit? (Type y for yes, n for no) ").lower()

    def player_commands(self, common_enemy_dict):
        """
        All commands that the player can do when there are no enemies

        :param common_enemy_dict: used for the random enemy encounter as well as the stats of the enemies in help.
        """
        print('What action do you want to do? We have the following.')

        #  for the user to see
        command_list = ["a = attack", 'b = move', 'c = status', 'd = help', 'e = quit']
        print(command_list)

        # asks player for the command that they want to do plus lowercase for sanitation
        player_actions = input("Please press the appropriate letter "
                               "for the command that you want to do. ").lower()
        print('')  # for spacing in the terminal

        # for attack
        if player_actions == 'a':
            # player can't fight anybody in player_command mode, has to be in attack mode
            type_print_effect('There are no enemies in sight...so far.\n')
            # bug fix, to not let the player go into attack mode after the print statement above
            print('')  # for terminal
            self.player_commands(common_enemy_dict)

        # for move
        elif player_actions == 'b':
            self.move(common_enemy_dict)

        # for status
        elif player_actions == 'c':
            # to differentiate player_command_attack_mode from the normal player_command
            # calls None for positional arguments because in passive mode there are no random enemies
            self.status(random_enemy=None, common_enemy_dict=None, who_called_me='passive_mode')

        # for help
        elif player_actions == 'd':
            # same idea with status
            self.help_game(common_enemy_dict, random_enemy=None, who_called_me='passive_mode')

        # for quit
        elif player_actions == 'e':
            # as well as this one
            self.quit_game(common_enemy_dict, random_enemy=None, who_called_me='passive_mode')
        else:
            type_print_effect("Invalid input.\n")
            print('')  # for spacing in the terminal
            self.player_commands(common_enemy_dict)

    def player_commands_attack_mode(self, random_enemy, common_enemy_dict):
        """
        All commands that the player can do when the player encounters an enemy

        :param random_enemy: used to determine the specific enemy that the player will attack when they encounter one
        in random enemy encounter
        :param common_enemy_dict: used for the classes of the enemy for the enemy to attack and other commands
        """
        print('What action do you want to do? We have the following.')

        #  for the user to see
        command_list = ["a = attack", 'b = FLEE', 'c = status', 'd = help', 'e = quit']
        print(command_list)

        # asks player for the command that they want to do plus lowercase for sanitation
        player_actions = input("Please press the appropriate letter "
                               "for the command that you want to do. ").lower()

        print('')  # for spacing in the terminal

        # for attack
        if player_actions == 'a':
            Player.attack(self, random_enemy, common_enemy_dict)

        # for flee
        elif player_actions == 'b':
            # an updated command that the player can do ONLY if they are in attack mode.
            # possibility for the player to run away
            self.flee(random_enemy, common_enemy_dict)

        # for status
        elif player_actions == 'c':
            # to differentiate player_command_attack_mode from the normal player command
            self.status(random_enemy, common_enemy_dict, who_called_me='attack_mode')

        # for help
        elif player_actions == 'd':
            self.help_game(common_enemy_dict, random_enemy, who_called_me='attack_mode')

        # for quit
        elif player_actions == 'e':
            self.quit_game(common_enemy_dict, random_enemy, who_called_me='attack_mode')
        else:
            type_print_effect("Invalid input.\n")
            print('')  # for spacing in the terminal
            self.player_commands_attack_mode(random_enemy, common_enemy_dict)
