#Chooses baddies based on criterion

import random
from baddies import henchmen
from goodies import pick_hero, pick_covert, pick_tech_ranged, pick_tech, pick_spider_friends, pick_str_rang

def hench_no_rand():
    henchie = henchmen()
    if henchie == 'Spider-Friends':
        hench_no_rand = pick_spider_friends()
    elif henchie == 'Phalanx':
        hench_no_rand = pick_tech()
    elif henchie == 'Thor Corps':
        hench_no_rand = pick_str_rang()
    elif henchie == 'Ghost Racers':
        hench_no_rand = pick_covert()
    elif henchie == 'Doombot Legion':
        hench_no_rand = pick_tech_ranged()
    else:
        hench_no_rand = pick_hero()
    return(henchie, hench_no_rand)
