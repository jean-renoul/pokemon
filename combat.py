import sys
sys.path.append("Classes")
from Classes.Pokemon import Pokemon
from Classes.Combat import Combat
from Classes.Moves import Moves
from globals import *
import time
import random

pokemon1 = salameche
pokemon2 = random.choice(liste_pokemon)
duel = Combat(pokemon1, pokemon2)

while pokemon1.vie > 0 and pokemon2.vie > 0:
    choix_move = input(f"Quel move voulez-vous utiliser ? {pokemon1.move1.nom} ou {pokemon1.move2.nom} ? ")
    if choix_move == pokemon1.move1.nom:
        choix_move = pokemon1.move1
    elif choix_move == pokemon1.move2.nom:
        choix_move = pokemon1.move2
    else:
        print ("Vous n'avez pas choisi un move valide.")
        continue
    duel.attack(pokemon1, pokemon2, choix_move)

    time.sleep(1)

    moves = [pokemon2.move1, pokemon2.move2]
    choix_move = random.choice(moves)
    if choix_move == pokemon1.move1.nom:
        choix_move = pokemon1.move1
    elif choix_move == pokemon1.move2.nom:
        choix_move = pokemon1.move2
    duel.attack(pokemon2, pokemon1, choix_move)