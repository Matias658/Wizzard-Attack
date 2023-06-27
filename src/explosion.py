import pygame
from config import *

class Explosion(pygame.sprite.Sprite):
    def __init__(self, animaciones:list, start_place:tuple):
        super().__init__()
        
        self.animaciones = animaciones
        self.indice = 0
        self.image = self.animaciones[self.indice]


        self.rect = self.image.get_rect()
        self.rect.midbottom = start_place
        
        self.contador = 0

    def update(self):
        self.contador += 1
        if self.contador >= 5:
            self.contador = 0
            self.indice += 1
            if self.indice >= 9:
                self.kill()
                
                
        self.image = self.animaciones[self.indice]
