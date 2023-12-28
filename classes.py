import pygame

liste_bloc_terre = pygame.sprite.Group()
liste_globale_sprites = pygame.sprite.Group()

class bloc_terre(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((16, 16))  # Taille du sprite
        self.image.fill((255,140,0))  # Couleur du sprite (rouge dans cet exemple)
        self.rect = self.image.get_rect()
        self.rect.x = x * 16
        self.rect.y = y * 16