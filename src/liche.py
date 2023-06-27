import pygame
import random
from config import *

class Liche(pygame.sprite.Sprite):
    def __init__(self, animaciones:list, start_place:tuple):
        super().__init__()
        
        self.animaciones = animaciones
        self.indice = 0
        self.image = self.animaciones[self.indice]

        self.rect = self.image.get_rect()
        self.rect.midbottom = start_place
        
        self.velocidad_X = SPEED_LICHE
        self.velocidad_Y = 0

        self.contador = 0

        self.direction = None
    
    def update(self):
        self.rect.x += self.velocidad_X
        self.rect.y += self.velocidad_Y
        if self.rect.right > WIDTH:
            self.velocidad_X = -SPEED_LICHE
        elif self.rect.x < 0:
            self.velocidad_X = SPEED_LICHE
            pass
        else:
            posicion_random = random.choice([-7, 7])
            if self.rect.left <= 0:
                self.rect.left = 0
                self.velocidad_X = SPEED_LICHE
                self.velocidad_Y = posicion_random
            elif self.rect.right >= WIDTH:
                self.rect.right = WIDTH
                self.velocidad_X = -SPEED_LICHE
                self.velocidad_Y = posicion_random
                self.indice = 0
            elif self.rect.top <= 0:
                self.rect.top = 0
                self.velocidad_Y = SPEED_LICHE
                self.velocidad_X = posicion_random
            elif self.rect.bottom >= HEIGHT - (HEIGHT // 6):
                self.rect.bottom = HEIGHT - (HEIGHT // 6)
                self.velocidad_Y = -SPEED_LICHE
                self.velocidad_X = posicion_random
            
        #Movimiento Derecha
        if self.velocidad_X > 0:
            self.direction = True
            self.contador += 1
            if self.contador >= 10:
                self.contador = 0
                self.indice += 1
                if self.indice >= 10:
                    self.indice = 0
        #Movimiento Izquierda
        elif self.velocidad_X < 0:
            self.direction = False
            if self.indice < 10:
                self.indice = 10
            else:
                self.contador += 1
                if self.contador >= 10:
                    self.contador = 0
                    self.indice += 1
                    if self.indice >= 20:
                        self.indice = 10

        self.image = self.animaciones[self.indice]
                 
            