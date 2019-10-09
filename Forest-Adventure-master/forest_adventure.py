from random import random, randrange, choice
from sys import argv

'''global variables'''
script, player = argv
prompt = "Which way will you go? "
directions = {
    'North': 0,
    'N': 0,
    'East': 1,
    'E': 1,
    'West': 2,
    'W': 2,
    'South': 3,
    'S': 3
}
unicorns_blessing = False
fish = False
lost = False
pie = False
knife = False


'''room functions'''

def unicorn():
    global unicorns_blessing
    print("""
You are alone.  And then, you are not alone.
Magic swirls, and an enormous white unicorn
materializes before you.  He looks at you,
and from somewhere deep inside your heart,
a gentle yet powerful voice speaks:

"Which is better?  A beautiful woman with no
wisdom, or a wise woman with no beauty?"
""")
    
    beauty = input('1.  Wisdom is its own beauty.\n2.  A beautiful woman can get what she wants without having to think.\n? ')

    print("""
The voice speaks again:

"I see.  Is it better to have nothing but hope,
or everything without joy?"
""")

    hope = input('1.  Hope and faith can accomplish anything.\n2.  The joy is in the having of things that make you happy.\n? ')

    print("""
Once more the voice comes to you:

"Understood.  And who is the better artist:
a child or an established professional?"
""")

    art = input('1.  That depends on whether or not the professional draws from the heart.\n2.  Obviously, practice makes perfect.\n? ')

    if '1' in beauty and '1' in hope and '1' in art:
        print("""
The voice sounds as if it smiling:

"You truly understand the important things in life.
May unseen doors open for you, and no harm befall you in your journey.
""")

        unicorns_blessing = True

    else:
        print("""
The voice sounds disappointed:

"Perhaps you should think about your answers,
and come back when you are ready."
""")

    print("In the blink of an eye, the unicorn is gone.\n\nAvailable paths: ", *paths('unicorn'))

    print("_"*25)
    choose = input(prompt).strip().title()
    print("_"*25)

    movement('unicorn', directions[choose])

def fishing_hole():
    global fish

    print("""
This is one of the most peaceful places you have ever been.
Fish swim throughout the crystalline waters, casting rainbows
in every direction.  A simple pole rests against a nearby tree.
""")

    go_fishing = input("Do you fish? ").strip().title()

    if "Y" in go_fishing:
        if fish:
            print("You catch another beautiful trout, but you release it.\nTwo big fish are too much to carry.\n")
        else:
            print("You catch an amazing trout nearly as long as your arm.\n")

    print("Available paths:\n", *paths('fishing_hole'))

    print("_"*25)
    choose = input(prompt).strip().title()
    print("_"*25)

    movement('fishing_hole', directions[choose])

def treant():
    print("""
A large, gnarled tree with a frightening face seems
to be sleeping here.  Four steps into the glade,
and you snap a twig.  The sound seems to echo, and
the mighty treant awakes.  It stands, growls, and
smashes its trunk-sized limbs down straight at you.

You dodge successfully, but now the treant is between
you and your exit to the South.

Available paths: 
""", *paths('treant'))

    print("_"*25)
    choose = input(prompt).strip().title()
    print("_"*25)

    if choose == "South" or choose == 'S':
        if unicorns_blessing:
            print("There is a bright flash of light, and you feel the unicorn run past you toward the treant.")
            dryad()
        else:
            death('treant')

    elif choose == 'East' or choose == 'E':
        print("The treant chases you for quite a while, but finally turns back.")
        pit()

def pit():
    print("""
You are in a large, flat, barren stretch of land.
The forest to the North is too dense to continue any further.
A massive pile of junk blocks your way to the East.

Available paths: 
""", *paths('pit'))

    input(prompt)

    fall_in_pit()

def goblin():
    print("""
The path dead-ends into a small clearing with a small
hut in the center.  A short, wart-covered goblin sits
on the front porch, smoking a pipe almost four times
as long as she is tall.  She looks up at you with a start,
then runs inside.  A moment later she returns with a bag
of random pots, pans, and other kitchen utensils, which
she promptly begins to hurl at you.

"You won't trick me again, you stupid stinking, filthy
fairies!" she screams.  You beat a hasty retreat back
to the battlefield.
""")

    print("_"*25)
    input()
    print("_"*25)

    battlefield()

