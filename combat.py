import sys
sys.path.append("Classes")
from Classes.Pokemon import Pokemon
from Classes.Combat import Combat

pokemon1 = Pokemon("Salameche", 1, "Feu", 39, 52, 33)
pokemon2 = Pokemon("Carapuce", 1, "Eau", 44, 48, 34)
duel = Combat(pokemon1, pokemon2)
print (duel.attack(pokemon1, pokemon2))