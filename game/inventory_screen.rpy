style inventory_lable:
    xalign 0.2

style slot:
    background Frame("square", 0, 0)
    minimum(125, 125)
    maximum(125, 125)
    xalign 0.0

screen inventory_screen:
    $ mc.get_ac()

    style_prefix "inventory"

    add "inventory.png"

    hbox:
        xpos 130 ypos 130
        spacing 10
        # Character Details
        vbox:
            xmaximum 300
            spacing 5
            text "Name: [player_name]" xalign 0.0
            text "[mc.profession]: Level [mc.level]" xalign 0.0
            text "Experience: [mc.xp] / [mc.next_level]" xalign 0.0
            text "Health: [mc.attributes['hp']] / [mc.max_hp]" xalign 0.0
            text "MP: [mc.attributes['mp']] / [mc.max_mp]" xalign 0.0
            text "AC: [mc.ac]" xalign 0.0
            text "Gold: [mc.gold]" xalign 0.0
            text "Equipment:" xalign 0.0

            # Equipped Items
            frame:
                style "slot"
                if mc.mainhand != None:
                    add mc.mainhand['name'].lower()
                else:
                    text "Mainhand" xalign 0.0 yalign 0.5
            frame:
                style "slot"
                if mc.offhand != None:
                    add mc.offhand['name'].lower()
                else:
                    text "Offhand" xalign 0.0 yalign 0.5
            frame:
                style "slot"
                if mc.armor != None:
                    add mc.armor['name'].lower()
                else:
                    text "Armor" xalign 0.0 yalign 0.5


        # Inventory
        grid 7 6:
            xpos 25 ypos 10
            spacing 10
            for item in mc.inventory:
                frame:
                    style "slot"
                    if isinstance(item, KeyItem):
                        add "bg keyitem"
                    imagebutton idle item.img.lower() action SetVariable("selected_item", item) xalign 0.5 yalign 0.5
            for i in range(len(mc.inventory), 42):
                frame:
                    style "slot"

        # Item Details
        vbox:
            xmaximum 340
#            xalign 0.0
            spacing 5
            text "Current Item:" xpos 150
            if selected_item != None:
                frame:
                    style "slot"
                    xpos 185
                    if isinstance(selected_item, KeyItem):
                        add "bg keyitem"
                    add selected_item.img.lower()
                text "[selected_item.name]" xpos 248 xalign 0.5 yalign 0.5
                text "[selected_item.value] Gold" xpos 248 xalign 0.5 yalign 0.5
#                text "A one handed longsword capable of doing 1d8 damage." xpos 248 xalign 0.5 yalign 0.5
                if isinstance(selected_item, Consumable):
                    textbutton "Use" action Function(selected_item.use, mc) xpos 248 xalign 0.5 yalign 0.5
                if isinstance(selected_item, Equipment):
                    if selected_item.is_equpped:
                        textbutton "Unequip" action Function(selected_item.unequip) xpos 248 xalign 0.5 yalign 0.5
                    else:
                        textbutton "Equip Mainhand" action Function(selected_item.equip, mc, "mainhand") xpos 248 xalign 0.5 yalign 0.5
                        textbutton "Equip Offhand" action Function(selected_item.equip, mc, "offhand") xpos 248 xalign 0.5 yalign 0.5
                        textbutton "Equip Armor" action Function(selected_item.equip, mc, "armor") xpos 248 xalign 0.5 yalign 0.5
                if not isinstance(selected_item, KeyItem):
                    if not isinstance(selected_item, Consumable):
                        textbutton "Drop" action [Function(selected_item.unequip), RemoveFromSet(mc.inventory, selected_item), SetVariable("selected_item", None)] xpos 248 xalign 0.5 yalign 0.5
                    else:
                        textbutton "Drop" action [RemoveFromSet(mc.inventory, selected_item), SetVariable("selected_item", None)] xpos 248 xalign 0.5 yalign 0.5
    textbutton "Return":
        action Return()
        xalign 0.5
        yalign 0.93
