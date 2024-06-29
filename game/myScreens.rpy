label myScreens:
    screen map():
        tag menu
        add "bg/bg map.png" size(1920, 1080)

        # park
        imagebutton:
            xpos 1195
            ypos 490
            idle "bg/park_idle.png"
            hover "bg/park_hover.png"
            action Jump("park")

        # ship
        imagebutton:
            xpos 409
            ypos 170
            idle "bg/ship_idle.png"
            hover "bg/ship_hover.png"
            action Jump("ship")
