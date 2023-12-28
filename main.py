import pygame
from pygame.locals import *
from random import randint
from mesClass import *

pygame.init()

# Définir les couleurs
BLUE = (135,206,250)
BROWN = (255,140,0)
BLACK = (0, 0, 0)

# Dmension de la fenêtre
WIDTH_SCREEN = 800
HEIGHT_SCREEN = 800

fenetre = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
pygame.display.set_caption("Fourmiliere")

# Boucle jusqu'à ce que l'utilisateur clique sur le bouton de fermeture
end = False

# Utilisé pour gérer la vitesse de rafraîchissement de l'écran
clock = pygame.time.Clock()

# Position du bloc de terre de depart
x = 0
y = 200

# Position de départ des fourmis
pos_xx_fourmi = randint(100, 700)
pos_yy_fourmi = 195

# couleur de fond
fenetre.fill((BLUE))

for i in range(595):
    for j in range(800):
        list_terre = terre(fenetre, x, y, 1, 1)
        x += 1
    x = 0
    y += 1
    
fourmi(fenetre, pos_xx_fourmi, pos_yy_fourmi, 5, 5)
fourmiDig()
# Boucle principale du programme
while not end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True
    
    # Mettre à jour l'écran
    pygame.display.update()

    # Limiter à 60 images par seconde
    clock.tick(60)

# Fermer la fenêtre et quitter.
pygame.quit()
