from Pokemon import Pokemon

class Combat:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def calculer_modifier(self,pokemon1, pokemon2):
        if pokemon1.type == "Feu":
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
        if pokemon1.type == "Eau":
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
        if pokemon1.type == "Sol":
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
        if pokemon1.type == "Plante":
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
        if pokemon1.type == "Insecte":
            if pokemon2.type == "Feu":
                return 0.5
            if pokemon2.type == "Plante":
                return 2
            if pokemon2.type == "Psy":
                return 2
            else:
                return 1
        if pokemon1.type == "Electrique":
            if pokemon2.type == "Eau":
                return 2
            if pokemon2.type == "Sol":
                return 0.5
            else:
                return 1
        if pokemon1.type == "Poison":
            if pokemon2.type == "Plante":
                return 2
            if pokemon2.type == "Psy":
                return 0.5
            else:
                return 1
        if pokemon1.type == "Psy":
            if pokemon2.type == "Insecte":
                return 0.5
            if pokemon2.type == "Poison":
                return 2
            else:
                return 1

    def attack(self, pokemon1, pokemon2):
        degats = ((2.4 * pokemon1.attaque * 40) / (pokemon2.defense * 50) + 2) * self.calculer_modifier(pokemon1, pokemon2)
        pokemon2.vie -= degats
        if self.calculer_modifier(pokemon1, pokemon2) == 2:
            print (f"C'est super efficace !")        
        print (f"{pokemon1.nom} attaque {pokemon2.nom} et lui inflige {degats} points de dégats !")
        if self.calculer_modifier(pokemon1, pokemon2) == 0.5:
            print (f"C'est pas très efficace...")
        return pokemon2.vie
