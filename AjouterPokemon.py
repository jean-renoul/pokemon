import sys


class AjouterPokemon:
    def __init__(self, screen):
        pygame.init()
        pygame.mixer.init()

        with open('pokedex.json') as json_file:
            self.data = json.load(json_file)

        pygame.display.set_caption("Pokemon")
        self.screen = screen
        self.image_fond = pygame.image.load("image/image_AjouterPokemon/fond.png")

        self.image_logo_pokemon = pygame.image.load("image/image_pokedex/pokemon_logo.png")
        self.rect_logo_pokemon = self.image_logo_pokemon.get_rect(topleft=(295, 40))

        self.font = pygame.font.Font("police_ecriture.ttf", 20)

        self.clic = pygame.mixer.Sound("son/son.mp3")

        self.en_menu = True
        self.quitter_ajouter_pokemon = False

        self.cartes = [
            (50, 225, "Lixy", pygame.image.load("image/image_AjouterPokemon/carte_lixy.png")),
            (325, 225, "Psykokwak", pygame.image.load("image/image_AjouterPokemon/carte_psykokwak.png")),
            (600, 225, "Tortipouss", pygame.image.load("image/image_AjouterPokemon/carte_tortipouss.png"))
        ]

        self.message_confirmation = ""

        pygame.display.flip()

    def passer_au_menu(self):    
        self.en_menu = True
        self.quitter_ajouter_pokemon = False
        self.bouton_quitter_presse = True

    def gerer_evenements(self):
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                pygame.quit()
                print("Fermeture du jeu")
                sys.exit()
            elif evenement.type == pygame.MOUSEBUTTONDOWN:
                if evenement.button == 1:
                    for x, y, pokemon_nom, carte in self.cartes:
                        rect_carte = pygame.Rect(x, y, carte.get_width(), carte.get_height())
                        if rect_carte.collidepoint(pygame.mouse.get_pos()):
                            self.ajouter_pokemon(pokemon_nom)
                            self.en_menu = True
                            self.quitter_ajouter_pokemon = False
                            self.bouton_quitter_presse = True
                            menu = Menu()
                            menu.run()

    def ajouter_pokemon(self, pokemon_nom):
        if pokemon_nom == "Tortipouss":
            nouveau_pokemon = {
                "nom": "Tortipouss",
                "niveau": "1",
                "type": "plante",
                "vie": "55",
                "attaque": "68",
                "defense": "64",
                "numero": "0387",
                "image": "image/image_pokedex/pokemon/tortipouss.png"
            }
        elif pokemon_nom == "Lixy":
            nouveau_pokemon = {
                "nom": "Lixy",
                "niveau": "1",
                "type": "electrik",
                "vie": "45",
                "attaque": "65",
                "defense": "34",
                "numero": "0403",
                "image": "image/image_pokedex/pokemon/lixy.png"
            }
        elif pokemon_nom == "Psykokwak":
            nouveau_pokemon = {
                "nom": "Psykokwak",
                "niveau": "1",
                "type": "eau",
                "vie": "50",
                "attaque": "52",
                "defense": "48",
                "numero": "0054",
                "image": "image/image_pokedex/pokemon/psykokwak.png"
            }

        if not any(pokemon["nom"] == nouveau_pokemon["nom"] for pokemon in self.data):
            self.data.append(nouveau_pokemon)

            with open('pokedex.json', 'w') as json_file:
                json.dump(self.data, json_file, indent=2)

            self.message_confirmation = f"Le Pokémon {nouveau_pokemon['nom']} a été ajouté au Pokédex."
        else:
            self.message_confirmation = f"Le Pokémon {nouveau_pokemon['nom']} a déjà été ajouté au Pokédex."

    def afficher_message_confirmation(self):
        texte_confirmation = self.font.render(self.message_confirmation, True, (0, 0, 0))
        self.screen.blit(texte_confirmation, (130, 180))

    def choix_AjouterPokemon(self):
        self.screen.blit(self.image_fond, (0, 0))

        for x, y, pokemon_nom, carte in self.cartes:
            rect_carte = carte.get_rect(topleft=(x, y))
            if rect_carte.collidepoint(pygame.mouse.get_pos()):
                carte = pygame.transform.scale(carte, (int(rect_carte.width * 1.05), int(rect_carte.height * 1.05)))

            self.screen.blit(carte, (x, y))

        self.screen.blit(self.image_logo_pokemon, self.rect_logo_pokemon.topleft)

        texte = self.font.render("Cliquer sur une carte pour ajouter le Pokémon", True, (0, 0, 0))
        self.screen.blit(texte, (130, 150))

        self.afficher_message_confirmation()

        pygame.display.flip()

    def executer(self):
        en_cours = True
        while en_cours:
            self.gerer_evenements()
            self.choix_AjouterPokemon()  # Correction : Utilisez 'self'
            pygame.time.Clock().tick(60)

    

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((850, 531))
    nouveau_pokemon = AjouterPokemon(screen)
    nouveau_pokemon.executer()

import pygame
import pygame.mixer
import json
from menu import *