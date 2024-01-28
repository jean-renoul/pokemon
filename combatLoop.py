from Classes.Combat import Combat
from Classes.Pokemon import Pokemon
from globals import *
import random
import pygame
from pygame.locals import *
import json
#from choix2pokemon import *
from Classes.menu import Menu




# Initialisation de pygame
pygame.init()
pygame.display.set_caption("Combat de Pokemon")



# Charger données pokemon
with open("pokemon.json", "r") as read_file:
    data = json.load(read_file)

liste_pokemon = []

for pokemon in data:
    # On se base sur un dictionnaire des attaques dans le fichier globals, on aurait aussi pu utiliser un json, mais on avait commencé par rentrer les données
    # des attaques et des pokemons dans un fichier globals, on a donc gardé ce fichier car il fonctionne
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


def lancer_combat(pokemon_joueur1, pokemon_joueur2,):
    pygame.mixer.init()
    pygame.mixer.music.load('son/musique_combat.mp3')
    pygame.mixer.music.play(-1) # -1 signifie que la musique va boucler

    
    # Vérification du niveau du pokemon, si il est niveau 3, un écran va s'afficher pour annoncer son évolution avant le combat.
    if pokemon_joueur1.niveau == 3:
        evolution(pokemon_joueur1)
    if pokemon_joueur2.niveau == 3:
        evolution(pokemon_joueur2)

    # Ces boucles permettent de retirer les pokemons du joueur du pool de pokemons disponibles pour l'ennemi, on évite les matchs miroirs car pas intéressants.    
    for pokemon in liste_pokemon:
        if pokemon.nom == pokemon_joueur1.nom:
            liste_pokemon.remove(pokemon)
            break
    for pokemon in liste_pokemon:
        if pokemon.nom == pokemon_joueur2.nom:
            liste_pokemon.remove(pokemon)
            break

    # On choisit deux pokemons aléatoirement pour l'ennemi
    pokemon_ennemi1 = random.choice(liste_pokemon)
    pokemon_ennemi2 = random.choice(liste_pokemon)
    
    # On établit ici la vie maximale de chaque pokemon, on en aura besoin pour réinitialiser les pokemons après chaque combat
    vie_max_joueur1 = pokemon_joueur1.vie
    vie_max_joueur2 = pokemon_joueur2.vie
    vie_max_ennemi1 = pokemon_ennemi1.vie
    vie_max_ennemi2 = pokemon_ennemi2.vie

    pokemon1 = pokemon_joueur1
    pokemon2 = pokemon_ennemi1
    pokemon3 = pokemon_joueur2
    pokemon4 = pokemon_ennemi2

    # On crée une instance de la classe Combat
    combat = Combat(pokemon1, pokemon3)

    # On ajoute les pokemons au pokedex
    
    combat.ajouter_au_pokedex(pokemon_joueur1)
    combat.ajouter_au_pokedex(pokemon_joueur2)
    combat.ajouter_au_pokedex(pokemon_ennemi1)
    combat.ajouter_au_pokedex(pokemon_ennemi2)
    
    # Initialisation de la variable qui détermine si l'attaque réussit
    miss_joueur = None
    miss_ennemi = None



    running = True
    tour_joueur = True
    
    # Boucle de jeu
    while running:

        # Si le combat est terminé on réinitialise les pokemons : les pokemons du joueur reviennent dans leur ordre de départ 
        # et la vie de chaque pokemon est remise à son maximum.

        # Si le combat est gagné, le pokemon actuel du joueur gagne un niveau et un autre combat se lance dans la foulée.
        if combat.check_vainqueur(pokemon2,pokemon4) == "victoire":
            pokemon1.niveau += 1
            pokemon1 = pokemon_joueur1
            pokemon3 = pokemon_joueur2
            pokemon1.vie = vie_max_joueur1
            pokemon2.vie = vie_max_ennemi1
            pokemon3.vie = vie_max_joueur2
            pokemon4.vie = vie_max_ennemi2
            ecran_de_victoire()
            lancer_combat(pokemon1, pokemon3)

        # Si le combat est perdu, on réinitialise les pokemons et on retourne au menu principal.
        elif combat.check_vainqueur(pokemon2,pokemon4) == "défaite":
            pokemon1 = pokemon_joueur1
            pokemon3 = pokemon_joueur2
            pokemon1.vie = vie_max_joueur1
            pokemon2.vie = vie_max_ennemi1
            pokemon3.vie = vie_max_joueur2
            pokemon4.vie = vie_max_ennemi2
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
                combat.vider_pokedex()
                running = False
                pygame.quit()

        # Si l'utilisateur clique sur un bouton
            if tour_joueur and event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # Effectue l'attaque choisie par le joueur
                    if event.pos[0] > 500 and event.pos[0] < 800 and event.pos[1] > 320 and event.pos[1] < 350:              
                        tour_joueur = False

                        afficher_infos(f"{pokemon1.nom} attaque {pokemon2.nom} avec {pokemon1.move1.nom} !")

                        # On détermine si l'attaque réussit ou non, les chances de rater sont de 20% et on empêche le joueur de rater 2 fois de suite 
                        # pour éviter la frustration de rater en boucle.
                        if miss_joueur == 1:
                            miss_joueur = 2
                        else:
                            miss_joueur = random.randint(1,5)
                            if miss_joueur == 1:
                                afficher_infos(f"{pokemon1.nom} rate son attaque !")
                            else:
                                # Si l'attaque réussit on appelle la méthode de calculs des dégats et on affiche les dégats ainsi que l'efficacité de l'attaque                            
                                degats = combat.attack(pokemon1, pokemon2, pokemon1.move1)
                                if combat.calculer_modifier(pokemon2, pokemon1.move1) == 2:
                                    afficher_infos(f"C'est super efficace !")
                                elif combat.calculer_modifier(pokemon2, pokemon1.move1) == 0.5:
                                    afficher_infos(f"C'est pas très efficace...")                                
                                afficher_infos(f"{pokemon1.nom} inflige {degats} points de dégats")

                                # On vérifie si le combat est terminé, et si le pokemon ennemi est KO, on le remplace par le deuxième pokemon ennemi.
                                combat.check_vainqueur(pokemon2,pokemon4)
                                if pokemon2.vie <= 0:
                                    afficher_infos(f"{pokemon2.nom} est KO !, {pokemon4.nom} prends sa place !")
                                    pokemon2, pokemon4 = pokemon4, pokemon2
                                                   
                    # Même chose que précédemment mais pour la deuxième attaque du pokemon   
                    if event.pos[0] > 500 and event.pos[0] < 800 and event.pos[1] > 370 and event.pos[1] < 400:
                        tour_joueur = False

                        afficher_infos(f"{pokemon1.nom} attaque {pokemon2.nom} avec {pokemon1.move2.nom} !")

                        if miss_joueur == 1:
                            miss_joueur = 2
                        else:
                            miss_joueur = random.randint(1,5)
                            if miss_joueur == 1:
                                afficher_infos(f"{pokemon1.nom} rate son attaque !")
                            else:

                                degats = combat.attack(pokemon1, pokemon2, pokemon1.move2)
                                if combat.calculer_modifier(pokemon2, pokemon1.move2) == 2:
                                    afficher_infos(f"C'est super efficace !")
                                elif combat.calculer_modifier(pokemon2, pokemon1.move2) == 0.5:
                                    afficher_infos(f"C'est pas très efficace...")
                                afficher_infos(f"{pokemon1.nom} inflige {degats} points de dégats")

                                combat.check_vainqueur(pokemon2,pokemon4)
                                if pokemon2.vie <= 0:
                                    afficher_infos(f"{pokemon2.nom} est KO !, {pokemon4.nom} prends sa place !")
                                    pokemon2, pokemon4 = pokemon4, pokemon2
                                                    
                    # Bouton pour changer de pokemon, on vérifie si le pokemon est KO avant de le changer.
                    if event.pos[0] > 500 and event.pos[0] < 800 and event.pos[1] > 420 and event.pos[1] < 450:
                        if pokemon3.vie <= 0:
                            afficher_infos(f"{pokemon3.nom} est KO, vous ne pouvez pas le sélectionner.")
                            break
                        tour_joueur = False
                        afficher_infos(f"{pokemon1.nom} reviens ! {pokemon3.nom} à toi !")
                        pokemon1, pokemon3 = pokemon3, pokemon1
                        

                    # Bouton pour fuir le combat, nous fait revenir au menu principal
                    if event.pos[0] > 500 and event.pos[0] < 800 and event.pos[1] > 470 and event.pos[1] < 520:
                        print ("Vous avez fuit le combat.")
                        pygame.mixer.music.stop()
                        running = False
                        # J'utilise la fonction exec pour relancer le menu principal, car le jeu plantait si on fuyait plusieurs fois de suite.
                        exec(open("main.py").read())
        
        # Tour de l'ennemi
        if not tour_joueur:

            if combat.check_vainqueur(pokemon2,pokemon4) == "victoire":
                pokemon1.niveau += 1
                pokemon1 = pokemon_joueur1
                pokemon3 = pokemon_joueur2
                pokemon1.vie = vie_max_joueur1
                pokemon2.vie = vie_max_ennemi1
                pokemon3.vie = vie_max_joueur2
                pokemon4.vie = vie_max_ennemi2
                ecran_de_victoire()
                lancer_combat(pokemon1, pokemon3)

            elif combat.check_vainqueur(pokemon2,pokemon4) == "défaite":
                pokemon1 = pokemon_joueur1
                pokemon3 = pokemon_joueur2
                pokemon1.vie = vie_max_joueur1
                pokemon2.vie = vie_max_ennemi1
                pokemon3.vie = vie_max_joueur2
                pokemon4.vie = vie_max_ennemi2
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

            # Effectue l'attaque choisie par l'ennemi.
            
            afficher_infos(f"{pokemon2.nom} attaque {pokemon1.nom} avec {choix_move.nom} !")

            if miss_ennemi == 1:
                miss_ennemi = 2
            else:
                miss_ennemi = random.randint(1,5)
                if miss_ennemi == 1:
                    afficher_infos(f"{pokemon2.nom} rate son attaque !")
                else:

                    degats = combat.attack(pokemon2, pokemon1, choix_move)
                    if combat.calculer_modifier(pokemon1, choix_move) == 2:
                        afficher_infos(f"C'est super efficace !")
                    elif combat.calculer_modifier(pokemon1, choix_move) == 0.5:
                        afficher_infos(f"C'est pas très efficace...")
                    afficher_infos(f"{pokemon2.nom} inflige {degats} points de dégats")

                    if pokemon1.vie <= 0:
                        combat.check_vainqueur(pokemon2,pokemon4)
                        afficher_infos(f"{pokemon1.nom} est KO !, {pokemon3.nom} prends sa place !")
                        pokemon1, pokemon3 = pokemon3, pokemon1
                            
            # On repasse au tour du joueur
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
            changer_pokemon = smallfont.render("Changer de pokemon", True, (0, 0, 0))
        else:
            changer_pokemon = smallfont.render("Changer de pokemon", True, (255, 255, 255))

        if 500 <= mouse[0] <= 750 and 460 <= mouse[1] <= 500:
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
            screen.blit(changer_pokemon, (500, 420))
            screen.blit(fuite, (500, 470))


        # Mettre à jour l'écran
        pygame.display.flip()

       
