import pygame
from config import *
#------------------------------------------------------MAGO-------------------------------------------------------------------------------------
mago_animaciones = [
               #quieto derecha 0-2
               pygame.transform.scale(pygame.image.load(r"src\images\PJ\PJ quieto\Mago 2 FUEGO1.png").convert_alpha(), (SIZE_PJ)),
               pygame.transform.scale(pygame.image.load(r"src\images\PJ\PJ quieto\Mago 2 FUEGO2.png").convert_alpha(), (SIZE_PJ)),
               pygame.transform.scale(pygame.image.load(r"src\images\PJ\PJ quieto\Mago 2 FUEGO3.png").convert_alpha(), (SIZE_PJ)),
               #quieto izquierda 3-5
               pygame.transform.scale(pygame.image.load(r"src\images\PJ\PJ quieto Izquierda\Mago quieto Izquierda1.png").convert_alpha(), (SIZE_PJ)),
               pygame.transform.scale(pygame.image.load(r"src\images\PJ\PJ quieto Izquierda\Mago quieto Izquierda2.png").convert_alpha(), (SIZE_PJ)),
               pygame.transform.scale(pygame.image.load(r"src\images\PJ\PJ quieto Izquierda\Mago quieto Izquierda3.png").convert_alpha(), (SIZE_PJ)),
               #moverse derecha 6-9
               pygame.transform.scale(pygame.image.load(r"src\images\PJ\PJ movimiento\Mago 2 Movimiento Fuego1.png").convert_alpha(), (SIZE_PJ)),
               pygame.transform.scale(pygame.image.load(r"src\images\PJ\PJ movimiento\Mago 2 Movimiento Fuego2.png").convert_alpha(), (SIZE_PJ)),
               pygame.transform.scale(pygame.image.load(r"src\images\PJ\PJ movimiento\Mago 2 Movimiento Fuego3.png").convert_alpha(), (SIZE_PJ)),
               pygame.transform.scale(pygame.image.load(r"src\images\PJ\PJ movimiento\Mago 2 Movimiento Fuego4.png").convert_alpha(), (SIZE_PJ)),
               #moverse izquierda 10-13
               pygame.transform.scale(pygame.image.load(r"src\images\PJ\PJ movimiento Izquierda\Mago 2 Movimiento Izquierda1.png").convert_alpha(), (SIZE_PJ)),
               pygame.transform.scale(pygame.image.load(r"src\images\PJ\PJ movimiento Izquierda\Mago 2 Movimiento Izquierda2.png").convert_alpha(), (SIZE_PJ)),
               pygame.transform.scale(pygame.image.load(r"src\images\PJ\PJ movimiento Izquierda\Mago 2 Movimiento Izquierda3.png").convert_alpha(), (SIZE_PJ)),
               pygame.transform.scale(pygame.image.load(r"src\images\PJ\PJ movimiento Izquierda\Mago 2 Movimiento Izquierda4.png").convert_alpha(), (SIZE_PJ)),
               #Salto Largo Derecha 14-16
               pygame.transform.scale(pygame.image.load(r"src\images\PJ\PJ Salto Prolongado Derecha\Salto Fuego Prolongado2.png").convert_alpha(), (SIZE_PJ)),
               pygame.transform.scale(pygame.image.load(r"src\images\PJ\PJ Salto Prolongado Derecha\Salto Fuego Prolongado3.png").convert_alpha(), (SIZE_PJ)),
               pygame.transform.scale(pygame.image.load(r"src\images\PJ\PJ Salto Prolongado Derecha\Salto Fuego Prolongado4.png").convert_alpha(), (SIZE_PJ)),
               #Salto Largo Izquierda 17-19
               pygame.transform.scale(pygame.image.load(r"src\images\PJ\PJ Salto Prolongado Izquierda\Salto Prolongado Izquierda 2.png").convert_alpha(), (SIZE_PJ)),
               pygame.transform.scale(pygame.image.load(r"src\images\PJ\PJ Salto Prolongado Izquierda\Salto Prolongado Izquierda 3.png").convert_alpha(), (SIZE_PJ)),
               pygame.transform.scale(pygame.image.load(r"src\images\PJ\PJ Salto Prolongado Izquierda\Salto Prolongado Izquierda 4.png").convert_alpha(), (SIZE_PJ)),
               #ataque derecha 20
               pygame.transform.scale(pygame.image.load(r"src\images\PJ\Mago Ataque Fuego.png").convert_alpha(), (SIZE_PJ)),
               #ataque izquierda 21
               pygame.transform.scale(pygame.image.load(r"src\images\PJ\Mago Ataque Izquierda.png").convert_alpha(), (SIZE_PJ)),
               #Muerte 22-28
               pygame.transform.scale(pygame.image.load(r"src\images\PJ\PJ Muerte\PJ Muerte1.png").convert_alpha(), (SIZE_PJ)),
               pygame.transform.scale(pygame.image.load(r"src\images\PJ\PJ Muerte\PJ Muerte2.png").convert_alpha(), (SIZE_PJ)),
               pygame.transform.scale(pygame.image.load(r"src\images\PJ\PJ Muerte\PJ Muerte3.png").convert_alpha(), (SIZE_PJ)),
               pygame.transform.scale(pygame.image.load(r"src\images\PJ\PJ Muerte\PJ Muerte4.png").convert_alpha(), (SIZE_PJ)),
               pygame.transform.scale(pygame.image.load(r"src\images\PJ\PJ Muerte\PJ Muerte5.png").convert_alpha(), (SIZE_PJ)),
               pygame.transform.scale(pygame.image.load(r"src\images\PJ\PJ Muerte\PJ Muerte6.png").convert_alpha(), (SIZE_PJ)),
               pygame.transform.scale(pygame.image.load(r"src\images\PJ\PJ Muerte\PJ Muerte7.png").convert_alpha(), (SIZE_PJ))]
