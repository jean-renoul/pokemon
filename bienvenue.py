import pygame
import choix  # Importer le module choix
import json

def run(screen):
    pygame.init()
    pygame.display.set_caption("Pokemon")
    
    # Chargement du fond d'écran
    background = pygame.image.load('image/image_ecran/bienvenue.png')

    # Chargement de l'image pour le bouton pokeball
    button_image = pygame.image.load('image/image_pokedex/pokeball.png')
    button_rect = button_image.get_rect(center=(screen.get_width() // 2, screen.get_height() // 1.15))

    # Chargement du son du clic sur les boutons
    click_sound = pygame.mixer.Sound('son/son.mp3')

    running = True
    while running:
        screen.blit(background, (0, 0))
        screen.blit(button_image, button_rect)  # Afficher l'image du bouton
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                vider_pokedex()
                running = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    click_sound.play()  # Jouez le son du clic
                    choix.choix(screen)  # Appeler la fonction choix() de choix.py
                    return
                
def vider_pokedex():
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
