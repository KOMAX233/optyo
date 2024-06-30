# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("Yamba", image="yamba")

define y_nvl = Character("Yamba", kind=nvl, image="yamba", callback=Phone_SendSound)
define e_nvl = Character("Eileen", kind=nvl, callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

init:
    # Variables initialization
    $ option = "1"
    $ left_server = False
    $ blocked = False
    $ Deleted_user_visited = 0
    $ channel1 = 0
    $ kambo_server = 0
    $ kambo_pf = 0
    $ joined = 0
    $ disconnected = 0


# The game starts here.

label start:

    scene bg park
    y "Welcome to the park!"
    
    # call screen key_listener

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    jump discordlist
    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show yamba happy

    # These display lines of dialogue.

    y "You've created a new Ren'Py game."

    y "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return

label discordlist:
    if (Deleted_user_visited < 4 and left_server is not True):
        # deleteduser
        jump deleteduser
    if ("1a" in option):
        # kambo
        y "2."
    if (Deleted_user_visited >= 4 and left_server is not True):
        # jambiserver
        y "3"
    if (len(option) >= 2):
        if (option[1] == "a"):
            # kamboserver
            y "4."
    if (left_server and blocked is not True):
        if (kambo_pf != 1):
            # Jambi
            y "5."
        else:
            # JambiNew
            y "6."

label deleteduser:
    label deleted_user:
    $ Deleted_user_visited += 1
    if Deleted_user_visited == 1:
        
        scene bg ship with dissolve
        pause 1.0

        show yamba normal e1m1 at center:
            yoffset 1080
            ease 0.7 yoffset 0


        y "Hello!"
        y e1m2 "bamba!"
        y phone e1m1 "let's look at phone!"

        #Phone conversation start
        show yamba e1m2_b:
            ease 0.5 xalign 0.7 

        nvl_narrator "05/22/2021 5:55 PM"
        y_nvl e2m2_b "I miss you. I do everyday..."
        y_nvl e1m2_b "I still miss you so much"
        y_nvl e1m2_b "where have the times gone"
        y_nvl e1m2_b "baby it's all wrong"
        y_nvl e1m2_b "where were the plans we made for two"
        y_nvl e1m2_b "I will wait for you patiently..."
        y_nvl e1m2_b "I will let you have your freedom and date other guys"
        y_nvl e1m2_b "and then I want to show you that I can be better than I was when we dated"
        y_nvl e1m2_b "I will be better"
        y_nvl e1m2_b "I will start working out, being more positive, getting a good job, learning anger control"
        y_nvl e1m2_b "I am taking therapy"
        y_nvl e1m2_b "I am learning how not to be jealous and insecure"
        y_nvl e1m2_b "please enjoy your life"
        y_nvl e1m2_b "until you are able to be with me"
        y_nvl e1m2_b "I love you"
        nvl_narrator "05/22/2021 10:58PM"
        y_nvl e1m2_b "I miss you"
        y_nvl e1m2_b "how are you able to move on"
        y_nvl e1m2_b "and forget about me so easily"
        y_nvl e1m2_b "did I really mean so little"
        y_nvl e1m2_b "I'm sorry that I became bad"
        y_nvl e1m2_b "but"
        y_nvl e1m2_b "I thought I still meant something"
        y_nvl e1m2_b "I really cared about you until the end"
        y_nvl e1m2_b "I was just weak and insecure"
        y_nvl e1m2_b "I'm so sorry"

        nvl_narrator "05/25/2021 8:10AM"
        y_nvl e1m2_b "I love you"
        y_nvl e1m2_b "I miss you everyday still"
        y_nvl e1m2_b "But I know you are happier without me"
        y_nvl e1m2_b "And life is long, so maybe I will have another chance"
        y_nvl e1m2_b "And even if not, I am happy to have met you"
        y_nvl e1m2_b "And I just want to be your friend"
        y_nvl e1m2_b "I love you"

        nvl_narrator "05/27/2021 3.24PM"
        y_nvl e1m2_b "I miss you"
        y_nvl e1m2_b "I love you"
        y_nvl e1m2_b "I miss you everyday"
        y_nvl e1m2_b "I love you baby"
        y_nvl e1m2_b "I love you so much"

        nvl_narrator "06/01/2021 12:11 PM"
        y_nvl e1m2_b "I miss you"
        y_nvl e1m2_b "baby"

        nvl_narrator "07/14/2021 2:49 PM"
        y_nvl e1m2_b "I miss you so much"
        y_nvl e1m2_b "why did you have to date someone older than me"
        y_nvl e1m2_b "why do you do this"
        y_nvl e1m2_b "I went to hospital because of how much u hurt me"
        y_nvl e1m2_b "but I still can't resent you"
        y_nvl e1m2_b "because l still love you"

        y_nvl e1m2_b "I loved how much you loved me and needed me"
        y_nvl e1m2_b "I loved how much you wanted me"
        y_nvl e1m2_b "I miss being there for you"
        y_nvl e1m2_b "and doing what you needed"
        y_nvl e1m2_b "even if I put too much pressure on myself"
        y_nvl e1m2_b "and got too dependent on your affection"
        y_nvl e1m2_b "I love you so much"
        y_nvl e1m2_b "I miss playing with you"
        y_nvl e1m2_b "being with you made my heart flutter"
        y_nvl e1m2_b "even if it was games I don't usually play"
        y_nvl e1m2_b "I love you"
        $ Deleted_user_visited += 1

        show yamba:
            ease 0.5 xalign 0.5 

        y normal e1m2 "are you ever gonna reply?"
        y normal e1m2 "dont give me hope"

        menu:
            "Continue reading":
                jump deleted_user_continue
                y "yesbamba"
    elif Deleted_user_visited < 4:
        y phone e1m1 "I click into the DM again..."

        #Phone conversation start
        show yamba e1m2_b:
            ease 0.5 xalign 0.7 
        nvl_narrator ""
        $ Deleted_user_visited += 1

        show yamba:
            ease 0.5 xalign 0.5 

        y normal e1m2 "are you ever gonna reply?"
        y normal e1m2 "dont give me hope"

        menu:
            "Continue reading":
                jump deleted_user_continue
                y "yesbamba"
    else:
        "Months of regret and apologies are just to mask the truth."
        
        "I always know she won't be back anymore."
        "Every day I keep myself busy so I can temporarily forget the pain, but how can I find out a way to forever fill the missing piece?"
        "If no girls will ever love me, I should just try every single one till success. "
        "It's been a year since she left. "
        "Now I've tried to make things work with many more girls but they never work out. "
        "I have hope to make things work with Kambo, a girl I met online and even met up with in real life a few times. "
        "She and I didn't get along at first but I feel like I'm slowly getting closer to her. "
        "My friend Jambi, who I've known since I was young, is trying to help me get with her... "
        "but I can't stop being jealous about how well they get along and how much he is her type."
        "The only thing that makes me feel a little better is that he swore on his favourite music artist that he wouldn't date her - I wanted to trust his words. "
        "..."
        "On one of my regular calls with Jambi in his server"
        jump jambiserver

        # "[Additional content for further visits.]"
        menu:
            "Continue reading":
                jump deleted_user_continue

label deleted_user_continue:
    "No reply."
    "..."
    "......"
    "........."
    "let's see if there's reply now."
    "............"
    jump deleted_user
