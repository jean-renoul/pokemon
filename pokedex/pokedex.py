import pygame
import pygame.mixer
import json
import sys

class Pokedex:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        # Charger les données JSON
        with open("pokedex/pokedex.json", "r") as fichier_json:
            self.donnees_pokemon = json.load(fichier_json)

        # Création de la fenêtre de notre pokédex.
        pygame.display.set_caption("Pokédex")
        self.ecran = pygame.display.set_mode((850, 531))
        self.logo = pygame.image.load('pokedex/assets/logopokeball.png')
        pygame.display.set_icon(self.logo)

        # Chargement de l'image du châssis du pokédex.
        self.image_fond = pygame.image.load("pokedex/assets/pokedex.png")

        # Police pour le texte
        self.police = pygame.font.Font("pokedex/assets/Retro Gaming.ttf", 20)

        # Son du clic
        self.son_clic = pygame.mixer.Sound("pokedex/assets/son.mp3")

        # Variables
        self.index_pokemon_courant = 0
        self.en_menu = True

        # Rectangles pour le bouton "Pokédex"
        self.rectangles_bouton_pokedex = pygame.Rect(290, 365, 250, 50)
        self.bouton_pokedex_survole = False

        # Rectangles pour le bouton "Quitter le Pokédex"
        self.rectangles_bouton_quitter = pygame.Rect(295, 425, 250, 50)
        self.bouton_quitter_survole = False

        # Chargement de l'image du logo Pokémon dans le menu
        self.image_logo_pokemon = pygame.image.load("pokedex/assets/pokemon_logo.png")  
        x_position_logo = 295  
        y_position_logo = 80  
        self.rect_logo_pokemon = self.image_logo_pokemon.get_rect(topleft=(x_position_logo, y_position_logo))

        # Chargement de l'image de la Pokéball pour le bouton de retour
        self.image_retour = pygame.image.load("pokedex/assets/pokeball.png")
        self.rect_retour = self.image_retour.get_rect(topleft=(710, 360))

        # Définir les mouvements de la Pokéball
        self.deplacement_x = 0
        self.deplacement_y = 0

        # Afficher le menu après l'initialisation
        self.afficher_menu()

    def afficher_menu(self):
        self.ecran.fill((255, 255, 255))
        self.ecran.blit(self.image_fond, (0, 0))

        # Afficher l'image du logo Pokémon dans le menu
        self.ecran.blit(self.image_logo_pokemon, self.rect_logo_pokemon)

        # Bouton "Accéder au Pokédex"
        texte_couleur_pokedex = (255, 255, 255)
        texte_surface_pokedex = self.police.render("Accéder au Pokédex", True, texte_couleur_pokedex)
        self.ecran.blit(texte_surface_pokedex, (290, 365))

        # Bouton "Quitter le Pokédex"
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

    def mettre_a_jour_couleurs_bouton_pokedex(self, pos_souris):
        self.bouton_pokedex_survole = self.rectangles_bouton_pokedex.collidepoint(pos_souris)
        self.bouton_quitter_survole = self.rectangles_bouton_quitter.collidepoint(pos_souris)

    def gerer_evenements(self):
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                pygame.quit()
                print("Fermeture du Pokédex.")
                sys.exit()
            elif evenement.type == pygame.MOUSEMOTION:
                if self.en_menu:
                    self.mettre_a_jour_couleurs_bouton_pokedex(pygame.mouse.get_pos())
                else:
                    if self.rect_retour.collidepoint(pygame.mouse.get_pos()):
                        self.image_retour = pygame.image.load("pokedex/assets/pokeball.png")
                    else:
                        self.image_retour = pygame.image.load("pokedex/assets/pokeball.png")
            elif evenement.type == pygame.MOUSEBUTTONDOWN:
                if evenement.button == 1:
                    if self.en_menu:
                        if self.rectangles_bouton_pokedex.collidepoint(evenement.pos):
                            self.en_menu = False
                            self.afficher_pokemon_courant()
                            self.son_clic.play()
                        elif self.rectangles_bouton_quitter.collidepoint(evenement.pos):
                            pygame.quit()
                            print("Fermeture du Pokédex.")
                            sys.exit()
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
pokedex = Pokedex()
pokedex.executer()