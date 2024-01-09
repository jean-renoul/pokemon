import pygame
pygame.init()

# Création de la première classe qui va représenter notre pokémon
class Player:
    def __init__(self):
        self.health_salameche = "39"
        self.health_carapuce = "44"
        self.health_taupiqueur = "30"
        self.health_saquedeneu = "65"
        self.health_chenipan = "45"
        self.health_pikachu = "35"
        self.health_tadmorv = "60"
        self.health_abra = "33"
        self.health_reptincel = "59"
        self.health_carabaffe = "64"
        self.health_triopiqueur = "50"
        self.health_bouldeneu = "85"
        self.health_chrysacier = "65"
        self.health_raichu = "55"
        self.health_grotadmorv = "80"
        self.health_kadabra = "53"

# Génération de la fenêtre pygame
pygame.display.set_caption("Pokemon zone de combat")
screen = pygame.display.set_mode((850, 531))

# Importation de l'image de fond
background = pygame.image.load("zone_combat/assets/combat.png")

running = True

# Boucle tant que cette condition est vraie
while running:

    # Appliquer l'arrière plan de notre jeu
    screen.blit(background, (0, 0))

    # Mettre à jour l'écran
    pygame.display.flip()

    #si l'utilisateur ferme la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")