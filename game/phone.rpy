init python:
    phone_texts = [
        "Message 1: Hello!",
        "Message 2: How are you?",
        "Message 3: Don't forget the meeting.",
        "Message 4: See you soon!"
    ]

    current_phone_text = 0

screen phone():
    tag menu
    # Add the phone background image
    add "phone.png" size(1920, 1080)
    
    # Display the current phone text at a specific position on the phone screen
    text "[phone_texts[current_phone_text]]" xpos 100 ypos 200 color "#000000" size 24

    # # Add interactive buttons for navigation
    # textbutton "Next" action SetVariable("current_phone_text", (current_phone_text + 1) % len(phone_texts)) xpos 500 ypos 700
    # textbutton "Back" action Return() xpos 600 ypos 700

    # # Example of an interactive imagebutton (e.g., app icon)
    # imagebutton:
    #     idle "images/app_icon.png"
    #     hover "images/app_icon_hover.png"
    #     xpos 300
    #     ypos 600
    #     action Jump("app_screen")  # Jump to another screen or label

screen key_listener():
    # key "m" action ShowMenu('map')
    # key "z" action ShowMenu('phone')
    key 'z' action Show("phone")
