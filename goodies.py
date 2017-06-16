import random
#Holds the Dicts for the goodies

#Key is Hero: Value is icons provided
team_avengers = {'Black Widow': 'Tech, Instinct', 'Captain America': 'Strength, Tech, Instinct, Covert', 'Captain America (Falcon)': 'Tech, Ranged, Instinct, Covert',
                'Captain America 1941': 'Strength, Tech, Instinct, Covert', 'Captain America, Secret Avenger': 'Strength, Tech, Ranged, Instinct, Covert',
                'Captain Marvel': 'Strength, Ranged', 'Cloak and Dagger': 'Ranged, Covert', 'Daredevil': 'Strength, Instinct, Covert', 'Falcon': 'Tech, Ranged, Instinct',
                'Goliath': 'Strength, Tech', 'Hawkeye':	'Tech, Instinct', 'Hercules': 'Strength, Tech, Instinct', 'Hulk': 'Strength, Instinct', 'Hulkling': 'Strength, Covert',
                'Iron Man': 'Tech, Ranged', 'Lady Thor': 'Tech, Ranged', 'Luke Cage': 'Strength, Instinct', 'Patriot': 'Strength, Tech, Instinct, Covert',
                'Peter Parker': 'Tech, Instinct', 'Stature': 'Strength, Tech', 'The Captain and the Devil': 'Strength, Tech, Ranged, Instinct, Covert', 'Thor': 'Strength, Ranged',
                'Tigra': 'Instinct, Covert', 'Vision': 'Tech, Ranged', 'Wiccan': 'Ranged, Covert'}


team_avengers_xmen = {'Storm and Black Panther': 'Tech, Ranged, Instinct, Covert'}


team_cabal = {'Black Swan': 'Ranged, Instinct, Covert', 'Corvus Glaive': 'Strength, Tech, Instinct', 'Maximus': 'Tech, Covert', 'Namor, The Sub-Mariner': 'Strength, Instinct',
            'Thanos': 'Strength, Ranged', 'Proxima Midnight': 'Instinct, Covert'}


team_fantasticfour = {'Human Torch': 'Ranged, Instinct', 'Invisible Woman': 'Ranged, Covert', 'Mr. Fantastic': 'Tech, Instinct', 'Thing': 'Strength, Instinct'}



team_guardians = {'Drax the Destroyer': 'Strength, Instinct', 'Gamora': 'Instinct, Covert', 'Groot': 'Strength, Covert', 'Rocket Raccoon': 'Tech, Ranged, Instinct',
                'Star-Lord': 'Tech, Ranged, Covert'}



team_hydra = {'Bob, Agent of Hydra': 'Tech, Instinct'}



team_illuminati = {'Beast': 'Strength, Tech', 'Black Bolt': 'Strength, Ranged, Covert', 'Black Panther': 'Strength, Tech, Instinct, Covert', 'Captain Britain': 'Strength, Covert',
                'Dr. Strange': 'Ranged, Instinct, Covert', 'Superior Iron Man': 'Tech, Ranged'}



team_marvelknights = {'Blade': 'Strength, Tech, Instinct, Covert', 'Daredevil': 'Strength, Tech, Instinct, Covert', 'Dr. Punisher, The Soldier Supreme': 'Tech, Ranged',
                    'Elektra': 'Instinct, Covert', 'Ghost Rider': 'Strength, Tech, Ranged', 'Iron Fist': 'Strength, Instinct', 'Moon Knight': 'Tech, Instinct',
                    'Punisher': 'Strength, Tech', 'Shang-Chi': 'Instinct, Covert'}



team_mercs = {'Deadpool': 'Strength, Tech, Instinct, Covert', 'Slapstick': 'Strength, Ranged', 'Solo': 'Tech, Instinct', 'Stingray': 'Tech, Ranged'}


team_newwarriors = {'Speedball': 'Ranged, Covert'}

