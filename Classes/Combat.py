import random
import json

class Combat:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def calculer_modifier(self,pokemon1, pokemon2, move):
        if move.type == "Feu":
            if pokemon2.type == "Eau":
                return 0.5
            if pokemon2.type == "Plante":
                return 2
            if pokemon2.type == "Sol":
                return 0.5
            if pokemon2.type == "Insecte":
                return 2
            else:
                return 1
        if move.type == "Eau":
            if pokemon2.type == "Feu":
                return 2
            if pokemon2.type == "Plante":
                return 0.5
            if pokemon2.type == "Sol":
                return 2
            if pokemon2.type == "Electrique":
                return 0.5
            else:
                return 1
        if move.type == "Sol":
            if pokemon2.type == "Feu":
                return 2
            if pokemon2.type == "Electrique":
                return 2
            if pokemon2.type == "Eau":
                return 0.5
            if pokemon2.type == "Plante":
                return 0.5
            else:
                return 1
        if move.type == "Plante":
            if pokemon2.type == "Feu":
                return 0.5
            if pokemon2.type == "Eau":
                return 2
            if pokemon2.type == "Sol":
                return 2
            if pokemon2.type == "Insecte":
                return 0.5
            else:
                return 1
        if move.type == "Insecte":
            if pokemon2.type == "Feu":
                return 0.5
            if pokemon2.type == "Plante":
                return 2
            if pokemon2.type == "Psy":
                return 2
            else:
                return 1
        if move.type == "Electrique":
            if pokemon2.type == "Eau":
                return 2
            if pokemon2.type == "Sol":
                return 0.5
            else:
                return 1
        if move.type == "Poison":
            if pokemon2.type == "Plante":
                return 2
            if pokemon2.type == "Psy":
                return 0.5
            else:
                return 1
        if move.type == "Psy":
            if pokemon2.type == "Insecte":
                return 0.5
            if pokemon2.type == "Poison":
                return 2
            else:
                return 1
        if move.type == "Normal":
            if pokemon2.type == "Combat":
                return 0.5
            if pokemon2.type == "Roche":
                return 2
            else:
                return 1

    def attack(self, pokemon1, pokemon2, move):
        degats = round((pokemon1.niveau * 0.4 * pokemon1.attaque * move.puissance) / (pokemon2.defense * 10) + 2) * self.calculer_modifier(pokemon1, pokemon2, move)
        aleatoire = random.randint(-1, 1)
        degats += aleatoire
        if degats <= 0:
            degats = 1
        pokemon2.vie -= degats                
        print (f"{pokemon1.nom} attaque {pokemon2.nom} avec {move.nom} et lui inflige {degats} points de dégats !")
        if self.calculer_modifier(pokemon1, pokemon2, move) == 2:
            print (f"C'est super efficace !")
        if self.calculer_modifier(pokemon1, pokemon2, move) == 0.5:
            print (f"C'est pas très efficace...")
        print (f"{pokemon2.nom} a maintenant {pokemon2.vie} points de vie.")
        return degats

    def check_vainqueur(self):
        if self.pokemon1.vie <= 0:
            return self.pokemon2
        elif self.pokemon2.vie <= 0:
            return self.pokemon1
        else:
            return False
        
    def ajouter_au_pokedex(self, pokemon1, pokemon2):
        with open('pokedex.json', 'r') as json_file:
            data = json.load(json_file)

        pokemon_a_ajouter = {
            "nom": pokemon1.nom,
            "niveau": pokemon1.niveau,
            "type": pokemon1.type,
            "vie": pokemon1.vie,
            "attaque": pokemon1.attaque,
            "defense": pokemon1.defense,
            "numero": pokemon1.numero,
            "image": pokemon1.image,
        }

        for pokemon in data:
            if pokemon["nom"] == pokemon_a_ajouter["nom"]:
                data.remove(pokemon)
                break

        data.append(pokemon_a_ajouter)
        with open('pokedex.json', 'w') as json_file:
            json.dump(data, json_file, indent=2)    


        pokemon_a_ajouter = {
            "nom": pokemon2.nom,
            "niveau": pokemon2.niveau,
            "type": pokemon2.type,
            "vie": pokemon2.vie,
            "attaque": pokemon2.attaque,
            "defense": pokemon2.defense,
            "numero": pokemon2.numero,
            "image": pokemon2.image,
        }
        for pokemon in data:
            if pokemon["nom"] == pokemon_a_ajouter["nom"]:
                data.remove(pokemon)
                break

        data.append(pokemon_a_ajouter)
        with open('pokedex.json', 'w') as json_file:
            json.dump(data, json_file, indent=2)
    