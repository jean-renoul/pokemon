import random
import json

class Combat:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    # méthode pour calculer le modificateur de dégats, en fonction du type de l'attaque utilisée, mise en relation ave le type du pokemon adverse
    def calculer_modifier(self, pokemon, move):
        if move.type == "Feu":
            if pokemon.type == "Eau":
                return 0.5
            if pokemon.type == "Plante":
                return 2
            if pokemon.type == "Sol":
                return 0.5
            if pokemon.type == "Insecte":
                return 2
            else:
                return 1
        if move.type == "Eau":
            if pokemon.type == "Feu":
                return 2
            if pokemon.type == "Plante":
                return 0.5
            if pokemon.type == "Sol":
                return 2
            if pokemon.type == "Electrique":
                return 0.5
            else:
                return 1
        if move.type == "Sol":
            if pokemon.type == "Feu":
                return 2
            if pokemon.type == "Electrique":
                return 2
            if pokemon.type == "Eau":
                return 0.5
            if pokemon.type == "Plante":
                return 0.5
            else:
                return 1
        if move.type == "Plante":
            if pokemon.type == "Feu":
                return 0.5
            if pokemon.type == "Eau":
                return 2
            if pokemon.type == "Sol":
                return 2
            if pokemon.type == "Insecte":
                return 0.5
            else:
                return 1
        if move.type == "Insecte":
            if pokemon.type == "Feu":
                return 0.5
            if pokemon.type == "Plante":
                return 2
            if pokemon.type == "Psy":
                return 2
            else:
                return 1
        if move.type == "Electrique":
            if pokemon.type == "Eau":
                return 2
            if pokemon.type == "Sol":
                return 0.5
            else:
                return 1
        if move.type == "Poison":
            if pokemon.type == "Plante":
                return 2
            if pokemon.type == "Psy":
                return 0.5
            else:
                return 1
        if move.type == "Psy":
            if pokemon.type == "Insecte":
                return 0.5
            if pokemon.type == "Poison":
                return 2
            else:
                return 1
        if move.type == "Normal":
            if pokemon.type == "Combat":
                return 0.5
            if pokemon.type == "Roche":
                return 2
            else:
                return 1

    # Méthode pour calculer les dégats infligés par une attaque, la formule est basée sur la formule officielle mais un petit peu remaniée, car les combats avaient
    # tendance à s'éterniser
    def attack(self, pokemon1, pokemon2, move):
        degats = round((((pokemon1.niveau * 0.4 + 2) * pokemon1.attaque * move.puissance) / pokemon2.defense / 50) + 2) * self.calculer_modifier(pokemon2, move)
        aleatoire = random.randint(-1, 1)
        degats += aleatoire
        if degats <= 0:
            degats = 1
        pokemon2.vie -= degats                
        return degats

    # Méthode pour vérifier si le combat est gagné, perdu ou pas encore terminé
    def check_vainqueur(self, pokemon3, pokemon4):
        if self.pokemon1.vie <= 0 and self.pokemon2.vie <= 0:
            return "défaite"
        elif pokemon3.vie <= 0 and pokemon4.vie <= 0:
            return "victoire"
        else:
            return False
        
    # Méthode pour enregistrer un pokemon dans le pokedex
    def ajouter_au_pokedex(self, pokemon):
        with open('pokedex.json', 'r') as json_file:
            data = json.load(json_file)

        pokemon_a_ajouter = {
            "nom": pokemon.nom,
            "niveau": pokemon.niveau,
            "type": pokemon.type,
            "vie": pokemon.vie,
            "attaque": pokemon.attaque,
            "defense": pokemon.defense,
            "numero": pokemon.numero,
            "image": pokemon.image,
        }
        # Cette boucle évite d'ajouter des doublons dans le pokedex
        for pokemon in data:
            if pokemon["nom"] == pokemon_a_ajouter["nom"]:
                data.remove(pokemon)
                break

        data.append(pokemon_a_ajouter)
        with open('pokedex.json', 'w') as json_file:
            json.dump(data, json_file, indent=2)

    # Méthode que l'on va lancer à chaque fois qu'on quitte le jeu, elle réinitialise le pokedex ainsi que la liste des pokemons disponibles
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