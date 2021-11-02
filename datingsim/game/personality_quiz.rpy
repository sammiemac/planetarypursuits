# This is a personality quiz that determines the Player's stats atthe beginning of the game.

label personality_quiz:

    "Thank you for choosing spend your summer at the International Space Aeronautics and Astronomy Center!"
    "Please fill out this form and present it to your manager on your first day."

    python:
        name = renpy.input("What is your name?")
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

    menu:
        "Question 1: What do you do in your spare time?"

        "I really like sports, whether I'm playing or just watching!":
            $ sporty += 3
        "I like hanging out with my friends or going out to parties with other people!":
            $ charming += 3
        "I like to endulge in my hobby, which is usually arts and crafts!":
            $ creative += 3
        "I prefer spending time by myself, like by reading a book or researching an interesting topic!":
            $ intelligent += 3
        "I usually play video games or board games, either online or with my friends!":
            $ playful += 3
    
    return
