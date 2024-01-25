import pygame
import json
from Classes.Pokemon import Pokemon
from globals import *
from combatLoop import lancer_combat

pygame.init()
pygame.display.set_caption("Pokemon")

screen = pygame.display.set_mode((850, 531))
width = screen.get_width()
height = screen.get_height()
background = pygame.image.load('image/image_ecran/combat.png')
smallfont = pygame.font.Font("police_ecriture.ttf", 20)


def choix_pokemon():
    

    #Charger données pokemon
    with open("pokemon.json", "r") as read_file:
        data = json.load(read_file)

    liste_pokemon = []

    for pokemon in data:

        move1 = moves_dict.get(pokemon["move1"])
        move2 = moves_dict.get(pokemon["move2"])


        instance = Pokemon(
            pokemon["nom"],
            pokemon["niveau"],
            pokemon["type"],
            pokemon["vie"],
            pokemon["attaque"],
            pokemon["defense"],
            move1,
            move2,
            pokemon["evolution"],
            pokemon["numero"],
            pokemon["image"]
            )
        liste_pokemon.append(instance)

    

    pokemon_courant = liste_pokemon[0]      
    running = True
    pokemon1 = None
    pokemon2 = None

    while running:
        # Chargement du fond d'écran        
        screen.blit(background, (0, 0))
        afficher_pokemon_courant(pokemon_courant)  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit() 
              
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if event.pos[0] > width/2 - 300 and event.pos[0] < width/2 - 130 and event.pos[1] > height/2 - 70 and event.pos[1] < height/2 + 50:
                        if liste_pokemon.index(pokemon_courant) == 0:
                            pokemon_courant = liste_pokemon[-1]
                            afficher_pokemon_courant(pokemon_courant)                           
                        else:
                            pokemon_courant = liste_pokemon[liste_pokemon.index(pokemon_courant) - 1]
                            afficher_pokemon_courant(pokemon_courant)
                    
                        

                    if event.pos[0] > width/2 + 100 and event.pos[0] < width/2 + 275 and event.pos[1] > height/2 - 70 and event.pos[1] < height/2 + 50:
                        if liste_pokemon.index(pokemon_courant) == len(liste_pokemon) - 1:
                            pokemon_courant = liste_pokemon[0]
                            afficher_pokemon_courant(pokemon_courant)                        
                        else:
                            pokemon_courant = liste_pokemon[liste_pokemon.index(pokemon_courant) + 1]
                            afficher_pokemon_courant(pokemon_courant)
                    
                    if event.pos[0] > width/2 - 100 and event.pos[0] < width/2 + 40 and event.pos[1] > height/2 - 100 and event.pos[1] < height/2 + 40:
                        if pokemon1 == None:                            
                            pokemon1 = pokemon_courant
                            liste_pokemon.remove(pokemon_courant)
                            pokemon_courant = liste_pokemon[0]
                            break
                        if pokemon2 == None:
                            pokemon2 = pokemon_courant
                            liste_pokemon.remove(pokemon_courant)
                            lancer_combat(pokemon1, pokemon2)

                        

                    

        pygame.display.flip()

def afficher_pokemon_courant(pokemon_courant):
    image_pokemon = pygame.image.load(f'image/image_pokedex/pokemon/{pokemon_courant.nom}.png')
    screen.blit(image_pokemon, (width/2 - 100, height/2 - 100))
    fleche_gauche = pygame.image.load('image/image_ecran/fleche_gauche.png')
    fleche_droite = pygame.image.load('image/image_ecran/fleche_droite.png')
    screen.blit(fleche_gauche, (width/2 - 300, height/2 - 90))
    screen.blit(fleche_droite, (width/2 + 100, height/2 - 100))
