class Pokedex: # Création de la classe Pokedex
    def __init__(self, screen): # Initialisation de la classe Pokedex
        pygame.init() # Initialisation de Pygame
        pygame.mixer.init() # Initialisation du module mixer de Pygame

        with open("pokedex.json", "r") as fichier_json: # Ouverture du fichier JSON
            self.donnees_pokemon = json.load(fichier_json) # Chargement des données du fichier JSON

        pygame.display.set_caption("Pokédex")
        self.ecran = screen # Définition de l'écran
        self.logo = pygame.image.load('image/icon_pokeball.png')  
        pygame.display.set_icon(self.logo)

        self.image_fond = pygame.image.load("image/image_pokedex/pokedex.png") # Chargement de l'image de fond

        self.police = pygame.font.Font("police_ecriture.ttf", 20)

        self.son_clic = pygame.mixer.Sound("son/son.mp3")

        self.index_pokemon_courant = 0 # Définition de l'index du pokémon courant
        self.en_menu = True # Définition de la variable en_menu
        self.quitter_pokedex = False # Définition de la variable quitter_pokedex
        self.bouton_quitter_presse = False # Définition de la variable bouton_quitter_presse

        self.rectangles_bouton_pokedex = pygame.Rect(290, 365, 250, 50) # Définition du rectangle du bouton "Accéder au Pokédex"

        self.rectangles_bouton_quitter = pygame.Rect(295, 425, 250, 50) # Définition du rectangle du bouton "Quitter le Pokédex"

        self.image_logo_pokemon = pygame.image.load("image/image_pokedex/pokemon_logo.png") # Chargement de l'image du logo Pokémon
        x_position_logo = 295
        y_position_logo = 80
        self.rect_logo_pokemon = self.image_logo_pokemon.get_rect(topleft=(x_position_logo, y_position_logo)) # Définition du rectangle du logo Pokémon

        self.image_retour = pygame.image.load("image/image_pokedex/pokeball.png") # Chargement de l'image du bouton retour
        self.rect_retour = self.image_retour.get_rect(topleft=(700, 353))
        self.deplacement_x = 0 
        self.deplacement_y = 0

        self.afficher_menu() # Affichage du menu

    def afficher_menu(self): # Définition de la fonction afficher_menu
        self.ecran.fill((255, 255, 255)) # Remplissage de l'écran avec du blanc
        self.ecran.blit(self.image_fond, (0, 0)) # Affichage de l'image de fond

        self.ecran.blit(self.image_logo_pokemon, self.rect_logo_pokemon) # Affichage du logo Pokémon

        texte_couleur_pokedex = (255, 255, 255)
        texte_surface_pokedex = self.police.render("Accéder au Pokédex", True, texte_couleur_pokedex) # Définition du texte "Accéder au Pokédex"
        self.ecran.blit(texte_surface_pokedex, (290, 365)) # Affichage du texte "Accéder au Pokédex"

        texte_couleur_quitter = (255, 255, 255)
        texte_surface_quitter = self.police.render("Quitter le Pokédex", True, texte_couleur_quitter) # Définition du texte "Quitter le Pokédex"
        self.ecran.blit(texte_surface_quitter, (295, 425)) # Affichage du texte "Quitter le Pokédex"

        pygame.display.flip() # Rafraîchissement de l'écran

    def afficher_pokemon_courant(self): # Définition de la fonction afficher_pokemon_courant
        self.ecran.fill((255, 255, 255)) 
        self.ecran.blit(self.image_fond, (0, 0)) # Affichage de l'image de fond
        pokemon_courant = self.donnees_pokemon[self.index_pokemon_courant] # Définition du pokémon courant
        image_pokemon = pygame.image.load(pokemon_courant["image"]) # Chargement de l'image du pokémon courant
        self.ecran.blit(image_pokemon, (335, 50)) # Affichage de l'image du pokémon courant

        infos_texte = [
            f"Nom: {pokemon_courant['nom']}",
            f"Niveau: {pokemon_courant['niveau']}",
            f"Type: {pokemon_courant['type']}",
            f"Vie: {pokemon_courant['vie']}",
            f"Attaque: {pokemon_courant['attaque']}",
            f"Défense: {pokemon_courant['defense']}",
            f"Numéro: {pokemon_courant['numero']}"
        ]

        y_position = 320
        for info in infos_texte:
            texte_surface = self.police.render(info, True, (0, 0, 0))
            self.ecran.blit(texte_surface, (300, y_position))
            y_position += 25

        self.ecran.blit(self.image_retour, self.rect_retour.move(self.deplacement_x, self.deplacement_y).topleft) # Affichage du bouton retour
        self.rectangles_fleches = [ # Définition des rectangles des flèches
            pygame.Rect(164, 355, 25, 34),
            pygame.Rect(164, 412, 25, 30),
            pygame.Rect(125, 388, 38, 25),
            pygame.Rect(190, 388, 38, 25)
        ]

        for rectangle in self.rectangles_fleches: # Affichage des rectangles des flèches
            pygame.draw.rect(self.ecran, (0, 0, 255), rectangle) # Affichage des rectangles des flèches

        pygame.display.flip() # Rafraîchissement de l'écran

    def passer_au_menu(self): # Définition de la fonction passer_au_menu
        self.en_menu = True # Définition de la variable en_menu
        self.quitter_pokedex = False # Définition de la variable quitter_pokedex
        self.bouton_quitter_presse = False # Définition de la variable bouton_quitter_presse
        self.afficher_menu() # Affichage du menu

    def gerer_evenements(self): # Définition de la fonction gerer_evenements
        for evenement in pygame.event.get(): # Définition de la variable evenement
            if evenement.type == pygame.QUIT: # Si l'événement est de type QUIT
                self.vider_pokedex()
                pygame.quit() # Fermeture de Pygame
            elif evenement.type == pygame.MOUSEMOTION: # Si l'événement est de type MOUSEMOTION
                if self.rect_retour.collidepoint(pygame.mouse.get_pos()): # Si la souris est sur le bouton retour
                    self.image_retour = pygame.image.load("image/image_pokedex/pokeball.png") # Chargement de l'image du bouton retour
                else: # Sinon
                    self.image_retour = pygame.image.load("image/image_pokedex/pokeball.png") # Chargement de l'image du bouton retour
            elif evenement.type == pygame.MOUSEBUTTONDOWN: # Si l'événement est de type MOUSEBUTTONDOWN
                if evenement.button == 1: # Si le bouton de la souris est le bouton gauche
                    if self.en_menu: # Si on est dans le menu
                        if self.rectangles_bouton_pokedex.collidepoint(evenement.pos): # Si la souris est sur le bouton "Accéder au Pokédex"
                            self.en_menu = False # On n'est plus dans le menu
                            self.afficher_pokemon_courant() # Affichage du pokémon courant
                            self.son_clic.play() # Jouer le son du clic
                        elif self.rectangles_bouton_quitter.collidepoint(evenement.pos): # Si la souris est sur le bouton "Quitter le Pokédex"
                            self.quitter_pokedex = True # On quitte le Pokédex
                            self.bouton_quitter_presse = True # Le bouton quitter est pressé
                            self.son_clic.play() # Jouer le son du clic
                            menu = Menu() # Création d'une instance de la classe Menu
                            menu.run()  # Exécution de la fonction run de la classe Menu
                    else:
                        if self.rect_retour.collidepoint(evenement.pos): # Si la souris est sur le bouton retour
                            self.en_menu = True # On est dans le menu
                            self.afficher_menu() # Affichage du menu
                            self.son_clic.play() # Jouer le son du clic
                        else:
                            if self.rectangles_fleches[2].collidepoint(evenement.pos): # Si la souris est sur la flèche gauche
                                self.changer_pokemon_precedent() # Changer le pokémon précédent
                                self.son_clic.play() # Jouer le son du clic
                            elif self.rectangles_fleches[3].collidepoint(evenement.pos): # Si la souris est sur la flèche droite
                                self.changer_pokemon_suivant() # Changer le pokémon suivant
                                self.son_clic.play() # Jouer le son du clic

    def changer_pokemon_precedent(self): # Définition de la fonction changer_pokemon_precedent
        self.index_pokemon_courant = (self.index_pokemon_courant - 1) % len(self.donnees_pokemon) # Définition de l'index du pokémon courant
        if not self.en_menu: # Si on n'est pas dans le menu
            self.afficher_pokemon_courant() # Affichage du pokémon courant

    def changer_pokemon_suivant(self): # Définition de la fonction changer_pokemon_suivant
        self.index_pokemon_courant = (self.index_pokemon_courant + 1) % len(self.donnees_pokemon) # Définition de l'index du pokémon courant
        if not self.en_menu: # Si on n'est pas dans le menu
            self.afficher_pokemon_courant() # Affichage du pokémon courant

    def executer(self): # Définition de la fonction executer
        en_cours = True # Définition de la variable en_cours
        while en_cours: # Tant que la variable en_cours est vraie
            self.gerer_evenements() # Gestion des événements
            pygame.time.Clock().tick(60) # Définition de la vitesse de rafraîchissement de l'écran

    def vider_pokedex(self):
        with open('pokedex.json', 'r') as json_file:
            data = json.load(json_file)

        starters = []
        for pokemon in data:
            if pokemon["nom"]  == "Pikachu" or pokemon["nom"]  == "Carapuce" or pokemon["nom"]  == "Salameche":
                starters.append(pokemon)

        with open('pokedex.json', 'w') as json_file:
            json.dump(starters, json_file, indent=2)

        with open('pokemon.json', 'r') as json_file:
            data = json.load(json_file)

        pokemons_base = []
        for pokemon in data:
            pokemons_base.append(pokemon)
            if pokemon["nom"]  == "tortipouss" or pokemon["nom"]  == "lixy" or pokemon["nom"]  == "psykokwak":
                pokemons_base.remove(pokemon)

        with open('pokemon.json', 'w') as json_file:
            json.dump(pokemons_base, json_file, indent=2)

    

# Création d'une instance de la classe Pokedex et exécution du programme
if __name__ == "__main__": # Si le fichier est exécuté directement
    pygame.init() # Initialisation de Pygame
    screen = pygame.display.set_mode((850, 531))
    pokedex = Pokedex(screen) # Création d'une instance de la classe Pokedex
    pokedex.executer() # Exécution de la fonction executer de la classe Pokedex

import pygame
import pygame.mixer
import json
import sys
from Classes.menu import *