#---------------------------------------------------------FIREBOLT--------------------------------------------------------------------------------
firebolt_animaciones = [
               #Derecha 0-2 
               pygame.transform.scale(pygame.image.load(r"src\images\PJ\Firebolt\Fuego1.png").convert_alpha(), (SIZE_FIREBOLT)),
               pygame.transform.scale(pygame.image.load(r"src\images\PJ\Firebolt\Fuego2.png").convert_alpha(), (SIZE_FIREBOLT)),
               pygame.transform.scale(pygame.image.load(r"src\images\PJ\Firebolt\Fuego3.png").convert_alpha(), (SIZE_FIREBOLT)),
               #Izquierda 3-5
               pygame.transform.scale(pygame.image.load(r"src\images\PJ\Firebolt Izquierda\Fuego Izquierda1.png").convert_alpha(), (SIZE_FIREBOLT)),
               pygame.transform.scale(pygame.image.load(r"src\images\PJ\Firebolt Izquierda\Fuego Izquierda2.png").convert_alpha(), (SIZE_FIREBOLT)),
               pygame.transform.scale(pygame.image.load(r"src\images\PJ\Firebolt Izquierda\Fuego Izquierda3.png").convert_alpha(), (SIZE_FIREBOLT))]
#---------------------------------------------------------KOLOSS--------------------------------------------------------------------------------
koloss_animaciones = [
               #Movimiento Derecha 0-3
               pygame.transform.scale(pygame.image.load(r"src\images\Enemigos\Koloss\Koloss Movimiento Derecha\Koloss Movimiento Derecha1.png").convert_alpha(), (SIZE_KOLOSS)),
               pygame.transform.scale(pygame.image.load(r"src\images\Enemigos\Koloss\Koloss Movimiento Derecha\Koloss Movimiento Derecha2.png").convert_alpha(), (SIZE_KOLOSS)),
               pygame.transform.scale(pygame.image.load(r"src\images\Enemigos\Koloss\Koloss Movimiento Derecha\Koloss Movimiento Derecha3.png").convert_alpha(), (SIZE_KOLOSS)),
               pygame.transform.scale(pygame.image.load(r"src\images\Enemigos\Koloss\Koloss Movimiento Derecha\Koloss Movimiento Derecha4.png").convert_alpha(), (SIZE_KOLOSS)),
               #Movimiento Izquierda 4-7
               pygame.transform.scale(pygame.image.load(r"src\images\Enemigos\Koloss\Koloss Movimiento Izquierda\Koloss Movimiento Izquierda1.png").convert_alpha(), (SIZE_KOLOSS)),
               pygame.transform.scale(pygame.image.load(r"src\images\Enemigos\Koloss\Koloss Movimiento Izquierda\Koloss Movimiento Izquierda2.png").convert_alpha(), (SIZE_KOLOSS)),
               pygame.transform.scale(pygame.image.load(r"src\images\Enemigos\Koloss\Koloss Movimiento Izquierda\Koloss Movimiento Izquierda3.png").convert_alpha(), (SIZE_KOLOSS)),
               pygame.transform.scale(pygame.image.load(r"src\images\Enemigos\Koloss\Koloss Movimiento Izquierda\Koloss Movimiento Izquierda4.png").convert_alpha(), (SIZE_KOLOSS))]
