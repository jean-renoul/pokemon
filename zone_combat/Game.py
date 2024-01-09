import pygame
from Player import Player


class Game:
    def __init__(self):
        # Génération de notre joueur
        self.player = Player()