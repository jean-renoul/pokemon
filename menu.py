class Menu:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Pokemon")
        self.screen = pygame.display.set_mode((850, 531))

        logo = pygame.image.load('image/icon_pokeball.png')
        pygame.display.set_icon(logo)

        self.background_menu = pygame.image.load('image/image_ecran/pokemon.png')

        pygame.mixer.init()
        pygame.mixer.music.load('son/pokemon.mp3')
        pygame.mixer.music.play(-1)

        self.click_sound = pygame.mixer.Sound('son/son.mp3')

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        self.font = pygame.font.Font('police_ecriture.ttf', 30)

        self.button_texts = ["Lancer une partie", "Ajouter un Pokémon", "Accéder au Pokédex", "Quitter"]

        self.button_rects = [self.font.render(text, True, self.WHITE).get_rect(center=(self.screen.get_width() // 2, 100 * (i + 1))) for i, text in enumerate(self.button_texts)]

        self.running = True
        self.in_menu = True
        self.in_choice = False
        self.pokedex_instance = None
        self.AjouterPokemon_instance = None


    def handle_button_click(self, index):
        self.click_sound.play()

        if index == 0:
            self.in_menu = False
            bienvenue.run(self.screen)
        elif index == 1:
            self.in_menu = False
            self.AjouterPokemon_instance = AjouterPokemon(self.screen)
            self.AjouterPokemon_instance.executer()
        elif index == 2:
            self.in_menu = False
            self.pokedex_instance = Pokedex(self.screen)
            self.pokedex_instance.executer()
        elif index == 3:
            self.running = False

    def run(self):
            while self.running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                        pygame.quit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.in_menu:
                            for i, rect in enumerate(self.button_rects):
                                if rect.collidepoint(event.pos):
                                    self.handle_button_click(i)
                        elif self.AjouterPokemon_instance and not self.AjouterPokemon_instance.en_menu:
                            self.AjouterPokemon_instance.gerer_evenements()
                            
                        elif self.pokedex_instance and not self.pokedex_instance.en_menu:
                            self.pokedex_instance.gerer_evenements()

                if self.pokedex_instance:
                    if self.pokedex_instance.quitter_pokedex:
                        self.pokedex_instance = None
                        self.in_menu = True

                if self.AjouterPokemon_instance:
                    if self.AjouterPokemon_instance.quitter_ajouter_pokemon:
                        self.AjouterPokemon_instance = None
                        self.in_menu = True        

                if self.in_menu:
                    self.screen.blit(self.background_menu, (0, 0))

                    for i, rect in enumerate(self.button_rects):
                        button_text = self.font.render(self.button_texts[i], True, self.BLACK)
                        text_rect = button_text.get_rect(center=rect.center)
                        self.screen.blit(button_text, text_rect)

                pygame.display.flip()

            pygame.quit()

import pygame
from pokedex import Pokedex
from AjouterPokemon import AjouterPokemon
import bienvenue