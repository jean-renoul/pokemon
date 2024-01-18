import pygame
import pygame.mixer
import json
import sys

class AjouterPokemon:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        # Charger les données du fichier json
        with open('pokedex.json') as json_file:
            self.data = json.load(json_file)

        # Générer la fenêtre de notre jeu
        pygame.display.set_caption("Pokemon")
        self.screen = pygame.display.set_mode((850, 531))
        self.image_fond = pygame.image.load("image/image_AjouterPokemon/fond.png")

        # Charger l'image du logo Pokémon
        self.image_logo_pokemon = pygame.image.load("image/image_pokedex/pokemon_logo.png")
        self.rect_logo_pokemon = self.image_logo_pokemon.get_rect(topleft=(295, 40))

        # Police pour le texte
        self.font = pygame.font.Font("police_ecriture.ttf", 20)

        # Son du clic
        self.clic = pygame.mixer.Sound("son/son.mp3")

        # Chargement des images des cartes pokemon
        self.cartes = [
            (50, 225, "Lixy", pygame.image.load("image/image_AjouterPokemon/carte_lixy.png")),
            (325, 225, "Psykokwak", pygame.image.load("image/image_AjouterPokemon/carte_psykokwak.png")),
            (600, 225, "Tortipouss", pygame.image.load("image/image_AjouterPokemon/carte_tortipouss.png"))
        ]

        pygame.display.flip()

    def gerer_evenements(self):
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                pygame.quit()
                print("Fermeture du jeu")
                sys.exit()
            elif evenement.type == pygame.MOUSEBUTTONDOWN:
                if evenement.button == 1:  # Clic gauche
                    self.ajouter_pokemon()

    def ajouter_pokemon(self):
        for x, y, pokemon_nom, carte in self.cartes:
            rect_carte = pygame.Rect(x, y, carte.get_width(), carte.get_height())
            if rect_carte.collidepoint(pygame.mouse.get_pos()):
                # Sélectionner le bon Pokémon en fonction du nom
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

                # Vérifier si le Pokémon n'est pas déjà présent dans la liste
                if not any(pokemon["nom"] == nouveau_pokemon["nom"] for pokemon in self.data):
                    # Ajouter le nouveau Pokémon à la liste existante dans le fichier JSON
                    self.data.append(nouveau_pokemon)

                    # Écrire les données mises à jour dans le fichier JSON
                    with open('pokedex.json', 'w') as json_file:
                        json.dump(self.data, json_file, indent=2)
                    
                    # Afficher le message de confirmation
                    print(f"Le Pokémon {nouveau_pokemon['nom']} a été ajouté au Pokédex.")
                else:
                    # Afficher le message que le Pokémon est déjà ajouté
                    print(f"Le Pokémon {nouveau_pokemon['nom']} a déjà été ajouté au Pokédex.")



    def choix_AjouterPokemon(self):
        # Afficher l'image de fond
        self.screen.blit(self.image_fond, (0, 0))

        # Appliquer un grossissement aux cartes lorsque le curseur est dessus
        for x, y, pokemon_nom, carte in self.cartes:
            rect_carte = carte.get_rect(topleft=(x, y))
            if rect_carte.collidepoint(pygame.mouse.get_pos()):
                # Appliquer un facteur de grossissement (1.05 dans cet exemple)
                carte = pygame.transform.scale(carte, (int(rect_carte.width * 1.05), int(rect_carte.height * 1.05)))

            self.screen.blit(carte, (x, y))

        # Afficher le logo Pokémon
        self.screen.blit(self.image_logo_pokemon, self.rect_logo_pokemon.topleft)

        # Afficher le texte
        texte = self.font.render("Cliquer sur une carte pour ajouter le Pokémon", True, (0, 0, 0))
        self.screen.blit(texte, (130, 150))

        pygame.display.flip()

# Créer une instance de la classe AjouterPokemon
nouveau_pokemon = AjouterPokemon()

# Boucle principale pour maintenir la fenêtre ouverte
while True:
    nouveau_pokemon.gerer_evenements()
    nouveau_pokemon.choix_AjouterPokemon()