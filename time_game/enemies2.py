from random import randint


def classes(text):
    return eval(text)

# (armor, ship_attack, player_attack, is_ship, supplies_provided, description)
ANCIENT_ENEMIES = {
    'Ankylosaurus': (46, 36, 15, True, 100, "A tank-like dinosaur with heavy armor plating on its back and a large club on its tail."),
    'Tyrannosaurus Rex': (31, 40, 41, False, 100, "A giant carnivore with massive razor-sharp teeth and tiny, mostly insignificant arms."),
    'Stegosaurus': (34, 16, 26, False, 100, "An herbivore with armor plates along its spine and long spikes on its tail."),
    'Deinonychus': (16, 33, 22, False, 100, "An extremely smart, super fast predator with nearly human-like hands."),
    'Triceratops': (39, 39, 13, False, 100, "A sturdy herbivore with three large horns on its head in front of a large armor plate."),
    'Pachycephalosaurus': (37, 31, 20, False, 100, "A roughly human-sized dinosaur with a hard, helmet-like head and a bad temper"),
    'Pteranodon': (22, 20, 17, False, 100, "An airborne dinosaur, gliding in for the kill.")
}

MIDDLEAGES_ENEMIES = {
    'Dragon': (37, 42, 39, True, 100, "The stuff of legends.  A flying, fire-breathing giant reptile."),
    'Evil Knight': (26, 15, 28, True, randint(0, 5), "Mobile human tank."),
    'Evil Wizard': (4, 25, 32, False, randint(0, 1), "Absolute magic corrupts absolutely."),
    'Pikeman': (17, 19, 12, False, randint(0, 2), "Battlefield fodder, except against cavalry."),
    'Plague Mob': (30, 44, 48, True, randint(0, 5), "Better for them to kill you than catch you..."),
    'Giant Rat': (6, 10, 9, False, randint(1, 2), "Probably the reason Plague Mobs exist."),
    'Bugbear': (25, 14, 18, False, 50, "What is it?  Big, ugly and mean, that's what.")
}

WWII_ENEMIES = {
    'Nazi Panzer Brigade': (40, 45, 45, True, 3, "German  tank unit."),
    'Nazi Grenadier Brigade': (28, 24, 31, False, 3, "German armored elite infantry unit."),
    'Nazi Lehr-Brigade': (23, 18, 36, False, 3, "German elite tactical unit."),
    'Italian Rifle Battalion': (18, 17, 27, False, 3, "Duck and cover!"),
    'Italian A.S. 42 Division': (20, 37, 19, False, 3, "Renowned Italian Anti-Aircraft unit."),
    'Japanese Bomber Squadron': (29, 11, 35, True, 2, "Unfair from the air."),  # strong against player
    'Japanese Kamikaze Squadron': (19, 38, 25, True, 0, "They'll die either way.  Will you?")
}

PRESENT_ENEMIES = {
    'An Army of Bureaucrats': (48, 51, 16, False, 0, "It's all in the people's best interests..."),
    "Kim Kardashian's Legal Team": (49, 4, 23, False, 5, "A.k.a. 'How to Get Away with Anything' Special P.R. Dept."),
    'The Red Tape Monster': (51, 34, 5, True, randint(-5, 0), "We all have to deal with it.  Can someone please just kill it?"),
    'PETA': (7, 35, 4, False, 10, "They were going to call themselves 'People for the Raising of Animals to a Status No Human can Ever Hope to Achieve', but the acronym wasn't pronouncable."),
    "Donald Trump's Hair": (3, 3, 6, False, 0, "It IS just hair, right?"),
    'Entitled Millennials': (5, 13, 7, True, randint(1, 5), "**sigh**  What about what _I_ want?"),
    'InstaTwit VineFace ChatrApp': (50, 2, 56, False, 0, "A Sentient Social Media monster.  Never let it see you...")
}

TIMESTREAM_ENEMIES = {
    'Time Twister': (9999, 9999, 9999, False, 0, "A twister through time.  Kinda self-explanatory.  Also kinda impossibly huge."),
    'White Rabbit': (9, 5, 34, False, 2, "...in a peacoat, no less."),
    'Time Sentinel': (24, 27, 21, True, 0, "He guards your lost Faux-lex"),
    'Chronodragon': (45, 53, 47, False, randint(-15, 15), "A bigger, nastier, more punctual version of a classic ridiculously hard foe."),
    'Tick': (41, 6, 40, False, 0, "No, not the insect, or the super hero."),
    'Tock': (42, 46, 3, True, 1, "What do you want to tock about?"),
    'Uhluhtc': (55, 7, 49, False, -45, "Nevermind that his name sounds like a sneeze.  He eats everything, so maybe run?"),
    'Echo': (1, 1, 1, False, 0, "You are staring at you staring at you staring at you staring...")
}

TECHNICALAGE_ENEMIES = {
    'Whirly-Chopper': (21, 21, 33, False, 0, "The name says it all."),
    'Smash-o-matic': (33, 43, 30, True, 0, "Maniacal robots are not original in naming their creations."),
    'Burglebot': (13, 32, 11, False, randint(-10, -5), "It steals things."),
    'S.U.R.F.': (8, 28, 8, False, 2, "Super Ultra Robot Frobnicator"),
    'Robo-Tank': (43, 49, 24, True, 0, "It's a robot AND a tank!  Two for the price of one!"),
    'B.O.M.B.': (2, 41, 46, False, 0, "Blast-o-matic Omni-directional Massive Boom-maker"),
    'B.I.G. B.O.M.B.': (54, 56, 55, True, 0, "Burst Initialized Gravitron Blast-o-matic Omni-directional Massive Boom-maker")
}

ALIENAGE_ENEMIES = {
    'Gray Humanoid': (11, 9, 43, False, 30, "Kinda looks like us?"),
    'Green Humanoid': (12, 22, 14, False, 20, "Rather lizard-like."),
    'Something tentacle-y': (32, 48, 53, True, randint(-5, 1), "What IS this thing?!"),
    'Venusians': (14, 23, 10, False, 75, "Femaliens."),
    'Space Blob': (38, 47, 42, True, randint(0, 7), "Something icky this way comes..."),
    'Blob Space': (52, 54, 52, False, -5, "A whole lotta ickiness."),
    'Probion': (15, 12, 37, False, 8, "Source of a lot of rumors.")
}

FARDISTANT_ENEMIES = {
    'Intellect': (44, 29, 54, False, 0, "Pure, concentrated thought."),
    'Force': (47, 50, 51, True, 0, "What moves you."),
    'Emotion': (53, 8, 44, True, 0, "Every experience at once."),
    'Mass': (35, 52, 2, True, 0, "The stuff that stuff is made of."),
    'Control': (36, 30, 29, False, 0, "All your base belong to us."),
    'Voice': (10, 55, 38, False, 0, "A self-sustaining, self-aware highly entertaining TV show, or a sound at ridiculous volume."),
    'Illusion': (56, 26, 50, False, 0, "These are not the droids you're looking for...")
}

TIME_JELLY = {
    'Time Jelly': (100, 0, 0, True, 0, "THIS is the source of all these problems?")
}