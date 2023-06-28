import pygame
import random
import sys
from config import *
from animaciones import *
from plataforma import Plataforma
from mago import Mago
from koloss import Koloss
from liche import Liche
from barra_de_vida import Life_bar
from vida import Vida
from coin import Coin
from powerup import Powerup
from explosion import Explosion

class Juego:
    def __init__(self):
        pygame.init()
        self.screen = screen
        pygame.display.set_caption("Wizzard Attack")
        icono = pygame.image.load(r"src\images\Icono.png")
        icono = pygame.transform.scale(icono.convert_alpha(), SIZE_ICON)
        pygame.display.set_icon(icono)

        self.reloj = pygame.time.Clock()

        self.sonido_menu = (r"src\sounds\Menu Inicio.mp3")
        self.musica_juego = (r"src\sounds\Musica Boss.mp3")
        self.musica_pause = (r"src\sounds\Pausa.mp3")
        self.musica_win = (r"src\sounds\Ganaste.mp3")
        self.sonido_play = (r"src\sounds\Game Start.mp3")
        self.sonido_firebolt = (r"src\sounds\Fireball.mp3")
        self.sonido_explosion = (r"src\sounds\Explosion.mp3")
        self.sonido_salto = (r"src\sounds\Salto Fuego.mp3")
        self.sonido_piso = (r"src\sounds\Chocar Piso.mp3")
        self.sonido_muerte = (r"src\sounds\Sonido Muerte.mp3")
        self.sonido_vida = (r"src\sounds\Vida nueva.mp3")
        self.sonido_coin = (r"src\sounds\Coin.mp3")
        self.sonido_powerup = (r"src\sounds\PowerUp.mp3")
        self.sonido_dolor = (r"src\sounds\Golpe.mp3")
        self.score = 0
        self.contador = 0
        self.contador_niveles = 1
        self.total_enemigos = 0
        self.muertes_enemigos = 0
        self.contador_partidas = 0
        self.contador_texto = 0
        self.contador_final = 0
        self.jugando = False
        self.finalizado = False
        self.flag_choque_piso = False
        self.flag_colision_koloss = False
        self.flag_colision_liche = False
        self.flag_colision_corazon = False
        self.flag_colision_coin = False
        self.flag_colision_powerup = False
        self.flag_establecer_enemigo = True
        self.flag_pause = False
        self.ganaste = False
        self.mensaje = None
        self.cooldown = COOLDOWN
        self.fondo = pygame.image.load(r"src\images\Escenario\Fondo_inicio.jpg").convert()
        self.fondo = pygame.transform.scale(self.fondo, (WIDTH, HEIGHT))
        self.fondo_end = pygame.image.load(r"src\images\Escenario\Fondo_win.png").convert()
        self.fondo_end = pygame.transform.scale(self.fondo_end, (WIDTH, HEIGHT))

        self.fuente_play = pygame.font.SysFont("bradleyhanditc", 100)
        self.fuente_texto = pygame.font.SysFont("ocraextended",50)
        self.fuente_score = pygame.font.SysFont("ocraextended",18)
        self.fuente_pixel = pygame.font.Font(r"src\Font\upheavtt.ttf", 50)

        self.sprites = pygame.sprite.Group()
        self.firebolt = pygame.sprite.Group()
        self.plataforma = pygame.sprite.Group()
        self.koloss = pygame.sprite.Group()
        self.liche = pygame.sprite.Group()
        self.item_vida = pygame.sprite.Group()
        self.item_coin = pygame.sprite.Group()
        self.item_powerup = pygame.sprite.Group()

    
        self.menu = pygame.mixer.Sound(self.sonido_menu)
        self.start = pygame.mixer.Sound(self.sonido_play)
        self.pause = pygame.mixer.Sound(self.musica_pause)
        self.sound_play = pygame.mixer.Sound(self.musica_juego)
        self.win = pygame.mixer.Sound(self.musica_win)
        self.salto = pygame.mixer.Sound(self.sonido_salto)
        self.choque_piso = pygame.mixer.Sound(self.sonido_piso) 
        self.muerte = pygame.mixer.Sound(self.sonido_muerte)
        self.explosion = pygame.mixer.Sound(self.sonido_explosion)
        self.vida_nueva = pygame.mixer.Sound(self.sonido_vida)
        self.coin = pygame.mixer.Sound(self.sonido_coin)
        self.powerup = pygame.mixer.Sound(self.sonido_powerup)
        self.dolor = pygame.mixer.Sound(self.sonido_dolor)

        self.sound_play.set_volume(0.5)
        self.menu.set_volume(0.3)

        self.mago = Mago(mago_animaciones, PLACE_PJ)
        self.vida = Life_bar(barra_vida_animaciones, DISPLAY_LIFE, self.sonido_muerte)

        self.plataforma_principal = Plataforma(r"src\images\Escenario\Plataforma_principal.png", SIZE_PLATAFORMA_PRINCIPAL, PLACE_PLATAFORMA_PRINCIPAL)
        self.plataforma_left = Plataforma(r"src\images\Escenario\plataforma.png", SIZE_PLATAFORMA, PLACE_PLATAFORMA_LEFT)
        self.plataforma_right = Plataforma(r"src\images\Escenario\plataforma.png", SIZE_PLATAFORMA, PLACE_PLATAFORMA_RIGHT)

        self.agregar_firebolt(self.firebolt)
        self.agregar_plataforma(self.plataforma_principal)
        self.agregar_plataforma(self.plataforma_left)
        self.agregar_plataforma(self.plataforma_right)
        
        self.agregar_sprite(self.plataforma_left)
        self.agregar_sprite(self.plataforma_right)
        self.agregar_sprite(self.plataforma_principal)        
        self.agregar_sprite(self.mago)
        self.agregar_sprite(self.vida)


    def agregar_sprite(self, sprite):   #Para mostrar los sprites
        self.sprites.add(sprite)

    def agregar_firebolt(self, firebolt):   #Lo agrega al grupo
        self.firebolt.add(firebolt)

    def agregar_plataforma(self, plataforma):   #Lo agrega al grupo
        self.plataforma.add(plataforma)
    
    def agregar_koloss(self,koloss):
        self.koloss.add(koloss)
    
    def agregar_liche(self,liche):
        self.liche.add(liche)

    def agregar_vida(self, vida):
        self.item_vida.add(vida)

    def agregar_coin(self, coin):
        self.item_coin.add(coin)
    
    def agregar_powerup(self, powerup):
        self.item_powerup.add(powerup)

    def comenzar(self):
        self.jugando = True
        self.finalizado = False
        self.sound_play.play(-1)
        while self.jugando:
            self.reloj.tick(FPS)

            self.actualizar_elementos()

            self.renderizar_pantalla()

            self.manejar_eventos()

            self.niveles()
            
                

    def manejar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.salir()
            elif evento.type == pygame.KEYDOWN and self.vida.quieto == False:
                self.mago.indice = 0
                if evento.key  == pygame.K_ESCAPE:
                    self.flag_pause = True
                    self.sound_play.stop()
                    self.pantalla_inico()
                if evento.key == pygame.K_a and self.mago.velocidad_X >=0:
                    self.mago.velocidad_X = -SPEED_PJ
                    # print(self.mago.velocidad_X)
                elif evento.key == pygame.K_d and self.mago.velocidad_X <=0:
                    self.mago.velocidad_X = SPEED_PJ
                    # print(self.mago.velocidad_X)
                elif evento.key == pygame.K_LEFT:
                    if self.contador >= self.cooldown:
                        self.contador = 0
                        self.mago.disparar(firebolt_animaciones, self.sonido_firebolt, SPEED_FIREBOLT, self.sprites, self.firebolt, evento.key)
                elif evento.key == pygame.K_RIGHT:
                    if self.contador >= self.cooldown:
                        self.contador = 0
                        # print(evento.key, "Derecha")
                        self.mago.disparar(firebolt_animaciones, self.sonido_firebolt, SPEED_FIREBOLT, self.sprites, self.firebolt, evento.key)
                elif evento.key == pygame.K_SPACE:
                    if self.mago.puede_saltar:
                        self.salto.play()
                        self.mago.velocidad_Y = -JUMP 
                        self.mago.puede_saltar = False
                        self.mago.planeo = True
                        # print("SALTO")
                elif evento.key == pygame.K_LSHIFT:
                    if self.mago.velocidad_X > 0:
                        self.mago.velocidad_X = BOOST
                    elif self.mago.velocidad_X < 0:
                        self.mago.velocidad_X = -BOOST

            elif evento.type == pygame.KEYUP:
                if evento.key == pygame.K_a and self.mago.velocidad_X < 0:
                    self.mago.velocidad_X = 0
                    # print(self.mago.velocidad_X)
                elif evento.key == pygame.K_d and self.mago.velocidad_X > 0:
                    self.mago.velocidad_X = 0
                    # print(self.mago.velocidad_X)
                elif evento.key == pygame.K_SPACE:
                    self.mago.planeo = False
                elif evento.key == pygame.K_RIGHT:
                    self.mago.accion = False   
                elif evento.key == pygame.K_LEFT:
                    self.mago.accion = False  
                elif evento.key == pygame.K_LSHIFT:
                    if self.mago.velocidad_X > 0:
                        self.mago.velocidad_X = BOOST
                    elif self.mago.velocidad_X < 0:
                        self.mago.velocidad_X = -BOOST


    def actualizar_elementos(self):
        self.sprites.update()
        if self.contador < self.cooldown:
            self.contador += 1
        if self.mago.activate == False:
            self.cooldown = COOLDOWN
        for firebolt in self.firebolt:
            if firebolt.rect.right <= 0:
                firebolt.kill()
            elif firebolt.rect.left >= WIDTH:
                firebolt.kill()

            lista_koloss = pygame.sprite.spritecollide(firebolt, self.koloss, True)
            if lista_koloss:    
                firebolt.kill()
                self.explosion.play()
                self.score += SCORE_KOLOSS
                self.muertes_enemigos -= 1
                koloss = lista_koloss[0]
                self.spawnear_items(koloss)
                print(self.muertes_enemigos)
                
            
            lista_liche = pygame.sprite.spritecollide(firebolt, self.liche, True)
            if lista_liche:    
                firebolt.kill()
                self.explosion.play()
                self.score += SCORE_LICHE
                self.muertes_enemigos -= 1
                liche = lista_liche[0]
                self.spawnear_items(liche)
                print(self.muertes_enemigos)

        #Comprueba que el PJ colisione con cualquier plataforma
        colisiones_plataforma = pygame.sprite.spritecollide(self.mago, self.plataforma, False)
        if colisiones_plataforma:
            if self.mago.velocidad_Y >= 0:
                plataforma = colisiones_plataforma[0]
                self.mago.rect.bottom = plataforma.rect.top + 25
                self.mago.velocidad_Y = 0
                self.mago.distancia_salto = 0
                if self.flag_choque_piso:
                    self.choque_piso.play()
                    self.flag_choque_piso = False
                    self.mago.puede_saltar = True
                self.salto.stop()
        else:
            #caer hasta colisionar.
            self.flag_choque_piso = True
            if self.mago.planeo:
                if self.mago.distancia_salto == 0:
                    self.mago.velocidad_Y = GLIDE
            else:
                self.mago.velocidad_Y += GRAVITY

        if self.vida.quieto == False:  
            colisiones_koloss = pygame.sprite.spritecollide(self.mago, self.koloss, False)
            if colisiones_koloss:
                if self.flag_colision_koloss:
                    self.vida.life_bar -= 1
                    self.flag_colision_koloss = False
                    self.score += SCORE_COLISION
                    self.dolor.play()
            else:
                self.flag_colision_koloss = True
            
            colisiones_liche = pygame.sprite.spritecollide(self.mago, self.liche, False)
            if colisiones_liche:
                if self.flag_colision_liche:
                    self.vida.life_bar -= 1
                    self.flag_colision_liche = False
                    self.score += SCORE_COLISION
                    self.dolor.play()
            else:
                self.flag_colision_liche = True
            # print(self.flag_colision)
            
            colisiones_corazon = pygame.sprite.spritecollide(self.mago, self.item_vida, True)
            if colisiones_corazon:
                if self.flag_colision_corazon:
                    self.vida.life_bar += 1
                    self.flag_colision_corazon = False
                    self.vida_nueva.play()
            else:
                self.flag_colision_corazon = True

            colisones_coin = pygame.sprite.spritecollide(self.mago, self.item_coin, True)
            if colisones_coin:
                if self.flag_colision_coin:
                    self.score += SCORE_COIN
                    self.coin.play()
            else:
                self.flag_colision_coin = True

            colisones_powerup = pygame.sprite.spritecollide(self.mago, self.item_powerup, True)
            if colisones_powerup:
                if self.flag_colision_powerup:
                    self.score += SCORE_COIN
                    self.mago.activate = True
                    self.mago.contador_powerup = 0
                    self.powerup.play()
                    self.cooldown = 5
            else:
                self.flag_colision_powerup = True

        else:
            self.mago.muerto = True
            self.mago.velocidad_X = 0

        if self.vida.flag_vida:
            self.mensaje = f"Has aguantado {self.contador_niveles - 1} oleadas. La próxima será :)"
            self.vida.flag_vida = False
            self.game_over()
            

    def niveles(self):
        match self.contador_niveles:
            case 1:
                if self.contador_texto >= CHARGE_TIME:
                    if self.flag_establecer_enemigo:
                        self.muertes_enemigos = WAVE_ONE
                        self.flag_establecer_enemigo = False
                        
                    if self.muertes_enemigos > 0:
                        if self.total_enemigos < WAVE_ONE:
                            self.generar_koloss(MAX_KOLOSS)
                            self.generar_liche(MAX_LICHE)
                    else:
                        self.contador_niveles = 2
                        self.score += SCORE_WAVE
                        self.flag_establecer_enemigo = True
                        self.total_enemigos = 0
                        self.contador_texto = 0
                        self.eliminar_enemigos()
            case 2:
                if self.contador_texto >= CHARGE_TIME:
                    if self.flag_establecer_enemigo:
                        self.muertes_enemigos = WAVE_TWO
                        self.flag_establecer_enemigo = False

                    if self.muertes_enemigos > 0:
                        if self.total_enemigos < WAVE_TWO:
                            self.generar_koloss(MAX_KOLOSS_2)
                            self.generar_liche(MAX_LICHE_2)
                    else:
                        self.contador_niveles = 3
                        self.flag_establecer_enemigo = True
                        self.score += SCORE_WAVE
                        self.total_enemigos = 0
                        self.contador_texto = 0
                        self.eliminar_enemigos()
            case 3:
                if self.contador_texto >= CHARGE_TIME:
                    if self.flag_establecer_enemigo:
                        self.muertes_enemigos = WAVE_THREE
                        self.flag_establecer_enemigo = False

                    if self.muertes_enemigos > 0:
                        if self.total_enemigos < WAVE_THREE:
                            self.generar_koloss(MAX_KOLOSS_3)
                            self.generar_liche(MAX_LICHE_3)
                    else:
                        if self.contador_final <= CHARGE_TIME:
                            self.contador_final += 1
                            self.finalizado = True
                            self.eliminar_enemigos()
                        else:
                            if self.score < SCORE_MIN:
                                self.mensaje = "PUNTAJE BAJO. La próxima será :("
                            else:
                                self.score += SCORE_WAVE
                                self.ganaste = True
                                self.mensaje = "FELICIDADES, HAS GANADO!!! :D"
                            self.game_over()

    def spawnear_items(self, enemigo):
        enemigo = enemigo.rect.center
        numero_random = random.randrange(0, 10)
        if numero_random == PROBABILITY_CORAZON:
            self.generar_corazones(enemigo)
        if numero_random in PROBABILITY_COIN:
            self.generar_coins(enemigo)
        if numero_random == PROBABILITY_POWERUP:
            self.generar_powerups(enemigo)
        self.generar_explosiones(enemigo)
        
    def generar_koloss(self, cantidad):
        if len(self.koloss) == 0:
            for i in range(cantidad):
                posicion_postiva = (random.randrange(WIDTH + 1000, WIDTH + 3500))
                posicion_negativa = (random.randrange(WIDTH - 3500, -1000))
                posicion_final = (random.choice([posicion_negativa, posicion_postiva]), HEIGHT - (HEIGHT // 6))
                print(posicion_final)
                koloss = Koloss(koloss_animaciones, posicion_final)

                self.agregar_koloss (koloss)
                self.agregar_sprite(koloss)
            self.total_enemigos += cantidad
            
    def generar_liche(self, cantidad):
        if len(self.liche) == 0:
            for i in range(cantidad):
                posicion_postiva = (random.randrange(WIDTH + 1000, WIDTH + 3500), random.randrange(0, HEIGHT - (HEIGHT // 6)))
                posicion_negativa = (random.randrange(WIDTH - 3500, -1000), random.randrange(0, HEIGHT - (HEIGHT // 6)))
                posicion_final = (random.choice([posicion_negativa, posicion_postiva]))
                print(posicion_final)
                liche = Liche(liche_animaciones, posicion_final)

                self.agregar_liche (liche)
                self.agregar_sprite(liche)
            self.total_enemigos += cantidad

    def generar_corazones(self, place):
        item_vida = Vida(corazon_animacion, place)
        self.agregar_vida(item_vida)
        self.agregar_sprite(item_vida)

    def generar_coins(self, place):
        item_coin = Coin(coin_animacion, place)
        self.agregar_coin(item_coin)
        self.agregar_sprite(item_coin)
    
    def generar_powerups(self, place):
        item_powerup = Powerup(powerup_animacion, place)
        self.agregar_powerup(item_powerup)
        self.agregar_sprite(item_powerup)
    
    def generar_explosiones(self, place):
        explosion = Explosion(muerte_animacion, place)
        self.agregar_sprite(explosion)

    def generar_texto(self, texto:str, fuente, place:tuple, color):
        titulo = fuente.render(f"{texto}", True, color)
        rect_titulo = titulo.get_rect()
        rect_titulo.midbottom = place
        self.screen.blit(titulo, rect_titulo)

    def eliminar_enemigos(self):
        for koloss in self.koloss:
            koloss.kill()
        
        for liche in self.liche:
            liche.kill()


    def renderizar_pantalla(self):
        self.screen.blit(self.fondo, ORIGIN)
        self.sprites.draw(self.screen)  
        if self.score < SCORE_MIN:
            self.generar_texto(f"SCORE:{self.score}", self.fuente_score, DISPLAY_SCORE, BORDO)
        else:
            self.generar_texto(f"SCORE:{self.score}", self.fuente_score, DISPLAY_SCORE, VERDE)

        if self.contador_texto <= CHARGE_TIME and self.contador_niveles == 1:
            self.contador_texto += 1
            self.generar_texto(f"OLEADA 1", self.fuente_pixel, DISPLAY_WAVE, GRIS)
            self.generar_texto(f"Cargando enemigos. Preparate", self.fuente_pixel, DISPLAY_WORD, GRIS)
        elif self.contador_texto <= CHARGE_TIME and self.contador_niveles == 2:
            self.contador_texto += 1
            self.generar_texto(f"OLEADA 2", self.fuente_pixel, DISPLAY_WAVE, GRIS)
            self.generar_texto(f"Cargando nuevos enemigos. Preparate", self.fuente_pixel, DISPLAY_WORD, GRIS)
        elif self.contador_texto <= CHARGE_TIME and self.contador_niveles == 3:
            self.contador_texto += 1
            self.generar_texto(f"OLEADA 3", self.fuente_pixel, DISPLAY_WAVE, GRIS)
            self.generar_texto(f"ULTIMA OLEADA. PREPARATE", self.fuente_pixel, DISPLAY_WORD, GRIS)
        elif self.finalizado:
            self.generar_texto(f"HAS COMPLETADO TODAS LAS OLEADAS", self.fuente_pixel, DISPLAY_WORD, GRIS)

        pygame.display.flip()

    
    def scoring_record(self):
        with open("Score.txt", "a", encoding="utf8") as file:
            file.write(f"----SCORING RECORD----\n")
            file.write(f"PARTIDA NÚMERO: {self.contador_partidas}\n")
            file.write(f"{self.mensaje}\n")
            file.write(f"SCORE FINAL: {self.score}\n")
            file.write("-----------------------\n")

    def pantalla_inico(self):
        flag = True
        mostrar_texto = True
        if self.flag_pause:
            self.pause.play(-1)
        else:
            self.menu.play(-1)

        while flag:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.salir()
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    self.pause.stop()
                    self.menu.stop()
                    self.start.play()
                    self.comenzar()

            self.screen.blit(self.fondo, ORIGIN)


            self.generar_texto("Wizzard Attack", self.fuente_play, DISPLAY_PLAY, CELESTE)
            if mostrar_texto:
                self.generar_texto("HAGA CLICK PARA COMENZAR", self.fuente_texto, DISPLAY_TEXTO, BLANCO)

            
            mostrar_texto = not mostrar_texto

            pygame.time.delay(500)
            pygame.display.flip()
            
    def stats_reset(self):
        self.salto.stop()
        self.contador = 0
        self.contador_niveles = 1
        self.total_enemigos = 0
        self.muertes_enemigos = 0
        self.contador_texto = 0
        self.contador_final = 0
        self.jugando = False
        self.finalizado = False
        self.flag_choque_piso = False
        self.flag_colision_koloss = False
        self.flag_colision_liche = False
        self.flag_colision_corazon = False
        self.flag_colision_coin = False
        self.flag_colision_powerup = False
        self.flag_establecer_enemigo = True
        self.sprites.remove(self.mago)
        self.sprites.remove(self.vida)
        self.sprites.empty()
        self.firebolt.empty()
        self.koloss.empty()
        self.liche.empty()
        self.item_vida.empty()
        self.item_coin.empty()
        self.item_powerup.empty()

        self.mago = Mago(mago_animaciones, PLACE_PJ)
        self.vida = Life_bar(barra_vida_animaciones, DISPLAY_LIFE, self.sonido_muerte)

        self.agregar_firebolt(self.firebolt)
        self.agregar_sprite(self.plataforma_left)
        self.agregar_sprite(self.plataforma_right)
        self.agregar_sprite(self.plataforma_principal)        
        self.agregar_sprite(self.mago)
        self.agregar_sprite(self.vida)

    def game_over(self):
        self.stats_reset()
        self.sound_play.stop()
        score_record = self.score
        self.contador_partidas += 1
        self.scoring_record()
        if self.ganaste:
            self.win.play(-1)
        else:
            self.menu.play(-1)
        self.score = 0
        self.ganaste = False
        flag = True
        mostrar_texto = True

        while flag:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.salir()
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    self.win.stop()
                    self.menu.stop()
                    self.start.play()
                    self.comenzar()
            self.screen.blit(self.fondo_end, ORIGIN)
            
            self.generar_texto("Wizzard Attack", self.fuente_play, DISPLAY_PLAY, CELESTE)
            self.generar_texto(f"SCORE: {score_record}", self.fuente_texto, DISPLAY_SCORE_2, CIAN)
            self.generar_texto(f"{self.mensaje}", self.fuente_pixel, DISPLAY_MESSAGE, CIAN)

            if mostrar_texto:
                self.generar_texto("HAGA CLICK PARA VOLVER A JUGAR", self.fuente_texto, DISPLAY_TEXTO, BLANCO)
            
            mostrar_texto = not mostrar_texto

            pygame.time.delay(500)
            pygame.display.flip()

            
    def salir(self):
        pygame.quit()
        sys.exit()