def rainbow():
    print("""
As you walk, something happens.  You're not sure what,
but whatever it is feels amazing, magical.  When you
come to your senses, you are standing on top of what
could be the world's largest rainbow. The view is glorious.

Available paths: 
""", *paths('rainbow'))

    print("_"*25)
    choose = input(prompt).strip().title()
    print("_"*25)

    movement('rainbow', directions[choose])

def waterfall():
    print("""
An enormous waterfall here stretches to the heavens.
The spray from it creates more rainbows than you could
ever count, and the pool beneath it looks like glass.
The pool continues into a clearing to the North, where
you can see hundreds of fish swimming in sparkling schools.

Available paths:
""", *paths('waterfall'))

    print("_"*25)
    choose = input().strip().title()
    print("_"*25)

    movement('waterfall', directions[choose])

def dryad():
    print("""
The trees here are very odd.  If it wasn't crazy,
you would almost think they looked like people.
Before you can totally dismiss that thought,
a woman steps out of the tree in front of you.
She is made out of wood, and looks as if she was
expertly carved by a master woodcarver.

She speaks, and her voice is like the rustling of the leaves:

"Welcome to Sylvana.  You are welcome to look around,
but unfortunately we have nothing here that
would be useful to you.  Just don't wake the treant.

With that, she steps back into the tree and disappears.

Available paths: 
""", *paths('dryad'))

    print("_"*25)
    choose = input(prompt).strip().title()
    print("_"*25)

    movement('dryad', directions[choose])

def warning_sign():
    print("""
The path branches here.  Lying on the ground at the
intersection, right next to the hole it was pulled
from, is a broken and heavily defaced sign.  It's hard 
to read with all the grafitti, but what you can make
out is a green, heavily caricaturized goblin head
with sharp teeth, drooling, with two black eyes and
several blades embedded in it, several tiny fairies,
most of them trapped in nets or squashed like bugs,
and the letters "ANG" in between them.

Available paths: 
""", *paths('warning_sign'))

    print("_"*25)
    choose = input().strip().title()
    print("_"*25)

    movement('warning_sign', directions[choose])

def battlefield():
    print("""
This place is a war zone, or what's left of one, anyway.
At the South end, nearly everything is obliterated and
charred.  Splintered wood and broken bottles and barrels
litter the path, which continues on to an open field.
To the North, the plants are randomly mutated into
rather grotesque forms of their former selves, and what
looks like rainbow-colored paint is splattered everywhere.

Available paths: 
""", *paths('battlefield'))

    print("_"*25)
    choose = input().strip().title()
    print("_"*25)

    movement('battlefield', directions[choose])

def butterflies():
    print("""
You emerge into a beautiful clearing.  A crystal river sparkles
to the West.  Unfortunately, it is impossible to cross.
To the South, a sheer cliff stretches up past the clouds.
You see a gigantic rainbow in the distance to the North.
Butterflies fill the air, dancing without a care in the world.

Available paths: 
""", *paths('butterflies'))

    print("_"*25)
    choose = input(prompt).strip().title()
    print("_"*25)

    movement('butterflies', directions[choose])

def dark_forest():
    global lost

    print("""
It's dark.

Really dark.

The darkness is palpable, seeping into your pores like some
evil fluid.  You have no idea where you are, or where you can go.

Which way will you try?
""", *paths('dark_forest'))

    print("_"*25)
    choose = input().strip().title()
    print("_"*25)

    if unicorns_blessing:
        print("A ghostly vision of the unicorn shimmers in front of you, guiding you through.\n")
        movement('dark_forest', directions[choose])

    else:
        get_lost = random()

        if get_lost < 0.1:
            if lost:
                death('dark_forest')
            else:
                lost = True
                print("\nYou are hopelessly lost.\n")
                dark_forest()

        else:
            lost = False
            print("You somehow make it through.")
            movement('dark_forest', randrange(4))

