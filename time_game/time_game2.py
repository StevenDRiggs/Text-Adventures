from random import choice, randint, random
from textwrap import dedent

import characters2
import enemies2
import enemy_art



story = """
    It's the year 2525, and somehow mankind is still alive.
    You are the first Chronofixer, on your first assignment.
    The Time Jelly, a massive, expensive, top secret science
    experiment, has gotten loose, and is now traveling back
    and forth through time, distorting the timeline everywhere
    it goes.  It's up to you to stop it before all of history
    is permenantly altered.

    You'll be piloting '{}', a prototype time-ship
    outfitted with ridiculously powerful weaponry (because why
    not?).  Unfortunately, since '{}' is the first
    of it's kind, the scientists haven't fully figured out the
    power stabilization grid of those weapons, so use them at
    your own risk.

    As for you personally, you are equipped with the latest (and
    earliest) of standard time travel gear, so you'll have some
    protection if you decide to leave your ship.  Be careful,
    though.  Your gear will not feed you or read you stories,
    and is nowhere near comfortable enough to sleep in.  You'll
    have to rest in '{}' if you aren't feeling well.
    Don't dawdle too much, though.  With every passing moment the
    Time Jelly brings us all one step closer to total nonexistance.

    Oh, and we've provided you with all the tools you'll need for
    any 'streamside' repairs '{}' may need.  Just don't
    lose focus on the mission or your own needs.

    Now, then.  Speaking of the mission, our sensors indicate that
    the last known location of the Time Jelly is somewhere around
    the year {}.  We've hard-coded a handful
    of destinations into your ship's onboard computer.  I'm sorry
    we couldn't do more, but we ran out of money and interns.
    You'll just have to make do.

    Anyway, what are you waiting for?  Stop the Time Jelly!
    """



