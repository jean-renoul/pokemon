import pygame
import json
import sys

class Pokedex:
    def __init__(self):
        pygame.init()

        # Charger les données JSON
        with open("pokedex/pokedex.json", "r") as fichier_json:
            self.donnees_pokemon = json.load(fichier_json)

        # Création de la fenêtre de notre pokédex.
        pygame.display.set_caption("Pokédex")
        self.ecran = pygame.display.set_mode((850, 531))
        self.logo = pygame.image.load('pokedex/assets/logopokeball.png')
        pygame.display.set_icon(self.logo)

        # Chargement de l'image du pokédex.
        self.image_fond = pygame.image.load("pokedex/assets/pokedex.png")

        # Police pour le texte
        self.police = pygame.font.Font("pokedex/assets/symtext.ttf", 20)

        # Variables
        self.index_pokemon_courant = 0
        self.en_menu = True  # Nouvelle variable pour gérer si nous sommes dans le menu

        # Rectangles pour le bouton "Pokédex"
        self.rectangles_bouton_pokedex = pygame.Rect(380, 400, 250, 50)

        # Nouvelle variable pour indiquer si le bouton est survolé
        self.bouton_pokedex_survole = False

        # Chargez l'image de la Pokéball pour le bouton de retour
        self.image_retour = pygame.image.load("pokedex/assets/pokeball.png")
        self.rect_retour = self.image_retour.get_rect(topleft=(710, 360))

        # Définir les mouvements de la Pokéball
        self.deplacement_x = 0
        self.deplacement_y = 0

        # Afficher le menu après l'initialisation
        self.afficher_menu()

    def afficher_menu(self):
        # Remplir l'écran avec la couleur blanche
        self.ecran.fill((255, 255, 255))

        # Afficher l'image du fond du Pokédex
        self.ecran.blit(self.image_fond, (0, 0))

        # Réinitialiser la couleur du bouton et supprimer le rectangle rouge
        self.bouton_pokedex_survole = False

        # Afficher le bouton "Pokédex"
        texte_couleur = (255, 0, 0) if self.bouton_pokedex_survole else (255, 255, 255)
        texte_surface = self.police.render("Accéder au Pokédex", True, texte_couleur)
        self.ecran.blit(texte_surface, (300, 390))

        # Rafraîchir l'écran
        pygame.display.flip()

    def afficher_pokemon_courant(self):
        # Remplir l'écran avec la couleur blanche
        self.ecran.fill((255, 255, 255))

        # Afficher l'image du fond du Pokédex
        self.ecran.blit(self.image_fond, (0, 0))

        # Afficher l'image du Pokémon actuel
        pokemon_courant = self.donnees_pokemon[self.index_pokemon_courant]
        image_pokemon = pygame.image.load(pokemon_courant["image"])
        self.ecran.blit(image_pokemon, (335, 50))

        # Afficher les informations du Pokémon
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

        # Afficher le bouton de retour
        self.ecran.blit(self.image_retour, self.rect_retour.move(self.deplacement_x, self.deplacement_y).topleft)

        # Création des rectangles pour les flèches.
        self.rectangles_fleches = [
            pygame.Rect(164, 355, 25, 34),  # Rectangle pour la flèche vers le haut
            pygame.Rect(164, 412, 25, 30),  # Rectangle pour la flèche vers le bas
            pygame.Rect(125, 388, 38, 25),  # Rectangle pour la flèche vers la gauche
            pygame.Rect(190, 388, 38, 25)   # Rectangle pour la flèche vers la droite
        ]

        # Dessiner les rectangles pour les flèches
        for rectangle in self.rectangles_fleches:
            pygame.draw.rect(self.ecran, (0, 0, 255), rectangle)

        # Rafraîchir l'écran
        pygame.display.flip()

    def mettre_a_jour_couleurs_fleches(self, pos_souris):
        # Réinitialiser la couleur par défaut pour toutes les flèches
        for rectangle in self.rectangles_fleches:
            pygame.draw.rect(self.ecran, (0, 0, 255), rectangle)

        # Vérifier si la souris survole les rectangles des flèches directionnelles
        if self.rectangles_fleches[0].collidepoint(pos_souris):
            pygame.draw.rect(self.ecran, (255, 0, 0), self.rectangles_fleches[0])  # Changer la couleur pour la flèche vers le haut
        elif self.rectangles_fleches[1].collidepoint(pos_souris):
            pygame.draw.rect(self.ecran, (255, 0, 0), self.rectangles_fleches[1])  # Changer la couleur pour la flèche vers le bas
        elif self.rectangles_fleches[2].collidepoint(pos_souris):
            pygame.draw.rect(self.ecran, (255, 0, 0), self.rectangles_fleches[2])  # Changer la couleur pour la flèche vers la gauche
        elif self.rectangles_fleches[3].collidepoint(pos_souris):
            pygame.draw.rect(self.ecran, (255, 0, 0), self.rectangles_fleches[3])  # Changer la couleur pour la flèche vers la droite

        # Rafraîchir l'écran
        pygame.display.flip()

    def mettre_a_jour_couleurs_bouton_pokedex(self, pos_souris):
        # Modifier la variable indiquant si le bouton est survolé
        self.bouton_pokedex_survole = self.rectangles_bouton_pokedex.collidepoint(pos_souris)

    def gerer_evenements(self):
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                pygame.quit()
                print("Fermeture du Pokédex.")
                sys.exit()
            elif evenement.type == pygame.MOUSEMOTION:
                if self.en_menu:
                    # Si nous sommes dans le menu, mettre à jour la couleur du bouton "Pokédex"
                    self.mettre_a_jour_couleurs_bouton_pokedex(pygame.mouse.get_pos())
                else:
                    # Sinon, vérifier si le bouton de retour est survolé
                    if self.rect_retour.collidepoint(pygame.mouse.get_pos()):
                        # Changer l'image du bouton de retour lorsqu'il est survolé
                        self.image_retour = pygame.image.load("pokedex/assets/pokeball.png")
                    else:
                        self.image_retour = pygame.image.load("pokedex/assets/pokeball.png")
            elif evenement.type == pygame.MOUSEBUTTONDOWN:
                if evenement.button == 1:  # Bouton gauche de la souris
                    if self.en_menu:
                        # Si nous sommes dans le menu, vérifier si le bouton "Pokédex" est cliqué
                        if self.rectangles_bouton_pokedex.collidepoint(evenement.pos):
                            self.en_menu = False  # Passer au mode Pokédex
                            self.afficher_pokemon_courant()
                    else:
                        # Sinon, vérifier si le bouton de retour est cliqué
                        if self.rect_retour.collidepoint(evenement.pos):
                            self.en_menu = True  # Revenir au menu principal
                            self.afficher_menu()
                        else:
                            # Sinon, vérifier si les flèches sont cliquées
                            if self.rectangles_fleches[2].collidepoint(evenement.pos):
                                self.changer_pokemon_precedent()
                            elif self.rectangles_fleches[3].collidepoint(evenement.pos):
                                self.changer_pokemon_suivant()

    def changer_pokemon_precedent(self):
        # Défilement vers le Pokémon précédent
        self.index_pokemon_courant = (self.index_pokemon_courant - 1) % len(self.donnees_pokemon)
        if not self.en_menu:
            self.afficher_pokemon_courant()

    def changer_pokemon_suivant(self):
        # Défilement vers le Pokémon suivant
        self.index_pokemon_courant = (self.index_pokemon_courant + 1) % len(self.donnees_pokemon)
        if not self.en_menu:
            self.afficher_pokemon_courant()

    def executer(self):
        # Boucle principale
        en_cours = True
        while en_cours:
            self.gerer_evenements()
            pygame.time.Clock().tick(60)  # Limiter la boucle à 60 images par seconde

# Création d'une instance de la classe Pokedex et exécution du programme
pokedex = Pokedex()
pokedex.executer()