team_shield = {'Agent X-13': 'Tech, Ranged, Instinct, Covert', 'Elsa Bloodstone': 'Strength, Tech, Ranged, Instinct, Covert', 'Nick Fury': 'Strength, Tech, Covert',
            'Steve Rodgers, Director of S.H.I.E.L.D': 'Strength, Tech, Instinct, Covert'}



team_spiderfriends = {'Agent Venom': 'Strength, Tech, Instinct', 'Black Cat': 'Instinct, Covert', 'Scarlet Spider': 'Strength, Instinct, Covert', 'Silk': 'Strength, Tech, Ranged, Instinct, Covert',
                    'Spider-Gwen': 'Strength, Tech, Instinct, Covert', 'Spider-Man': 'Strength, Tech, Instinct, Covert', 'Spider-Woman': 'Strength, Ranged, Covert',
                    'Symbiote Spider-Man': 'Strength, Ranged, Instinct, Covert', 'Ultimate Spider-Man': 'Strength, Tech, Instinct, Covert'}


team_unaffiliated = {'Arkon The Magnificent': 'Strength, Ranged, Instinct, Covert', 'Deadpool': 'Tech, Instinct, Covert',
                    'Silver Surfer': 'Strength, Ranged, Covert', 'Winter Soldier': 'Strength, Tech, Covert'}


team_xforce = {'Cable': 'Tech, Ranged, Covert', 'Colossus': 'Strength, Covert', 'Domino': 'Tech, Instinct, Covert', 'Forge': 'Tech', 'Wolverine': 'Strength, Instinct, Covert'}



team_xmen = {'Angel': 'Strength, Instinct, Covert', 'Apocalyptic Kitty Pryde': 'Tech, Covert', 'Bishop': 'Tech, Ranged, Covert', 'Cyclops': 'Strength, Ranged',
            'Emma Frost': 'Strength, Ranged, Instinct, Covert', 'Gambit': 'Ranged, Instinct, Covert', 'Iceman': 'Strength, Ranged', 'Jean Grey': 'Ranged, Covert',
            'Magik': 'Ranged, Covert', 'Nightcrawler': 'Instinct, Covert', 'Old Man Logan': 'Instinct, Covert', 'Phoeix Force Cyclops': 'Ranged, Instinct, Covert',
            'Professor X': 'Ranged, Instinct, Covert', 'Rogue': 'Strength, Covert', 'Ruby Summers': 'Strenght, Ranged', 'Soulsword Colossus': 'Strength, Instinct, Covert',
            'Storm': 'Ranged, Covert', 'Time-Traveling Jean Grey': 'Ranged, Instinct, Covert', 'Wolverine': 'Instinct'}

# #Function to pick a hero
def pick_hero():
    hero, attribute = random.choice(list(team_xmen.items()) + list(team_xforce.items()) + list(team_spiderfriends.items()) + list(team_shield.items()) + list(team_newwarriors.items()) +
                                    list(team_mercs.items()) + list(team_marvelknights.items()) + list(team_illuminati.items()) +
                                    list(team_hydra.items()) + list(team_guardians.items()) + list(team_fantasticfour.items()) +
                                    list(team_cabal.items()) + list(team_avengers_xmen.items()) + list(team_avengers.items()))

    return(hero, attribute)

#Function to pick and avenger if a Mastermind Villian requires it
def pick_avenger():
    hero, attribute = random.choice(list(team_avengers.items()))
    while attribute != 'Strength, Covert':
        hero, attribute = random.choice(list(team_avengers.items()))
    else:
        return(hero, attribute)

def pick_xmen():
    hero, attribute = random.choice(list(team_xmen.items()))
    return(hero, attribute)