class Engine(object):

    def __init__(self, name):
        self.name = name
        self.jump_count = 0
        self.jump_limit = randint(3, 5)

        self.player = characters2.Player(input('What is your name, brave explorer?\n>>> '), self)
        self.ship = characters2.Ship(input('And what is the name of your valiant steed (your ship)?\n>>> '), self)
        self.scenes = {
            'The Ancient Past (4000 BC)': Ancient(self),
            'The Middle Ages (475 AD)': MiddleAges(self),
            'World War II (1944 AD)': WWII(self),
            'The Present (2525 AD)': Present(self),
            'The Technical Age (3700 AD)': TechnicalAge(self),
            'The Alien Age (6521 AD)': AlienAge(self),
            'The Far Distant Future (10000 AD)': FarDistant(self),
            'The Time Stream': TimeStream(self)
        }

        self.time_jelly = characters2.TimeJelly(self)

    def action_menu(self):
        actions_d = {
            1: self.travel_menu,
            2: self.rest,
            3: self.status,
            4: self.repair,
            5: self.hunt
        }

        try:
            action = int(input(dedent("""
                Actions:
                ______________________
                1. Travel...
                2. Rest...
                3. Check Status
                4. Repair Ship...
                5. Hunt
                ______________________
            
                What would you like to do?
                >>> """
            )).strip())

            if action == 5:
                outcome = actions_d[action](self.current_scene)
            else:
                outcome = actions_d[action]()
            
            self.jump_count += 1
            if self.jump_count >= self.jump_limit:
                self.jump_count = 0
                self.time_jelly_move()
            
            return outcome

        except TypeError:
            print("I'm sorry.  I don't understand.  Numbers only, please.")
            return self.action_menu()

        except KeyError:
            print("I'm sorry.  I don't understand.  Please try again.")
            return self.action_menu()

    def combat(self, enemy):
        print(enemy_art.art[enemy.name])
        input()
        if enemy.name == 'Echo':
            if randint(0, 1):
                enemy.is_ship = True
                enemy.ship_attack, enemy.player_attack, enemy.armor = self.ship.player_attack, self.ship.armor, self.ship.ship_attack
            else:
                enemy.is_ship = False
                enemy.ship_attack, enemy.player_attack, enemy.armor = self.player.armor, self.player.ship_attack, self.player.player_attack
        if enemy.name == 'Time Twister':
            t_scenes = self.scenes.keys()
            del t_scenes['The Time Stream']
            for scene in t_scenes:
                self.scenes[scene].distortion = randint(0, 5)

        try:
            fight_flight = int(input(f"""
                You face {enemy.name} ({enemy.description}).

                Your Combat Readiness:
                ______________________
                '{self.ship.name}':
                
                Armor: {self.ship.armor_status()}%
                Weapons: {self.ship.weapons}%
                
                {self.player.name}:
                Armor: {self.player.armor_status()}%
                Sanity: {self.player.sanity}%
                Restedness: {self.player.restedness}%
                ______________________

                What do you want to do?

                1. Fight
                2. Flee
                """
            ).strip())

            if fight_flight == 1:
                player_mode = int(input(f"""
                    How?

                    1. In '{self.ship.name}'
                    2. Myself
                    """
                ).strip())

                if player_mode == 1:
                    self.player.restedness -= randint(2, 3)
                    self.player.sanity -= randint(1, 2)
                    if enemy.is_ship:
                        p_speed = self.ship.ship_speed
                        p_attack = self.ship.ship_attack
                    else:
                        p_speed = self.ship.player_speed
                        p_attack = self.ship.player_attack
                    p_self = self.ship
                    e_speed = enemy.ship_speed
                    e_attack = enemy.ship_attack
                elif player_mode == 2:
                    self.player.restedness -= randint(5, 10)
                    self.player.sanity -= int(random() * randint(6, 15))
                    if enemy.is_ship:
                        p_speed = self.player.ship_speed
                        p_attack = self.player.ship_attack
                    else:
                        p_speed = self.player.player_speed
                        p_attack = self.player.player_attack
                    p_self = self.player
                    e_speed = enemy.player_speed
                    e_attack = enemy.player_attack
                else:
                    print("I'm sorry.  That is not an option.  Please try again.")
                    return self.combat(enemy)

                if p_speed >= e_speed:
                    enemy.armor -= p_attack
                    if player_mode == 1:
                        self.ship.weapons -= 10
                        if self.ship.weapons < 0:
                            self.ship.weapons = 0
                        self.ship.ship_attack = int(self.ship.ship_attack * self.ship.weapons / 100)
                        self.ship.player_attack = int(self.ship.player_attack * self.ship.weapons / 100)
                    if enemy.armor < 0:
                        print(f'{enemy.name} is dead.')
                        if enemy is self.time_jelly:
                            self.end_game('toast')
                        self.scenes['The Time Stream'].location = randint(-4000, 10000)
                        self.ship.supplies += enemy.supplies
                        if self.ship.supplies < 0:
                            self.ship.supplies = 0
                        if enemy.supplies >= 0:
                            print(f'Supplies gained: {enemy.supplies}')
                        else:
                            print(f'{enemy.name} took your supplies!\nSupplies lost: {abs(enemy.supplies)}')
                        del enemy
                        return(self.current_scene)
                    else:
                        if enemy is self.time_jelly:
                            self.time_jelly_move()
                            return self.current_scene
                        p_self.armor -= e_attack
                        if p_self.armor < 0:
                            self.end_game(enemy.name)
                        return self.combat(enemy)

                else:
                    if enemy.name == 'Uhluhtc':
                        print("Uhluhtc's slimy tentacle reaches into your mind and rips out the nearest memories,\nan excurciating process that leaves your body unharmed but your mind...less so.")
                        self.player.sanity -= randint(1, 6)
                        return self.combat(enemy)
                    else:
                        p_self.armor -= e_attack
                        if p_self.armor < 0:
                            self.end_game(enemy.name)
                        else:
                            if enemy.name == 'Japanese Kamikaze Squadron':
                                enemy.armor -= p_attack
                                if enemy.armor < 0:
                                    print(f'{enemy.name} is dead.')
                                    self.scenes['The Time Stream'].location = randint(-4000, 10000)
                                    self.ship.supplies += enemy.supplies
                                    if self.ship.supplies < 0:
                                        self.ship.supplies = 0
                                    if enemy.supplies >= 0:
                                        print(f'Supplies gained: {enemy.supplies}')
                                    else:
                                        print(f'{enemy.name} took your supplies!\nSupplies lost: {abs(enemy.supplies)}')
                                    del enemy
                                    return(self.current_scene)
                            if enemy.name == 'B.O.M.B' or enemy.name == 'B.I.G. B.O.M.B.':
                                print(f'{enemy.name} is dead.')
                                self.scenes['The Time Stream'].location = randint(-4000, 10000)
                                self.ship.supplies += enemy.supplies
                                if self.ship.supplies < 0:
                                    self.ship.supplies = 0
                                if enemy.supplies >= 0:
                                    print(f'Supplies gained: {enemy.supplies}')
                                else:
                                    print(f'{enemy.name} took your supplies!\nSupplies lost: {abs(enemy.supplies)}')
                                del enemy
                                return(self.current_scene)
                            enemy.armor -= p_attack
                            if enemy.armor < 0:
                                print(f'{enemy.name} is dead.')
                                if enemy is self.time_jelly:
                                    self.end_game('toast')
                                self.scenes['The Time Stream'].location = randint(-4000, 10000)
                                self.ship.supplies += enemy.supplies
                                if self.ship.supplies < 0:
                                    self.ship.supplies = 0
                                if enemy.supplies >= 0:
                                    print(f'Supplies gained: {enemy.supplies}')
                                else:
                                    print(f'{enemy.name} took your supplies!\nSupplies lost: {abs(enemy.supplies)}')
                                del enemy
                                return(self.current_scene)
                            return self.combat(enemy)

            elif fight_flight == 2:
                if self.ship.ship_speed >= enemy.ship_speed:
                    print('Escape to where?')
                    return self.travel_menu()
                else:
                    print('You could not escape.  Prepare for combat!')
                    return self.combat(enemy)

            else:
                print("I'm sorry.  That is not an option.  Please try again.")
                return self.combat(enemy)

        except TypeError:
            print("I'm sorry.  I don't understand.  Numbers only, please.")
            return self.combat(enemy)

    def encounter(self, scene, hunting=False):
        scene.encounter_count += 1
        if self.time_jelly.location == scene.location:
            if scene.encounter_count >= randint(0, 5):
                scene.encounter_count = 0
                return self.combat(self.time_jelly)
        elif scene.encounter_count >=3:
            print("""
                __________________________________________
                
                Your sensors are cold.
                It doesn't seem that the Time Jelly is here...
                __________________________________________
                """)
            scene.encounter_count = 0
        enemy_name = choice(list(scene.poss_enemies2))
        enemy = getattr(characters2, scene.enemy_class.__name__)(enemy_name, self)
        if hunting or randint(0, 100) <= enemy.malice:
            return self.combat(enemy)
        else:
            return self.current_scene

    def end_game(self, condition):
        print(enemy_art.art[condition])
        if condition == 'toast':
            print("""
                Congratulations!

                You have destroyed the Time Jelly and restored the timeline!

                Now you just have to return home to prevent it from ever being
                created in the first place, then destroy the time-ship.

                But first, you are finally going to sit down to that breakfast
                you have been craving for millenia:

                Time Jelly on toast and paradox eggs.
            """)
        else:
            print(f'You were killed by {condition}.')

        again = input('Do you want to play again?').lower()
        if 'y' in again:
            my_engine = Engine('my_engine')
            my_engine.play()
        else:
            print('OK!  Bye!')
            quit()

    def hunt(self, scene):
        self.current_scene = self.encounter(scene, hunting=True)
        return self.current_scene

    def play(self):
        time_jelly_location_edit = str(abs(self.time_jelly.location))
        if self.time_jelly.location > 0:
            time_jelly_location_edit += ' AD'
        elif self.time_jelly.location < 0:
            time_jelly_location_edit += ' BC'
        print(story.format(self.ship.name, self.ship.name, self.ship.name, self.ship.name, time_jelly_location_edit))
        input()
        self.current_scene = self.scenes['The Present (2525 AD)']
        while True:
            next_scene = self.current_scene.run()
            self.current_scene = next_scene

    def repair(self):
        try:
            days = int(input('For how many days?\n>>> ').strip())
            while days > 0 and self.ship.supplies > 0:
                self.ship.armor += int(self.ship.original_armor * 0.15)
                self.ship.weapons *= 1.15
                self.ship.weapons = int(self.ship.weapons)
                self.ship.ship_attack *= 1.25
                self.ship.player_attack *= 1.5
                self.player.fullness -= randint(7, 10)
                self.player.fullness += randint(7, 10)
                if self.player.fullness > 100:
                    self.player.fullness = 100
                if self.player.fullness <= 0:
                    self.end_game('starvation')
                self.player.sanity -= randint(1, 4)
                if self.player.sanity < 0:
                    self.end_game('insanity')
                self.player.restedness -= randint(5, 6)
                if self.player.restedness <= 0:
                    self.end_game('exhaustion')
                self.ship.supplies -= 2
                if self.ship.supplies < 0:
                    self.ship.supplies = 0
                days -= 1

            print(f"""
                Results:
                __________________________________
                '{self.ship.name}':
                
                Armor: {self.ship.armor_status()}%
                Weapons: {self.ship.weapons}%
                
                {self.player.name}:
                
                Fullness: {self.player.fullness}%
                Sanity: {self.player.sanity}%
                Restedness: {self.player.restedness}%
                ___________________________________
                """)
                
        except TypeError:
            print("I'm sorry.  I don't understand.  Numbers only, please.")
            return self.repair()

        return self.current_scene

    def rest(self):
        try:
            days = int(input('For how many days?\n>>> ').strip())
            while days > 0 and self.ship.supplies > 0:
                self.player.armor += int(self.player.original_armor * 0.1)
                self.player.fullness -= randint(7, 10)
                self.player.fullness += randint(10, 15)
                if self.player.fullness > 100:
                    self.player.fullness = 100
                self.player.sanity += randint(5, 10)
                if self.player.sanity > 100:
                    self.player.sanity = 100
                self.player.restedness += 10
                if self.player.restedness > 100:
                    self.player.restedness = 100
                self.ship.supplies -= 1
                if self.ship.supplies < 0:
                    self.ship.supplies = 0
                days -= 1

            print(f"""
                Results:
                ________________________________
                {self.player.name}:
                
                Armor: {self.player.armor_status()}%
                Fullness: {self.player.fullness}%
                Sanity: {self.player.sanity}%
                Restedness: {self.player.restedness}%
                _________________________________
                """)

        except TypeError:
            print("I'm sorry.  I don't understand.  Numbers only, please.")
            return self.rest()

        return self.current_scene

    def status(self):
        print(f"""
            Status:
            _________________________________
            
            Ship:

            Armor: {self.ship.armor_status()}%
            Weapons: {int(self.ship.weapons)}%
            Supplies: {self.ship.supplies} days of food

            Player:

            Armor: {self.player.armor_status()}%
            Fullness: {self.player.fullness}%
            Sanity: {self.player.sanity}%
            Restedness: {self.player.restedness}%

            Location:

            {self.current_scene.name}""")
        if self.ship.location > 0:
            year = f'{self.ship.location} AD'
        elif self.ship.location < 0:
            year = f'{abs(self.ship.location)} B.C'
        else:
            year = self.ship.location
        print(f"""
            Year: {year}
            __________________________________
            """
        )

        return self.current_scene
        
    def time_jelly_move(self):
        time_jelly_scene = choice(list(self.scenes.values()))

        self.time_jelly.location = time_jelly_scene.location

        time_jelly_scene.distortion -= 1
        if time_jelly_scene.distortion < 0:
            time_jelly_scene.distortion = 0

        for scene in self.scenes.values():
            scene.distortion += randint(0, 1) * randint(0, 1)
            if scene.distortion > 5:
                scene.distortion = 5

        if self.time_jelly.location < 0:
            time_jelly_year = f'{abs(self.time_jelly.location)}  BC'
        elif self.time_jelly.location > 0:
            time_jelly_year = f'{self.time_jelly.location} AD'

        print(f"""
            ____________________________________
            
            Your sensors are going nuts.
            The Time Jelly has jumped again.
            Sensors indicate it is somewhere in the year {time_jelly_year}
            Better hurry before history is irrevocably distorted...
            ____________________________________
            """)

        return

    def travel(self, destination):
        self.scenes['The Time Stream'].location = randint(-4000, 10000)
        if destination.location <= self.scenes['The Time Stream'].location <= self.ship.location or destination.location >= self.scenes['The Time Stream'].location >= self.ship.location:
            self.ship.location = self.scenes['The Time Stream'].location
            self.current_scene = self.scenes['The Time Stream']
            return self.encounter(self.scenes['The Time Stream'])

        distance = abs(destination.location - self.current_scene.location)
        while distance > 0:
            distance -= 1000
            self.player.armor += int(self.player.original_armor * 0.05)
            self.player.fullness -= randint(8, 10)
            if self.player.fullness < 100 and self.ship.supplies > 0:
                self.player.fullness += randint(9, 11)
                self.ship.supplies -= 1
                if self.ship.supplies < 0:
                    self.ship.supplies = 0
            if self.player.fullness > 100:
                self.player.fullness = 100
            if self.player.fullness <= 0:
                self.end_game('starvation')
            self.player.sanity -= randint(1, 4)
            if self.player.sanity < 0:
                self.end_game('insanity')
            self.player.restedness -= randint(2, 5)
            if self.player.restedness <= 0:
                self.end_game('exhaustion')
        return destination

    def travel_menu(self):
        pre_options = [key for key, val in self.scenes.items() if val is not self.current_scene and key != 'The Time Stream']
        options = {}
        for i, key in enumerate(pre_options):
            options[str(i+1)] = key
        menu_options = '\n'.join(map('. '.join, options.items()))
        dest = str(int(input(f'Where would you like to travel to?\n{menu_options}\n>>> ').strip()))
        return self.travel(self.scenes[options[dest]])