def intro():
    print("""
You are a renowned adventurer.  You have traveled the entire world,
defating horrible monsters and acquiring vast treasures.  There is
almost nothing that you haven't seen or done, and almost nowhere you
haven't been.

It is for that reason that you have decided to seek what may be the
greatest treasure ever rumored to exist:

The Chalice of Malice.

According to legend, an interdimensional traveler with great power
was horribly mistreated while visiting a certain realm, and trapped
the entire dimension in tiny form in the bowl of a large golden cup.
Supposedly, the owner of the Chalice of Malice will have the power to
travel to this alternate world.

The new adventures to be had make your heart race!
""")

    start()

def start():
    print("""
You are in a dark forest.  Paths extend in all directions.

Available paths:
""", *paths('start'))

    print("_"*25)
    choose = input(prompt).strip().title()
    print("_"*25)

    movement('start', directions[choose])

def false_farm():
    print("""
The forest opens here to a large farm.  Sort of.  Upon closer
inspection, you realize that all the 'buildings' are actually
highly detailed cardboard cutouts.  Even the sign overhead seems
suspicious:

"REEL FARRM"

Hmmm...

Available paths:
""", *paths('false_farm'))

    print("_"*25)
    choose = input(prompt).strip().title()
    print("_"*25)

    movement('false_farm', directions[choose])

def fae():
    print("""
You walk into an open meadow full of resting butterflies.

"Hey, watch where you're walking!" a tiny voice squeaks.

Looking down, you realize that they're not butterflies
at all, but fairies.  Thousands of them, all armed with
various tiny weapons.  Most of them are sleeping, many
drooling.  Piles of pixie dust are everywhere.

"Hey, watch it!" another voice cries.

The fairies start to rouse, then wake each other.
As they all complain about being woken up, you
notice one voice repeating itself; it's the first
fairy that yelled at you:

"That ugly goblin sent a giant to step on us!
Hurry up!  Wake up and take it down!"

Realizing that he's talking about you, you decide
that the safest route is back the way you came.
""")

    print("_"*25)
    input()
    print("_"*25)
    
    battlefield()

def mountain_top():
    print("""
You are on a high mountain top.  The view is glorious.
To the North, you see an open field, full of color.
To the East, something sparkles in the clouds.
To the Southeast, you see something peeking through the trees.

Available paths:
""", *paths('mountain_top'))

    print("_"*25)
    choose = input(prompt).strip().title()
    print("_"*25)

    movement('mountain_top', directions[choose])

def cloud_castle():
    print("""
You're not sure how you got here, but you emerge literally
walking on clouds.  A beautiful castle stands before you,
made entirely out of snowflakes, with raindrop windows.

You try to knock on the shimmering gate, but your hand passes
right through.  A ghostly voice floats across the sky:

"I am sorry, mortal.  The splendors of this realm are not for
those living in the world of flesh."

Available paths:
""", *paths('cloud_castle'))

    print("_"*25)
    choose = input(prompt).strip().title()
    print("_"*25)

    movement('cloud_castle', directions[choose])

def fog():
    print("""
A thick fog envelops this whole area.  You can barely see
the path before you.  The path to the West seems to glow
slightly.  From the East, you smell fresh apple pie.

Available paths:
""", *paths('fog'))

    print("_"*25)
    choose = input(prompt).strip().title()
    print("_"*25)

    movement('fog', directions[choose])

def farm():
    global pie

    print("""
A quaint little farm lies before you.  No one is around.
""")

    if not pie:
        print("A fresh-baked Dutch apple pie sits on the window sill.\n")
        take_pie = input("Do you take the pie? ").strip().title()
        if "Y" in take_pie:
            pie = True
            print("\nMmm...delicious.\n")
        else:
            print("\nYeah, you shouldn't steal pies.\n")

    else:
        print("The window sill is empty.  I wonder why?\n")

    print("Available paths:\n", *paths('farm'))

    print("_"*25)
    choose = input(prompt).strip().title()
    print("_"*25)

    movement('farm', directions[choose])

def minotaur():
    print("""
You come upon a mammoth minotaur dancing alone in a magical light.
This thing is a giant, even by minotaur standards.  As you enter,
it sees you and stops.
""")

    if pie:
        print("""
The minotaur roars:

"THIEF!  YOU STOLE MY PIE!!  I CAN SMELL IT ON YOU!!!"

It charges.
""")

        if knife:
            print("""
The sword is too heavy for you to wield effectively, but it
does allow you to earn your escape.
""")
            movement('minotaur', randrange(4))

        elif unicorns_blessing:
            print("\nThe unicorn appears and battles the minotaur, allowing you to escape.\n")
            movement('minotaur', randrange(4))

        else:
            print("\n You try to outrun the ridiculously large ruminant.")
            if random() < 0.1:
                print("You succeed.\n")
                movement('minotaur', randrange(4))
            else:
                print("You fail.\n")
                death('minotaur')

    else: # no pie
        print("""
The breakdancing bovine waits exactly three beats, then resumes its disturbing gyrating.

You decide not to stick around.
""")
        print("_"*25)
        minotaur_cave()

