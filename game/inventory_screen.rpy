style inventory_lable:
    xalign 0.2

style slot:
    minimum(80, 80)
    maximum(80, 80)
    xalign 0.5

screen inventory_screen:
    style_prefix "inventory"

    add "inventory.png"

    textbutton "Return":
        action Return()
        xalign 0.5
        yalign 0.93
