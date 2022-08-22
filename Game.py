# No idea what this game is yet, but it has 4 elements lol
# maybe it'sa fire emblem + ff tactics clone?
# how do you get into a battle?
# basis is elemental war
# why a battle at all and not a matching game?
# save this for later, try something practical
import os

damage_types = (
    "FIRE",
    "WATER",
    "AIR",
    "EARTH"
)
elemental_type_pairs = {
    "FIRE": "WATER",
    "WATER": "AIR",
    "AIR": "EARTH",
    "EARTH": "FIRE",
}
unit_types = (
    "SCHOLAR",
    "KNIGHT",
    "MUSE",
    "THIEF",
    "MAGE"
)
unit_types_upgrades = {
    "SCHOLAR": "ALCHEMIST",
    "KNIGHT": "PALADIN",
    "MUSE": "BARD",
    "THIEF": "ROGUE",
    "MAGE": "SORCERER"
}
weapon_types = {
    "AXE": "SWORD",
    "SWORD": "SPEAR",
    "SPEAR": "BOW",
    "BOW": "KNIFE",
    "KNIFE": "AXE"
}


# default location? or dialogbox?
def open_saved_game():
    gamefile = os.startfile("C:\\")


def attack(Userattack):
    try:
        return elemental_type_pairs[Userattack]
    except KeyError:
        print('Invalid attacking type')


# begin game here:
print(f"Select a class:")
for unit in unit_types:
    print(f'{unit}'.upper())
try :
    player_class_input = input().upper()
    if player_class_input in unit_types:
    #player class is assigned here
     player_class = player_class_input
except:
    print(1)

print(player_class_input)
print(unit_types_upgrades[player_class_input])
# User_attack = input()
# print(attack(User_attack))