def gnome():
    print("""
A gnome guards an iron door here.

Sort of.

A gnome is passed out in front of an iron door, his chair overturned,
his face planted firmly in the ground, his butt in the air.
A mug with a little very strongly smelling alcohol is turned on its
side to one side of him.  To the other, an iron key.
""")

    print("_"*25)
    door_choose = input("Do you use the key and go through the door?").strip().title()
    print("_"*25)

    if "Y" in door_choose:
        mumbles = []
        murmur = ''
        if unicorns_blessing:
            mumbles.append("You smell like a unicorn...")
        if knife:
            mumbles.append("That's a nice sword...")
        if fish:
            mumbles.append("Here, fishy, fishy, fishy...")
        mumbles.append("Don't lie to a dragon...")
        
        murmur = ':  {}'.format(choice(mumbles))

        print("As you grab the key, the gnome mumbles{}.".format(murmur))

        treasure()

    else: # no to door_choose
        print("\nAvailable paths:\n", *paths('gnome'))

        print("_"*25)
        choose = input(prompt).strip().title()
        print("_"*25)

        movement('gnome', directions[choose])

def miniature_village():
    print("""
You come to a tiny village.  Literally tiny - the tallest rooftops come
to your waist.  Someone shrieks, and all the doors and windows slam shut.
The only sign of life now is the smoke rolling from the chimneys.

Available paths:
""", *paths('miniature_village'))

    print("_"*25)
    choose = input(prompt).strip().title()
    print("_"*25)

    movement('miniature_village', directions[choose])

def dead_end():
    print("""
There is nothing here.  Why did you come this way?

Available paths:
""", *paths('dead_end'))

    print("_"*25)
    choose = input(prompt).strip().title()
    print("_"*25)

    movement('dead_end', directions[choose])

def haunted_forest():
    print("""
The forest takes a dark turn.  There are no leaves on the trees.
The branches look like claws and keep reaching toward you.
It may be the wind, but it sounds like screams.

Maybe you should just move on.

Available paths:
""", *paths('haunted_forest'))

    print("_"*25)
    choose = input(prompt).strip().title()
    print("_"*25)

    movement('haunted_forest', directions[choose])

def minotaur_cave():
    global knife

    print("""
You enter a huge cave.  An olympian mattress lies on the floor.
All around the walls are various weapons.  Most of them are too
big for you to even pick up with both hands.
""")

    if not knife:
        print("\nThe only one small enough for you to use is a (relatively) small dagger, which to you is a full-sized sword.")

        take_knife = input("\nDo you take the knife? ").strip().title()

        if "Y" in take_knife:
            knife = True
            print("\nIt's heavy, but you arm yourself with the blade.\n")
        else:
            print("\nOkay...I would have taken the weapon.\n")
    
    print("Available paths:\n", *paths('minotaur_cave'))

    print("_"*25)
    choose = input(prompt).strip().title()
    print("_"*25)

    movement('minotaur_cave', directions[choose])

