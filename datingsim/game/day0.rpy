label day0:

    scene bg_black
    play music "<from 2>audio/passage.mp3" volume 0.3

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
    with fade

    play sound "<from 0 to 2.5>audio/alarm.wav" volume 0.1

    "BEEP! BEEP! BEEP!"

    MC "Ugh..."

    play sound "audio/alarm_off.wav" volume 0.1

    "BEEP! BEE---"

    MC "Finally, some peace and quiet..."

    "."

    ".."

    "..."

    MC "WAIT A MINUTE-- WHAT TIME IS IT?!"

    MC "Oh god, it's already 8:16! I need to get ready fast!"

    MC "Alright, I'm all dressed up and ready to go."

    # "(I scramble to my desk and grab a few papers. I look down at them, horrified.)"

    # MC "Ah! I completely forgot to fills these in... I need to make sure to do that before I go to work today!"

    # call personality_quiz

    # "(As I finish up the form, I realize that was more of a personality quiz than an offical, professional form...)"

    # MC "Huh, kind of a weird thing to fill out..."

    #"(I place the form in my bag and grab my name tag. It says \"[name]\", perfectly spelled and everything!)"

    MC "Oh right, my name tag. I should get that before I forget."

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

    MC "Alright, looks like I've got everything! I should go before I-- HOLY CRAP, I'M REALLY LATE!"

    scene bg_isaac
    with fade
    play music "audio/planet.mp3"

    MC "Wow, look at that."

    "(I find myself standing in front of the International Space Aeronautics and Astronomy Center, or ISAAC for short. Named after the famous Isaac Newton, of course!)"

    "(I frantically pull out my phone and double-check where I'm supposed to meet my new boss.)"

    "(I was able to make up for some lost time by breaking a few traffic rules, but now I need to make sure I don't get lost on this huge campus!)"

    MC "Hm, \"Building 8, Room 52\"..."

    "(Luckily, there's a map of the campus nearby, so I take a quick look and try to memorize the path to the correct building.)"

    MC "Alright, I think I got it down... Let's do this!"

    scene bg_hallway
    with fade

    MC "*Ahem* Hellooo?"

    "(I'm standing in the middle of a semi-deserted hallway, looking at a door with a huge red sign posted on it.)"

    image door sign:
        "img_sign.jpg"
        xalign 0.5
        yalign 0.3
        zoom 0.5
    show door sign

    "RESTRICTED AREA: NO ACCESS TO ROOM 52"

    MC "This {i}is{/i} the room, right...?"

    hide door sign

    "(I double check my email again, and it defintely says 'Building 8, Room 52.' I even walked around this building several times to make sure it was the right place.)"

    "(I look down at the door handle.)"

    MC "I mean, it doesn't hurt to try..."

    "(I place a shaky hand on the handle and slowly open the door. Surprisingly, it's unlocked, despite the warning sign.)"

    scene bg_controlroom
    with fade

    "(I find myself in a strange control room, filled with large consoles with many blinking buttons. It doesn't seem like anyone's in here...)"

    Mars "Oh crap--!"

    "(There's a sudden crash towards the back of the room. I turn my head to see a strange-looking man crouching by the wall, a small metal table having fallen to the floor.)"

    "(The man straightens up, rubbing the back of his head sheepishly.)"

    show test_mars

    Mars "Dangit, there goes my first impression..."

    MC "Uh, and you are...?"

    "(The man turned to me, blushing in embarrassment. He had wild, messy red hair and his eyes were a vibrant orange.)"
    "(He had some weird crop top on, showing off his athletic features. I could only describe his clothes as being strangely historic, like he was from another time.)"

    Mars "Oh well, that's a bit of a complicated question--"

    Mars "My name's Mars. Like the planet, Mars. 'Cuz, well... I {i}am{/i} Mars."

    MC "You... {i}are{/i} Mars?"

    "(He laughed sheepishly.)"

    Mars "I can see how that can be confusing..."

    MC "So you're saying that you're {i}the{/i} Mars, the {i}planet{/i}?!"

    Mars "Yup! Welcome to ISAAC!"

    "(I stare blankly at him, dumbfounded.)"

    Mars "I know you're still a bit confused, so let me explain a bit!"

    Mars "Let me start with a question: Do you know why you're here today?"

    MC "Uh, I'm the new intern for ISAAC. I'm supposed to be--"

    "(I pause for a moment. I suddenly realize that I actually {i}don't{/i} know what I'm supposed to doing here...)"

    MC "--doing intern stuff. Y'know, like grabbing coffee and filing... files..."

    Mars "Lemme guess, you don't actually know why you're here."

    MC "Nope, not a clue."

    Mars "Well, you're actually participating in a super cool project called the \"Interplantery Exchange Program\"!"

    MC "...What's that?"

    "hello world"
