from random import random, randint, choice
from copy import deepcopy
import enemies2


class Character(object):

    def __init__(self, engine):
        self.engine = engine
        self.name = ''
        self.armor = 1
        self.ship_attack = 0
        self.player_attack = 0
        self.player_speed = self.player_attack / self.armor
        self.ship_speed = self.ship_attack / self.armor
        self.is_ship = False
        self.supplies = 0


class Player(Character):

    def __init__(self, name, engine):
        super().__init__(engine)
        self.name = name
        self.armor = randint(29**2 // 2.5 * 2500, 29**2 // 2.5 * 7500)  # basic time travel gear
        self.original_armor = deepcopy(self.armor)
        self.player_attack = randint(29**2 // 2.5 * 2500, self.armor)
        self.ship_attack = randint(29**2 // 2.5 * 2500, self.player_attack)  # basic blaster
        self.fullness = 100  # percent
        self.sanity = 100  # percent
        self.restedness = 100  # percent
        self.supplies = 0

    def armor_status(self):
        return int(self.armor / self.original_armor * 100)


class Ship(Character):

    def __init__(self, ship_name, engine):
        super().__init__(engine)
        self.name = ship_name
        self.supplies = 50  # days
        self.weapons = 100  # percent
        self.armor = randint(29**2 // 2.5 * 25000, 29**2 // 2.5 * 75000)
        self.original_armor = deepcopy(self.armor)
        self.ship_attack = int(self.weapons / 100 * randint(29**2 // 2.5 * 25000, 29**2 // 2.5 * 75000))
        self.player_attack = int(self.weapons / 100 * randint(29**2 // 2.5 * 25000, 29**2 // 2.5 * 75000))
        self.is_ship = True

    def armor_status(self):
        return int(self.armor / self.original_armor * 100)


class Enemy(Character):

    def __init__(self, class_, name, engine):
        super().__init__(engine)
        self.malice = 50  # percent
        self.description = enemies2.classes(class_)[name][5]
        self.is_ship = enemies2.classes(class_)[name][3]
        self.name = name
        self.supplies = enemies2.classes(class_)[name][4]
        
        interim = enemies2.classes(class_)[name][0]**2 // 2.5
        if interim == 0:
            self.armor = randint(1250, 3750)
        else:
            self.armor = randint(interim * 2500, interim * 7500)

        interim = enemies2.classes(class_)[name][1]**2 // 2.5
        if interim == 0:
            self.ship_attack = randint(1250, 3750)
        else:
            self.ship_attack = randint(interim * 2500, interim * 7500)

        interim = enemies2.classes(class_)[name][2]**2 // 2.5
        if interim == 0:
            self.player_attack = randint(1250, 3750)
        else:
            self.player_attack = randint(interim * 2500, interim * 7500)


class AncientEnemy(Enemy):

    def __init__(self, name, engine):
        super().__init__('ANCIENT_ENEMIES', name, engine)
        self.malice += randint(-50, 25)


class MiddleAgesEnemy(Enemy):

    def __init__(self, name, engine):
        super().__init__('MIDDLEAGES_ENEMIES', name, engine)
        self.malice += randint(-25, 50)


class WWIIEnemy(Enemy):

    def __init__(self, name, engine):
        super().__init__('WWII_ENEMIES', name, engine)
        self.malice += randint(0, 50)


class PresentEnemy(Enemy):

    def __init__(self, name, engine):
        super().__init__('PRESENT_ENEMIES', name, engine)
        self.malice += randint(-40, -35)


class TechnicalAgeEnemy(Enemy):

    def __init__(self, name, engine):
        super().__init__('TECHNICALAGE_ENEMIES', name, engine)
        self.malice += randint(-35, -25)


class AlienAgeEnemy(Enemy):

    def __init__(self, name, engine):
        super().__init__('ALIENAGE_ENEMIES', name, engine)
        self.malice += randint(-15, 25)


class FarDistantEnemy(Enemy):

    def __init__(self, name, engine):
        super().__init__('FARDISTANT_ENEMIES', name, engine)
        self.malice = 75


class TimeStreamEnemy(Enemy):

    def __init__(self, name, engine):
        super().__init__('TIMESTREAM_ENEMIES', name, engine)
        self.malice = 100


class TimeJelly(Enemy):

    def __init__(self, engine):
        super().__init__('TIME_JELLY', 'Time Jelly', engine)
        self.ship_attack = 0
        self.player_attack = 0
        self.malice = 0
        self.location = choice(list(self.engine.scenes.values())).location