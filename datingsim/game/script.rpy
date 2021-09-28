# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define e = Character("Eileen")

# Player options: name and pronouns
define t = Character("Me")
default mc_sub_up = ""       # Pronoun used as subject of the sentence (He is/She is/They are), uppercase and lowercase
default mc_sub_lo = ""
default mc_sct_up = ""       # Pronoun used as subject of the sentence and uses contraction (He's/She's/They're), uppercase and lowercase
default mc_sct_lo = ""
default mc_obj_up = ""       # Pronoun used as object of the sentence (Him/Her/Them), uppercase and lowercase
default mc_obj_lo = ""
default mc_pspc_up = ""      # Pronoun used as specific possessive (His/Her/Their), uppercase and lowercase
default mc_pspc_lo = ""
default mc_pgen_up = ""      # Pronoun used as general possessive (His/Hers/Theirs), uppercase and lowercase
default mc_pgen_lo = ""

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_black
    play music "<from 2>audio/passage.mp3" volume 0.3

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    # e "You've created a new Ren'Py game."

    # e "Once you add a story, pictures, and music, you can release it to the world!"

    "(My body feels light, like I'm floating in the air.)"

    "(But I can't see anything. I try to look around me, but everything is dark.)"

    "(It's scary at first, but now it feels peaceful. I close my eyes, and I let the wind carry me.)"

    "(Then, I feel something warm, like the Sun is gently shining on my skin.)"

    "(A slight chill passes by, like a cool autumn breeze that toussles my hair.)"

    "(And then, I feel like I've landed, like the wind has placed me gingerly on the ground.)"

    "(I open my eyes.)"

    scene bg_space:
        xalign 0.5
        yalign 0.5
        zoom 0.5
    with dissolve

    "(I look around me, and it's no longer darkness. Instead, I see a vast universe.)"

    "(I'm standing on a comet as it flies through space, as if it's giving me a tour of the galaxy.)"

    "(I can see all the planets of our solar system; from Mars, to Jupiter, even Pluto.)"

    "(And of course, our Earth.)"

    "(It's beautiful.)"

    "(A satellite passes by me, slowly beeping away.)"

    image satellite far:
        "satellite.png"
        xalign 0.5
        yalign 0.5
        zoom 0.25
    show satellite far
    with dissolve

    play sound "<from 0 to 2.5>audio/alarm.wav" volume 0.03

    "Beep. Beep. Beep."

    "(Why does that sound familiar?)"

    image satellite close:
        "satellite.png"
        xalign 0.5
        yalign 0.5
        zoom 0.5
    show satellite close
    with dissolve

    play sound "<from 0 to 2.5>audio/alarm.wav" volume 0.1

    "Beep! Beep! Beep!"

    "(The satellite is getting closer...!)"

    image satellite closer:
        "satellite.png"
        xalign 0.5
        yalign 0.5
        zoom 1.5
    show satellite closer
    with dissolve

    play sound "<from 0 to 2.5>audio/alarm.wav" volume 0.35

    "BEEP. BEEP. BEEP."

    "(I-I think it's going to crash with my comet!)"

    image satellite closest:
        "satellite.png"
        xalign 0.5
        yalign 0.5
        zoom 3.5
    show satellite closest
    with dissolve

    play sound "<from 0 to 2.5>audio/alarm.wav" volume 0.7

    "BEEP! BEEP! BEEP!"

    "(AHHHHHHHH--!!!)"

    stop music fadeout 0.1

    scene bg_bedroom:
        xalign 0.5
        yalign 0.5
    with fade

    play sound "<from 0 to 2.5>audio/alarm.wav" volume 0.1

    "BEEP! BEEP! BEEP!"

    t "Ugh..."

    play sound "audio/alarm_off.wav" volume 0.1

    "BEEP! BEE---"

    t "Finally, some peace and quiet..."

    "."

    ".."

    "..."

    t "WAIT A MINUTE-- WHAT TIME IS IT?!"

    t "Oh god, it's already 8:16! I need to get ready fast!"

    t "Alright, I'm all dressed up and ready to go."

    t "Oh right, my name tag. I should get that before I forget."

    python:
        name = renpy.input("What's your name?")
        name = name.strip() or "Taylor"
    menu:
        "What are your preferred pronouns?"

        "He/Him/His":
            $ mc_sub_up = "He is"
            $ mc_sub_lo = "he is"
            $ mc_sct_up = "He's"
            $ mc_sct_lo = "he's"
            $ mc_obj_up = "Him"
            $ mc_obj_lo = "him"
            $ mc_pspc_up = "His"
            $ mc_pspc_lo = "his"
            $ mc_pgen_up = "His"
            $ mc_pgen_lo = "his"
        "She/Her/Hers":
            $ mc_sub_up = "She is"
            $ mc_sub_lo = "she is"
            $ mc_sct_up = "She's"
            $ mc_sct_lo = "she's"
            $ mc_obj_up = "Her"
            $ mc_obj_lo = "her"
            $ mc_pspc_up = "Her"
            $ mc_pspc_lo = "her"
            $ mc_pgen_up = "Hers"
            $ mc_pgen_lo = "hers"
        "They/Them/Theirs":
            $ mc_sub_up = "They are"
            $ mc_sub_lo = "they are"
            $ mc_sct_up = "They're"
            $ mc_sct_lo = "they're"
            $ mc_obj_up = "Them"
            $ mc_obj_lo = "them"
            $ mc_pspc_up = "Their"
            $ mc_pspc_lo = "their"
            $ mc_pgen_up = "theirs"
            $ mc_pgen_lo = "theirs"
    "(I look down at my name tag, and it says \"[name]\", perfectly spelled and everything!)"

    t "Alright, looks like I've got everything! I should go before I-- HOLY CRAP, I'M REALLY LATE!"

    scene bg_isaac
    with fade
    play music "audio/planet.mp3"

    t "Wow, look at that."

    "(I find myself standing in front of the International Space Aeronautics and Astronomy Center, or ISAAC for short. Named after the famous Isaac Newton, of course!)"

    "(I frantically pull out my phone and double-check where I'm supposed to meet my new boss.)"

    "(I was able to make up for some lost time by breaking a few traffic rules, but now I need to make sure I don't get lost on this huge campus!)"

    t "Hm, \"Building 8, Room 52\"..."

    "(Luckily, there's a map of the campus nearby, so I take a quick look and try to memorize the path to the correct building.)"

    t "Alright, I think I got it down... Let's do this!"

    scene bg_hallway
    with fade

    t "*Ahem* Hellooo?"

    "(I'm standind in the middle of a semi-deserted hallway, looking at a door with a huge red sign posted on it.)"

    "WARNING: NO ACCESS TO ROOM 52"

    t "This {i}is{/i} the room, right...?"

    "(I double check my email again, and it defintely says 'Building 8, Room 52.' I even walked around this building several times to make sure it was the right place.)"

    "(I look down at the door handle.)"

    t "I mean, it doesn't hurt to try..."

    "(I place a shaky hand on the handle and slowly open the door. Surprisingly, it's unlocked, despite the warning sign.)"

    scene bg_controlroom
    with fade

    pause

    "hello world"

    # This ends the game.

    return
