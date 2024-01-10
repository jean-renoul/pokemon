import pygame
from Player import Player
from Ennemie import Ennemie

pygame.init()

# Génération de la fenêtre pygame
pygame.display.set_caption("Pokemon zone de combat")
screen = pygame.display.set_mode((850, 531))

# Importation de l'image de fond
background = pygame.image.load("zone_combat/assets/combat.png")

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health_salameche = "39"
        self.image = pygame.image.load("zone_combat/assets/pokemon/salameche_inverse.png")
        self.rect = self.image.get_rect()
        self.rect.x = 150
        self.rect.y = 220

class Ennemie(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health_carapuce = "44"
        self.image = pygame.image.load("zone_combat/assets/pokemon/carapuce.png")
        self.rect = self.image.get_rect()
        self.rect.x = 470  # Position X de l'ennemi
        self.rect.y = 70  # Position Y de l'ennemi

class Game:
    def __init__(self):
        # Génération de notre joueur
        self.player = Player(self)
        # Génération de l'ennemi
        self.ennemie = Ennemie()

game = Game()
running = True

# Boucle tant que cette condition est vraie
while running:
    # Appliquer l'arrière-plan de notre jeu
    screen.blit(background, (0, 0))

    # Appliquer l'image de mon Pokémon
    screen.blit(game.player.image, game.player.rect)

    # Appliquer l'image de l'ennemi
    screen.blit(game.ennemie.image, game.ennemie.rect)

    # Mettre à jour l'écran
    pygame.display.flip()

    # Si l'utilisateur ferme la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