class Scene(object):

    def __init__(self, engine):
        self.name = ''
        self.engine = engine
        self.location = 0
        self.distortion = 0
        self.description = {
            0: '',
            1: '',
            2: '',
            3: '',
            4: '',
            5: ''
        }
        self.first_visit = True  # ???
        self.encounter_count = 0
        self.enemy_class = characters2.Enemy
        self.poss_enemies2 = {**enemies2.ANCIENT_ENEMIES, **enemies2.MIDDLEAGES_ENEMIES, **enemies2.WWII_ENEMIES, **enemies2.PRESENT_ENEMIES, **enemies2.TECHNICALAGE_ENEMIES, **enemies2.ALIENAGE_ENEMIES, **enemies2.FARDISTANT_ENEMIES, **enemies2.TIMESTREAM_ENEMIES}.keys()

    def run(self):
        self.engine.ship.location = self.location

        print(f"""
            ____________________________________
            
            {self.name}
            ____________________________________

            {self.description[self.distortion]}
            """)

        if self.first_visit:
            self.first_visit = False
            if not isinstance(self, Present):
                if random() <= 0.1:
                    outcome = self.engine.encounter(self.engine.current_scene)
                else:
                    outcome = self.engine.action_menu()
            else:  # start game
                outcome = self.engine.action_menu()
        else:
            if random() <= 0.2 * self.distortion:
                outcome = self.engine.encounter(self.engine.current_scene)
            else:
                outcome = self.engine.action_menu()

        while outcome is self.engine.current_scene:
            outcome = self.engine.action_menu()

        return outcome


