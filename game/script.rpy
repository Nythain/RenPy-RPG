﻿# The script of the game goes in this file.

#Declare music
define audio.gamemusic = "audio/teller-of-the-tales-by-kevin-macleod-from-filmmusic-io.mp3"

# Declare some character select stuff
default player_character = 0
image playerPortrait = DynamicImage("character[player_character]")
default player_name = ""

# Some Python to create the player and enemy classes


# The game starts here.

label start:
    play music gamemusic

#    call screen town_map_screen

    # Creating some NPCs
    $ na = Creature(Character("Narrator"), "Narrator")
    $ fa = Creature(Character("Mysterious Creature"), "Sarina")
 
    scene bg forrest door

    show fairy at truecenter

    fa.c "Why hello there. I've never seen anyone like you before."
    fa.c "Are you a man or a woman?"

    # Choosing our character. Male or Female warrior for now
    call screen choose_character

    show playerPortrait at left

    fa.c "Well that's most definitely interesting!"
    fa.c "Oh, how rude of me. I don't even know your name yet."

    # Trying to get a player input name
    $ player_name = renpy.input("Do you dare give a magical stranger your real name, or just an alias?")

    # Creating the main character class object
    $ mc = Player(Character([player_name]), [player_name], "Warrior")

    # Whipping up a quick enemy class object to test combat
    $ enemy1 = Monster(Character("Bob"), "Bob", "Goblin")

    fa.c "It's nice to meet you [player_name]. I wish there was time for more pleasantries but a wild [enemy1.race] has appeared!"

    show goblin at right with moveinright

    fa.c "Ready yourself [player_name]."

    hide fairy

    # Starting the combat loop until someone dies
    call battle_loop

    # If main character dies, game over
    if mc.hp <= 0:
        hide playerPortrait
        "You have died"
        return
    
    hide goblin
    show fairy at truecenter

    fa.c "Whew, that was close!"
    fa.c "You might just be strong enough to aid the people of KyCitia in their quest to defeat an evil dragon who terrorizes them!"

    scene bg_map with dissolve

    na.c "With that, the unkown creature pushes you through a magical doorway. On the other side, you arrive in a foreign town."
    na.c "As you look around, you notice a shop, what appears to be an tavern and inn, a school of some sorts, and a castle off in the distance."

    # Heading to the town map
    call screen town_map_screen

    return
