import pygame
from Player import Player
from Ennemie import Ennemie

class Game:
    def __init__(self):
        # Génération de notre joueur
        self.player = Player(self)
        # Génération de l'ennemi
        self.ennemie = Ennemie()