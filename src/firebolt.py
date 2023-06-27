import pygame

class Firebolt(pygame.sprite.Sprite):
    def __init__(self, animaciones:str, center:tuple, speed:int, direction):
        super().__init__()  #llama al constructor del padre
        
        self.animaciones = animaciones
        self.indice = 0
        self.image = self.animaciones[self.indice]


        self.rect = self.image.get_rect()
        self.rect.center = center

        self.velocidad_X = speed
        self.velocidad_Y = speed
        
        self.flag_lado = direction
        self.contador = 0

        

    def update(self):
        # print(self.flag_lado)
        if self.flag_lado:
            self.rect.x += self.velocidad_X
            self.contador += 1
            if self.contador >= 5:
                self.contador = 0
                self.indice += 1
                if self.indice >= 3:
                    self.indice = 0
        else:
            self.rect.x -= self.velocidad_X
            if self.indice == 0:
                self.indice = 3
            self.contador += 1
            if self.contador >= 5:
                self.contador = 0
                self.indice += 1
                if self.indice >= 6:
                    self.indice = 3
        self.image = self.animaciones[self.indice]
