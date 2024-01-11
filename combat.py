import sys
sys.path.append("Classes")
from Classes.Combat import Combat
from Classes.Moves import Moves
from globals import *
import time
import random

pokemon1 = salameche
pokemon2 = random.choice(liste_pokemon)
from globals import *
import time
import random
import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_caption("Combat de Pokemon")

# Variables graphiques
screen = pygame.display.set_mode((850, 531))
background = pygame.image.load("zone_combat/assets/combat.png")
image_pokemon_joueur = pygame.image.load("zone_combat/assets/pokemon/salameche_inverse.png")
image_pokemon_ennemi = pygame.image.load("zone_combat/assets/pokemon/carapuce.png")
smallfont = pygame.font.Font("zone_combat/assets/Fonts/Retro Gaming.ttf", 20)


# Variables jeu
pokemon1 = salameche
pokemon2 = random.choice(liste_pokemon)
duel = Combat(pokemon1, pokemon2)


running = True

# Boucle tant que cette condition est vraie
while running:
    # Appliquer l'arrière-plan de notre jeu
    screen.blit(background, (0, 0))

    # Appliquer l'image de mon Pokémon
    screen.blit(image_pokemon_joueur, (80, 220))
    info_pokemon_joueur = smallfont.render(f"{salameche.nom} : {salameche.vie} pv", True, (255, 255, 255))    
    pygame.draw.rect(screen, (208, 199, 124), (60, 470, 300, 50))
    screen.blit(info_pokemon_joueur, (80, 475))

    # Appliquer l'image de l'ennemi
    screen.blit(image_pokemon_ennemi, (500, 70))
    info_pokemon_ennemi = smallfont.render(f"{pokemon2.nom} : {pokemon2.vie} pv", True, (255, 255, 255))
    pygame.draw.rect(screen, (208, 199, 124), (475, 10, 300, 50))
    screen.blit(info_pokemon_ennemi, (500, 20))


    print (f"Vous rencontrez un {pokemon2.nom} sauvage !")
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



    # Mettre à jour l'écran
    pygame.display.flip()

    # Si l'utilisateur ferme la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            







