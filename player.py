import pygame
from constantes import *

def getSurfaceFromSpriteSheet(path, columnas, filas):
    """ Toma un spritesheet. Toma su alto y ancho, convvirtiendo cada imagen en un frame guardado dentro de una lista """
    lista = []
    surface_imagen = pygame.image.load(path)
    fotograma_ancho = int(surface_imagen.get_width()/columnas)
    fotograma_alto = int(surface_imagen.get_height()/filas)

    for columna in range(columnas):
        for fila in range(filas):
            x = columna * fotograma_ancho
            y = fila * fotograma_alto
            surface_fotograma = surface_imagen.subsurface(x,y,fotograma_ancho, fotograma_alto)
            lista.append(surface_fotograma)
    return  lista

class Player:
    def __init__(self, posicion_inicial) -> None:
        self.walk_der = getSurfaceFromSpriteSheet(PATH_IMAGE+"derecha_sprite.png",4,1)
        self.walk_izq = getSurfaceFromSpriteSheet(PATH_IMAGE+"izquierda_spritet.png",4,1)
        self.walk_up = getSurfaceFromSpriteSheet(PATH_IMAGE+"arriba.png",4,1)
        self.walk_down = getSurfaceFromSpriteSheet(PATH_IMAGE+"abajo_sprite.png",4,1)
        self.stay = getSurfaceFromSpriteSheet(PATH_IMAGE+"stay.png",4,1)
        self.frame = 0
        self.speed_walk = 0
        self.direccion_plano = 0
        self.posicion = list(posicion_inicial)
        self.animation = self.stay
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()

    def mover(self, direccion, direccion_plano):
        if direccion == "derecha":
            if self.rect.right < ANCHO_VENTANA:
                self.speed_walk = 0.5
                self.animation = self.walk_der
                self.direccion_plano = direccion_plano
                self.rect.topleft = self.posicion
        elif direccion == "izquierda":
            if self.rect.left > 0:
                self.speed_walk = -0.5
                self.animation = self.walk_izq
                self.direccion_plano = direccion_plano
                self.rect.topleft = self.posicion
        elif direccion == "arriba":
                self.speed_walk = -0.5
                self.animation = self.walk_up
                self.direccion_plano = direccion_plano
                self.rect.topleft = self.posicion
        elif direccion == "abajo":
            self.speed_walk = 0.5
            self.animation = self.walk_down
            self.direccion_plano = direccion_plano
            self.rect.topleft = self.posicion
        elif direccion == "stay":
            self.speed_walk = 0
            self.animation = self.stay
            self.rect.topleft = self.posicion

    def update(self):
        if (self.frame < len(self.animation) - 1):
            self.frame += 1
        else:
            self.frame = 0

        self.posicion[self.direccion_plano] += self.speed_walk

    def draw(self, screen):
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.posicion)
""" 
    def mostrar(self, pantalla):
        pantalla.blit(self.image, self.posicion) """