# The script of the game goes in this file.

#Declare music
define audio.gamemusic = "audio/teller-of-the-tales-by-kevin-macleod-from-filmmusic-io.mp3"

# Declare some character select stuff
default player_gender = 0
default player_class = ""
image genderPortrait = DynamicImage("character[player_gender]")
image playerPortrait = DynamicImage("[player_class][player_gender].png")
default player_name = ""

# Inventory stuff
default selected_item = None

# The game starts here.

label start:
    play music gamemusic

    # Creating some NPCs
    $ na = Character("Narrator")
    $ fa = Character("Mysterious Creature")
 
    scene bg forrest door

    show fairy at truecenter

    fa "Why hello there. I've never seen anyone like you before."
    fa "Are you a boy or a girl?"

    # Choosing our character. Male or Female warrior for now
    call screen choose_gender

    show genderPortrait at left

    fa "Well that's most definitely interesting!"
    fa "And what of your journeys? How would you describe yourself?"

    hide genderPortrait
    hide fairy

    call screen choose_class

    show playerPortrait at left
    show fairy at truecenter

    fa "Oh, how rude of me. I don't even know your name yet."

    # Trying to get a player input name
    $ player_name = renpy.input("Do you dare give a magical stranger your real name, or just an alias?")

    # Creating the main character class object
    python:
        mc = Player(Character(player_name), player_name, player_class)
        starting_mainhand = Equipment(starting_gear[mc.profession][0], starting_gear[mc.profession][0])
        starting_mainhand.equip(mc, "mainhand")
        starting_offhand = Equipment(starting_gear[mc.profession][1], starting_gear[mc.profession][1])
        starting_offhand.equip(mc, "offhand")
        starting_armor = Equipment(starting_gear[mc.profession][2], starting_gear[mc.profession][2])
        starting_armor.equip(mc, "armor")
        mc.get_ac()
        mc.inventory.extend([starting_mainhand, starting_offhand, starting_armor])

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
