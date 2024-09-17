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
                    value main_character.hp
                    range main_character.max_hp
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None
                    
                null width 5
                
                text "[main_character.hp] / [main_character.max_hp]" size 16
                
                
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
                
    text "[player_name] vs. [enemy1.name]" xalign 0.5 yalign 0.05 size 30