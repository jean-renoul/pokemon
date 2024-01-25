import sys


class AjouterPokemon: # Création de la classe AjouterPokemon
    def __init__(self, screen): # Initialisation de la classe AjouterPokemon
        pygame.init() # Initialisation de Pygame
        pygame.mixer.init() # Initialisation du module mixer de Pygame

        with open('pokemon.json') as json_file: # Ouverture du fichier JSON
            self.data = json.load(json_file) # Chargement des données du fichier JSON

        pygame.display.set_caption("Pokemon") # Définition du titre de la fenêtre
        self.screen = screen
        self.image_fond = pygame.image.load("image/image_AjouterPokemon/fond.png") # Chargement de l'image de fond

        self.image_logo_pokemon = pygame.image.load("image/image_pokedex/pokemon_logo.png") # Chargement de l'image du logo Pokémon
        self.rect_logo_pokemon = self.image_logo_pokemon.get_rect(topleft=(295, 40)) 

        self.font = pygame.font.Font("police_ecriture.ttf", 20)

        self.clic = pygame.mixer.Sound("son/son.mp3")

        self.en_menu = True # Définition de la variable en_menu
        self.quitter_ajouter_pokemon = False # Définition de la variable quitter_ajouter_pokemon

        self.cartes = [
            (50, 225, "Lixy", pygame.image.load("image/image_AjouterPokemon/carte_lixy.png")),
            (325, 225, "Psykokwak", pygame.image.load("image/image_AjouterPokemon/carte_psykokwak.png")),
            (600, 225, "Tortipouss", pygame.image.load("image/image_AjouterPokemon/carte_tortipouss.png"))
        ]

        self.message_confirmation = ""

        pygame.display.flip() # Rafraîchissement de l'écran

    def passer_au_menu(self): # Définition de la fonction passer_au_menu    
        self.en_menu = True # Définition de la variable en_menu
        self.quitter_ajouter_pokemon = False # Définition de la variable quitter_ajouter_pokemon
        self.bouton_quitter_presse = True # Définition de la variable bouton_quitter_presse

    def gerer_evenements(self): # Définition de la fonction gerer_evenements
        for evenement in pygame.event.get(): # Boucle pour gérer les événements
            if evenement.type == pygame.QUIT: # Si l'événement est de type QUIT
                pygame.quit() # Fermeture de la fenêtre
                sys.exit()
            elif evenement.type == pygame.MOUSEBUTTONDOWN: # Si l'événement est de type MOUSEBUTTONDOWN
                if evenement.button == 1: # Si le bouton de la souris est le bouton gauche
                    for x, y, pokemon_nom, carte in self.cartes: # Boucle pour parcourir les cartes
                        rect_carte = pygame.Rect(x, y, carte.get_width(), carte.get_height()) # Définition du rectangle de la carte
                        if rect_carte.collidepoint(pygame.mouse.get_pos()): # Si la souris est sur la carte
                            self.ajouter_pokemon(pokemon_nom) # Ajout du pokémon
                            self.en_menu = True # Définition de la variable en_menu
                            self.quitter_ajouter_pokemon = False # Définition de la variable quitter_ajouter_pokemon
                            self.bouton_quitter_presse = True # Définition de la variable bouton_quitter_presse
                            menu = Menu() # Création de l'objet menu
                            menu.run() # Exécution de la fonction run

    def ajouter_pokemon(self, pokemon_nom): # Définition de la fonction ajouter_pokemon
        if pokemon_nom == "Tortipouss":
            nouveau_pokemon = {
                "nom": "Tortipouss",
                "niveau": 1,
                "type": "plante",
                "vie": 55,
                "attaque": 68,
                "defense": 64,
                "numero": "0387",
                "image": "image/image_pokedex/pokemon/tortipouss.png"
            }
        elif pokemon_nom == "Lixy":
            nouveau_pokemon = {
                "nom": "Lixy",
                "niveau": 1,
                "type": "electrik",
                "vie": 45,
                "attaque": 65,
                "defense": 34,
                "numero": "0403",
                "image": "image/image_pokedex/pokemon/lixy.png"
            }
        elif pokemon_nom == "Psykokwak":
            nouveau_pokemon = {
                "nom": "Psykokwak",
                "niveau": 1,
                "type": "eau",
                "vie": 50,
                "attaque": 52,
                "defense": 48,
                "numero": "0054",
                "image": "image/image_pokedex/pokemon/psykokwak.png"
            }

        if not any(pokemon["nom"] == nouveau_pokemon["nom"] for pokemon in self.data): # Si le pokémon n'est pas déjà dans le Pokédex
            self.data.append(nouveau_pokemon) # Ajout du pokémon dans le Pokédex

            with open('pokemon.json', 'w') as json_file: # Ouverture du fichier JSON
                json.dump(self.data, json_file, indent=2) # Sauvegarde des données dans le fichier JSON

    def choix_AjouterPokemon(self): # Définition de la fonction choix_AjouterPokemon
        self.screen.blit(self.image_fond, (0, 0)) # Affichage de l'image de fond

        for x, y, pokemon_nom, carte in self.cartes: # Boucle pour parcourir les cartes
            rect_carte = carte.get_rect(topleft=(x, y)) # Définition du rectangle de la carte
            if rect_carte.collidepoint(pygame.mouse.get_pos()): # Si la souris est sur la carte
                carte = pygame.transform.scale(carte, (int(rect_carte.width * 1.05), int(rect_carte.height * 1.05))) # Agrandissement de la carte

            self.screen.blit(carte, (x, y)) # Affichage de la carte

        self.screen.blit(self.image_logo_pokemon, self.rect_logo_pokemon.topleft) # Affichage du logo Pokémon

        texte = self.font.render("Cliquer sur une carte pour ajouter le Pokémon", True, (0, 0, 0)) # Définition du texte
        self.screen.blit(texte, (130, 150)) # Affichage du texte

        pygame.display.flip() # Rafraîchissement de l'écran

    def executer(self): # Définition de la fonction executer
        en_cours = True # Définition de la variable en_cours
        while en_cours: # Boucle pour exécuter le programme
            self.gerer_evenements() # Exécution de la fonction gerer_evenements
            self.choix_AjouterPokemon() # Exécution de la fonction choix_AjouterPokemon
            pygame.time.Clock().tick(60) # Définition du nombre d'images par seconde

    

if __name__ == "__main__": # Si le fichier est exécuté
    pygame.init() # Initialisation de Pygame
    screen = pygame.display.set_mode((850, 531)) # Définition de la taille de la fenêtre
    nouveau_pokemon = AjouterPokemon(screen) # Création d'une instance de la classe AjouterPokemon
    nouveau_pokemon.executer() # Exécution de la fonction executer de la classe AjouterPokemon

import pygame
import pygame.mixer
import json
from menu import *