def pick_tech():
    hero, attribute = random.choice(list(team_xmen.items()) + list(team_xforce.items()) + list(team_spiderfriends.items()) + list(team_shield.items()) + list(team_newwarriors.items()) +
                                            list(team_mercs.items()) + list(team_marvelknights.items()) + list(team_illuminati.items()) +
                                            list(team_hydra.items()) + list(team_guardians.items()) + list(team_fantasticfour.items()) +
                                            list(team_cabal.items()) + list(team_avengers_xmen.items()) + list(team_avengers.items()))
    while 'Tech' not in attribute:
        hero, attribute = random.choice(list(team_xmen.items()) + list(team_xforce.items()) + list(team_spiderfriends.items()) + list(team_shield.items()) + list(team_newwarriors.items()) +
                                                list(team_mercs.items()) + list(team_marvelknights.items()) + list(team_illuminati.items()) +
                                                list(team_hydra.items()) + list(team_guardians.items()) + list(team_fantasticfour.items()) +
                                                list(team_cabal.items()) + list(team_avengers_xmen.items()) + list(team_avengers.items()))
    else:
        return(hero, attribute)

def pick_spider_friends():
    hero, attribute = random.choice(list(team_spiderfriends.items()))
    return(hero, attribute)

def pick_mar_knights():
    hero, attribute = random.choice(list(team_marvelknights.items()))
    return(hero, attribute)

def pick_ranged_instinct():
    hero, attribute = random.choice(list(team_xmen.items()) + list(team_xforce.items()) + list(team_spiderfriends.items()) + list(team_shield.items()) + list(team_newwarriors.items()) +
                                            list(team_mercs.items()) + list(team_marvelknights.items()) + list(team_illuminati.items()) +
                                            list(team_hydra.items()) + list(team_guardians.items()) + list(team_fantasticfour.items()) +
                                            list(team_cabal.items()) + list(team_avengers_xmen.items()) + list(team_avengers.items()))
    while 'Ranged, Instinct' not in attribute:
        hero, attribute = random.choice(list(team_xmen.items()) + list(team_xforce.items()) + list(team_spiderfriends.items()) + list(team_shield.items()) + list(team_newwarriors.items()) +
                                                list(team_mercs.items()) + list(team_marvelknights.items()) + list(team_illuminati.items()) +
                                                list(team_hydra.items()) + list(team_guardians.items()) + list(team_fantasticfour.items()) +
                                                list(team_cabal.items()) + list(team_avengers_xmen.items()) + list(team_avengers.items()))
    else:
        return(hero, attribute)

def pick_str_tech_ranged():
    hero, attribute = random.choice(list(team_xmen.items()) + list(team_xforce.items()) + list(team_spiderfriends.items()) + list(team_shield.items()) + list(team_newwarriors.items()) +
                                            list(team_mercs.items()) + list(team_marvelknights.items()) + list(team_illuminati.items()) +
                                            list(team_hydra.items()) + list(team_guardians.items()) + list(team_fantasticfour.items()) +
                                            list(team_cabal.items()) + list(team_avengers_xmen.items()) + list(team_avengers.items()))
    while 'Strength, Tech, Ranged' not in attribute:
        hero, attribute = random.choice(list(team_xmen.items()) + list(team_xforce.items()) + list(team_spiderfriends.items()) + list(team_shield.items()) + list(team_newwarriors.items()) +
                                                list(team_mercs.items()) + list(team_marvelknights.items()) + list(team_illuminati.items()) +
                                                list(team_hydra.items()) + list(team_guardians.items()) + list(team_fantasticfour.items()) +
                                                list(team_cabal.items()) + list(team_avengers_xmen.items()) + list(team_avengers.items()))
    else:
        return(hero, attribute)