# Fonction affichant un texte sur une surface donnée
def drawText(surface, text, color, rect, font, aa=False, bkg=None):
    rect = Rect(rect)
    y = rect.top
    lineSpacing = -2

    fontHeight = font.size("police_ecriture.ttf")[1]

    while text:
        i = 1

        if y + fontHeight > rect.bottom:
            break

        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1
     
        if i < len(text): 
            i = text.rfind(" ", 0, i) + 1

        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing

        text = text[i:]

    return text

# Fonction affichant un message pendant 2 secondes
def afficher_infos(message):
    pygame.draw.rect(screen, (208, 199, 124), (475, 300, 350, 200))
    drawText(screen, message, (255, 255, 255), (500, 320, 275, 175), smallfont)
    pygame.display.flip()
    pygame.time.delay(2000)

# Fonctions affichant un écran de victoire
def ecran_de_victoire():
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 850, 531))
    message_victoire = smallfont.render(f"Vous avez gagné !", True, (255, 255, 255))
    screen.blit(message_victoire, (300, height / 2))
    pygame.display.flip()
    pygame.time.delay(5000)

# Fonctions affichant un écran de défaite
def ecran_de_defaite():
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 850, 531))
    message_defaite = smallfont.render(f"Vous avez perdu...", True, (255, 255, 255))
    screen.blit(message_defaite, (300, height / 2))
    pygame.display.flip()
    pygame.time.delay(5000)

# Fonction gérant l'évolution du pokemon et affichant un écran d'évolution
def evolution(pokemon_joueur):
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 850, 531))
    message_evolution = smallfont.render(f"{pokemon_joueur.nom} évolue en {pokemon_joueur.evolution} !", True, (255, 255, 255))
    screen.blit(message_evolution, (width/4, height / 2))
    pygame.display.flip()
    pygame.time.delay(5000)
    
    # On charge les données du fichier pokemon_evolution.json, qui contient les données des pokemons évolués séparés des pokemons de base.
    # On cherche le pokemon évolué correspondant au pokemon du joueur, et on remplace les données du pokemon du joueur par celles du pokemon évolué.
    # On ajoute les pokemons évolués au pool de pokemons disponibles pour l'ennemi.
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
