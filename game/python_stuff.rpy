init python:

    modifiers = {1:-5, 2:-4, 3:-4, 4:-3, 5:-3, 6:-2, 7:-2, 8:-1, 9:-1, 10:0, 11:0, 12:1, 13:1, 14:2, 15:2, 16:3, 17:3, 18:4,
                19:4, 20:5, 21:5, 22:6, 23:6, 24:7, 25:7, 26:8, 27:8, 28:9, 29:9, 30:10}
    proficiency_bonus_progression = {1:2, 2:2, 3:2, 4:2, 5:3, 6:3, 7:3, 8:3, 9:4,
                                    10:4, 11:4, 12:4, 13:5, 14:5, 15:5, 16:5, 17:6, 18:6, 19:6, 20:6}
    level_progression = {1:0, 2:300, 4:2700, 5:6500, 6:14000, 7:23000, 8:34000, 9:48000, 10:64000, 11:85000, 12:100000,
                        13:120000, 14:140000, 15:165000, 16:195000, 17:225000, 18:265000, 19:305000, 20:355000}
    monster_proficiency_bonus = {0:2, 0.125:2, 0.25:2, 0.5:2, 1:2, 2:2, 3:2, 4:2, 5:3, 6:3, 7:3, 8:3, 9:4, 10:4, 11:4, 12:4, 13:5, 14:5,
                                15:5, 16:5, 17:6, 18:6, 19:6, 20:6, 21:7, 22:7, 23:7, 24:7, 25:8, 26:8, 27:8, 28:8, 29:9, 30:9}                        
    professions = {
            "Warrior":
            {"attack_stat":"str", "hp":13, "mp":0, "str":16, "dex":14, "con":16, "int":10, "wis":11, "cha":10},
            "Thief":
            {"attack_stat":"dex", "hp":10, "mp":0, "str":10, "dex":16, "con":14, "int":11, "wis":10, "cha":16},
            "Mage":
            {"attack_stat":"int", "hp":9, "mp":5, "str":10, "dex":14, "con":16, "int":16, "wis":10, "cha":11},
            "Priest":
            {"attack_stat":"wis", "hp":10, "mp":5, "str":16, "dex":10, "con":14, "int":10, "wis":16, "cha":11}
            }
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
    attributes = ["str", "dex", "con", "int", "wis", "cha"]
    skills = {"Acrobatics":"dex", "Animal Handling":"wis", "Arcana":"int", "Athletics":"str", "Deception":"cha",
            "History":"int", "Insight":"wis", "Intimidation":"cha", "Medicine":"wis", "Nature":"int", "Perception":"wis",
            "Performance":"cha", "Persuasion":"cha", "Religion":"int", "Sleight of Hand":"dex", "Stealth":"dex", "Survival":"wis"}

    class Creature:
        def __init__(self, character, name, prof):
            self.c = character
            self.name = name
            self.type = prof
            if self.type in professions:
                self.attributes = professions[self.type]
            elif self.type in monsters:
                self.attributes = monsters[self.type]
            self.max_hp = self.attributes['hp']
            self.max_mp = self.attributes['mp']
            self.attack_stat = self.attributes['attack_stat']
            self.attack_bonus = modifiers[self.attributes[self.attack_stat]]


    class Player(Creature):
        def __init__(self, character, name, prof):
            super().__init__(character, name, prof)
            self.proficiency_bonus = 2
            self.ac = 18


    class Monster(Creature):
        def __init__(self, character, name, prof):
            super().__init__(character, name, prof)
            self.ac = self.attributes['ac']
            self.proficiency_bonus = monster_proficiency_bonus[self.attributes['cr']]


    def dice_roller(times, sides):
        total = 0
        for time in range(1, times + 1):
            total += renpy.random.randint(1, sides)
        return total
