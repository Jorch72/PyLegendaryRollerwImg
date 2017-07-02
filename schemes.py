#Hold the Schemes dict
import random
from goodies import pick_hero

def schemes():
    schemes = ['Brainwash the Military', 'Weave a Web of Lies', 'The Unbreakable Enigma Code', 'Change the Outcome of WWII',
            'The Clone Saga', 'Pan-Dimensional Plague', 'Steal the Weaponized Plutonium','Capture Baby Hope',
            'Massive Earthquake Generator', 'Super Hero Civil War', "Replace the Earth's Leaders with Killerbots",
            'Midtown Bank Robbery', 'Smash Two Dimensions Together', 'Dark Alliance', 'Corrupt the Next Generation of Heroes',
            'Enthrone the Barons of Battleworld', 'Deadlands Hordes Charge the Wall', 'Master the Mysteries of Kung-Fu',
            'Secret Wars', 'Sinister Ambitions', 'The God-Emperor of Battleworld', 'Predict Future Crime', 'Nitro the Supervillain Threatens Crowds',
            'Imprison Unregistered Superhumans', 'Dark Reign of H.A.M.M.E.R. Officers', 'Intergalactic Kree Nega-Bomb',
            'United States Split by Civil War', 'Unite the Shards', 'Bathe Earth in Cosmic Rays', 'Portals to the Dark Dimension',
            'Invincible Force Field', 'Flood the Planet with Melted Glaciers', 'Pull Reality into the Negative Zone',
            'Unleash the Power of the Cosmic Cube', 'The Legacy Virus']
    schemes = random.choice(schemes)
    hero, attribute = pick_hero()
    if schemes == 'Massive Earthquake Generator' and 'Strength' not in attribute:
        hero, attribute = pick_hero()
    elif schemes == 'The God-Emperor of Battleworld' and 'Tech' not in attribute:
        hero, attribute = pick_hero()
    elif schemes == 'The Legacy Virus' and 'Tech' not in attribute:
        hero, attribute = pick_hero()
    else:
        hero, attribute = pick_hero()
    return (schemes, hero, attribute)
