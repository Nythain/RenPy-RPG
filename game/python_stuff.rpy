init python:

    modifiers = {1:-5, 2:-4, 3:-4, 4:-3, 5:-3, 6:-2, 7:-2, 8:-1, 9:-1, 10:0, 11:0, 12:1, 13:1, 14:2, 15:2, 16:3, 17:3, 18:4,
                19:4, 20:5, 21:5, 22:6, 23:6, 24:7, 25:7, 26:8, 27:8, 28:9, 29:9, 30:10}
    proficiency_bonus_progression = {1:2, 2:2, 3:2, 4:2, 5:3, 6:3, 7:3, 8:3, 9:4,
                                    10:4, 11:4, 12:4, 13:5, 14:5, 15:5, 16:5, 17:6, 18:6, 19:6, 20:6}
    level_progression = {1:0, 2:300, 4:2700, 5:6500, 6:14000, 7:23000, 8:34000, 9:48000, 10:64000, 11:85000, 12:100000,
                        13:120000, 14:140000, 15:165000, 16:195000, 17:225000, 18:265000, 19:305000, 20:355000}
    professions = {
            "Warrior":{"hp":13, "str":16, "dex": 14, "con": 16, "int": 10, "wis": 11, "cha":10},
            "Thief":{"hp":10, "str":10, "dex": 16, "con": 14, "int": 11, "": 10, "cha":16},
            "Mage":{"hp":9,"str":10, "dex": 14, "con": 16, "int": 16, "wis": 10, "cha":11},
            "Priest":{"hp":10, "str":16, "dex": 10, "con": 14, "int": 10, "wis": 16, "cha":11}
            }
    saving_throws = ["str", "dex", "con", "int", "wis", "cha"]
    skills = {"Acrobatics":"dex", "Animal Handling":"wis", "Arcana":"int", "Athletics":"str", "Deception":"cha",
            "History":"int", "Insight":"wis", "Intimidation":"cha", "Medicine":"wis", "Nature":"int", "Perception":"wis",
            "Performance":"cha", "Persuasion":"cha", "Religion":"int", "Sleight of Hand":"dex", "Stealth":"dex", "Survival":"wis"}

    class Creature:
        def __init__(self, character, name, prof):
            self.c = character
            self.name = name
            self.type = prof
            self.hp = 1
            self.str = 1
            self.dex = 1
            self.con = 1
            self.int = 1
            self.wis = 1
            self.cha = 1
            self.proficiency_bonus = 2


    class Player(Creature):
        def __init__(self, character, name, prof):
            super().__init__(character, name, prof)
            if self.type in professions:
                for y, value in professions[self.type].items():
                    setattr(self, y, value)


    class Monster(Creature):
        def __init__(self, character, name, prof):
            super().__init__(character, name, prof)
            self.race = race
            if self.race == "Goblin":
            if self.type in professions:
                for y, value in professions[self.type].items():
                    setattr(self, y, value)


    def dice_roller(times, sides):
        total = 0
        for time in range(1, times + 1):
            total += renpy.random.randint(1, sides)
        return total
