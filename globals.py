import sys
sys.path.append("Classes")
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
feuillage = Moves("Feuillage", "Plante", 40)
mimi_queue = Moves("Mimi-Queue", "Normal", 50)
ecume = Moves("Ecume", "Eau", 40)
crocs_eclair = Moves("Crocs Eclair", "Electrique", 40)



moves_dict = {
    "griffe": griffe,
    "flammeche": flammeche,
    "charge": charge,
    "pistolet a O": pistolet_a_O,
    "tunnel": tunnel,
    "fouet lianes": fouet_lianes,
    "double dard": double_dard,
    "vive attaque": vive_attaque,
    "eclair": eclair,
    "ecras'face": ecras_face,
    "detritus": detritus,
    "choc mental": choc_mental,
    "feuillage": feuillage,
    "mimi-queue": mimi_queue,
    "ecume": ecume,
    "crocs eclair": crocs_eclair


}

#Pokemons starters
#salameche = Pokemon("Salameche", 1, "Feu", 39, 52, 33, griffe, flammeche)
#carapuce = Pokemon("Carapuce", 1, "Eau", 44, 48, 34, charge, pistolet_a_O)
#taupiqueur = Pokemon("Taupiqueur", 1, "Sol", 30, 52, 35, griffe, tunnel)
#saquedeneu = Pokemon("Saquedeneu", 1, "Plante", 65, 42, 32, charge, fouet_lianes)
#chenipan = Pokemon("Chenipan", 1, "Insecte", 45, 40, 36, charge, double_dard)
#pikachu = Pokemon ("Pikachu", 1, "Electrique", 35, 55, 40, vive_attaque, eclair)
#tadmorv = Pokemon ("Tadmorv", 1, "Poison", 60, 37, 37, ecras_face, detritus)
#abra = Pokemon ("Abra", 1, "Psy", 33, 55, 29, choc_mental, charge)

#liste_pokemon = [salameche, carapuce, taupiqueur, saquedeneu, chenipan, pikachu, tadmorv, abra]

# Pokemons évolués

#reptincel = Pokemon ("Reptincel", 1, "Feu", 59, 72, 53)
#carabaffe = Pokemon ("Carabaffe", 1, "Eau", 64, 68, 54)
#triopiqueur = Pokemon ("Triopiqueur", 1, "Sol", 50, 72, 55)
#bouldeneu = Pokemon ("Bouldeneu", 1, "Plante", 85, 62, 52)
#chrysacier = Pokemon ("Chrysacier", 1, "Insecte", 65, 60, 56)
#raichu = Pokemon ("Raichu", 1, "Electrique", 55, 75, 60)
#grotadmorv = Pokemon ("Grotadmorv", 1, "Poison", 80, 58, 57)
#kadabra = Pokemon ("Kadabra", 1, "Psy", 53, 75, 59)
