import pygame

#Pantalla
WIDTH = 1500
HEIGHT = 800
PANTALLA = (WIDTH, HEIGHT)
ORIGIN = (0,0)
CENTER = (WIDTH // 2, HEIGHT // 2)
DISPLAY = (WIDTH, HEIGHT)
DISPLAY_CENTER_X = WIDTH // 2
DISPLAY_CENTER_Y = HEIGHT // 2
DISPLAY_TOP = 0
DISPLAY_BOTTOM = HEIGHT
DISPLAY_PLAY = (DISPLAY_CENTER_X, DISPLAY_TOP + 150)
DISPLAY_TEXTO = (DISPLAY_CENTER_X, DISPLAY_BOTTOM)
DISPLAY_SCORE = (60, 40)
DISPLAY_SCORE_2 = (DISPLAY_CENTER_X, DISPLAY_CENTER_Y // 1.5)
DISPLAY_MESSAGE = (DISPLAY_CENTER_X, DISPLAY_CENTER_Y)
DISPLAY_LIFE = (WIDTH - 20, 40)
DISPLAY_WAVE = (DISPLAY_CENTER_X, DISPLAY_CENTER_Y // 1.5)
DISPLAY_WORD = (DISPLAY_CENTER_X, DISPLAY_CENTER_Y // 1.9)
SIZE_ICON = (128,128)
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))

CHARGE_TIME = 300
#Caracteristicas
#PJ
PLACE_PJ = (DISPLAY_CENTER_X, HEIGHT - (HEIGHT // 6))
SIZE_PJ = (128,128)
LIFE_PJ = 3
SPEED_PJ = 5
BOOST = 10
JUMP = 5
GRAVITY = 1
GLIDE = 1
MAX_HEIGHT_JUMP = -300
SPEED_FIREBOLT = 15
SIZE_FIREBOLT = (84,60)
COOLDOWN = 40
SIZE_EFFECTS = (256, 38)
#Koloss
SIZE_KOLOSS = (166,248)
SPEED_KOLOSS = 3
MAX_KOLOSS = 3
MAX_KOLOSS_2 = 4
MAX_KOLOSS_3 = 6
#Liche
SIZE_LICHE = (122,93)
SPEED_LICHE = 7
MAX_LICHE = 4
MAX_LICHE_2 = 5
MAX_LICHE_3 = 8
#Plataformas
PLACE_PLATAFORMA_PRINCIPAL = (0 ,DISPLAY_BOTTOM)
PLACE_PLATAFORMA_LEFT = (WIDTH // 10, HEIGHT // 2)
PLACE_PLATAFORMA_RIGHT = (WIDTH // 1.5, HEIGHT // 2.5)
SIZE_PLATAFORMA_PRINCIPAL = (WIDTH, HEIGHT // 5)
SIZE_PLATAFORMA = (256, 100)
#Score-Oleadas
SCORE_KOLOSS = 250
SCORE_LICHE = 375
SCORE_COIN = 500
SCORE_COLISION = -700
SCORE_WAVE = 1250
WAVE_ONE = 10
WAVE_TWO = 25
WAVE_THREE = 40
SCORE_MIN = 25000
#Item
SIZE_LIFE_BAR = (164,64)
SIZE_ITEM_CORAZON = (64,64)
SIZE_ITEM_CORAZON_2 = (84,84)
SIZE_COIN = (64,64)
SIZE_POWERUP = (64,64)
SIZE_EXPLOTION = (128,128)
PROBABILITY_COIN = ((2,7))
PROBABILITY_POWERUP = 3
PROBABILITY_CORAZON = 5
ITEMS_GRAVITY = 6
DESPAWN = 500
#Colores
ROJO = (255, 0,0)
BORDO = (92, 16, 16)
VERDE  = (0, 255, 0)
AZUL = (0, 0, 255)
CELESTE = (69, 128, 207)
CIAN = (128, 255, 255)
BLANCO = (255, 255, 255)
GRIS = (58, 58, 58)