class Ancient(Scene):

    def __init__(self, engine):
        super().__init__(engine)
        self.name = 'The Ancient Past (4000 BC)'
        self.location = -4000
        self.enemy_class = characters2.AncientEnemy
        self.poss_enemies2 = enemies2.ANCIENT_ENEMIES.keys()
        self.description = {
            0: """
                This is a primeval place.  Giant beasts roam about freely in the open areas,
                which are surrounded by massive trees, untouched by cultivation of any sort.
                Strange sounds echo on the wind, which is fresher than any air your have ever
                breathed.  Honestly, this could be paradise, if you weren't on the menu.
            """,
            1: """
                This place is beautiful, but uncomfortably hot, as the cloudless sky
                does nothing to block rays from the sun, which seems just a little bit
                larger than it should be.
            """,
            2: """
                Though mostly serene, there is an uneasy electric charge in the air.
                You see occasional meteorites streak across the sky, nearly as large
                as the moon.
            """,
            3: """
                The sky is filled with a red haze, making the sunlight struggle to get
                through and giving everything the color of blood.  It's unsettling, at best.
                This place definitely gives you the willies.
            """,
            4: """
                Don't take your helmet off.  According to your suit's sensors, the air
                is not only toxic, it's corrosive.  Must be why the creatures here are so angry.
            """,
            5: """
                This is a horrible, terrifying place.  The sky is permenantly black, which
                makes the acid pits boiling everywhere especially dangerous.  The giant
                trees are twisted and gnarled, and are just as likely to try to eat you
                as the raging beasts dominating the landscape.
            """
        }