def pick_instinct():
    hero, attribute = random.choice(list(team_xmen.items()) + list(team_xforce.items()) + list(team_spiderfriends.items()) + list(team_shield.items()) + list(team_newwarriors.items()) +
                                            list(team_mercs.items()) + list(team_marvelknights.items()) + list(team_illuminati.items()) +
                                            list(team_hydra.items()) + list(team_guardians.items()) + list(team_fantasticfour.items()) +
                                            list(team_cabal.items()) + list(team_avengers_xmen.items()) + list(team_avengers.items()))
    while 'Instinct' not in attribute:
        hero, attribute = random.choice(list(team_xmen.items()) + list(team_xforce.items()) + list(team_spiderfriends.items()) + list(team_shield.items()) + list(team_newwarriors.items()) +
                                                list(team_mercs.items()) + list(team_marvelknights.items()) + list(team_illuminati.items()) +
                                                list(team_hydra.items()) + list(team_guardians.items()) + list(team_fantasticfour.items()) +
                                                list(team_cabal.items()) + list(team_avengers_xmen.items()) + list(team_avengers.items()))
    else:
        return(hero, attribute)

def pick_str_rang():
    hero, attribute = random.choice(list(team_xmen.items()) + list(team_xforce.items()) + list(team_spiderfriends.items()) + list(team_shield.items()) + list(team_newwarriors.items()) +
                                            list(team_mercs.items()) + list(team_marvelknights.items()) + list(team_illuminati.items()) +
                                            list(team_hydra.items()) + list(team_guardians.items()) + list(team_fantasticfour.items()) +
                                            list(team_cabal.items()) + list(team_avengers_xmen.items()) + list(team_avengers.items()))
    while 'Strength, Ranged' not in attribute:
        hero, attribute = random.choice(list(team_xmen.items()) + list(team_xforce.items()) + list(team_spiderfriends.items()) + list(team_shield.items()) + list(team_newwarriors.items()) +
                                                list(team_mercs.items()) + list(team_marvelknights.items()) + list(team_illuminati.items()) +
                                                list(team_hydra.items()) + list(team_guardians.items()) + list(team_fantasticfour.items()) +
                                                list(team_cabal.items()) + list(team_avengers_xmen.items()) + list(team_avengers.items()))
    else:
        return(hero, attribute)

def pick_xforce():
    hero, attribute = random.choice(list(team_xforce.items()))
    return(hero, attribute)

def pick_covert():
    hero, attribute = random.choice(list(team_xmen.items()) + list(team_xforce.items()) + list(team_spiderfriends.items()) + list(team_shield.items()) + list(team_newwarriors.items()) +
                                            list(team_mercs.items()) + list(team_marvelknights.items()) + list(team_illuminati.items()) +
                                            list(team_hydra.items()) + list(team_guardians.items()) + list(team_fantasticfour.items()) +
                                            list(team_cabal.items()) + list(team_avengers_xmen.items()) + list(team_avengers.items()))
    while 'Covert' not in attribute:
        hero, attribute = random.choice(list(team_xmen.items()) + list(team_xforce.items()) + list(team_spiderfriends.items()) + list(team_shield.items()) + list(team_newwarriors.items()) +
                                                list(team_mercs.items()) + list(team_marvelknights.items()) + list(team_illuminati.items()) +
                                                list(team_hydra.items()) + list(team_guardians.items()) + list(team_fantasticfour.items()) +
                                                list(team_cabal.items()) + list(team_avengers_xmen.items()) + list(team_avengers.items()))
    else:
        return(hero, attribute)

def pick_mar_knights_str():
    hero, attribute = random.choice(list(team_marvelknights.items()))
    while 'Strength' not in attribute:
        hero, attribute = random.choice(list(team_marvelknights.items()))
    else:
        return(hero, attribute)