def treasure():
    print("""
You enter into a massive room, filled to the brim with every treasure
imaginable.  Of course, a gigantic dragon rests upon the pile.

The dragon looks at you, and a harsh, intimidating voice resonates from
within the pit of your stomach:

"You are either very brave or very foolish, entering the lair of a dragon.
Honestly, I don't care which.  You're just in time for dinner."

The dragon unfurls and stretches, the slowly crawls toward you, licking its lips.
""")

    print("_"*25)
    dragon_choose = input("""
Choose quick:
1.  "I have the unicorn's blessing!"
2.  "Stay back or I'll kill you!"
3.  "You're hungry?  I have some food!"
4.  "Nope, not dealing with this" (FLEE)
? """).strip().title()
    print("_"*25)

    if '1' in dragon_choose:
        print("The dragon sniffs you deeply.")
        if unicorns_blessing:
            print("""
"So you do."

Suddenly, the dragon's entire appearance changes.  His scales soften,
his eyes grow large and liquid, and he nuzzles you.  He is surprisingly soft.

A soft voice floats across your ears:

"I love the unicorn.  She's awesome.  Take whatever you want.
""")
            win()

        else: # no unicorn's blessing
            print("LIAR!")
            death('dragon')

    elif '2' in dragon_choose:
        if knife:
            print("\nSo it's a fight you want?  Then so be it.\n")
            if random() < 0.25:
                print("Somehow, miraculously, you vanquish the dragon.")
                win()
            else:
                print("So, um, dragons are tough.")
                death('dragon')
        else:
            print("So, um, dragons are tough.  And you tried to fight one without a weapon...")
            death('dragon')

    elif '3' in dragon_choose:
        if fish:
            print("""
You offer the dragon your fish.  He sniffs it hungrily, thinks for a moment,
then takes it and flies away.
""")
            win()
        else:
            print("""
The dragon sniffs you.

"Of course you have food.  YOU are food."
""")
            death('dragon')

    else: # flee
        if random() < 0.75:
            print("The lazy dragon gives up the chase and you escape.")
            gnome()
        else:
            print("Hmmm... Probably should have laid off the pie.")
            death('dragon')

def abyss0():
    print("""
You fall for an impossibly long time.  Eventually you black out.
You awake in a terrible, dream-like place.
There is nothing in any direction.

Available paths: 
""", *paths('abyss0'))

    print("_"*25)
    choose = input(prompt).strip().title()
    print("_"*25)

    movement('abyss0', directions[choose])

def abyss1():
    print("""
The nothingness swirls around you so fast that you can't tell
if it's you or the world that's actually spinning.
You would give anything to just get your bearings,
if there were anything to reference, that is.

Available paths: 
""", *paths('abyss1'))

    print("_"*25)
    choose = input(prompt).strip().title()
    print("_"*25)

    movement('abyss1', directions[choose])

def abyss2():
    print("""
You launch into the air at breakneck speed.
Under different circumstances, flying would
probably be fun, but this simply makes you
extremely naseous.

Available paths: 
""", *paths('abyss2'))

    print("_"*25)
    choose = input(prompt).strip().title()
    print("_"*25)

    movement('abyss2', directions[choose])


'''engine functions'''

def paths(room):
    paths_dict = {
        'unicorn': ['South'],
        'fishing_hole': ['South'],
        'treant': ['East', 'South'],
        'pit': ['West', 'South'],
        'goblin': ['South'],
        'rainbow': ['North', 'South'],
        'waterfall': ['North', 'South'],
        'dryad': ['North', 'South'],
        'warning_sign': ['North', 'East', 'South'],
        'battlefield': ['North', 'West', 'South'],
        'butterflies': ['North', 'East'],
        'dark_forest': ['North', 'East', 'West', 'South'],
        'start': ['North', 'East', 'West', 'South'],
        'false_farm': ['North', 'West'],
        'fae': ['North'],
        'mountain_top': ['East', 'South'],
        'cloud_castle': ['North', 'East', 'West', 'South'],
        'fog': ['North', 'East', 'West', 'South'],
        'farm': ['West', 'South'],
        'minotaur': ['South'],
        'gnome': ['North', 'East'],
        'miniature_village': ['North', 'West'],
        'dead_end': ['North'],
        'haunted_forest': ['North', 'East'],
        'minotaur_cave': ['North', 'West'],
        'abyss0': ['North', 'East', 'West', 'South'],
        'abyss1': ['North', 'East', 'West', 'South'],
        'abyss2': ['North', 'East', 'West', 'South']
    }

    return paths_dict[room]