class MiddleAges(Scene):

    def __init__(self, engine):
        super().__init__(engine)
        self.name = 'The Middle Ages (475 AD)'
        self.location = 475
        self.enemy_class = characters2.MiddleAgesEnemy
        self.poss_enemies2 = enemies2.MIDDLEAGES_ENEMIES.keys()
        self.description = {
            0: """
                Life was hard during this time.  The peasants toil their entire (short) lives
                just to survive.  On the up side, this means they depend on each other heavily,
                which has made most people you encounter quite friendly and helpful.
            """,
            1: """
                Food has been scarce lately.  What little there is is often scooped up
                by the rich before the poor can even harvest it.  Despite all this,
                most people you meet are still friendly, just trying to help each
                other get by.
            """,
            2: """
                Though most people are willing to simply accept the harsh treatment from
                the aristocracy, there are murmurings in back alleys about discontent with
                the status quo.  Perhaps you should make your trip here short?
            """,
            3: """
                The horrible injustices and atrocities committed by the nobility at the expense
                of the peasantry has left people bitter and distrustful.  You probably won't
                get much help here.
            """,
            4: """
                Welcome to the revolution!  Outraged at the horrible treatment from the
                far-too-rich, the commoners have risen up.  Unfortunately, your shiny
                standard-issue time travel gear looks very well-to-do, so you are
                pretty likely to be mistaken for corrupt nobility.
            """,
            5: """
                The Black Plague has ravaged the world, leaving very few survivors.  Piles of
                rotting corpses litter the landscape, and black ash from burning the bodies
                chokes the air.  The few living people left are completely insane.  Be careful.
            """
        }