#---------------------------------------------------------LICHE---------------------------------------------------------------------------------
liche_animaciones = [
               #Movimeinto Derecha 0-9
               pygame.transform.scale(pygame.image.load(r"src\images\Enemigos\Liche\Liche Derecha\Liche Derecha1.png").convert_alpha(), (SIZE_LICHE)),
               pygame.transform.scale(pygame.image.load(r"src\images\Enemigos\Liche\Liche Derecha\Liche Derecha2.png").convert_alpha(), (SIZE_LICHE)),
               pygame.transform.scale(pygame.image.load(r"src\images\Enemigos\Liche\Liche Derecha\Liche Derecha3.png").convert_alpha(), (SIZE_LICHE)),
               pygame.transform.scale(pygame.image.load(r"src\images\Enemigos\Liche\Liche Derecha\Liche Derecha4.png").convert_alpha(), (SIZE_LICHE)),
               pygame.transform.scale(pygame.image.load(r"src\images\Enemigos\Liche\Liche Derecha\Liche Derecha5.png").convert_alpha(), (SIZE_LICHE)),
               pygame.transform.scale(pygame.image.load(r"src\images\Enemigos\Liche\Liche Derecha\Liche Derecha6.png").convert_alpha(), (SIZE_LICHE)),
               pygame.transform.scale(pygame.image.load(r"src\images\Enemigos\Liche\Liche Derecha\Liche Derecha7.png").convert_alpha(), (SIZE_LICHE)),
               pygame.transform.scale(pygame.image.load(r"src\images\Enemigos\Liche\Liche Derecha\Liche Derecha8.png").convert_alpha(), (SIZE_LICHE)),
               pygame.transform.scale(pygame.image.load(r"src\images\Enemigos\Liche\Liche Derecha\Liche Derecha9.png").convert_alpha(), (SIZE_LICHE)),
               pygame.transform.scale(pygame.image.load(r"src\images\Enemigos\Liche\Liche Derecha\Liche Derecha10.png").convert_alpha(), (SIZE_LICHE)),
               #Movimeinto Derecha 10-19
               pygame.transform.scale(pygame.image.load(r"src\images\Enemigos\Liche\Liche Izquierda\Liche Izquierda1.png").convert_alpha(), (SIZE_LICHE)),
               pygame.transform.scale(pygame.image.load(r"src\images\Enemigos\Liche\Liche Izquierda\Liche Izquierda2.png").convert_alpha(), (SIZE_LICHE)),
               pygame.transform.scale(pygame.image.load(r"src\images\Enemigos\Liche\Liche Izquierda\Liche Izquierda3.png").convert_alpha(), (SIZE_LICHE)),
               pygame.transform.scale(pygame.image.load(r"src\images\Enemigos\Liche\Liche Izquierda\Liche Izquierda4.png").convert_alpha(), (SIZE_LICHE)),
               pygame.transform.scale(pygame.image.load(r"src\images\Enemigos\Liche\Liche Izquierda\Liche Izquierda5.png").convert_alpha(), (SIZE_LICHE)),
               pygame.transform.scale(pygame.image.load(r"src\images\Enemigos\Liche\Liche Izquierda\Liche Izquierda6.png").convert_alpha(), (SIZE_LICHE)),
               pygame.transform.scale(pygame.image.load(r"src\images\Enemigos\Liche\Liche Izquierda\Liche Izquierda7.png").convert_alpha(), (SIZE_LICHE)),
               pygame.transform.scale(pygame.image.load(r"src\images\Enemigos\Liche\Liche Izquierda\Liche Izquierda8.png").convert_alpha(), (SIZE_LICHE)),
               pygame.transform.scale(pygame.image.load(r"src\images\Enemigos\Liche\Liche Izquierda\Liche Izquierda9.png").convert_alpha(), (SIZE_LICHE)),
               pygame.transform.scale(pygame.image.load(r"src\images\Enemigos\Liche\Liche Izquierda\Liche Izquierda10.png").convert_alpha(), (SIZE_LICHE))]
