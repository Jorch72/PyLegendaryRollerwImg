#Holds the baddie dicts
import random
from goodies import pick_spider_friends, pick_tech, pick_str_rang, pick_covert, pick_tech_ranged, pick_hero

def masterminds():
    masterminds = ['Galactus', 'Supreme Intelligence of the Kree', 'Thanos', 'Mole Man', 'Zombie Green Goblin', 'Madelyne Pryor, Goblin Queen',
                'Wasteland Hulk', 'Nimrod, Super Sentinel', 'King Hyperion', 'Spider-Queen', 'Shiklah, The Demon Bride', 'Immortal Emperor Zheng Zhu',
                'Ragnarok', 'Maria Hill, Director of S.H.I.E.L.D.', 'Misty Knight', 'Authoritarian Iron Man', 'Baron Helmut Zemo', 'Baron Heinrich Zemo',
                'Arnim Zola', 'Carnage', 'Mysterio', 'Evil Deadpool', 'Macho Gomez', 'Magneto', 'Red Skull', 'Loki', 'Dr. Doom', 'Mephisto', 'Stryfe',
                'Apocalypse', 'Mr. Sinister', 'Kingpin']
    masterminds = random.choice(masterminds)
    return masterminds

def henchmen():
    henchmen = ['Sentinel', 'Hand Ninjas', 'Savage Land Mutates', 'Phalanx', 'Maggia Goons', 'Cape-Killers', 'Mandroid',
            'Khonshu Guardians', 'Magma Men', 'M.O.D.O.K.S', 'Thor Corps', 'Ghost Racers', 'Doombot Legion', 'Spider-Infected']
    henchmen = random.choice(henchmen)
    return henchmen

def villains():
    villains = ['Heralds of Galactus', 'Kree Starforce', 'Infinity Gems', 'Subterranea', 'The Deadlands', 'Limbo', 'Wasteland',
            'Sentinel Territories', 'Utopolis', 'Monster Metropolis', "K'un-Lun", 'Registration Enforcers', 'S.H.I.E.L.D. Elite',
            'Heroes for Hire', 'Superhuman Registration Act', 'Thunderbolts', 'Masters of Evil (WWII)', "Zola's Creations",
            'Maximum Carnage', 'Sinister Six', 'Evil Deadpool Corpse', 'HYDRA',
            'Enemies of Asgard', 'Underworld', 'MLF', 'Four Horsemen', 'Marauders', 'Streets of New York',
            'Great Lakes Avengers', "Deadpool's Secret Secret Wars", "X-Men '92", 'Guardians of Knowhere', 'Domain of Apocalypse',
            'Manhattan (Earth-1610)', 'Radiation', 'Skrulls', 'Spider-Foes', 'Masters of Evil']
    villains = random.choice(villains)
    return villains
