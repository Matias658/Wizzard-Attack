import pygame
from config import *

class Plataforma(pygame.sprite.Sprite):
    def __init__(self, path_image:str, size:tuple, place:tuple) -> None:
        super().__init__()

        self.image = pygame.image.load(path_image).convert_alpha()
        self.image = pygame.transform.scale(self.image, size)

        self.rect = self.image.get_rect()
        self.rect.bottomleft = place

    
