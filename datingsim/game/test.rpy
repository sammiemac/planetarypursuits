# This file is for testing game features
default hike = False
default playg = False
default bike = False
default fish = False
default pic = False

label test:

    show test_mars
    Mars "Hello world!"
    hide test_mars
    show test_jupiter
    Jupiter "Hello world."
    hide test_jupiter
    show test_pluto
    Pluto "H-Hello world..."
    hide test_pluto

    "Gonna test how jumps work."
    call jumpy
    "If you're seeing this, the test worked!"

    show test_jupiter
    Jupiter "So is there a reason why I'm here?"
    menu:
        MC "Uh..."
        "I just wanted to stare into your pretty eyes.":
            "(They seemed to like that...)"
            $ j_points += 5
            "JUPITER POINTS: [j_points]"
            jump eyes
        "I came here to talk smack about you.":
            "(They didn't like that...)"
            $ j_points -= 5
            "JUPITER POINTS: [j_points]"
            jump smack
        "I'm not really sure either.":
            jump idk

label jumpy:
    "Hello there"
    return

label eyes:
    MC "I just wanted to stare into your eyes. Y'know, humans don't usually have that eye color!"
    "(Jupiter blushes a little bit.)"
    Jupiter "It's whatever, I guess."
    jump part2

label smack:
    MC "I came here to talk smack about you. Y'know, I expected you to be a lot grander than the other planets."
    "(Jupiter glares at you.)"
    Jupiter "Hmph, I don't need a human to be impressed by me."
    jump part2

label idk:
    MC "I'm not really sure either. Honestly, I was going to ask you the exact same question!"
    "(Jupiter sighs.)"
    jump part2

label part2:
    call screen park_imagemap

screen park_imagemap():
    imagemap:
        auto "screen park %s"

        hotspot (402, 60, 207, 207):
            if hike is False:
                action Jump("hiking")
            else:
                action Notify("You already did this today!")
        hotspot (86, 292, 200, 200):
            if playg is False:
                action Jump("playground")
            else:
                action Notify("You already did this today!")
        hotspot (506, 467, 200, 200):
            if bike is False:
                action Jump("biking")
            else:
                action Notify("You already did this today!")
        hotspot (782, 183, 200, 200):
            if fish is False:
                action Jump("fishing")
            else:
                action Notify("You already did this today!")
        hotspot (1023, 378, 207, 207):
            if pic is False:
                action Jump("picnic")
            else:
                action Notify("You already did this today!")

label hiking:
    "You chose hiking"
    $ hike = True
    $ stamina -= 1
    if stamina <= 0:
        jump done
    else:
        call screen park_imagemap

label playground:
    "You chose playground"
    $ playg = True
    $ stamina -= 1
    if stamina <= 0:
        jump done
    else:
        call screen park_imagemap

label biking:
    "You chose biking"
    $ bike = True
    $ stamina -= 1
    if stamina <= 0:
        jump done
    else:
        call screen park_imagemap

label fishing:
    "You chose fishing"
    $ fish = True
    $ stamina -= 1
    if stamina <= 0:
        jump done
    else:
        call screen park_imagemap

label picnic:
    "You chose picnic"
    $ pic = True
    $ stamina -= 1
    if stamina <= 0:
        jump done
    else:
        call screen park_imagemap

label done:
    "Guess the date is done for today."
