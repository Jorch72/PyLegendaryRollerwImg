#Tuple pairs of masterminds and villains they lead
import random
from goodies import pick_avenger, pick_xmen, pick_tech, pick_spider_friends, pick_mar_knights, pick_ranged_instinct, pick_str_tech_ranged, pick_instinct, pick_str_rang, pick_xforce, pick_covert, pick_mar_knights_str, pick_hero
from baddies import villains

paired_baddies = {'Galactus': 'Heralds of Galactus',
'Supreme Intelligence of the Kree':	'Kree Starforce',
'Thanos': 'Infinity Gems',
'Mole Man':	'Subterranea',
'Zombie Green Goblin': 'The Deadlands',
'Madelyne Pryor, Goblin Queen':	'Limbo',
'Wasteland Hulk': 'Wasteland',
'Nimrod, Super Sentinel': 'Sentinel Territories',
'King Hyperion': 'Utopolis',
'Spider-Queen':	'Spider-Infected',
'Shiklah, The Demon Bride':	'Monster Metropolis',
'Immortal Emperor Zheng Zhu': "K'un-Lun",
'Ragnarok':	'Registration Enforcers',
'Maria Hill, Director of S.H.I.E.L.D.':	'S.H.I.E.L.D. Elite',
'Misty Knight': 'Heroes for Hire',
'Authoritarian Iron Man': 'Superhuman Registration Act',
'Baron Helmut Zemo': 'Thunderbolts',
'Baron Heinrich Zemo':	'Masters of Evil (WWII)',
'Arnim Zola': "Zola's Creations",
'Carnage': 'Maximum Carnage',
'Mysterio': 'Sinister Six',
'Evil Deadpool': 'Evil Deadpool Corpse',
'Macho Gomez': "Deadpool's 'Friends'",
'Magneto': 'Brotherhood',
'Red Skull': 'HYDRA',
'Loki':	'Enemies of Asgard',
'Dr. Doom':	'Doombot Legion',
'Mephisto':	'Underworld',
'Stryfe': 'MLF',
'Apocalypse': 'Four Horsemen',
'Mr. Sinister':	'Marauders',
'Kingpin': 'Streets of New York'}

#Returns a Mastermind with their Villain pair - if the conditions are true also returns an opponent
def bad_pair():
    mastermind_pair, villain_pair = random.choice(list(paired_baddies.items()))
    oppenent = pick_hero()
    if mastermind_pair == 'Zombie Green Goblin':
        opponent = pick_avenger()
    elif mastermind_pair == 'Madelyne Pryor, Goblin Queen':
        opponent = pick_xmen()
    elif mastermind_pair == 'Nimrod, Super Sentinel':
        opponent = pick_tech()
    elif mastermind_pair == 'Wasteland Hulk':
        opponent = pick_tech()
    elif mastermind_pair == 'Spider-Queen':
        opponent = pick_spider_friends()
    elif mastermind_pair == 'Immortal Emperor Zheng Zhu':
        opponent = pick_mar_knights()
    elif mastermind_pair == 'Ragnarok':
        oppenent = pick_ranged_instinct()
    elif mastermind_pair == 'Misty Knight':
        oppenent = pick_mar_knights()
    elif mastermind_pair == 'Authoritarian Iron Man':
        oppenent = pick_str_tech_ranged()
    elif mastermind_pair == 'Baron Helmut Zemo':
        oppenent = pick_tech()
    elif mastermind_pair == 'Arnim Zola':
        oppenent = pick_tech()
    elif mastermind_pair == 'Mysterio':
        oppenent = pick_instinct()
    elif mastermind_pair == 'Magneto':
        oppenent = pick_xmen()
    elif mastermind_pair == 'Loki':
        oppenent = pick_str_rang()
    elif mastermind_pair == 'Mephisto':
        oppenent = pick_mar_knights()
    elif mastermind_pair == 'Stryfe':
        oppenent = pick_xforce()
    elif mastermind_pair == 'Apocalypse':
        oppenent = pick_instinct()
    elif mastermind_pair == 'Mr. Sinister':
        oppenent = pick_covert()
    elif mastermind_pair == 'Kingpin':
        oppenent = pick_mar_knights_str()
    else:
        oppenent = pick_hero()
    return(mastermind_pair, villain_pair, oppenent)
