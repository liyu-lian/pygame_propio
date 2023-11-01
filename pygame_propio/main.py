import pygame
import sys
from constantes import *
from player import Player

screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()

imagen_fondo = pygame.image.load(PATH_IMAGE+"fondo_aparicion.jpg")
imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))

player_1 = Player(0,0,[500, 400],4)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_1.control("walk_l")
            elif event.key == pygame.K_RIGHT:
                player_1.control("walk_r")
            else:
                player_1.control("stay")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_1.control("stay")

    screen.blit(imagen_fondo, imagen_fondo.get_rect())
    #delta_ms = print(clock.tick(FPS))

    player_1.update()
    player_1.draw(screen)
    #player update -- verificar como el ´layer interactua con todo el nivel
    # enemigos update
    # player dibujarlo
    # dibujar todo el nivel
    
    pygame.display.flip()

    




