import pygame
import dresseur  # Importer le module dresseur

def choix(screen):
    pygame.init()
    pygame.display.set_caption("Pokemon")
    # Chargement du fond d'écran
    background = pygame.image.load('image/image_ecran/bienvenue2.png')
    # Chargement de l'image pour le bouton pokeball
    button_image = pygame.image.load('image/image_pokedex/pokeball.png')  
    button_rect = button_image.get_rect(center=(screen.get_width() // 2, screen.get_height() // 1.15))  # Positionner un peu plus bas sur l'écran

     # Chargement du son du clic sur les boutons
    click_sound = pygame.mixer.Sound('son/son.mp3')

    running = True
    while running:
        screen.blit(background, (0, 0))
        screen.blit(button_image, button_rect)  # Afficher l'image du bouton
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                   click_sound.play()  # Jouez le son du clic
                   dresseur.dresseur(screen)  # Appeler la fonction dresseur() de dresseur.py
                   return
