import pygame
import sys
from constantes import *
from player import Player

screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()

imagen_fondo = pygame.image.load(PATH_IMAGE+"fondo_aparicion.jpg")
imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))

pos_rect = 0

player_1 = Player(POSICION_INICIAL)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_1.mover("izquierda", 0)
            elif event.key == pygame.K_RIGHT:
                player_1.mover("derecha", 0)
            elif event.key == pygame.K_UP:
                player_1.mover("arriba", 1)
            elif event.key == pygame.K_DOWN:
                player_1.mover("abajo", 1)
            else:
                player_1.mover("stay", 0)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_1.mover("stay", 0)

    player_1.update()
    player_1.draw(screen)

    #player update -- verificar como el ´layer interactua con todo el nivel
    # enemigos update
    # player dibujarlo
    # dibujar todo el nivel
    
    pygame.display.flip()
    screen.blit(imagen_fondo, imagen_fondo.get_rect())
    #delta_ms = print(clock.tick(FPS))




