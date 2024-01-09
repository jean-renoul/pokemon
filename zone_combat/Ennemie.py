import pygame

class Ennemie(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health_carapuce = "44"
        self.image = pygame.image.load("zone_combat/assets/pokemon/carapuce.png")
        self.rect = self.image.get_rect()
        self.rect.x = 470  # Position X de l'ennemi
        self.rect.y = 70  # Position Y de l'ennemi
