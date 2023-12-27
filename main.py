import pygame
from pygame.locals import *
from random import randint

pygame.init()

# Définir les couleurs
BLUE = (135,206,250)
BROWN = (255,140,0)
BLACK = (0, 0, 0)

# Dmension de la fenêtre
WIDTH_SCREEN = 800
HEIGHT_SCREEN = 800

# Dimension des bloc de terre
width_rect = WIDTH_SCREEN / 50
height_rect = HEIGHT_SCREEN / 50

# Liste pour mettre la liste des bloc de terre
land_bloc_list = []

random_ant_x = randint(0, 800)
ant_pos_y = 140

screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
pygame.display.set_caption("Fourmiliere")

# Boucle jusqu'à ce que l'utilisateur clique sur le bouton de fermeture
end = False

# Utilisé pour gérer la vitesse de rafraîchissement de l'écran
clock = pygame.time.Clock()

# Position et taille du rectangle
x = 0
y = 0

# couleur de fond
screen.fill((BLUE))

# Ouvrir le fichier texte
with open('m.txt', 'r') as file:
    # Boucle à travers chaque ligne du fichier
    for row in file:
        # Boucle à travers chaque sprite dans la ligne
        for sprite in row:
            # Si le sprite est 'm', dessiner un rectangle
            if sprite == 'm':
                land_bloc = pygame.draw.rect(screen, BROWN, [x, y, width_rect, height_rect])
                land_bloc_list.append(land_bloc)
            # Déplacer la position x sur la droite
            x += width_rect

        # Déplacer la position y vers le bas et réinitialiser la position x
        x = 0
        y += height_rect

def draw_ant(x, y):
    ant = pygame.draw.rect(screen, BLACK, [x, y, 5, 5])
    return ant


# faire creuser la fourmi
def dig_ant(ant, land_bloc_list):
    for land_bloc in land_bloc_list:
        if ant.colliderect(land_bloc):
            pygame.draw.rect(screen, BLUE, land_bloc)


# Boucle principale du programme
while not end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True

    ant = draw_ant(random_ant_x, ant_pos_y)
    if ant_pos_y < 700 and random_ant_x < 700 and random_ant_x > 100:
        ant_pos_y+=1
        random_ant_x-=1
    elif random_ant_x == 99:
        random_ant_x -= 1
        ant_pos_y+=1
    dig_ant(ant, land_bloc_list)
    
    # Mettre à jour l'écran
    pygame.display.update()

    # Limiter à 60 images par seconde
    clock.tick(60)

# Fermer la fenêtre et quitter.
pygame.quit()