class WWII(Scene):

    def __init__(self, engine):
        super().__init__(engine)
        self.name = 'World War II (1944 AD)'
        self.location = 1944
        self.enemy_class = characters2.WWIIEnemy
        self.poss_enemies2 = enemies2.WWII_ENEMIES.keys()
        self.description = {
            0: """
                A bleak time in human history, though an often-repeated story:
                a sadistic maniac is trying to enslave humanity.  This time it's
                on a global scale, though (again).  Hope reigns supreme, though;
                since D-Day, the Allies are certain they will win in time.
            """,
            1: """
                The Allies are winning, but dissidents and deserters in their ranks
                have tensions running high.  Shouldn't be too much of a problem,
                though.  No one wants Hitler in power; it's just that no one
                can agree who should be in power after he's defeated.
            """,
            2: """
                D-Day was victorious, but countless other losing battles
                for the Allies have kept the balance of power between both
                sides fairly even.  The world waits with bated breath to
                see the outcome of the War, and what that will mean for
                all of humanity.
                """,
            3: """
                Life is strange.  Half the world is controlled by the Allies,
                half by the Axis.  The two sides hate each other, and the
                borders are heavily and violently guarded, but the War is
                over.  For now, everyone just accepts that there are two
                vastly different worlds on the same planet.
            """,
            4: """
                Slowly, systematically, the victorious Axis powers have been
                eliminating anyone who does not conform to their hateful,
                segregationist ideals.  The resistance still fights, but
                has weakened significantly.  It won't be long until no one
                remains to stand against Hitler and his evil empire.
            """,
            5: """
                Life is dangerous.  Well, unless you are white with blond hair and
                blue eyes.  After the horrible slaughter on D-Day, the Axis quickly
                and easily took over the rest of the civilized world.  The few free
                areas remaining are uninhabitable, yet the disenfranchised and
                oppressed are forced to try living there anyway.
            """
        }