def pick_tech_ranged():
    hero, attribute = random.choice(list(team_xmen.items()) + list(team_xforce.items()) + list(team_spiderfriends.items()) + list(team_shield.items()) + list(team_newwarriors.items()) +
                                            list(team_mercs.items()) + list(team_marvelknights.items()) + list(team_illuminati.items()) +
                                            list(team_hydra.items()) + list(team_guardians.items()) + list(team_fantasticfour.items()) +
                                            list(team_cabal.items()) + list(team_avengers_xmen.items()) + list(team_avengers.items()))
    while 'Tech, Ranged' not in attribute:
        hero, attribute = random.choice(list(team_xmen.items()) + list(team_xforce.items()) + list(team_spiderfriends.items()) + list(team_shield.items()) + list(team_newwarriors.items()) +
                                                list(team_mercs.items()) + list(team_marvelknights.items()) + list(team_illuminati.items()) +
                                                list(team_hydra.items()) + list(team_guardians.items()) + list(team_fantasticfour.items()) +
                                                list(team_cabal.items()) + list(team_avengers_xmen.items()) + list(team_avengers.items()))
    else:
        return(hero, attribute)

def pick_str_tech():
    hero, attribute = random.choice(list(team_xmen.items()) + list(team_xforce.items()) + list(team_spiderfriends.items()) + list(team_shield.items()) + list(team_newwarriors.items()) +
                                            list(team_mercs.items()) + list(team_marvelknights.items()) + list(team_illuminati.items()) +
                                            list(team_hydra.items()) + list(team_guardians.items()) + list(team_fantasticfour.items()) +
                                            list(team_cabal.items()) + list(team_avengers_xmen.items()) + list(team_avengers.items()))
    while 'Strength, Tech' not in attribute:
        hero, attribute = random.choice(list(team_xmen.items()) + list(team_xforce.items()) + list(team_spiderfriends.items()) + list(team_shield.items()) + list(team_newwarriors.items()) +
                                                list(team_mercs.items()) + list(team_marvelknights.items()) + list(team_illuminati.items()) +
                                                list(team_hydra.items()) + list(team_guardians.items()) + list(team_fantasticfour.items()) +
                                                list(team_cabal.items()) + list(team_avengers_xmen.items()) + list(team_avengers.items()))
    else:
        return(hero, attribute)

def pick_ranged():
    hero, attribute = random.choice(list(team_xmen.items()) + list(team_xforce.items()) + list(team_spiderfriends.items()) + list(team_shield.items()) + list(team_newwarriors.items()) +
                                            list(team_mercs.items()) + list(team_marvelknights.items()) + list(team_illuminati.items()) +
                                            list(team_hydra.items()) + list(team_guardians.items()) + list(team_fantasticfour.items()) +
                                            list(team_cabal.items()) + list(team_avengers_xmen.items()) + list(team_avengers.items()))
    while 'Ranged' not in attribute:
        hero, attribute = random.choice(list(team_xmen.items()) + list(team_xforce.items()) + list(team_spiderfriends.items()) + list(team_shield.items()) + list(team_newwarriors.items()) +
                                                list(team_mercs.items()) + list(team_marvelknights.items()) + list(team_illuminati.items()) +
                                                list(team_hydra.items()) + list(team_guardians.items()) + list(team_fantasticfour.items()) +
                                                list(team_cabal.items()) + list(team_avengers_xmen.items()) + list(team_avengers.items()))
    else:
        return(hero, attribute)

def pick_strength():
    hero, attribute = random.choice(list(team_xmen.items()) + list(team_xforce.items()) + list(team_spiderfriends.items()) + list(team_shield.items()) + list(team_newwarriors.items()) +
                                            list(team_mercs.items()) + list(team_marvelknights.items()) + list(team_illuminati.items()) +
                                            list(team_hydra.items()) + list(team_guardians.items()) + list(team_fantasticfour.items()) +
                                            list(team_cabal.items()) + list(team_avengers_xmen.items()) + list(team_avengers.items()))
    while 'Strength' not in attribute:
        hero, attribute = random.choice(list(team_xmen.items()) + list(team_xforce.items()) + list(team_spiderfriends.items()) + list(team_shield.items()) + list(team_newwarriors.items()) +
                                                list(team_mercs.items()) + list(team_marvelknights.items()) + list(team_illuminati.items()) +
                                                list(team_hydra.items()) + list(team_guardians.items()) + list(team_fantasticfour.items()) +
                                                list(team_cabal.items()) + list(team_avengers_xmen.items()) + list(team_avengers.items()))
    else:
        return(hero, attribute)

