label myScreens:
    screen map():
        tag menu
        add "bg map.png" size(1920, 1080)

        # park
        imagebutton:
            xpos 1195
            ypos 490
            idle "park_idle.png"
            hover "park_hover.png"
            action Jump("park")

        # ship
        imagebutton:
            xpos 409
            ypos 170
            idle "ship_idle.png"
            hover "ship_hover.png"
            action Jump("ship")
