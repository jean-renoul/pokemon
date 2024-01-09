import pygame
pygame.init()

# Génération de la fenêtre pygame
pygame.display.set_caption("Pokemon zone de combat")
screen = pygame.display.set_mode((850, 531))

# Importation de l'image de fond
background = pygame.image.load("zone_combat/assets/combat.png")

running = True

# Boucle tant que cette condition est vraie
while running:

    # Appliquer l'arrière plan de notre jeu
    screen.blit(background, (0, 0))

    # Mettre à jour l'écran
    pygame.display.flip()

    #si l'utilisateur ferme la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")