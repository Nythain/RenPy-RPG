label map_screens:
    
# Map
screen town_map_screen:
    add "bg_map.png"

    # Castle
    imagebutton:
        xpos 1108
        ypos 60
        idle "castle_idle.png"
        hover "castle_hover"
        action Jump("castle")

    # School
    imagebutton:
        xpos 422
        ypos 7
        idle "school_idle.png"
        hover "school_hover"
        action Jump("school")

    # Tavern
    imagebutton:
        xpos 705
        ypos 460
        idle "tavern_idle.png"
        hover "tavern_hover"
        action Jump("tavern")

    # Shop
    imagebutton:
        xpos 403
        ypos 628
        idle "shop_idle.png"
        hover "shop_hover"
        action Jump("shop")

# Back Button
screen back_button:
    imagebutton:
        xpos 100
        ypos 100
        idle "back_idle.png"
        hover "back_hover"
        action Jump("town_map")
