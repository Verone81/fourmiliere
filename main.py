import pygame
#from pygame.locals import *
from random import randint
pygame.init()

# Définir les couleurs
BLUE = (135,206,250)
BROWN = (255,140,0)
BLACK= (0, 0, 0)

# Dmension de la fenêtre
WIDTH_SCREEN= 800
HEIGHT_SCREEN = 800

# Dimension des bloc de terre
width_rect =WIDTH_SCREEN / 50
height_rect = HEIGHT_SCREEN / 50

# Position de la fourmi au hasard
random_ant_pos = randint(0, 800)
y_ant_pos = 140

screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
pygame.display.set_caption("Fourmiliere")

# Boucle jusqu'à ce que l'utilisateur clique sur le bouton de fermeture.
end = False

# Utilisé pour gérer la vitesse de rafraîchissement de l'écran.
clock = pygame.time.Clock()

# Position de départ des blocs de terre.
x = 0
y = 0

# Liste pour mettre la liste des bloc de terre.
land_bloc_list = []

# couleur de fond...
screen.fill((BLUE))

# Ouvrir le fichier texte.

with open('m.txt', 'r') as file:
    # Boucle à travers chaque ligne du fichier.
    for row in file:
        # Boucle à travers chaque sprite dans la ligne.
        for sprite in row:
            # Si le sprite est 'm', dessiner un rectangle
            if sprite == 'm':
                land_bloc = pygame.draw.rect(screen, (255,140,0), [x, y, width_rect, height_rect])
                land_bloc_list.append(land_bloc)
            # Déplacer la position x sur la droite
            x += width_rect
        # Déplacer la position y vers le bas et réinitialiser la position x
        x = 0
        y += height_rect

# Dessiner une fourmi
def draw_ant(x, y):
    ant = pygame.draw.rect(screen, (0, 0, 0), [x, y, 5, 5])
    return ant
    
# Faire creuser la fourmi
def make_ant_dig(ant, land_bloc_list):
    for land_bloc in land_bloc_list:
        if ant.colliderect(land_bloc):
            land_bloc_list.remove(land_bloc)
            pygame.draw.rect(screen, BLUE, land_bloc) # Dessiner par-dessus le bloc de terre avec la couleur de fond
            ant.y+=1
            pygame.draw.rect(screen, BLACK, ant)
            if ant.y > 770:
                break

    
ant = draw_ant(random_ant_pos, y_ant_pos)
# Boucle principale du programme
while not end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True

    
    ant = draw_ant(random_ant_pos, y_ant_pos)
    make_ant_dig(ant, land_bloc_list)
    
    # Mettre à jour l'écran
    pygame.display.update()

    # Limiter à 60 images par seconde
    clock.tick(60)

# Fermer la fenêtre et quitter.
pygame.quit()
