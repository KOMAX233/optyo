# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("yamba")
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
        "Yamba 05/22/2021 5:55 PM"
        "I miss you. I do everyday..."
        "I still miss you so much"
        "where have the times gone"
        "baby it's all wrong"
        "where were the plans we made for two"
        # Ren'Py automatically scrolls, but you can use pauses or player clicks to pace the dialogue.
        "I will wait for you patiently..."
        "I will let you have your freedom and date other guys"
        "and then I want to show you that I can be better than I was when we dated"
        "I will be better"
        "I will start working out, being more positive, getting a good job, learning anger control"
        "I am taking therapy"
        "I am learning how not to be jealous and insecure"
        "please enjoy your life"
        "until you are able to be with me"
        "I love you"
        "Yamba 05/22/2021 10:58PM"
        "I miss you"
        "how are you able to move on"
        "and forget about me so easily"
        "did I really mean so little"
        "I'm sorry that I became bad"
        "but"
        "I thought I still meant something"
        "I really cared about you until the end"
        "I was just weak and insecure"
        "I'm so sorry"

        "Yamba 05/25/2021 8:10AM"
        "I love you"
        "I miss you everyday still"
        "But I know you are happier without me"
        "And life is long, so maybe I will have another chance"
        "And even if not, I am happy to have met you"
        "And I just want to be your friend"
        "I love you"

        "Yamba 05/27/2021 3.24PM"
        "I miss you"
        "I love you"
        "I miss you everyday"
        "I love you baby"
        "I love you so much"

        "Yamba 06/01/2021 12:11 PM"
        "I miss you"
        "baby"

        "Yamba 07/14/2021 2:49 PM"
        "I miss you so much"
        "why did you have to date someone other than me"
        "why do you do this"
        "I went to hospital because of how much u hurt me"
        "but I still can't resent you"
        "because l still love you"

        "I loved how much you loved me and needed me"
        "I loved how much you wanted me"
        "I miss being there for you"
        "and doing what you needed"
        "even if I put too much pressure on myself"
        "and got too dependent on your affection"
        "I love you so much"
        "I miss playing with you"
        "being with you made my heart flutter"
        "even if it was games I don't usually play"
        "I love you"


        # "[Your content continues here.]"
        menu:
            "Continue reading":
                jump deleted_user_continue
                y "yesbamba"
    elif Deleted_user_visited < 4:
        "I click into the DM again today..."
        "Yamba 05/22/2021 5:55 PM"
        "I miss you. I do everyday..."
        # "[Condensed content for subsequent visits.]"
        menu:
            "Continue reading":
                jump deleted_user_continue
                y "nobamba"
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
        # jump jambiserver

        # "[Additional content for further visits.]"
        menu:
            "Continue reading":
                jump deleted_user_continue

label deleted_user_continue:
    "No reply."
    return
