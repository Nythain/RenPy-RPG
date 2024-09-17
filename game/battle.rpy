# Combat related stuff goes here

# The main combat loop
label battle_loop:
    hide fairy
    show screen battle_stats_screen

    while (enemy1.hp > 0) and (mc.hp > 0):
        menu:
            "Attack!":
                python:
                    attack_roll = dice_roller(1, 20)
                    damage_roll = 0
                    if attack_roll == 1:
                        damage = 0
                    elif attack_roll == 20 or attack_roll + mc.attack_bonus > enemy1.ac:
                        damage_roll = dice_roller(1, 8)
                        damage = (damage_roll + mc.damage_bonus)
                        enemy1.hp -= damage
                    else:
                        damage = 0
                mc.c "En garde you filthy swine!"
                if damage > 0:
                    "[player_name] rolled [attack_roll] + [mc.attack_bonus] to hit.\n[enemy1.name] took [damage_roll] + [mc.damage_bonus] damage."
                else:
                    "[player_name] rolled [attack_roll] and missed their target."

        if enemy1.hp > 0:
            python:
                damage_roll = 0
                attack_roll = dice_roller(1, 20)
                if attack_roll == 1:
                    damage = 0
                elif attack_roll == 20 or attack_roll + enemy1.attack_bonus > mc.ac:
                    damage_roll = dice_roller(1, 6)
                    damage = (damage_roll + enemy1.damage_bonus)
                    mc.hp -= damage
                else:
                    damage = 0
            enemy1.c "Me kill tall fleshy thing yes!"
            if damage > 0:
                "[enemy1.name] rolled [attack_roll] + [enemy1.attack_bonus] to hit.\n[player_name] took [damage_roll] + [enemy1.damage_bonus] damage."
            else:
                "[enemy1.name] rolled [attack_roll] and missed their target."

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
                    value mc.hp
                    range mc.max_hp
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None
                null width 5
                text "[mc.hp] / [mc.max_hp]" size 16
    frame:
        xalign 0.99 yalign 0.05
        xminimum 220 xmaximum 220
        vbox:
            text "[enemy1.name]" size 22 xalign 0.5
            null height 5
            hbox:
                bar:
                    xmaximum 130
                    value enemy1.hp
                    range enemy1.max_hp
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None
                null width 5
                text "[enemy1.hp] / [enemy1.max_hp]" size 16
