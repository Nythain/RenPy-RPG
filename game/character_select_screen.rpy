screen choose_gender:
    imagebutton:
        at left
        focus_mask True
        idle "character1.png"
        action [SetVariable("player_gender", 1), Return()]

    imagebutton:
        at right
        focus_mask True
        idle "character2.png"
        action [SetVariable("player_gender", 2), Return()]

screen choose_class:
    $ tip = GetTooltip()
    if tip:
        frame:
            background "#00000080"
            xalign 0.5
            ypos 100
            text tip xcenter 0.5 color "#ffffff" text_align 0.5

    imagebutton:
        at left
        focus_mask True
        idle DynamicImage("Warrior[player_gender].png")
        tooltip "A valiant warrior. You rely on your strength to see things through."
        action [SetVariable("player_class", "Warrior"), Return()]

    imagebutton:
        xpos 485
        yalign 1.0
        focus_mask True
        idle DynamicImage("Thief[player_gender].png")
        tooltip "The nimble thief. Wits and cunning have always gotten you by."
        action [SetVariable("player_class", "Thief"), Return()]

    imagebutton:
        xpos 975
        yalign 1.0
        focus_mask True
        idle DynamicImage("Mage[player_gender].png")
        tooltip "The powerful mage. A master of the arcane arts, but very fragile."
        action [SetVariable("player_class", "Mage"), Return()]

    imagebutton:
        at right
        focus_mask True
        idle DynamicImage("Priest[player_gender].png")
        tooltip "The devout priest. Capable of holy good and the strength to smite evil."
        action [SetVariable("player_class", "Priest"), Return()]

