import pygame

def run(screen):
    pygame.init()
    pygame.display.set_caption("Pokemon")
    background = pygame.image.load('menu/image/bienvenue.png')

    button_image = pygame.image.load('menu/image/pokeball.png')  # Charger votre image pour le bouton
    button_rect = button_image.get_rect(center=(screen.get_width() // 2, screen.get_height() // 1.15))  # Positionner un peu plus bas sur l'écran

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
                    # Faire quelque chose lorsque le bouton est cliqué
                    print("Le bouton a été cliqué !")  # Exemple : affichage dans la console