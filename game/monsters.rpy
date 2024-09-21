init python:
    monsters = {
            "Goblin":
            {"attack_stat":"dex", "cr":0.25, "xp":50, "ac":15,
            "hp":7, "mp":0, "str":8, "dex":14, "con":10, "int":10, "wis":8, "cha":8,
            "attack":[(1, 6), "slashing"]},
            "Lizardman":
            {"attack_stat":"str", "cr":0.5, "xp":100, "ac":15,
            "hp":22, "mp":0, "str":15, "dex":10, "con":13, "int":7, "wis":12, "cha":7,
            "attack":[(1, 6), "piercing", (1, 6), "bludgeoning"]},
            "Mimic":
            {"attack_stat":"str", "cr":2, "xp":450, "ac":12,
            "hp":58, "mp":0, "str":17, "dex":12, "con":15, "int":5, "wis":13, "cha":8,
            "attack":[(1, 8), "piercing", "", "", (1, 8), "acid"]},
            "Ogre":
            {"attack_stat":"str", "cr":2, "xp":450, "ac":11,
            "hp":59, "mp":0, "str":19, "dex":8, "con":16, "int":5, "wis":7, "cha":7,
            "attack":[(2, 8), "bludgeoning"]},
            "Orc":
            {"attack_stat":"str", "cr":0.5, "xp":100, "ac":13,
            "hp":15, "mp":0, "str":16, "dex":12, "con":16, "int":7, "wis":11, "cha":10,
            "attack":[(1, 12), "slashing"]},
            "Giant Rat":
            {"attack_stat":"dex", "cr":0.125, "xp":25, "ac":12,
            "hp":7, "mp":0, "str":7, "dex":15, "con":11, "int":2, "wis":10, "cha":4,
            "attack":[(1, 4), "piercing"]},
            "Skeleton":
            {"attack_stat":"dex", "cr":0.25, "xp":50, "ac":13,
            "hp":13, "mp":0, "str":10, "dex":14, "con":15, "int":6, "wis":8, "cha":6,
            "attack":[(1, 6), "piercing"]},
            "Slime":
            {"attack_stat":"str", "cr":0.5, "xp":100, "ac":8,
            "hp":22, "mp":0, "str":12, "dex":6, "con":16, "int":1, "wis":6, "cha":2,
            "attack":[(1, 6), "bludgeoning", "", "", (2, 6), "acid"]},
            "Troll":
            {"attack_stat":"str", "cr":5, "xp":1800, "ac":15,
            "hp":84, "mp":0, "str":18, "dex":13, "con":20, "int":7, "wis":9, "cha":7,
            "attack":[(1, 6), "piercing", (2, 6), "slashing", "", "", (2, 6), "slashing"]},
            "Dire Wolf":
            {"attack_stat":"str", "cr":1, "xp":200, "ac":14,
            "hp":37, "mp":0, "str":17, "dex":15, "con":15, "int":3, "wis":12, "cha":7,
            "attack":[(2, 6), "piercing"]},
            "Zombie":
            {"attack_stat":"str", "cr":0.25, "xp":50, "ac":8,
            "hp":15, "mp":0, "str":13, "dex":6, "con":16, "int":3, "wis":6, "cha":5,
            "attack":[(1, 6), "bludgeoning"]},
            "Baby Red Dragon":
            {"attack_stat":"str", "cr":7, "xp":1100, "ac":17,
            "hp":75, "mp":0, "str":19, "dex":10, "con":17, "int":12, "wis":11, "cha":15,
            "attack":[(1, 10), "piercing", "", "", (1, 6), "fire"]}
            }
