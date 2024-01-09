import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health_salameche = "39"
        #self.health_carapuce = "44"
        #self.health_taupiqueur = "30"
        #self.health_saquedeneu = "65"
        #self.health_chenipan = "45"
        #self.health_pikachu = "35"
        #self.health_tadmorv = "60"
        #self.health_abra = "33"
        #self.health_reptincel = "59"
        #self.health_carabaffe = "64"
        #self.health_triopiqueur = "50"
        #self.health_bouldeneu = "85"
        #self.health_chrysacier = "65"
        #self.health_raichu = "55"
        #self.health_grotadmorv = "80"
        #self.health_kadabra = "53"
        self.image = pygame.image.load("zone_combat/assets/pokemon/salameche.png")
        self.rect = self.image.get_rect()
        self.rect.x = 150
        self.rect.y = 220