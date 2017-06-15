#Pairs the villains with the 'always fights'

import random
from baddies import villains
from goodies import pick_hero, pick_str_covert, pick_avenger_tech, pick_ran_covert, pick_avenger, pick_instinct, pick_str_tech, pick_xmen, pick_ranged, pick_mar_knights, pick_strength, pick_covert, pick_tech_instinct, pick_xmen

def paired_villains():
    baddie = villains()
    hero = pick_hero()
    if baddie == 'The Deadlands':
        hero = pick_avenger()
    elif baddie == 'Registration Enforcers':
        hero = pick_instinct()
    elif baddie == 'Superhuman Registration Act':
        hero = pick_str_tech()
    elif baddie == 'Sinister Six':
        hero = pick_instinct()
    elif baddie == 'Brotherhood':
        hero = pick_xmen()
    elif baddie == 'Enemies of Asgard':
        hero = pick_ranged()
    elif baddie == 'Underworld':
        hero = pick_mar_knights()
    elif baddie == 'Four Horsemen':
        hero = pick_instinct()
    elif baddie == 'Streets of New York':
        hero = pick_strength()
    elif baddie == 'CSA Special Marshals':
        hero = pick_covert()
    elif baddie == 'Great Lakes Avengers':
        hero = pick_str_covert()
    elif baddie == "X-Men '92":
        hero = pick_tech_instinct()
    elif baddie == 'Domain of Apocalypse':
        hero = pick_xmen()
    elif baddie == 'Manhattan (Earth-1610)':
        hero = pick_ran_covert()
    elif baddie == 'Radiation':
        hero = pick_strength()
    elif baddie == 'Spider-Foes':
        hero = pick_covert()
    elif baddie == 'Masters of Evil':
        hero = pick_avenger_tech()
    return (baddie, hero)
