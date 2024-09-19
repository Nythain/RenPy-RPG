# Combat related stuff goes here

# The main combat loop
label battle_loop:
    show screen battle_stats_screen

    while (enemy1.attributes['hp'] > 0) and (mc.attributes['hp'] > 0):
        menu:
            "Attack!":
                python:
                    attack_roll = dice_roller(1, 20)
                    damage_roll = 0
                    if attack_roll == 1:
                        damage = 0
                    elif attack_roll == 20 or attack_roll + mc.attack_bonus + mc.proficiency_bonus >= enemy1.ac:
                        damage_roll = dice_roller(1, 8)
                        damage = (damage_roll + mc.attack_bonus)
                        enemy1.attributes['hp'] -= damage
                    else:
                        damage = 0
                mc.c "En garde you filthy swine!"
            "Defend":
                mc.c "I feel it best to defend."


        if enemy1.attributes['hp'] > 0:
            python:
                damage = 0
                if len(enemy1.attributes['attack']) > 4:
                    attack_roll = dice_roller(1, 20)
                    if attack_roll == 1 or attack_roll + enemy1.attack_bonus + enemy1.proficiency_bonus < mc.ac:
                        damage += 0
                    else:
                        damage_roll1 = dice_roller(*enemy1.attributes['attack'][0])
                        damage_roll2 = dice_roller(*enemy1.attributes['attack'][4])
                        damage += (damage_roll1 + damage_roll2 + enemy1.attack_bonus)
                elif len(enemy1.attributes['attack']) == 4:
                    attack_roll1 = dice_roller(1, 20)
                    if attack_roll1 == 1 or attack_roll1 + enemy1.attack_bonus + enemy1.proficiency_bonus < mc.ac:
                        damage += 0
                    else:
                        damage_roll1 = dice_roller(*enemy1.attributes['attack'][0])
                        damage += (damage_roll1 + enemy1.attack_bonus)
                    attack_roll2 = dice_roller(1, 20)
                    if attack_roll2 == 1 or attack_roll2 + enemy1.attack_bonus + enemy1.proficiency_bonus < mc.ac:
                        damage += 0
                    else:
                        damage_roll2 = dice_roller(*enemy1.attributes['attack'][2])
                        damage += (damage_roll2 + enemy1.attack_bonus)
                else:
                    attack_roll = dice_roller(1, 20)
                    if attack_roll == 1 or attack_roll + enemy1.attack_bonus + enemy1.proficiency_bonus < mc.ac:
                        damage += 0
                    else:
                        damage_roll = dice_roller(*enemy1.attributes['attack'][0])
                        damage += (damage_roll + enemy1.attack_bonus)
                mc.attributes['hp'] -= damage
            enemy1.c "Me kill tall fleshy thing yes!"

    hide screen battle_stats_screen

# The battle stats display
screen battle_stats_screen:
    frame:
        xalign 0.01 yalign 0.05
        xminimum 220 xmaximum 220
        vbox:
            text "[player_name]" size 22 xalign 0.5
            null height 5
            hbox:
                bar:
                    xmaximum 130
                    value mc.attributes['hp']
                    range mc.max_hp
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None
                null width 5
                text "[mc.attributes['hp']] / [mc.max_hp]" size 16
    frame:
        xalign 0.99 yalign 0.05
        xminimum 220 xmaximum 220
        vbox:
            text "[enemy1.name]" size 22 xalign 0.5
            null height 5
            hbox:
                bar:
                    xmaximum 130
                    value enemy1.attributes['hp']
                    range enemy1.max_hp
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None
                null width 5
                text "[enemy1.attributes['hp']] / [enemy1.max_hp]" size 16
