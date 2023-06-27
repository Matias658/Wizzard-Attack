import pygame
from config import *

class Life_bar(pygame.sprite.Sprite):
    def __init__(self, animaciones:list, start_place:tuple, sound):
        super().__init__()
        self.sound = pygame.mixer.Sound(sound)
        self.life_bar = LIFE_PJ
        
        self.animaciones = animaciones
        self.indice = 0
        self.image = self.animaciones[self.indice]

        self.rect = self.image.get_rect()
        self.rect.midright = start_place
        
        self.contador = 0
        self.flag_vida = False
        self.flag_sound = True
        self.quieto = False

    def update(self):

        if self.life_bar == 3:
            self.indice = 0
        elif self.life_bar == 2:
            self.indice = 1
        elif self.life_bar == 1:
            self.indice = 2
        elif self.life_bar == 0:
            self.indice = 3
        
        if self.life_bar > 3:
            self.life_bar = LIFE_PJ
        
        if self.life_bar <= 0:
            if self.flag_sound:
                self.sound.play()
                self.flag_sound = False
            self.contador += 1
            self.quieto = True
            if self.contador > 200:
                self.flag_vida = True
        self.image = self.animaciones[self.indice]
                 
            