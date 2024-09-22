init python:

    modifiers = {1:-5, 2:-4, 3:-4, 4:-3, 5:-3, 6:-2, 7:-2, 8:-1, 9:-1, 10:0, 11:0, 12:1, 13:1, 14:2, 15:2, 16:3, 17:3, 18:4,
                19:4, 20:5, 21:5, 22:6, 23:6, 24:7, 25:7, 26:8, 27:8, 28:9, 29:9, 30:10
                }
    monster_proficiency_bonus = {0:2, 0.125:2, 0.25:2, 0.5:2, 1:2, 2:2, 3:2, 4:2, 5:3, 6:3, 7:3, 8:3, 9:4, 10:4, 11:4, 12:4, 13:5, 14:5,
                                15:5, 16:5, 17:6, 18:6, 19:6, 20:6, 21:7, 22:7, 23:7, 24:7, 25:8, 26:8, 27:8, 28:8, 29:9, 30:9
                                }                        
    player_proficiency_bonus = {1:2, 2:2, 3:2, 4:2, 5:3, 6:3, 7:3, 8:3, 9:4,
                                10:4, 11:4, 12:4, 13:5, 14:5, 15:5, 16:5, 17:6, 18:6, 19:6, 20:6
                                }
    level_progression = {1:0, 2:300, 4:2700, 5:6500, 6:14000, 7:23000, 8:34000, 9:48000, 10:64000, 11:85000, 12:100000,
                        13:120000, 14:140000, 15:165000, 16:195000, 17:225000, 18:265000, 19:305000, 20:355000
                        }
    attributes = ["str", "dex", "con", "int", "wis", "cha"]
    skills = {"Acrobatics":"dex", "Animal Handling":"wis", "Arcana":"int", "Athletics":"str", "Deception":"cha",
            "History":"int", "Insight":"wis", "Intimidation":"cha", "Medicine":"wis", "Nature":"int", "Perception":"wis",
            "Performance":"cha", "Persuasion":"cha", "Religion":"int", "Sleight of Hand":"dex", "Stealth":"dex", "Survival":"wis"
            }
    professions = {
            "Warrior":
            {"attack_stat":"str", "magic_stat": "cha", "hp":13, "mp":0, "str":16, "dex":10, "con":16, "int":10, "wis":11, "cha":14},
            "Thief":
            {"attack_stat":"dex", "magic_stat": "cha", "hp":10, "mp":0, "str":10, "dex":16, "con":14, "int":11, "wis":10, "cha":16},
            "Mage":
            {"attack_stat":"dex", "magic_stat": "int", "hp":9, "mp":5, "str":10, "dex":14, "con":16, "int":16, "wis":10, "cha":11},
            "Priest":
            {"attack_stat":"str", "magic_stat": "wis", "hp":10, "mp":5, "str":16, "dex":10, "con":14, "int":10, "wis":16, "cha":11}
            }
    starting_gear = {"Warrior":["Longsword", "Shield", "Chain Mail"],
                    "Thief":["Rapier", "Shortsword", "Leather"],
                    "Mage":["Dagger", "Arcane Focus", None],
                    "Priest":["Mace", "Shield", "Scale Mail"]
                    }

    def dice_roller(times, sides):
        total = 0
        for time in range(1, times + 1):
            total += renpy.random.randint(1, sides)
        return total

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
            self.profession = prof
            self.level = 1
            self.xp = 0
            self.proficiency_bonus = 2
            self.ac = 10 + modifiers[self.attributes['dex']]
            self.gold = 0
            self.mainhand = None
            self.offhand = None
            self.armor = None
            self.inventory = []

        def get_ac(self):
            if self.armor != None:
                self.ac = self.armor['armor_class']
            if self.offhand['name'] == 'Shield':
                self.ac += 2
            return self.ac

        def add_hp(self, amount):
            self.attributes['hp'] += amount
            if self.attributes['hp'] > max_hp:
                self.attributes['hp'] = max_hp

        def add_xp(self, amount):
            self.xp += amount

        def level_up(self):
            pass

        def equip_item(self, item_name, pos):
            if any(d['name'] == item_name for d in items):
                for item in items:
                    try:
                        if item['name'] == item_name and item['hands']:
                            if pos == "mainhand":
                                if self.offhand == None:
                                    self.mainhand = item
                                elif self.offhand['hands'] != 2 and item['hands'] != 2:
                                    self.mainhand = item
                            elif pos == "offhand":
                                if self.mainhand == None:
                                    self.offhand = item
                                elif self.mainhand['hands'] != 2 and item['hands'] != 2:
                                    self.offhand = item
                    except:
                        self.armor = item

        def unequip_item(self,item_name):
            if self.mainhand['name'] == item_name:
                self.mainhand = None
            elif self.offhand['name'] == item_name:
                self.offhand = None
            elif self.armor['name'] == item_name:
                self.armor = None

    class Monster(Creature):
        def __init__(self, character, name, prof):
            super().__init__(character, name, prof)
            self.ac = self.attributes['ac']
            self.proficiency_bonus = monster_proficiency_bonus[self.attributes['cr']]

    class InventoryItem:
        def __init__(self, img, name):
            self.img = img
            self.name = name
            for item in items:
                if item['name'] == self.name:
                    self.value = item['cost']

    class Equipable(InventoryItem):
        def __init__(self, img, name):
            super().__init__(img, name)
            self.is_equpped = False
            self.equipped_to = None

        def equip(self, target):
            self.is_equpped = True
            self.equipped_to = target

        def unequip(self):
            self.is_equpped = False
            self.equipped_to = None

    class Equipment(Equipable):
        def __init__(self, img, name):
            super().__init__(img, name)

        def equip(self, target, pos):
            Equipable.equip(self, target)
            target.equip_item(self.name, pos)

        def unequip(self):
            self.equipped_to.unequip_item(self.name)
            Equipable.unequip(self)
    
    class Consumable(InventoryItem):
        def __init__(self, img, name, hp_gain):
            super().__init__(img, name)
            self.hp_gain = hp_gain

            def use(self, target):
                inventory.remove(self)
                target.add_hp(self.hp_gain)

    class NonConsumable:
        pass

    class KeyItem:
        pass