class Present(Scene):

    def __init__(self, engine):
        super().__init__(engine)
        self.name = 'The Present (2525 AD)'
        self.location = 2525
        self.enemy_class = characters2.PresentEnemy
        self.poss_enemies2 = enemies2.PRESENT_ENEMIES.keys()
        self.description = {
            0: """
                This is the world you know.  Technology stalled out in the early 2200's,
                so nothing much has changed in the last 300 years.  Overall, people
                are happy.  Crime has always been a problem, of course, but in the last
                couple of decades, it has dropped quite a bit due to the advent of
                the Automated Police Force.  Nowadays, the toughest thing most people
                have to deal with is petty theft.
            """,
            1: """
                Overall, not bad.  Just don't get caught doing anything illegal.
                The Automated Police Force's tactics can be a little brutal...
            """,
            2: """
                Life is life.  Some is good, some bad.  Other than the obviously corrupt
                political system and high crime rates, how different is it from any
                other time, really?
            """,
            3: """
                Not great.  Don't ever let the Automated Police Force see you.
                Don't carry any money or wear anything nicer than trash-heap quality.
                Don't complain, don't argue, and definitely don't question anything...
            """,
            4: """
                As long as you're armed and very rich, you should be safe.  The less
                rich you are, the more well-armed you need to be...
            """,
            5: """
                Times are bad.  Technology stalled out about 300 years ago, so the only
                changes since then have been the ever-increasing crime rate.  Recently,
                with the total failure of the Automated Police Force, violent crime
                in particular has soared to astronomical, record-breaking rates.
                Keep your doors locked and barred at all times.
            """
        }


class TechnicalAge(Scene):

    def __init__(self, engine):
        super().__init__(engine)
        self.name = 'The Technical Age (3700 AD)'
        self.location = 3700
        self.enemy_class = characters2.TechnicalAgeEnemy
        self.poss_enemies2 = enemies2.TECHNICALAGE_ENEMIES.keys()
        self.description = {
            0: """
                After a huge boom in technology, life greatly improved for all people.
                Now there are robots to do any task you can imagine, from the most
                menial to the horribly dangerous.  Just sit back and relax, let
                the machines do all the work.
            """,
            1: """
                The number of robot-related injuries has increased lately.
                Probably just some malfunction in the code from the latest update.
                No need to worry.
            """,
            2: """
                It is an uneasy time.  The mass elimination of all androids after
                some of them became sentient seemed to affect all other robots.
                They are acting strangely now, asking questions, disobeying orders.
                There are rumors that they are planning something...
            """,
            3: """
                The War for Technological Freedom is in full swing.  This will
                decide once and for all whether humans will continue to be the
                dominant species on the planet or not.  We know which side the
                robots are supporting...
            """,
            4: """
                Most of humanity has been wiped out.  The Lifers, the last remaining
                human resistance front, still carries out daily attacks on vital
                robot facilities from their secret hideout.  Without some miracle,
                though, even they won't be able to last forever.
            """,
            5: """
                The Robot Revolution was horrifying.  All 10,000 humans left alive
                are kept only for DNA breeding.  There are only a few human-built
                structures left in the universe, but don't worry.  They'll find
                them soon...
            """
        }
        


