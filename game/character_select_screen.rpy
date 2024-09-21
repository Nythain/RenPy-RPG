screen choose_character:
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
        idle "character1.png"
        tooltip "A valiant male warrior. You rely on your strength to see things through."
        action [SetVariable("player_character", 1), Return()]

    imagebutton:
        at right
        focus_mask True
        idle "character2.png"
        tooltip "A valiant female warrior. You rely on your strength to see things through."
        action [SetVariable("player_character", 2), Return()]
