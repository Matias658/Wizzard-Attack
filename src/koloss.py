import pygame
from config import *

class Koloss(pygame.sprite.Sprite):
    def __init__(self, animaciones:list, start_place:tuple):
        super().__init__()
        
        self.animaciones = animaciones
        self.indice = 0
        self.image = self.animaciones[self.indice]

        self.rect = self.image.get_rect()
        self.rect.midbottom = start_place
        
        self.velocidad_X = SPEED_KOLOSS

        self.contador = 0

        self.direction = None
        self.muerte = False
    
    def update(self):
        self.rect.x += self.velocidad_X
        if self.rect.right > WIDTH:
            self.velocidad_X = -SPEED_KOLOSS
        elif self.rect.x < 0:
            self.velocidad_X = SPEED_KOLOSS
            pass
        else:
            if self.rect.left <= 0:
                self.rect.left = 0
                self.velocidad_X = SPEED_KOLOSS
            elif self.rect.right >= WIDTH:
                self.rect.right = WIDTH
                self.velocidad_X = -SPEED_KOLOSS
                self.indice = 0
       
        #Movimiento Derecha
        if self.velocidad_X > 0:
            self.direction = True
            self.contador += 1
            if self.contador >= 10:
                self.contador = 0
                self.indice += 1
                if self.indice >= 4:
                    self.indice = 0
        #Movimiento Izquierda
        elif self.velocidad_X < 0:
            self.direction = False
            if self.indice == 0:
                self.indice = 4
            else:
                self.contador += 1
                if self.contador >= 10:
                    self.contador = 0
                    self.indice += 1
                    if self.indice >= 8:
                        self.indice = 4

        self.image = self.animaciones[self.indice]
                 
            