#---------------------------------------------------------BARRA DE VIDA----------------------------------------------------------------------------
barra_vida_animaciones = [
               #Vida completa 0
               pygame.transform.scale(pygame.image.load(r"src\images\ITEMS\Barra De Vida\Barra De Vida1.png").convert_alpha(), (SIZE_LIFE_BAR)),
               #Vida 2 corazones 1
               pygame.transform.scale(pygame.image.load(r"src\images\ITEMS\Barra De Vida\Barra De Vida2.png").convert_alpha(), (SIZE_LIFE_BAR)),
               #Vida 1 corazon 2
               pygame.transform.scale(pygame.image.load(r"src\images\ITEMS\Barra De Vida\Barra De Vida3.png").convert_alpha(), (SIZE_LIFE_BAR)),
               #Vida vacía 3
               pygame.transform.scale(pygame.image.load(r"src\images\ITEMS\Barra De Vida\Barra De Vida4.png").convert_alpha(), (SIZE_LIFE_BAR))]
#-------------------------------------------------------------CORAZON-------------------------------------------------------------------------------
corazon_animacion = [
               #Vida completa 0
               pygame.transform.scale(pygame.image.load(r"src\images\ITEMS\Corazon.png").convert_alpha(), (SIZE_ITEM_CORAZON)),
               #Vida 2 corazones 1
               pygame.transform.scale(pygame.image.load(r"src\images\ITEMS\Corazon.png").convert_alpha(), (SIZE_ITEM_CORAZON_2)),]
#--------------------------------------------------------------COIN-------------------------------------------------------------------------------
coin_animacion = [
               #Movimiento 0-5
               pygame.transform.scale(pygame.image.load(r"src\images\ITEMS\Coin\Coin1.png").convert_alpha(), (SIZE_COIN)),
               pygame.transform.scale(pygame.image.load(r"src\images\ITEMS\Coin\Coin2.png").convert_alpha(), (SIZE_COIN)),
               pygame.transform.scale(pygame.image.load(r"src\images\ITEMS\Coin\Coin3.png").convert_alpha(), (SIZE_COIN)),
               pygame.transform.scale(pygame.image.load(r"src\images\ITEMS\Coin\Coin4.png").convert_alpha(), (SIZE_COIN)),
               pygame.transform.scale(pygame.image.load(r"src\images\ITEMS\Coin\Coin5.png").convert_alpha(), (SIZE_COIN)),
               pygame.transform.scale(pygame.image.load(r"src\images\ITEMS\Coin\Coin6.png").convert_alpha(), (SIZE_COIN))]
