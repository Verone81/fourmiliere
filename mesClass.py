import pygame
from pygame.locals import *
list_fourmi = []
list_terre = []
list_global = []

def terre(surface, x, y, largeur, hauteur):
    bloc = pygame.draw.rect(surface, (255,140,0), [x, y, largeur, hauteur])
    return list_terre.append(bloc)
   


        

class fourmi():
    def __init__(self, surface, x, y, largeur, hauteur):
        self.surface = surface
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        pygame.draw.rect(surface, (0, 0, 0), [x, y, largeur, hauteur])
class fourmiDig(fourmi):
    def __init__(self):
        for fourmi in terre:
            if fourmi.colliderect(terre):
                pygame.draw.rect(self.surface,(255,0, 0), self.x, self.y, self.largeur, self.hauteur  )


          
