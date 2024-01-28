#fichier obsolète qui traitait le combat 1vs1, remplacé par combatLoop.py
import sys
sys.path.append("Classes")
from Classes.Combat1vs1 import Combat
from Classes.Pokemon import Pokemon
from globals import *
import random
import pygame
from pygame.locals import *
import json
# from choix2pokemon import *
from Classes.menu import Menu




# Initialisation de pygame
pygame.init()
pygame.display.set_caption("Combat de Pokemon")



# Charger données pokemon
with open("pokemon.json", "r") as read_file:
    data = json.load(read_file)

liste_pokemon = []

for pokemon in data:

    move1 = moves_dict.get(pokemon["move1"])
    move2 = moves_dict.get(pokemon["move2"])


    instance = Pokemon(
        pokemon["nom"],
        pokemon["niveau"],
        pokemon["type"],
        pokemon["vie"],
        pokemon["attaque"],
        pokemon["defense"],
        move1,
        move2,
        pokemon["evolution"],
        pokemon["numero"],
        pokemon["image"]
        )
    liste_pokemon.append(instance) 

# Variables graphiques
screen = pygame.display.set_mode((850, 531))
width = screen.get_width()
height = screen.get_height()

background = pygame.image.load("image/image_ecran/combat.png")
smallfont = pygame.font.Font("police_ecriture.ttf", 20)

menu = Menu()


