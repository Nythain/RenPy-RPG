# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define s = Character("Mystery Creature")
define mc = Character("[player_name]")
define na = Character("Narrator")

#Declare music
define audio.gamemusic = "audio/teller-of-the-tales-by-kevin-macleod-from-filmmusic-io.mp3"

# Declare some character select stuff
default player_character = 0
image playerPortrait = DynamicImage("character[player_character]")
default player_name = ""

# Some Python to create the player and enemy classes
init python:
    class Creature:
        def __init__(self, name):
            self.name = name
            self.attack_bonus = 0
            self.ac = 10
            self.max_hp = 10

    class Player(Creature):
        def __init__(self, name, prof):
            super().__init__(name)
            if prof == "Warrior":
                self.max_hp += 3
                self.hp = self.max_hp
                self.attack_bonus += 5
                self.ac += 6

    class Monster(Creature):
        def __init__(self, name, race):
            super().__init__(name)
            self.race = race
            if self.race == "Goblin":
                self.max_hp -= 3
                self.hp = self.max_hp
                self.attack_bonus += 4
                self.ac += 5


# The game starts here.

label dice_roll:
    python:
        d4 = renpy.random.randint(1, 4)
        d6 = renpy.random.randint(1, 6)
        d8 = renpy.random.randint(1, 8)
        d10 = renpy.random.randint(1, 10)
        d12 = renpy.random.randint(1, 12)
        d20 = renpy.random.randint(1, 20)
    return

label start:
    play music gamemusic

#    call screen town_map_screen

    scene bg forrest door

    show fairy at truecenter

    s "Why hello there. I've never seen anyone like you before."
    s "Are you a man or a woman?"

    call screen choose_character

    show playerPortrait at left

    s "Well that's most definitely interesting!"
    s "Oh, how rude of me. I don't even know your name yet."

    $ player_name = renpy.input("Do you dare give a magical stranger your real name, or just an alias?")

    $ main_character = Player("[player_name]", "Warrior")
    $ enemy1 = Monster("Bob", "Goblin")

    s "It's nice to meet you [player_name]. I wish there was time for more pleasantries but a wild [enemy1.race] has appeared!"

    show goblin at right with moveinright

    s "Ready yourself [player_name]."

    call battle_loop
    if main_character.hp <= 0:
        hide playerPortrait
        "You have died"
        return
    
    hide goblin
    show fairy at truecenter

    s "Whew, that was close!"
    s "You might just be strong enough to aid the people of KyCitia in their quest to defeat an evil dragon who terrorizes them!"

    scene bg_map with dissolve

    na "With that, the unkown creature pushes you through a magical doorway. On the other side, you arrive in a foreign town."
    na "As you look around, you notice a shop, what appears to be an tavern and inn, a school of some sorts, and a castle off in the distance."

    call screen town_map_screen

    return


label battle_loop:
    hide fairy
    show screen battle_stats_screen

    while (enemy1.hp > 0) and (main_character.hp > 0):
        call dice_roll
        menu:
            "Attack!":
                python:
                    damage = 0
                    if d20 == 1:
                        pass
                    elif d20 == 20 or d20 + main_character.attack_bonus > enemy1.ac:
                        damage = (d8 + 3)
                        enemy1.hp -= damage
                mc "Take that!\n[player_name] rolled [d20 + main_character.attack_bonus] to hit.\n[enemy1.name] took [damage] damage."

        call dice_roll
        if enemy1.hp > 0:
            python:
                damage = 0
                if d20 == 1:
                    pass
                elif d20 == 20 or d20 + enemy1.attack_bonus > main_character.ac:
                    damage = (d6 + 2)
                    main_character.hp -= damage
            "[enemy1.name] attacks viciously!\n[enemy1.name] rolled [d20] to hit.\n[player_name] took [damage] damage."

    hide screen battle_stats_screen