def pick_str_covert():
    hero, attribute = random.choice(list(team_xmen.items()) + list(team_xforce.items()) + list(team_spiderfriends.items()) + list(team_shield.items()) + list(team_newwarriors.items()) +
                                            list(team_mercs.items()) + list(team_marvelknights.items()) + list(team_illuminati.items()) +
                                            list(team_hydra.items()) + list(team_guardians.items()) + list(team_fantasticfour.items()) +
                                            list(team_cabal.items()) + list(team_avengers_xmen.items()) + list(team_avengers.items()))
    while 'Strength, Covert' not in attribute:
        hero, attribute = random.choice(list(team_xmen.items()) + list(team_xforce.items()) + list(team_spiderfriends.items()) + list(team_shield.items()) + list(team_newwarriors.items()) +
                                                list(team_mercs.items()) + list(team_marvelknights.items()) + list(team_illuminati.items()) +
                                                list(team_hydra.items()) + list(team_guardians.items()) + list(team_fantasticfour.items()) +
                                                list(team_cabal.items()) + list(team_avengers_xmen.items()) + list(team_avengers.items()))
    else:
        return(hero, attribute)

def pick_tech_instinct():
    hero, attribute = random.choice(list(team_xmen.items()) + list(team_xforce.items()) + list(team_spiderfriends.items()) + list(team_shield.items()) + list(team_newwarriors.items()) +
                                            list(team_mercs.items()) + list(team_marvelknights.items()) + list(team_illuminati.items()) +
                                            list(team_hydra.items()) + list(team_guardians.items()) + list(team_fantasticfour.items()) +
                                            list(team_cabal.items()) + list(team_avengers_xmen.items()) + list(team_avengers.items()))
    while 'Tech, Instinct' not in attribute:
        hero, attribute = random.choice(list(team_xmen.items()) + list(team_xforce.items()) + list(team_spiderfriends.items()) + list(team_shield.items()) + list(team_newwarriors.items()) +
                                                list(team_mercs.items()) + list(team_marvelknights.items()) + list(team_illuminati.items()) +
                                                list(team_hydra.items()) + list(team_guardians.items()) + list(team_fantasticfour.items()) +
                                                list(team_cabal.items()) + list(team_avengers_xmen.items()) + list(team_avengers.items()))
    else:
        return(hero, attribute)

def pick_ran_covert():
    hero, attribute = random.choice(list(team_xmen.items()) + list(team_xforce.items()) + list(team_spiderfriends.items()) + list(team_shield.items()) + list(team_newwarriors.items()) +
                                            list(team_mercs.items()) + list(team_marvelknights.items()) + list(team_illuminati.items()) +
                                            list(team_hydra.items()) + list(team_guardians.items()) + list(team_fantasticfour.items()) +
                                            list(team_cabal.items()) + list(team_avengers_xmen.items()) + list(team_avengers.items()))
    while 'Ranged, Covert' not in attribute:
        hero, attribute = random.choice(list(team_xmen.items()) + list(team_xforce.items()) + list(team_spiderfriends.items()) + list(team_shield.items()) + list(team_newwarriors.items()) +
                                                list(team_mercs.items()) + list(team_marvelknights.items()) + list(team_illuminati.items()) +
                                                list(team_hydra.items()) + list(team_guardians.items()) + list(team_fantasticfour.items()) +
                                                list(team_cabal.items()) + list(team_avengers_xmen.items()) + list(team_avengers.items()))
    else:
        return(hero, attribute)

def pick_avenger_tech():
    hero, attribute = random.choice(list(team_avengers.items()))
    while 'Tech' not in attribute:
        hero, attribute = random.choice(list(team_avengers.items()))
    else:
        return(hero, attribute)