def lancer_combat(pokemon_joueur):
    pygame.mixer.init()
    pygame.mixer.music.load('son/musique_combat.mp3')
    pygame.mixer.music.play(-1) # -1 signifie que la musique va boucler

    pokemon1 = pokemon_joueur

    if pokemon1.niveau == 3:
        evolution(pokemon1)
        
    for pokemon in liste_pokemon:
        if pokemon.nom == pokemon1.nom:
            liste_pokemon.remove(pokemon)
            break

    pokemon2 = random.choice(liste_pokemon)
    
    vie_max_joueur = pokemon1.vie
    vie_max_ennemi = pokemon2.vie

    duel = Combat(pokemon1, pokemon2)
    duel.ajouter_au_pokedex(pokemon1, pokemon2)

    running = True
    tour_joueur = True
    
    # Boucle de jeu
    while running:

        if duel.check_vainqueur() == pokemon1:
            pokemon1.niveau += 1
            pokemon1.vie = vie_max_joueur
            pokemon2.vie = vie_max_ennemi
            ecran_de_victoire()
            lancer_combat(pokemon1)

        elif duel.check_vainqueur() == pokemon2:
            pokemon1.vie = vie_max_joueur
            pokemon2.vie = vie_max_ennemi
            ecran_de_defaite()
            pygame.mixer.music.stop()
            menu.run()

        image_pokemon_joueur = pygame.image.load(f"image/image_pokedex/pokemon/{pokemon1.nom}_inverse.png")
        image_pokemon_ennemi = pygame.image.load(f"image/image_pokedex/pokemon/{pokemon2.nom}.png")
        info_pokemon_joueur = smallfont.render(f"{pokemon1.nom} : {pokemon1.vie} pv | niv. {pokemon1.niveau}", True, (255, 255, 255))
        info_pokemon_ennemi = smallfont.render(f"{pokemon2.nom} : {pokemon2.vie} pv | niv. {pokemon2.niveau}", True, (255, 255, 255))
        

        # Si l'utilisateur ferme la fenêtre
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        # Si l'utilisateur clique sur un bouton
            if tour_joueur and event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # Effectue l'attaque choisie par le joueur et affiche les dégats ainsi que l'efficacité de l'attaque
                    if event.pos[0] > 500 and event.pos[0] < 800 and event.pos[1] > 320 and event.pos[1] < 350:                        
                        tour_joueur = False                       

                        afficher_infos(f"{pokemon1.nom} attaque {pokemon2.nom} avec {pokemon1.move1.nom} !")
                        degats = duel.attack(pokemon1, pokemon2, pokemon1.move1)

                        if duel.calculer_modifier(pokemon1, pokemon2, pokemon1.move1) == 2:
                            afficher_infos(f"C'est super efficace !")
                        elif duel.calculer_modifier(pokemon1, pokemon2, pokemon1.move1) == 0.5:
                            afficher_infos(f"C'est pas très efficace...")
                        
                        afficher_infos(f"{pokemon1.nom} inflige {degats} points de dégats")
                        duel.check_vainqueur()
                        
                    if event.pos[0] > 500 and event.pos[0] < 800 and event.pos[1] > 370 and event.pos[1] < 400:
                        tour_joueur = False

                        afficher_infos(f"{pokemon1.nom} attaque {pokemon2.nom} avec {pokemon1.move2.nom} !")
                        degats = duel.attack(pokemon1, pokemon2, pokemon1.move2)

                        if duel.calculer_modifier(pokemon1, pokemon2, pokemon1.move2) == 2:
                            afficher_infos(f"C'est super efficace !")
                        elif duel.calculer_modifier(pokemon1, pokemon2, pokemon1.move2) == 0.5:
                            afficher_infos(f"C'est pas très efficace...")

                        afficher_infos(f"{pokemon1.nom} inflige {degats} points de dégats")
                        duel.check_vainqueur()

                    # Bouton pour fuir le combat
                    if event.pos[0] > 500 and event.pos[0] < 800 and event.pos[1] > 420 and event.pos[1] < 450:
                        print ("Vous avez fuit le combat.")
                        pygame.mixer.music.stop()
                        running = False
                        exec(open("main.py").read())
        
        # Tour de l'ennemi
        if not tour_joueur:

            if duel.check_vainqueur() == pokemon1:
                pokemon1.niveau += 1
                pokemon1.vie = vie_max_joueur
                pokemon2.vie = vie_max_ennemi
                ecran_de_victoire()
                lancer_combat(pokemon1)

            elif duel.check_vainqueur() == pokemon2:
                pokemon1.vie = vie_max_joueur
                pokemon2.vie = vie_max_ennemi
                ecran_de_defaite()
                pygame.mixer.music.stop()
                menu.run()

            # L'ennemi choisit une attaque aléatoire
            moves = [pokemon2.move1, pokemon2.move2]
            choix_move = random.choice(moves)
            if choix_move == pokemon2.move1.nom:
                choix_move = pokemon2.move1
            elif choix_move == pokemon2.move2.nom:
                choix_move = pokemon2.move2

            # Effectue l'attaque choisie par l'ennemi et affiche les dégats ainsi que l'efficacité de l'attaque
            afficher_infos(f"{pokemon2.nom} attaque {pokemon1.nom} avec {choix_move.nom} !")
            degats = duel.attack(pokemon2, pokemon1, choix_move)

            if duel.calculer_modifier(pokemon2, pokemon1, choix_move) == 2:
                afficher_infos(f"C'est super efficace !")

            elif duel.calculer_modifier(pokemon2, pokemon1, choix_move) == 0.5:
                afficher_infos(f"C'est pas très efficace...")

            afficher_infos(f"{pokemon2.nom} inflige {degats} points de dégats")
            duel.check_vainqueur()

            tour_joueur = True
            pygame.event.clear() # Permet de ne pas prendre en compte les clics de l'utilisateur pendant le tour de l'ennemi et l'affichage des informations

        # Effet de hover sur les boutons
        mouse = pygame.mouse.get_pos()

        if 500 <= mouse[0] <= 750 and 310 <= mouse[1] <= 350:
            attaque1 = smallfont.render(f"{pokemon1.move1.nom}", True, (0, 0, 0))
        else:
            attaque1 = smallfont.render(f"{pokemon1.move1.nom}", True, (255, 255, 255))
        
        if 500 <= mouse[0] <= 750 and 360 <= mouse[1] <= 400:
            attaque2 = smallfont.render(f"{pokemon1.move2.nom}", True, (0, 0, 0))
        else:
            attaque2 = smallfont.render(f"{pokemon1.move2.nom}", True, (255, 255, 255))
        
        if 500 <= mouse[0] <= 750 and 410 <= mouse[1] <= 450:
            fuite = smallfont.render("Fuite", True, (0, 0, 0))
        else:
            fuite = smallfont.render("Fuite", True, (255, 255, 255))

        # Appliquer l'arrière-plan
        screen.blit(background, (0, 0))

        # Appliquer l'image et les infos du pokemon du joueur
        screen.blit(image_pokemon_joueur, (80, 220))        
        pygame.draw.rect(screen, (208, 199, 124), (60, 470, 370, 50))
        screen.blit(info_pokemon_joueur, (80, 475))

        # Appliquer l'image et les infos du pokemon de l'ennemi
        screen.blit(image_pokemon_ennemi, (525, 100))    
        pygame.draw.rect(screen, (208, 199, 124), (475, 10, 370, 50))
        screen.blit(info_pokemon_ennemi, (500, 20))

        #Appliquer les boutons
        pygame.draw.rect(screen, (208, 199, 124), (475, 300, 350, 200))
        if tour_joueur == True:  
            screen.blit(attaque1, (500, 320))
            screen.blit(attaque2, (500, 370))
            screen.blit(fuite, (500, 420))


        # Mettre à jour l'écran
        pygame.display.flip()

       
