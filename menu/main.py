import pygame
import json

pygame.init()

# Génération de la fenêtre du jeu
pygame.display.set_caption("Pokemon")
screen = pygame.display.set_mode((850, 531))
# Charger votre logo
logo = pygame.image.load('assets/logopokeball.png')

# Définir le logo de la fenêtre
pygame.display.set_icon(logo)
# Chargement du fond d'écran du menu
background_menu = pygame.image.load('assets/pokemon.jpg')

# Couleurs
WHITE = (255, 255, 255)
BUTTON_COLOR = (70, 130, 180)  # Couleur des ellipses derrière les boutons (bleu ciel)

# Police de caractères pour le texte du menu
font = pygame.font.Font(None, 36)

# Textes des boutons
button_texts = ["Lancer une partie", "Ajouter un Pokémon", "Accéder au Pokédex", "Quitter"]

# Rectangles pour les boutons
button_rects = []

# Création des rectangles pour chaque bouton
for i, text in enumerate(button_texts):
    button_text = font.render(text, True, WHITE)
    button_rect = button_text.get_rect(center=(screen.get_width() // 2, 100 * (i + 1)))
    button_rects.append(button_text.get_rect(center=(screen.get_width() // 2, 100 * (i + 1))))

running = True
in_menu = True
in_choice = False  # Ajout de la variable d'état pour l'écran de choix

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN and in_menu:
            # Vérification si le clic de souris est sur l'un des boutons
            for i, rect in enumerate(button_rects):
                if rect.collidepoint(event.pos):
                    if i == 0:
                        # Passer de l'écran de menu à l'interface de choix
                        in_menu = False
                        in_choice = True
                    # Le reste de votre code pour les autres boutons reste inchangé

    # Affichage du contenu en fonction de l'état (menu ou choix)
    if in_menu:
        screen.blit(background_menu, (0, 0))
        # Affichage des ellipses derrière les boutons du menu
        for i, rect in enumerate(button_rects):
            ellipse_rect = pygame.Rect(rect.left - 20, rect.top - 10, rect.width + 40, rect.height + 20)
            pygame.draw.ellipse(screen, BUTTON_COLOR, ellipse_rect)
            # Affichage du texte des boutons
            button_text = font.render(button_texts[i], True, WHITE)
            text_rect = button_text.get_rect(center=rect.center)
            screen.blit(button_text, text_rect)
    elif in_choice:
        # Importer et exécuter le contenu de choix.py
        import choix
        choix.run(screen)  # Exécutez la fonction run() de choix.py en passant l'écran

    pygame.display.flip()

pygame.quit()

