import pygame
from Game import Game
from Player import Player
from Ennemie import Ennemie

pygame.init()

# Génération de la fenêtre pygame
pygame.display.set_caption("Pokemon zone de combat")
screen = pygame.display.set_mode((850, 531))

# Importation de l'image de fond
background = pygame.image.load("zone_combat/assets/combat.png")

# Chargement de notre jeu
game = Game()

running = True

# Boucle tant que cette condition est vraie
while running:
    # Appliquer l'arrière-plan de notre jeu
    screen.blit(background, (0, 0))

    # Appliquer l'image de mon Pokémon
    screen.blit(game.player.image, game.player.rect)

    # Appliquer l'image de l'ennemie
    screen.blit(game.ennemie.image, game.ennemie.rect)

    # Mettre à jour l'écran
    pygame.display.flip()

    # Si l'utilisateur ferme la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")