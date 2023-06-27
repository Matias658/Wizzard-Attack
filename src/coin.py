import pygame
from config import *

class Coin(pygame.sprite.Sprite):
    def __init__(self, animaciones:list, start_place:tuple):
        super().__init__()
        
        self.animaciones = animaciones
        self.indice = 0
        self.image = self.animaciones[self.indice]


        self.rect = self.image.get_rect()
        self.rect.midbottom = start_place
        
        self.contador = 0
        self.contador_despawn = 0
        self.velocidad_Y = ITEMS_GRAVITY

    def update(self):
        self.rect.y += self.velocidad_Y
        if self.rect.bottom >= HEIGHT - (HEIGHT // 6):
            self.velocidad_Y = 0
            
        self.contador += 1
        if self.contador >= 5:
            self.contador = 0
            self.indice += 1
            if self.indice >= 6:
                self.indice = 0

        self.image = self.animaciones[self.indice]

        self.contador_despawn += 1
        if self.contador_despawn >= DESPAWN:
            self.kill()