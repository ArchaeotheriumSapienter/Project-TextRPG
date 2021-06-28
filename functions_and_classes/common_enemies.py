"""
File: common_enemies.py

This file has all of the __init__ attributes of the common enemies
"""


class DeformedMutatedHuman:
    """
    Subclass of characters, a common enemy
    """

    def __init__(self):
        self.name = 'Deformed Mutated Human'
        self.health = 10
        self.health_max = 10
        self.attack = 20
        self.double_damage = 0
        self.leeching = 0
        self.defense = 5
        self.shield_bubble = 0
        self.shield_bubble_max = 0
        self.ultimate_levelup_bar = 0
        self.ultimate_levelup_bar_per_attack = 0
        self.levelup_bar = 0
        self.levelup_bar_max = 0
        self.levelup_per_defeated_enemy = 0


class MutatedHuman:
    """
    Subclass of character, a common enemy
    """

    def __init__(self):
        self.name = 'Mutated Human'
        self.health = 20
        self.health_max = 20
        self.attack = 10
        self.double_damage = 0
        self.leeching = 0
        self.defense = 7
        self.shield_bubble = 0
        self.shield_bubble_max = 0
        self.ultimate_levelup_bar = 0
        self.ultimate_levelup_bar_per_attack = 0
        self.levelup_bar = 0
        self.levelup_bar_max = 0
        self.levelup_per_defeated_enemy = 0


class LostWanderer:
    """
    Subclass of character, a common enemy
    """

    def __init__(self):
        self.name = 'Lost Wanderer'
        self.health = 5
        self.health_max = 5
        self.attack = 20
        self.double_damage = 0
        self.leeching = 5
        self.defense = 7
        self.shield_bubble = 0
        self.shield_bubble_max = 0
        self.ultimate_levelup_bar = 0
        self.ultimate_levelup_bar_per_attack = 0
        self.levelup_bar = 0
        self.levelup_bar_max = 0
        self.levelup_per_defeated_enemy = 0


class Chaser:
    """
    Subclass of character, a common enemy
    """

    def __init__(self):
        self.name = 'Chaser'
        self.health = 15
        self.health_max = 15
        self.attack = 15
        self.double_damage = 0
        self.leeching = 2
        self.defense = 10
        self.shield_bubble = 0
        self.shield_bubble_max = 0
        self.ultimate_levelup_bar = 0
        self.ultimate_levelup_bar_per_attack = 0
        self.levelup_bar = 0
        self.levelup_bar_max = 0
        self.levelup_per_defeated_enemy = 0
