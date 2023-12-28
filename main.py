import pygame
from classes import *
from random import randint
# Initiliser pygame
pygame.init()

# Definir les couleurs
BLUE = (135,206,250)
BROWN = (255,140,0)
BLACK = (0, 0, 0)

# Dimension de la fenetre
WIDTH_SCREEN, HEIGHT_SCREEN = 800, 800

# Nommer et afficher l'ecran
screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
pygame.display.set_caption("Fourmiliere")

# Couleur de fond
screen.fill((BLUE))

# Variable de position des blocs de terre
xx = 0
yy = 0 

# variable pour la position des fourmi 
fourmi_xx = randint(100, 700)
fourmi_yy = 9 * 16 - 5

# fabrication des blocs de terre
with  open("m.txt", "r") as fichier:
    for ligne in fichier:
        for sprite in ligne:
            if sprite == "m":
                _bloc_terre = bloc_terre(xx, yy)
                liste_bloc_terre.add(_bloc_terre)
                liste_globale_sprites.add(_bloc_terre)
            xx += 1
        xx = 0
        yy += 1
_fourmi = fourmi(fourmi_xx,fourmi_yy )
liste_fourmi.add(_fourmi)
liste_globale_sprites.add(_fourmi)
# Boucle jusqu'a ce que l'utilisateur clique sur le bouton de fermeture
end = False

# Utiliser pour gerer la vitesse de rafraichissement de l'ecran
clock = pygame.time.Clock()

# Boucle principale du programme
while not end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True
    # Mettre a jour et dessiner la fourmiliere
    
    liste_globale_sprites.update()
    screen.fill(BLUE)
    liste_globale_sprites.draw(screen)
    
    # Rafraichir l'ecran
    pygame.display.update()

    # Limiter à 60 images par seconde
    clock.tick(60)

# Fermer la fenêtre et quitter.
pygame.quit()