#--------------------------------------------------------------POWER UP-------------------------------------------------------------------------------
powerup_animacion = [
               #Movimiento 0-11
               pygame.transform.scale(pygame.image.load(r"src\images\ITEMS\Powerup\Powerup1.png").convert_alpha(), (SIZE_POWERUP)),
               pygame.transform.scale(pygame.image.load(r"src\images\ITEMS\Powerup\Powerup2.png").convert_alpha(), (SIZE_POWERUP)),
               pygame.transform.scale(pygame.image.load(r"src\images\ITEMS\Powerup\Powerup3.png").convert_alpha(), (SIZE_POWERUP)),
               pygame.transform.scale(pygame.image.load(r"src\images\ITEMS\Powerup\Powerup4.png").convert_alpha(), (SIZE_POWERUP)),
               pygame.transform.scale(pygame.image.load(r"src\images\ITEMS\Powerup\Powerup5.png").convert_alpha(), (SIZE_POWERUP)),
               pygame.transform.scale(pygame.image.load(r"src\images\ITEMS\Powerup\Powerup6.png").convert_alpha(), (SIZE_POWERUP)),
               pygame.transform.scale(pygame.image.load(r"src\images\ITEMS\Powerup\Powerup7.png").convert_alpha(), (SIZE_POWERUP)),
               pygame.transform.scale(pygame.image.load(r"src\images\ITEMS\Powerup\Powerup8.png").convert_alpha(), (SIZE_POWERUP)),
               pygame.transform.scale(pygame.image.load(r"src\images\ITEMS\Powerup\Powerup9.png").convert_alpha(), (SIZE_POWERUP)),
               pygame.transform.scale(pygame.image.load(r"src\images\ITEMS\Powerup\Powerup10.png").convert_alpha(), (SIZE_POWERUP)),
               pygame.transform.scale(pygame.image.load(r"src\images\ITEMS\Powerup\Powerup11.png").convert_alpha(), (SIZE_POWERUP)),
               pygame.transform.scale(pygame.image.load(r"src\images\ITEMS\Powerup\Powerup12.png").convert_alpha(), (SIZE_POWERUP))]
#---------------------------------------------------------------MUERTE-------------------------------------------------------------------------------
muerte_animacion = [
               #Muerte 0-9
               pygame.transform.scale(pygame.image.load(r"src\images\Enemigos\Explosion\Explosion1.png").convert_alpha(), (SIZE_EXPLOTION)),
               pygame.transform.scale(pygame.image.load(r"src\images\Enemigos\Explosion\Explosion2.png").convert_alpha(), (SIZE_EXPLOTION)),
               pygame.transform.scale(pygame.image.load(r"src\images\Enemigos\Explosion\Explosion3.png").convert_alpha(), (SIZE_EXPLOTION)),
               pygame.transform.scale(pygame.image.load(r"src\images\Enemigos\Explosion\Explosion4.png").convert_alpha(), (SIZE_EXPLOTION)),
               pygame.transform.scale(pygame.image.load(r"src\images\Enemigos\Explosion\Explosion5.png").convert_alpha(), (SIZE_EXPLOTION)),
               pygame.transform.scale(pygame.image.load(r"src\images\Enemigos\Explosion\Explosion6.png").convert_alpha(), (SIZE_EXPLOTION)),
               pygame.transform.scale(pygame.image.load(r"src\images\Enemigos\Explosion\Explosion7.png").convert_alpha(), (SIZE_EXPLOTION)),
               pygame.transform.scale(pygame.image.load(r"src\images\Enemigos\Explosion\Explosion8.png").convert_alpha(), (SIZE_EXPLOTION)),
               pygame.transform.scale(pygame.image.load(r"src\images\Enemigos\Explosion\Explosion9.png").convert_alpha(), (SIZE_EXPLOTION)),
               pygame.transform.scale(pygame.image.load(r"src\images\Enemigos\Explosion\Explosion10.png").convert_alpha(), (SIZE_EXPLOTION))]