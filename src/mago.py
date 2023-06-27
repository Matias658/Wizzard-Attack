import pygame
from firebolt import Firebolt
from config import *

class Mago(pygame.sprite.Sprite):
    def __init__(self, animaciones:list, start_place:tuple):
        super().__init__()
        
        self.animaciones = animaciones
        self.indice = 0
        self.image = self.animaciones[self.indice]

        self.rect = self.image.get_rect()
        self.rect.midbottom = start_place
        
        self.velocidad_X = 0
        self.velocidad_Y = 0

        self.contador_powerup = 0
        self.distancia_salto = 0
        self.contador = 0
        self.puede_saltar = True
        self.planeo = False
        self.direction = True
        self.accion = False
        self.activate = False
        self.muerto = False
    
    def update(self):
        self.rect.x += self.velocidad_X
        self.rect.y += self.velocidad_Y
        if self.rect.left <= 0:
            self.rect.left = 0
        elif self.rect.right >= WIDTH:
            self.rect.right = WIDTH
        # elif self.rect.top <= 0:
        #     self.rect.top = 0

        self.distancia_salto += self.velocidad_Y
        # print(self.distancia_salto)
        if self.distancia_salto <= MAX_HEIGHT_JUMP:
            self.distancia_salto = 0

        #Quieto Derecha
        if self.velocidad_X == 0 and self.accion == False:
            if self.direction:
                self.contador += 1
                if self.puede_saltar == False:  #Salto
                    if self.indice == 0:
                        self.indice = 14
                    elif self.contador >= 8:
                        self.contador = 0
                        self.indice += 1
                        if self.indice >= 17:
                            self.indice = 14
                elif self.contador >= 8:
                    self.contador = 0
                    self.indice += 1
                    if self.indice >= 3:
                        self.indice = 0
            else:   #Quieto Izquierda
                if self.puede_saltar == False:  #Salto
                    self.contador += 1
                    if self.indice == 0:
                        self.indice = 17
                    if self.contador >= 8:
                        self.contador = 0
                        self.indice += 1
                        if self.indice >= 20:
                            self.indice = 17
                elif self.indice == 0:
                    self.indice = 3
                else:
                    self.contador += 1
                    if self.contador >= 8:
                        self.contador = 0
                        self.indice += 1
                        if self.indice >= 6:
                            self.indice = 3
        #Movimiento Derecha
        elif self.velocidad_X > 0:
            self.direction = True
            if self.puede_saltar == False:  #Salto
                self.contador += 1
                if self.indice == 0:
                    self.indice = 14
                if self.contador >= 8:
                    self.contador = 0
                    self.indice += 1
                    if self.indice >= 17:
                        self.indice = 14
            elif self.indice == 0:
                self.indice = 6
            else:
                self.contador += 1
                if self.contador >= 10:
                    self.contador = 0
                    self.indice += 1
                    if self.indice >= 10:
                        self.indice = 6
        #Movimiento Izquierda
        elif self.velocidad_X < 0:
            self.direction = False
            if self.puede_saltar == False:  #Salto
                self.contador += 1
                if self.indice == 0:
                    self.indice = 17
                if self.contador >= 8:
                    self.contador = 0
                    self.indice += 1
                    if self.indice >= 20:
                        self.indice = 17
            elif self.indice == 0:
                self.indice = 10
            else:
                self.contador += 1
                if self.contador >= 10:
                    self.contador = 0
                    self.indice += 1
                    if self.indice >= 14:
                        self.indice = 10

        if self.muerto:
            if self.indice >= 0 and self.indice < 22:
                self.indice = 22
            self.contador += 1
            if self.contador >= 5:
                self.contador = 0
                self.indice += 1
                if self.indice >= 28:
                    self.indice = 28

        self.image = self.animaciones[self.indice]
        
        if self.activate:
            self.contador_powerup += 1
            if self.contador_powerup >= 300:
                self.activate = False
                self.contador_powerup = 0

    def disparar(self, animaciones, sound, speed, sprites, firebolts, direction):
        self.accion = True
        if direction == 1073741903:
            direction = True    #Disparo a la derecha
            self.direction = True
            firebolt = Firebolt(animaciones, self.rect.midright, speed, direction)
            self.indice = 20
            firebolt.indice = 0
        elif direction == 1073741904:
            direction = False   #Disparo a la izquierda 
            self.direction = False
            firebolt = Firebolt(animaciones, self.rect.midleft, speed, direction)
            self.indice = 21
            firebolt.indice = 0
            
        sound = pygame.mixer.Sound(sound)
        sound.set_volume(0.5)
        sound.play()
        sprites.add(firebolt)
        firebolts.add(firebolt)           
     