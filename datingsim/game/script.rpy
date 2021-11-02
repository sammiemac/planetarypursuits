# This file is used to define global variables and call each script file for each day of the game.

# Defining Player options: name and pronouns
define MC = Character("Me")
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

# Defining the Planets
define Earth = Character("Earth")
define Mars = Character("Mars", who_color="#e6001b")
define Jupiter = Character("Jupiter", who_color="#d64700")
define Pluto = Character("Pluto", who_color="#ff75d8")

# Defining Player variables for relationships and stamina
default stamina = 3
default m_points = 5
default j_points = 5
default p_points = 5

# Defining Player stats
# default sporty = 0
# default charming = 0
# default intelligent = 0
# default creative = 0
# default playful = 0

# The game starts here.
label start:

    call day0
    call test

    return
