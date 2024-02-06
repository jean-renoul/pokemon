class Menu:
    def __init__(self):
        # Initialisation de pygame
        pygame.init()
        #Configuration de l'affichage de la fenêtre de jeu
        pygame.display.set_caption("Pokemon")
        self.screen = pygame.display.set_mode((850, 531))
        #Chargement de l'icône et du fond d'écran du menu
        logo = pygame.image.load('image/icon_pokeball.png')
        pygame.display.set_icon(logo)

        self.background_menu = pygame.image.load('image/image_ecran/pokemon.png')
        # Initialisation de la musique de fond et des effets sonores
        pygame.mixer.init()
        pygame.mixer.music.load('son/pokemon.mp3')
        pygame.mixer.music.play(-1)

        self.click_sound = pygame.mixer.Sound('son/son.mp3')
        # Définition des couleurs et de la police
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        self.font = pygame.font.Font('police_ecriture.ttf', 30)
        # Textes des boutons du menu
        self.button_texts = ["Lancer une partie", "Ajouter un Pokémon", "Accéder au Pokédex", "Quitter"]
        # Création des rectangles pour les boutons
        self.button_rects = [self.font.render(text, True, self.WHITE).get_rect(center=(self.screen.get_width() // 2, 100 * (i + 1))) for i, text in enumerate(self.button_texts)]
        # Variables de statut du menu
        self.running = True
        self.in_menu = True
        self.in_choice = False
        self.pokedex_instance = None
        self.AjouterPokemon_instance = None


    def handle_button_click(self, index):
        self.click_sound.play()
        # Gestion des actions en fonction du bouton cliqué
        if index == 0:
            # Lancer une partie
            self.in_menu = False
            bienvenue.run(self.screen)
        if index == 1:
            # Ajouter un Pokémon
            self.in_menu = False
            self.AjouterPokemon_instance = AjouterPokemon(self.screen)
            self.AjouterPokemon_instance.executer()
        elif index == 2:
            # Accéder au Pokédex
            self.in_menu = False
            self.pokedex_instance = Pokedex(self.screen)
            self.pokedex_instance.executer()
        elif index == 3:
            # Quitter le jeu
            self.running = False

    def run(self):
            while self.running:
                for event in pygame.event.get():
                    # Gestion des événements
                    if event.type == pygame.QUIT:
                        # Quitter le jeu
                        self.vider_pokedex()
                        self.running = False
                        pygame.quit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # Gestion des clics de souris
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
                # Affichage des éléments du menu
                if self.in_menu:
                    self.screen.blit(self.background_menu, (0, 0))

                    for i, rect in enumerate(self.button_rects):
                        button_text = self.font.render(self.button_texts[i], True, self.BLACK)
                        text_rect = button_text.get_rect(center=rect.center)
                        self.screen.blit(button_text, text_rect)

                pygame.display.flip()

            self.vider_pokedex()
            pygame.quit()

    def vider_pokedex(self):
        # Charger les données du Pokédex depuis le fichier JSON
        with open('pokedex.json', 'r') as json_file:
            data = json.load(json_file)
        # Filtrer les Pokémon de départ et les conserver
        starters = []
        for pokemon in data:
            if pokemon["nom"]  == "Pikachu" or pokemon["nom"]  == "Carapuce" or pokemon["nom"]  == "Salameche":
                starters.append(pokemon)
        # Réécrire le fichier JSON avec les Pokémon de départ uniquement
        with open('pokedex.json', 'w') as json_file:
            json.dump(starters, json_file, indent=2)
        # Charger les données des autres Pokémon depuis un autre fichier JSON
        with open('pokemon.json', 'r') as json_file:
            data = json.load(json_file)
        # Filtrer les Pokémon de base et les conserver
        pokemons_base = []
        for pokemon in data:
            pokemons_base.append(pokemon)
            if pokemon["nom"]  == "tortipouss" or pokemon["nom"]  == "lixy" or pokemon["nom"]  == "psykokwak":
                pokemons_base.remove(pokemon)
        # Réécrire le fichier JSON avec les Pokémon de base uniquement
        with open('pokemon.json', 'w') as json_file:
            json.dump(pokemons_base, json_file, indent=2)

import pygame
from Classes.pokedex import Pokedex
from Classes.AjouterPokemon import AjouterPokemon
import bienvenue
import json