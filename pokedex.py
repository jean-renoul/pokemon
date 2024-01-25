class Pokedex:
    def __init__(self, screen):
        pygame.init()
        pygame.mixer.init()

        with open("pokedex.json", "r") as fichier_json: # Ouverture du fichier JSON
            self.donnees_pokemon = json.load(fichier_json) # Chargement des données du fichier JSON

        pygame.display.set_caption("Pokédex")
        self.ecran = screen 
        self.logo = pygame.image.load('image/icon_pokeball.png') 
        pygame.display.set_icon(self.logo) 

        self.image_fond = pygame.image.load("image/image_pokedex/pokedex.png")

        self.police = pygame.font.Font("police_ecriture.ttf", 20)

        self.son_clic = pygame.mixer.Sound("son/son.mp3")

        self.index_pokemon_courant = 0
        self.en_menu = True
        self.quitter_pokedex = False
        self.bouton_quitter_presse = False

        self.rectangles_bouton_pokedex = pygame.Rect(290, 365, 250, 50)
        self.bouton_pokedex_survole = False

        self.rectangles_bouton_quitter = pygame.Rect(295, 425, 250, 50)
        self.bouton_quitter_survole = False

        self.image_logo_pokemon = pygame.image.load("image/image_pokedex/pokemon_logo.png")
        x_position_logo = 295
        y_position_logo = 80
        self.rect_logo_pokemon = self.image_logo_pokemon.get_rect(topleft=(x_position_logo, y_position_logo))

        self.image_retour = pygame.image.load("image/image_pokedex/pokeball.png")
        self.rect_retour = self.image_retour.get_rect(topleft=(700, 353))

        self.deplacement_x = 0
        self.deplacement_y = 0

        self.afficher_menu()

    def afficher_menu(self):
        self.ecran.fill((255, 255, 255))
        self.ecran.blit(self.image_fond, (0, 0))

        self.ecran.blit(self.image_logo_pokemon, self.rect_logo_pokemon)

        texte_couleur_pokedex = (255, 255, 255)
        texte_surface_pokedex = self.police.render("Accéder au Pokédex", True, texte_couleur_pokedex)
        self.ecran.blit(texte_surface_pokedex, (290, 365))

        texte_couleur_quitter = (255, 255, 255)
        texte_surface_quitter = self.police.render("Quitter le Pokédex", True, texte_couleur_quitter)
        self.ecran.blit(texte_surface_quitter, (295, 425))

        pygame.display.flip()

    def afficher_pokemon_courant(self):
        self.ecran.fill((255, 255, 255))
        self.ecran.blit(self.image_fond, (0, 0))
        pokemon_courant = self.donnees_pokemon[self.index_pokemon_courant]
        image_pokemon = pygame.image.load(pokemon_courant["image"])
        self.ecran.blit(image_pokemon, (335, 50))

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

        self.ecran.blit(self.image_retour, self.rect_retour.move(self.deplacement_x, self.deplacement_y).topleft)
        self.rectangles_fleches = [
            pygame.Rect(164, 355, 25, 34),
            pygame.Rect(164, 412, 25, 30),
            pygame.Rect(125, 388, 38, 25),
            pygame.Rect(190, 388, 38, 25)
        ]

        for rectangle in self.rectangles_fleches:
            pygame.draw.rect(self.ecran, (0, 0, 255), rectangle)

        pygame.display.flip()

    def passer_au_menu(self):
        self.en_menu = True
        self.quitter_pokedex = False
        self.bouton_quitter_presse = False
        self.afficher_menu()

    def gerer_evenements(self):
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                pygame.quit()
                print("Fermeture du Pokédex.")
                sys.exit()
            elif evenement.type == pygame.MOUSEMOTION:
                if self.rect_retour.collidepoint(pygame.mouse.get_pos()):
                    self.image_retour = pygame.image.load("image/image_pokedex/pokeball.png")
                else:
                    self.image_retour = pygame.image.load("image/image_pokedex/pokeball.png")
            elif evenement.type == pygame.MOUSEBUTTONDOWN:
                if evenement.button == 1:
                    if self.en_menu:
                        if self.rectangles_bouton_pokedex.collidepoint(evenement.pos):
                            self.en_menu = False
                            self.afficher_pokemon_courant()
                            self.son_clic.play()
                        elif self.rectangles_bouton_quitter.collidepoint(evenement.pos):
                            self.quitter_pokedex = True
                            self.bouton_quitter_presse = True
                            self.son_clic.play()
                            menu = Menu()
                            menu.run()
                    else:
                        if self.rect_retour.collidepoint(evenement.pos):
                            self.en_menu = True
                            self.afficher_menu()
                            self.son_clic.play()
                        else:
                            if self.rectangles_fleches[2].collidepoint(evenement.pos):
                                self.changer_pokemon_precedent()
                                self.son_clic.play()
                            elif self.rectangles_fleches[3].collidepoint(evenement.pos):
                                self.changer_pokemon_suivant()
                                self.son_clic.play()

    def changer_pokemon_precedent(self):
        self.index_pokemon_courant = (self.index_pokemon_courant - 1) % len(self.donnees_pokemon)
        if not self.en_menu:
            self.afficher_pokemon_courant()

    def changer_pokemon_suivant(self):
        self.index_pokemon_courant = (self.index_pokemon_courant + 1) % len(self.donnees_pokemon)
        if not self.en_menu:
            self.afficher_pokemon_courant()

    def executer(self):
        en_cours = True
        while en_cours:
            self.gerer_evenements()
            pygame.time.Clock().tick(60)

    

# Création d'une instance de la classe Pokedex et exécution du programme
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((850, 531))
    pokedex = Pokedex(screen)
    pokedex.executer()

import pygame
import pygame.mixer
import json
import sys
from menu import *