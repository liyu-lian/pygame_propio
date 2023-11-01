import pygame
from constantes_juego import *

pos_rect = [30, 60]

pygame.init()
pantalla = pygame.display.set_mode((TAMAÑO_VENTANA))
pygame.display.set_caption("Birthday Party")

icono = pygame.image.load("./imagenes/ICON.png")
icono = pygame.transform.scale(icono, (300,300))
pygame.display.set_icon(icono)

tiempo = pygame.time.Clock()
fondo = pygame.image.load("./imagenes/fondo_aparicion.jpg")
fondo = pygame.transform.scale(fondo, (TAMAÑO_VENTANA))

flag_correr = True
while flag_correr:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_correr = False


    lista_teclas = pygame.key.get_pressed()

    if lista_teclas[pygame.K_RIGHT] == True:
        
        pos_rect[0] = pos_rect[0] + 1

    if lista_teclas[pygame.K_LEFT] == True:
        
        pos_rect[0] -= 1

    if lista_teclas[pygame.K_DOWN] == True:

        pos_rect[1] += 1

    if lista_teclas[pygame.K_UP] == True:
        pos_rect[1] -= 1 

    
    pantalla.blit(fondo, fondo.get_rect())

    pygame.draw.circle(pantalla, (255,255,255), pos_rect, 80)

    pygame.display.flip()

pygame.quit()
#fin del juego