def movement(from_room, direction):
    def wrong_way():
        print("You can't go that way.\nAvailable paths: ", *paths(from_room))

        print("_"*25)
        choose = input(prompt).strip().title()
        print("_"*25)

        movement(from_room, directions[choose])

    move_to = {
        'unicorn': [wrong_way, wrong_way, wrong_way, rainbow],
        'fishing_hole': [wrong_way, wrong_way, wrong_way, waterfall],
        'treant': [wrong_way, pit, wrong_way, dryad],
        'pit': [wrong_way, wrong_way, treant, warning_sign],
        'goblin': [wrong_way, wrong_way, wrong_way, battlefield],
        'rainbow': [unicorn, wrong_way, wrong_way, butterflies],
        'waterfall': [fishing_hole, wrong_way, wrong_way, dark_forest],
        'dryad': [treant, wrong_way, wrong_way, start],
        'warning_sign': [pit, battlefield, wrong_way, false_farm],
        'battlefield': [goblin, wrong_way, warning_sign, fae],
        'butterflies': [rainbow, dark_forest, wrong_way, wrong_way],
        'dark_forest': [waterfall, start, butterflies, cloud_castle],
        'start': [dryad, false_farm, dark_forest, fog],
        'false_farm': [warning_sign, wrong_way, start, wrong_way],
        'fae': [battlefield, wrong_way, wrong_way, wrong_way],
        'mountain_top': [wrong_way, cloud_castle, wrong_way, gnome],
        'cloud_castle': [dark_forest, fog, mountain_top, miniature_village],
        'fog': [start, farm, cloud_castle, dead_end],
        'farm': [wrong_way, wrong_way, fog, haunted_forest],
        'minotaur': [minotaur_cave, haunted_forest, farm, fog],
        'gnome': [mountain_top, miniature_village, wrong_way, wrong_way],
        'miniature_village': [cloud_castle, wrong_way, gnome, wrong_way],
        'dead_end': [fog, wrong_way, wrong_way, wrong_way],
        'haunted_forest': [farm, minotaur_cave, wrong_way, wrong_way],
        'minotaur_cave': [minotaur, wrong_way, haunted_forest, wrong_way],
        'abyss0': [abyss2, abyss1, abyss1, abyss1],
        'abyss1': [abyss0, abyss0, abyss0, abyss2],
        'abyss2': [abyss1, abyss2, abyss1, rainbow]
    }

    move_to[from_room][direction]()



'''situation functions'''

def win():
    global script, player

    print("""
Congratulations!

You have found the legendary Chalice of Malice!

Now to see about this other world...




As you gaze into the bowl, you see an entire world unfold before you.

The longer you look, the larger everything gets.

Too late, you realize that you are not shrinking into this world,

it is expanding into yours.

Within moments, everything you have ever known sits neatly within

the tiny cup, and a new and entirely unfamiliar world is

exploding around you.

At your feet, you see an unfamiliar object.  It is rectangular, about

the size of your hand.  One side is smooth, shiny black glass and the

other is some new kind of material, black and hard like wood,

but soft to the touch.  As you look at it, it vibrates and makes

a loud noise somewhat like fast cricket chirps.  A green button

appears on the glass.

You push the button, and a voice comes from the device:





"Congratulations.  You have escaped the cursed world.  Now your real

adventure begins.  Seek out a person named {}.  They will help you on

on your newest chapter of this most wonderful journey."







""".format(player))

    choose = input("Congratulations!  You win!  Do you want to play again?\nYou will KEEP any boons you have gained.\n? ").strip().title()

    if "Y" in choose:
        print("_"*25)
        intro()
    else:
        print("Thank you for playing {}!".format(script[:-3]))
        quit()

def death(cause):
    death_msg = {
        'treant': "Messing with a treant is a terrible idea.\nYou are squished flat effortlessly.\n",
        'dark_forest': "You wander in the dark for the rest of your natural life.",
        'minotaur': "You are no match for the massive minotaur.\nNever come between a minotaur and his pie.",
        'dragon': "The dragon unleashes a raging fireball, and you crisp very quickly.\nToasty!"
    }

    print(death_msg[cause])

    choose = input("Do you want to try again?\nYou will LOSE any boons you have gained.\n? ").strip().title()

    if "Y" in choose:
        global unicorns_blessing
        unicorns_blessing = False
        global fish
        fish = False
        global lost
        lost = False
        global pie
        pie = False
        global knife
        knife = False

        print("_"*25)
        start()

    else:
        quit()

def fall_in_pit():
    print("""
The earth rumbles, and you are thrown to the ground.
A massive cavernous hole opens up underneath you and you fall through.
""")
    abyss0()

if __name__ == "__main__":
    intro()