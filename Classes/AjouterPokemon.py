import sys # Importer le module sys pour pouvoir quitter le jeu
import pygame # Importer le module pygame pour pouvoir créer le jeu
import pygame.mixer # Importer le module pygame.mixer pour pouvoir jouer des sons
import json # Importer le module json pour pouvoir lire et écrire des fichiers json
from Classes.menu import Menu # Importer la classe Menu pour pouvoir retourner au menu
 
class AjouterPokemon: # Créer la classe AjouterPokemon
    def __init__(self, screen): # Créer la méthode __init__ qui est exécutée à la création d'un objet de la classe
        pygame.init() # Initialiser pygame
        pygame.mixer.init() # Initialiser pygame.mixer

        with open('pokemon.json') as json_file: # Ouvrir le fichier pokemon.json
            self.data = json.load(json_file) # Charger le contenu du fichier dans la variable self.data

        pygame.display.set_caption("Pokemon") # Changer le titre de la fenêtre
        self.screen = screen # Créer une variable screen dans la classe AjouterPokemon et lui assigner la valeur de la variable screen passée en paramètre
        self.image_fond = pygame.image.load("image/image_AjouterPokemon/fond.png") # Charger l'image du fond

        self.image_logo_pokemon = pygame.image.load("image/image_pokedex/pokemon_logo.png") # Charger l'image du logo pokemon
        self.rect_logo_pokemon = self.image_logo_pokemon.get_rect(topleft=(295, 40)) # Créer un rectangle autour de l'image du logo pokemon

        self.font = pygame.font.Font("police_ecriture.ttf", 20) # Charger la police d'écriture

        self.clic = pygame.mixer.Sound("son/son.mp3") # Charger le son du clic

        self.en_menu = True # Créer une variable en_menu et lui assigner la valeur True
        self.quitter_ajouter_pokemon = False # Créer une variable quitter_ajouter_pokemon et lui assigner la valeur False

        self.cartes = [ # Créer une liste de tuples contenant les coordonnées et le nom des pokémons
            (50, 225, "lixy", pygame.image.load("image/image_AjouterPokemon/carte_lixy.png")),
            (325, 225, "psykokwak", pygame.image.load("image/image_AjouterPokemon/carte_psykokwak.png")),
            (600, 225, "tortipouss", pygame.image.load("image/image_AjouterPokemon/carte_tortipouss.png"))
        ]

        self.image_fleche = pygame.image.load("image/fleches.png") # Charger l'image de la flèche
        self.rect_fleche = self.image_fleche.get_rect(topright=(800, 0)) # Créer un rectangle autour de l'image de la flèche

        pygame.display.flip() # Rafraîchir l'écran

    def passer_au_menu(self): # Créer la méthode passer_au_menu
        self.en_menu = True # Changer la valeur de la variable en_menu à True
        self.quitter_ajouter_pokemon = False # Changer la valeur de la variable quitter_ajouter_pokemon à False
        self.bouton_quitter_presse = True # Changer la valeur de la variable bouton_quitter_presse à True

    def gerer_evenements(self): # Créer la méthode gerer_evenements
        for evenement in pygame.event.get(): # Pour chaque événement dans la liste des événements
            if evenement.type == pygame.QUIT: # Si l'événement est de type QUIT
                self.vider_pokedex() # Appeler la méthode vider_pokedex
                pygame.quit() # Quitter pygame
                sys.exit() # Quitter le jeu
            elif evenement.type == pygame.MOUSEBUTTONDOWN: # Si l'événement est de type MOUSEBUTTONDOWN
                if evenement.button == 1: # Si le bouton de la souris est le bouton gauche
                    for x, y, pokemon_nom, carte in self.cartes: # Pour chaque carte dans la liste des cartes
                        rect_carte = pygame.Rect(x, y, carte.get_width(), carte.get_height()) # Créer un rectangle autour de la carte
                        if rect_carte.collidepoint(pygame.mouse.get_pos()): # Si le clic est sur la carte
                            self.ajouter_pokemon(pokemon_nom) # Appeler la méthode ajouter_pokemon
                            self.passer_au_menu() # Appeler la méthode passer_au_menu
                            menu = Menu() # Créer un objet de la classe Menu
                            menu.run() # Appeler la méthode run de l'objet menu

                    # Vérifier si le clic est sur la flèche
                    if self.rect_fleche.collidepoint(evenement.pos): # Si le clic est sur la flèche
                        self.passer_au_menu() # Appeler la méthode passer_au_menu
                        menu = Menu() # Créer un objet de la classe Menu
                        menu.run() # Appeler la méthode run de l'objet menu

    def ajouter_pokemon(self, pokemon_nom): # Créer la méthode ajouter_pokemon
        if pokemon_nom == "tortipouss":
            nouveau_pokemon = {
                "nom": "tortipouss",
                "niveau": 1,
                "type": "Plante",
                "vie": 55,
                "attaque": 68,
                "defense": 64,
                "move1": "charge",
                "move2": "feuillage",
                "evolution": "boskara",
                "numero": "0387",
                "image": "image/image_pokedex/pokemon/tortipouss.png"
            }
        elif pokemon_nom == "lixy":
            nouveau_pokemon = {
                "nom": "lixy",
                "niveau": 1,
                "type": "Electrique",
                "vie": 45,
                "attaque": 65,
                "defense": 34,
                "move1": "vive attaque",
                "move2": "eclair",
                "evolution": "luxio",
                "numero": "0403",
                "image": "image/image_pokedex/pokemon/lixy.png"
            }
        elif pokemon_nom == "psykokwak":
            nouveau_pokemon = {
                "nom": "psykokwak",
                "niveau": 1,
                "type": "Eau",
                "vie": 50,
                "attaque": 52,
                "defense": 48,
                "move1": "charge",
                "move2": "pistolet a O",
                "evolution": "akwakwak",
                "numero": "0054",
                "image": "image/image_pokedex/pokemon/psykokwak.png"
            }

        if not any(pokemon["nom"] == nouveau_pokemon["nom"] for pokemon in self.data): # Si le pokemon n'est pas déjà dans le pokedex
            self.data.append(nouveau_pokemon) # Ajouter le nouveau pokemon à la liste des pokemons

            with open('pokemon.json', 'w') as json_file: # Ouvrir le fichier pokemon.json
                json.dump(self.data, json_file, indent=2) # Écrire la liste des pokemons dans le fichier pokemon.json

    def choix_AjouterPokemon(self): # Créer la méthode choix_AjouterPokemon
        self.screen.blit(self.image_fond, (0, 0)) # Afficher l'image du fond

        for x, y, pokemon_nom, carte in self.cartes: # Pour chaque carte dans la liste des cartes
            rect_carte = carte.get_rect(topleft=(x, y)) # Créer un rectangle autour de la carte
            if rect_carte.collidepoint(pygame.mouse.get_pos()): # Si la souris est sur la carte
                carte = pygame.transform.scale(carte, (int(rect_carte.width * 1.05), int(rect_carte.height * 1.05))) # Agrandir la carte

            self.screen.blit(carte, (x, y)) # Afficher la carte

        self.screen.blit(self.image_logo_pokemon, self.rect_logo_pokemon.topleft) # Afficher le logo pokemon

        texte = self.font.render("Cliquer sur une carte pour ajouter le Pokémon", True, (0, 0, 0))
        self.screen.blit(texte, (130, 150)) # Afficher le texte

        # Afficher la flèche
        self.screen.blit(self.image_fleche, self.rect_fleche)

        pygame.display.flip() # Rafraîchir l'écran

    def executer(self): # Créer la méthode executer
        en_cours = True 
        while en_cours: # Tant que en_cours est True
            self.gerer_evenements() # Appeler la méthode gerer_evenements
            self.choix_AjouterPokemon() # Appeler la méthode choix_AjouterPokemon
            pygame.time.Clock().tick(60) # Limiter le nombre d'images par seconde à 60

    def vider_pokedex(self): # Méthode que l'on va lancer à chaque fois qu'on quitte le jeu, elle réinitialise le pokedex ainsi que la liste des pokemons disponibles
        with open('pokedex.json', 'r') as json_file: # Ouvrir le fichier pokedex.json
            data = json.load(json_file) # Charger le contenu du fichier dans la variable data

        starters = [] # Créer une liste starters
        for pokemon in data: # Pour chaque pokemon dans la liste des pokemons
            if pokemon["nom"]  == "Pikachu" or pokemon["nom"]  == "Carapuce" or pokemon["nom"]  == "Salameche": # Si le pokemon est Pikachu, Carapuce ou Salameche
                starters.append(pokemon) # Ajouter le pokemon à la liste starters

        with open('pokedex.json', 'w') as json_file: # Ouvrir le fichier pokedex.json
            json.dump(starters, json_file, indent=2) # Écrire la liste starters dans le fichier pokedex.json

        with open('pokemon.json', 'r') as json_file: # Ouvrir le fichier pokemon.json
            data = json.load(json_file) # Charger le contenu du fichier dans la variable data

        pokemons_base = [] # Créer une liste pokemons_base
        for pokemon in data: # Pour chaque pokemon dans la liste des pokemons
            pokemons_base.append(pokemon) # Ajouter le pokemon à la liste pokemons_base
            if pokemon["nom"]  == "tortipouss" or pokemon["nom"]  == "lixy" or pokemon["nom"]  == "psykokwak": # Si le pokemon est tortipouss, lixy ou psykokwak
                pokemons_base.remove(pokemon) # Retirer le pokemon de la liste pokemons_base

        with open('pokemon.json', 'w') as json_file: # Ouvrir le fichier pokemon.json
            json.dump(pokemons_base, json_file, indent=2) # Écrire la liste pokemons_base dans le fichier pokemon.json

if __name__ == "__main__": # Si le fichier est exécuté directement
    pygame.init() # Initialiser pygame
    screen = pygame.display.set_mode((850, 531))
    nouveau_pokemon = AjouterPokemon(screen) # Créer un objet de la classe AjouterPokemon
    nouveau_pokemon.executer() # Appeler la méthode executer de l'objet nouveau_pokemon
