init python:
    items = [
        # Ranged Weapons
        {"name":"Club", "type":"simple", "hands": 1, "cost":.1, "damage":(1, 4), "damage_type":"bludgeoning", "weight":2},
        {"name":"Dagger", "type":"simple", "hands": 1, "cost":2, "damage":(1, 4), "damage_type":"piercing", "weight":1},
        {"name":"Greatclub", "type":"simple", "hands": 2, "cost":.2, "damage":(1, 8), "damage_type":"bludgeoning", "weight":10},
        {"name":"Handaxe", "type":"simple", "hands": 1, "cost":5, "damage":(1, 6), "damage_type":"slashing", "weight":2},
        {"name":"Javelin", "type":"simple", "hands": 1, "cost":.5, "damage":(1, 6), "damage_type":"piercing", "weight":2},
        {"name":"Light Hammer", "type":"simple", "hands": 1, "cost":2, "damage":(1, 4), "damage_type":"bludgeoning", "weight":2},
        {"name":"Mace", "type":"simple", "hands": 1, "cost":5, "damage":(1, 6), "damage_type":"bludgeoning", "weight":4},
        {"name":"Quarterstaff", "type":"simple", "hands": 1, "cost":.2, "damage":(1, 6), "damage_type":"bludgeoning", "weight":4},
        {"name":"Sickle", "type":"simple", "hands": 1, "cost":1, "damage":(1, 4), "damage_type":"slashing", "weight":2},
        {"name":"Spear", "type":"simple", "hands": 1, "cost":1, "damage":(1, 6), "damage_type":"piercing", "weight":3},
        {"name":"Battleaxe", "type":"martial", "hands": 1, "cost":10, "damage":(1, 8), "damage_type":"slashing", "weight":4},
        {"name":"Flail", "type":"martial", "hands": 1, "cost":10, "damage":(1, 8), "damage_type":"bludgeoning", "weight":2},
        {"name":"Glaive", "type":"martial", "hands": 2, "cost":20, "damage":(1, 10), "damage_type":"slashing", "weight":6},
        {"name":"Greataxe", "type":"martial", "hands": 2, "cost":30, "damage":(1, 12), "damage_type":"slashing", "weight":7},
        {"name":"Greatsword", "type":"martial", "hands": 2, "cost":50, "damage":(2, 6), "damage_type":"slashing", "weight":6},
        {"name":"Halberd", "type":"martial", "hands": 2, "cost":20, "damage":(1, 10), "damage_type":"slashing", "weight":6},
        {"name":"Lance", "type":"martial", "hands": 1, "cost":10, "damage":(1, 12), "damage_type":"piercing", "weight":6},
        {"name":"Longsword", "type":"martial", "hands": 1, "cost":15, "damage":(1, 8), "damage_type":"slashing", "weight":3},
        {"name":"Maul", "type":"martial", "hands": 2, "cost":10, "damage":(2, 6), "damage_type":"bludgeoning", "weight":10},
        {"name":"Morningstar", "type":"martial", "hands": 1, "cost":15, "damage":(1, 8), "damage_type":"piercing", "weight":4},
        {"name":"Pike", "type":"martial", "hands": 1, "cost":5, "damage":(1, 10), "damage_type":"piercing", "weight":18},
        {"name":"Rapier", "type":"martial", "hands": 1, "cost":25, "damage":(1, 8), "damage_type":"piercing", "weight":2},
        {"name":"Scimitar", "type":"martial", "hands": 1, "cost":25, "damage":(1, 6), "damage_type":"slashing", "weight":3},
        {"name":"Shortsword", "type":"martial", "hands": 1, "cost":10, "damage":(1, 6), "damage_type":"piercing", "weight":2},
        {"name":"Trident", "type":"martial", "hands": 1, "cost":5, "damage":(1, 6), "damage_type":"piercing", "weight":4},
        {"name":"War Pick", "type":"martial", "hands": 1, "cost":5, "damage":(1, 8), "damage_type":"piercing", "weight":2},
        {"name":"Warhammer", "type":"martial", "hands": 1, "cost":15, "damage":(1, 8), "damage_type":"bludgeoning", "weight":2},
        {"name":"Whip", "type":"martial", "hands": 1, "cost":2, "damage":(1, 4), "damage_type":"slashing", "weight":3},
        # Ranged Weapons
        {"name":"Light Crossbow", "type":"simple", "hands": 2, "cost":25, "damage":(1, 8), "damage_type":"piercing", "weight":5},
        {"name":"Dart", "type":"simple", "hands": 1, "cost":.05, "damage":(1, 4), "damage_type":"piercing", "weight":0.25},
        {"name":"Shortbow", "type":"simple", "hands": 2, "cost":25, "damage":(1, 6), "damage_type":"piercing", "weight":2},
        {"name":"Sling", "type":"simple", "hands": 1, "cost":.1, "damage":(1, 4), "damage_type":"bludgeoning", "weight":0},
        {"name":"Blowgun", "type":"martial", "hands": 1, "cost":10, "damage":(1, 1), "damage_type":"piercing", "weight":1},
        {"name":"Hand Crossbow", "type":"martial", "hands": 1, "cost":75, "damage":(1, 6), "damage_type":"piercing", "weight":3},
        {"name":"Heavy Crossbow", "type":"martial", "hands": 1, "cost":50, "damage":(1, 10), "damage_type":"piercing", "weight":18},
        {"name":"Longbow", "type":"martial", "hands": 1, "cost":50, "damage":(1, 8), "damage_type":"piercing", "weight":2},
        {"name":"Net", "type":"martial", "hands": 1, "cost":1, "damage": "None", "weight":3},
        # Armor
        {"name":"Padded", "cost":5, "armor_class":11 + 3, "weight":8},
        {"name":"Leather", "cost":10, "armor_class":11 + 3, "weight":10},
        {"name":"Studded Leather", "cost":45, "armor_class":12 + 3, "weight":13},
        {"name":"Hide", "cost":10, "armor_class":12 + 2, "weight":12},
        {"name":"Chain Shirt", "cost":50, "armor_class":13 + 2, "weight":20},
        {"name":"Scale Mail", "cost":50, "armor_class":14 + 2, "weight":45},
        {"name":"Breastplate", "cost":400, "armor_class":14 + 2, "weight":20},
        {"name":"Half Plate", "cost":750, "armor_class":15 + 2, "weight":40},
        {"name":"Ring Mail", "cost":30, "armor_class":14, "weight":40},
        {"name":"Chain Mail", "cost":75, "armor_class":16, "weight":55},
        {"name":"Splint", "cost":200, "armor_class":17, "weight":60},
        {"name":"Plate", "cost":1500, "armor_class":18, "weight":65},
        {"name":"Shield", "hands":1, "cost":10, "armor_class":2, "weight":6},
        # Arcane Focus
        {"name":"Arcane Focus", "type":"arcane", "hands": 1, "cost":1, "damage": "None", "weight":0.25},
        # Consumables
        {"name":"Potion", "cost":50, "weight":0.5}
    ]
