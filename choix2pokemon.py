import pygame
import ajouter

def choix2pokemon(screen):
    pygame.init()
    pygame.display.set_caption("Pokemon")
    # Chargement du fond d'écran
    background = pygame.image.load('menu/image/image_ecran/choixpokemon.png')
    
    # Chargement de l'image pour la première pokeball et ajustement de la taille
    pokeball1_image = pygame.image.load('menu/image/image_pokedex/pokeball.png')  
    pokeball1_image = pygame.transform.scale(pokeball1_image, (pokeball1_image.get_width() // 2, pokeball1_image.get_height() // 2))
    pokeball1_rect = pokeball1_image.get_rect(center=(screen.get_width() // 2 - 125, screen.get_height() // 1.32))  # Décaler vers la droite
    
    # Chargement de l'image pour la deuxième pokeball et ajustement de la taille
    pokeball2_image = pygame.image.load('menu/image/image_pokedex/pokeball.png')  
    pokeball2_image = pygame.transform.scale(pokeball2_image, (pokeball2_image.get_width() // 2, pokeball2_image.get_height() // 2))
    pokeball2_rect = pokeball2_image.get_rect(center=(screen.get_width() // 2 + 9, screen.get_height() // 1.32))  # Décaler vers la gauche
    
    pokeball3_image = pygame.image.load('menu/image/image_pokedex/pokeball.png')  
    pokeball3_image = pygame.transform.scale(pokeball3_image, (pokeball3_image.get_width() // 2, pokeball3_image.get_height() // 2))
    pokeball3_rect = pokeball3_image.get_rect(center=(screen.get_width() // 2 + 140, screen.get_height() // 1.32))  # Décaler vers la gauche
    
    # Chargement du son du clic sur les boutons
    click_sound = pygame.mixer.Sound('menu/son/son.mp3')

    running = True
    while running:
        screen.blit(background, (0, 0))
        screen.blit(pokeball1_image, pokeball1_rect)  # Afficher la première pokeball
        screen.blit(pokeball2_image, pokeball2_rect)  # Afficher la deuxième pokeball
        screen.blit(pokeball3_image, pokeball3_rect)  #Afficher la troisième pokeball
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pokeball1_rect.collidepoint(event.pos) or pokeball2_rect.collidepoint(event.pos) or pokeball3_rect.collidepoint(event.pos):
                    click_sound.play()  # Jouez le son du clic
                    ajouter.ajouter(screen)  # Appeler la fonction ajouter() de ajouter.py
                    return