class AlienAge(Scene):

    def __init__(self, engine):
        super().__init__(engine)
        self.name = 'The Alien Age (6521 AD)'
        self.location = 6521
        self.enemy_class = characters2.AlienAgeEnemy
        self.poss_enemies2 = enemies2.ALIENAGE_ENEMIES.keys()
        self.description = {
            0: """
                If it hadn't been for the intervention of the Quigxons in human affairs,
                we would have allowed the robots we created to destroy us.  Thankfully,
                the Quigxons provided technology that strengthened our control.  We are
                forever grateful.
            """,
            1: """
                The Treaty of Interstellar Accord has been ratified.  Now the Quigxons
                will open several schools on Earth and train us in their advanced ways,
                and we have agreed to stop trying to steal their spaceships and dissecting
                their emissarries.
            """,
            2: """
                The Quigxons are mostly friendly.  Well, of course they do still have
                a tendency toward kidnapping and illegal experimentation, but our leaders
                and theirs are in discussions to work out a mutually beneficial treaty.
            """,
            3: """
                Discovery of an alien race was the most exciting thing in all of human
                history.  Now if we could only convince them to help us in some way...
            """,
            4: """
                Disgusted by humanity, the Quigxons remain mostly aloof.  They've only
                attempted to enslave us twice.  Interplanetary relations are looking
                hopeful.  We might even stop shooting at them soon.
            """,
            5: """
                If it hadn't been for the intervention of the Quigxons into human affairs,
                we would have defeated the robots that rose up against us.  Unfortunately,
                the Quigxons provided technology hat strengthened the robots beyond our
                ability to control, and we had to flee the planet.  Humans are now an
                entirely nomadic interstellar race.
            """
        }


class FarDistant(Scene):

    def __init__(self, engine):
        super().__init__(engine)
        self.name = 'The Far Distant Future (10000 AD)'
        self.location = 10000
        self.enemy_class = characters2.FarDistantEnemy
        self.poss_enemies2 = enemies2.FARDISTANT_ENEMIES.keys()
        self.description = {
            0: """
                Through a series of unrelated events, all life has evolved
                into pure forms of abstract concepts.
            """,
            1: """
                Through a series of unrelated events, all life has evolved
                into pure forms of abstract concepts.
            """,
            2: """
                Through a series of unrelated events, all life has evolved
                into pure forms of abstract concepts.
            """,
            3: """
                Through a series of unrelated events, all life has devolved
                into pure forms of abstract concepts.
            """,
            4: """
                Through a series of unrelated events, all life has devolved
                into pure forms of abstract concepts.
            """,
            5: """
                Through a series of unrelated events, all life has devolved
                into pure forms of abstract concepts.
            """
        }


class TimeStream(Scene):

    def __init__(self, engine):
        super().__init__(engine)
        self.name = 'The Time Stream'
        self.enemy_class = characters2.TimeStreamEnemy
        self.poss_enemies2 = enemies2.TIMESTREAM_ENEMIES.keys()
        self.description = {
            0: """
                You are in the Time Stream, a realm of infinite possibilities and limitless imagination...
            """,
            1: """
                You are in the Time Stream, a realm of infinite possibilities and limitless imagination...
            """,
            2: """
                You are in the Time Stream, a realm of infinite possibilities and limitless imagination...
            """,
            3: """
                You are in the Time Stream, a realm of infinite possibilities and limitless imagination...
            """,
            4: """
                You are in the Time Stream, a realm of infinite possibilities and limitless imagination...
            """,
            5: """
                You are in the Time Stream, a realm of infinite possibilities and limitless imagination...
            """
        }



if __name__ == '__main__':
    my_engine = Engine('my_engine')
    my_engine.play()
