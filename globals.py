import sys
sys.path.append("Classes")
from Classes.Pokemon import Pokemon
from Classes.Moves import Moves

# Attaques des pokemons
griffe = Moves("Griffe", "Normal", 50)
flammeche = Moves("Flammeche", "Feu", 40)
charge = Moves("Charge", "Normal", 50)
pistolet_a_O = Moves("Pistolet a O", "Eau", 40)
tunnel = Moves("Tunnel", "Sol", 40)
fouet_lianes = Moves("Fouet Lianes", "Plante", 40)
double_dard = Moves("Double Dard", "Insecte", 40)
vive_attaque = Moves("Vive Attaque", "Normal", 50)
eclair = Moves("Eclair", "Electrique", 40)
ecras_face = Moves("Ecras'Face", "Normal", 40)
detritus = Moves("Detritus", "Poison", 40)
choc_mental = Moves("Choc Mental", "Psy", 40)





salameche = Pokemon("Salameche", 1, "Feu", 39, 52, 33, griffe, flammeche)
carapuce = Pokemon("Carapuce", 1, "Eau", 44, 48, 34, charge, pistolet_a_O)
taupiqueur = Pokemon("Taupiqueur", 1, "Sol", 30, 52, 35, griffe, tunnel)
saquedeneu = Pokemon("Saquedeneu", 1, "Plante", 65, 42, 32, charge, fouet_lianes)
chenipan = Pokemon("Chenipan", 1, "Insecte", 45, 40, 36, charge, double_dard)
pikachu = Pokemon ("Pikachu", 1, "Electrique", 35, 55, 40, vive_attaque, eclair)
tadmorv = Pokemon ("Tadmorv", 1, "Poison", 60, 37, 37, ecras_face, detritus)
abra = Pokemon ("Abra", 1, "Psy", 33, 55, 29, choc_mental, charge)

liste_pokemon = [salameche, carapuce, taupiqueur, saquedeneu, chenipan, pikachu, tadmorv, abra]