# Fonction affichant un texte sur une surface donnée
def drawText(surface, text, color, rect, font, aa=False, bkg=None):
    rect = Rect(rect)
    y = rect.top
    lineSpacing = -2

    # get the height of the font
    fontHeight = font.size("police_ecriture.ttf")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word      
        if i < len(text): 
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]

    return text

# Fonction affichant un message pendant 2 secondes
def afficher_infos(message):
    pygame.draw.rect(screen, (208, 199, 124), (475, 300, 350, 200))
    drawText(screen, message, (255, 255, 255), (500, 320, 275, 175), smallfont)
    pygame.display.flip()
    pygame.time.delay(2000)

def ecran_de_victoire():
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 850, 531))
    message_victoire = smallfont.render(f"Vous avez gagné !", True, (255, 255, 255))
    screen.blit(message_victoire, (300, height / 2))
    pygame.display.flip()
    pygame.time.delay(5000)

def ecran_de_defaite():
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 850, 531))
    message_defaite = smallfont.render(f"Vous avez perdu...", True, (255, 255, 255))
    screen.blit(message_defaite, (300, height / 2))
    pygame.display.flip()
    pygame.time.delay(5000)

def evolution(pokemon_joueur):
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 850, 531))
    message_evolution = smallfont.render(f"{pokemon_joueur.nom} évolue en {pokemon_joueur.evolution} !", True, (255, 255, 255))
    screen.blit(message_evolution, (width/4, height / 2))
    pygame.display.flip()
    pygame.time.delay(5000)
    
    with open("pokemon_evolution.json", "r") as read_file:
        data = json.load(read_file)
    
    for pokemon in data:

        move1 = moves_dict.get(pokemon["move1"])
        move2 = moves_dict.get(pokemon["move2"])


        instance = Pokemon(
            pokemon["nom"],
            pokemon["niveau"],
            pokemon["type"],
            pokemon["vie"],
            pokemon["attaque"],
            pokemon["defense"],
            move1,
            move2,
            pokemon["evolution"],
            pokemon["numero"],
            pokemon["image"]
            )
        liste_pokemon.append(instance)

    for pokemon in liste_pokemon:
        if pokemon.nom == pokemon_joueur.evolution:
            pokemon_joueur.nom = pokemon.nom
            pokemon_joueur.niveau = pokemon.niveau
            pokemon_joueur.type = pokemon.type
            pokemon_joueur.vie = pokemon.vie
            pokemon_joueur.attaque = pokemon.attaque
            pokemon_joueur.defense = pokemon.defense
            pokemon_joueur.move1 = pokemon.move1
            pokemon_joueur.move2 = pokemon.move2
            pokemon_joueur.evolution = pokemon.evolution
            pokemon_joueur.numero = pokemon.numero
            pokemon_joueur.image = pokemon.image
            break

