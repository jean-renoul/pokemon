# Importation des modules nécessaires
import pygame
import bienvenue
import choix

# Initialisation de Pygame
pygame.init()

# Configuration de la fenêtre principale
pygame.display.set_caption("Pokemon")
screen = pygame.display.set_mode((850, 531))

# Chargement et configuration de l'icône de la fenêtre
logo = pygame.image.load('menu/image/logopokeball.png')
pygame.display.set_icon(logo)

# Chargement de l'image de fond du menu
background_menu = pygame.image.load('menu/image/test.png')

# Initialisation et lecture de la musique de fond
pygame.mixer.init()
pygame.mixer.music.load('menu/image/pokemon.mp3')
pygame.mixer.music.play(-1)

# Chargement du son de clic
click_sound = pygame.mixer.Sound('menu/image/son.mp3')

# Définition des couleurs utilisées
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Définition de la police utilisée pour les boutons
font = pygame.font.Font('menu/image/Retro Gaming.ttf', 30)

# Textes des boutons
button_texts = ["Lancer une partie", "Ajouter un Pokémon", "Accéder au Pokédex", "Quitter"]

# Rectangles des boutons
button_rects = []

# Création des rectangles des boutons
for i, text in enumerate(button_texts):
    button_text = font.render(text, True, WHITE)
    button_rect = button_text.get_rect(center=(screen.get_width() // 2, 100 * (i + 1)))
    button_rects.append(button_rect)

# Variables de contrôle
running = True
in_menu = True
in_choice = False

# Boucle principale du programme
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Quitter le programme si la fenêtre est fermée
            running = False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if in_menu:
                # Vérifier si un bouton est cliqué
                for i, rect in enumerate(button_rects):
                    if rect.collidepoint(event.pos):
                        # Jouer le son de clic
                        click_sound.play()
                        # Exécuter différentes actions en fonction du bouton cliqué
                        if i == 0:
                            in_menu = False
                            bienvenue.run(screen)
                        elif i == 3:
                            running = False
            elif in_choice:
                # Si dans l'écran de choix, exécuter la fonction de choix
                choix.choix(screen)

    if in_menu:
        # Afficher l'image de fond du menu
        screen.blit(background_menu, (0, 0))

        # Afficher les boutons
        for i, rect in enumerate(button_rects):
            button_text = font.render(button_texts[i], True, BLACK)
            text_rect = button_text.get_rect(center=rect.center)
            screen.blit(button_text, text_rect)

    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter Pygame à la fin
pygame.quit()
