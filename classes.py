import pygame
from pygame.locals import *

liste_bloc_terre = pygame.sprite.Group()
liste_globale_sprites = pygame.sprite.Group()
liste_fourmi = pygame.sprite.Group()
class bloc_terre(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((16, 16))  # Taille du sprite
        self.image.fill((255,140,0))  # Couleur du sprite (rouge dans cet exemple)
        self.rect = self.image.get_rect()
        self.rect.x = x * 16
        self.rect.y = y * 16

class fourmi(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5, 5))
        self.image.fill((0, 0, 0))
        self.rect =self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        if self.rect.y < 700 and self.rect.x < 700 and self.rect.x > 100:
            self.rect.y +=1
            self.rect.x-=1

        creuser_terre = pygame.sprite.spritecollide(self, liste_bloc_terre, False)
        for bloc in creuser_terre:
            bloc.kill()
            
                
        
        
