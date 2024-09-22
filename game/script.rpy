# The script of the game goes in this file.

#Declare music
define audio.gamemusic = "audio/teller-of-the-tales-by-kevin-macleod-from-filmmusic-io.mp3"

# Declare some character select stuff
default player_character = 0
image playerPortrait = DynamicImage("character[player_character]")
default player_name = ""

# Inventory stuff
default selected_item = None

# The game starts here.

label start:
    play music gamemusic

    call screen inventory_screen

    # Creating some NPCs
    $ na = Character("Narrator")
    $ fa = Character("Mysterious Creature")
 
    scene bg forrest door

    show fairy at truecenter

    fa "Why hello there. I've never seen anyone like you before."
    fa "Are you a man or a woman?"

    # Choosing our character. Male or Female warrior for now
    call screen choose_character

    show playerPortrait at left

    fa "Well that's most definitely interesting!"
    fa "Oh, how rude of me. I don't even know your name yet."

    # Trying to get a player input name
    $ player_name = renpy.input("Do you dare give a magical stranger your real name, or just an alias?")

    # Creating the main character class object
    python:
        mc = Player(Character([player_name]), [player_name], "Warrior")
        starting_mainhand = Equipment("a", starting_gear[mc.profession][0])
        starting_mainhand.equip(mc, "mainhand")
        starting_offhand = Equipment("a", starting_gear[mc.profession][1])
        starting_offhand.equip(mc, "offhand")
        starting_armor = Equipment("a", starting_gear[mc.profession][2])
        starting_armor.equip(mc, "armor")
        mc.ac = mc.get_ac()

    # Whipping up a quick enemy class object to test combat
    $ enemy1 = Monster(Character("Bob"), "Bob", "Goblin")

    fa "It's nice to meet you [player_name]. I wish there was time for more pleasantries but a wild [enemy1.type] has appeared!"

    show goblin at right with moveinright

    fa "Ready yourself [player_name]."

    hide fairy

    # Starting the combat loop until someone dies
    call battle_loop

    # If main character dies, game over
    if mc.attributes['hp'] <= 0:
        hide playerPortrait
        "You have died"
        return
    
    hide goblin
    show fairy at truecenter

    fa "Whew, that was close!"
    fa "You might just be strong enough to aid the people of KyCitia in their quest to defeat an evil dragon who terrorizes them!"

    scene bg_map with dissolve

    na "With that, the unkown creature pushes you through a magical doorway. On the other side, you arrive in a foreign town."
    na "As you look around, you notice a shop, what appears to be an tavern and inn, a school of some sorts, and a castle off in the distance."

    # Heading to the town map
    call screen town_map_screen

    return
