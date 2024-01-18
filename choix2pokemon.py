import pygame
import json
from Classes.Pokemon import Pokemon
from globals import *
from combat import lancer_combat

def choix2pokemon(screen):
    pygame.init()
    pygame.display.set_caption("Pokemon")

    # Charger données pokemon
    with open("pokemon.json", "r") as read_file:
        data = json.load(read_file)

    liste_pokemon = []

    for pokemon in data[0].values():

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
            move2
            )
        liste_pokemon.append(instance)    

    # Chargement du fond d'écran
    background = pygame.image.load('image/image_ecran/choixpokemon.png')
    
    # Chargement de l'image pour la première pokeball et ajustement de la taille
    pokeball1_image = pygame.image.load('image/image_pokedex/pokeball.png')  
    pokeball1_image = pygame.transform.scale(pokeball1_image, (pokeball1_image.get_width() // 2, pokeball1_image.get_height() // 2))
    pokeball1_rect = pokeball1_image.get_rect(center=(screen.get_width() // 2 - 243, screen.get_height() //  1.94))  # Décaler vers la droite
    
    # Chargement de l'image pour la deuxième pokeball et ajustement de la taille
    pokeball2_image = pygame.image.load('image/image_pokedex/pokeball.png')  
    pokeball2_image = pygame.transform.scale(pokeball2_image, (pokeball2_image.get_width() // 2, pokeball2_image.get_height() // 2))
    pokeball2_rect = pokeball2_image.get_rect(center=(screen.get_width() // 2 - 75, screen.get_height() //  1.94))  # Décaler vers la gauche
    
    pokeball3_image = pygame.image.load('image/image_pokedex/pokeball.png')  
    pokeball3_image = pygame.transform.scale(pokeball3_image, (pokeball3_image.get_width() // 2, pokeball3_image.get_height() // 2))
    pokeball3_rect = pokeball3_image.get_rect(center=(screen.get_width() // 2 + 130, screen.get_height() // 1.94))  # Décaler vers la gauche


    pokeball4_image = pygame.image.load('image/image_pokedex/pokeball.png')  
    pokeball4_image = pygame.transform.scale(pokeball4_image, (pokeball4_image.get_width() // 2, pokeball4_image.get_height() // 2))
    pokeball4_rect = pokeball4_image.get_rect(center=(screen.get_width() // 2 + 285 , screen.get_height() //  1.94))  # Décaler vers la droite
    

    pokeball5_image = pygame.image.load('image/image_pokedex/pokeball.png')  
    pokeball5_image = pygame.transform.scale(pokeball5_image, (pokeball5_image.get_width() // 2, pokeball5_image.get_height() // 2))
    pokeball5_rect = pokeball5_image.get_rect(center=(screen.get_width() // 2 - 243, screen.get_height() // 1.135))  # Décaler vers la droite
    

    pokeball6_image = pygame.image.load('image/image_pokedex/pokeball.png')  
    pokeball6_image = pygame.transform.scale(pokeball6_image, (pokeball6_image.get_width() // 2, pokeball6_image.get_height() // 2))
    pokeball6_rect = pokeball6_image.get_rect(center=(screen.get_width() // 2 -75, screen.get_height() // 1.135))  # Décaler vers la droite
    


    pokeball7_image = pygame.image.load('image/image_pokedex/pokeball.png')  
    pokeball7_image = pygame.transform.scale(pokeball7_image, (pokeball7_image.get_width() // 2, pokeball7_image.get_height() // 2))
    pokeball7_rect = pokeball7_image.get_rect(center=(screen.get_width() // 2 +130, screen.get_height() // 1.135))  # Décaler vers la droite
    



    pokeball8_image = pygame.image.load('image/image_pokedex/pokeball.png')  
    pokeball8_image = pygame.transform.scale(pokeball8_image, (pokeball8_image.get_width() // 2, pokeball8_image.get_height() // 2))
    pokeball8_rect = pokeball8_image.get_rect(center=(screen.get_width() // 2 + 285, screen.get_height() // 1.135))  # Décaler vers la droite
    
    
    # Chargement du son du clic sur les boutons
    click_sound = pygame.mixer.Sound('son/son.mp3')


    running = True
    while running:
        screen.blit(background, (0, 0))
        screen.blit(pokeball1_image, pokeball1_rect)  # Afficher la première pokeball
        screen.blit(pokeball2_image, pokeball2_rect)  # Afficher la deuxième pokeball
        screen.blit(pokeball3_image, pokeball3_rect)  #Afficher la troisième pokeball
        screen.blit(pokeball4_image, pokeball4_rect)  #Afficher la quatrième pokeball
        screen.blit(pokeball5_image, pokeball5_rect)  # Afficher la cinquième pokeball
        screen.blit(pokeball6_image, pokeball6_rect)  # Afficher la sixième pokeball
        screen.blit(pokeball6_image, pokeball7_rect)  # Afficher la septième pokeball
        screen.blit(pokeball6_image, pokeball8_rect)  # Afficher la huitième pokeball
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pokeball1_rect.collidepoint(event.pos):
                    click_sound.play()  # Jouez le son du clic
                    lancer_combat(liste_pokemon[5])
                if pokeball2_rect.collidepoint(event.pos):
                    click_sound.play()
                    lancer_combat(liste_pokemon[1])
                if pokeball3_rect.collidepoint(event.pos):
                    click_sound.play()
                    lancer_combat(liste_pokemon[2])
                if pokeball4_rect.collidepoint(event.pos):
                    click_sound.play()
                    lancer_combat(liste_pokemon[6])
                if pokeball5_rect.collidepoint(event.pos):
                    click_sound.play()
                    lancer_combat(liste_pokemon[3])
                if pokeball6_rect.collidepoint(event.pos):
                    click_sound.play()
                    lancer_combat(liste_pokemon[7])
                if pokeball7_rect.collidepoint(event.pos):
                    click_sound.play()
                    lancer_combat(liste_pokemon[0])
                if pokeball8_rect.collidepoint(event.pos):
                    click_sound.play()
                    lancer_combat(liste_pokemon[4])


    
