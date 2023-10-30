import pygame
from constantes import *

def getSurfaceFromSpriteSheet(path, columnas, filas, flip = False):
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
    def __init__(self, x, y, posicion_inicial, speed_walk) -> None:
        self.walk_der = getSurfaceFromSpriteSheet(PATH_IMAGE+"derecha_sprite.png",4,1)
        self.walk_izq = getSurfaceFromSpriteSheet(PATH_IMAGE+"izquierda_spritet.png",4,1)

        self.stay = getSurfaceFromSpriteSheet(PATH_IMAGE+"stay.png",4,1)
        self.frame = 0 #frame de animación del personaje
        self.score = 0
        self.posicion_inicial = posicion_inicial
        self.move_x = x
        self.move_y = y
        self.speed_walk = speed_walk
        
        self.animation = self.stay
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()

    def control(self, action):
        if (action == "walk_r"):
            self.move_x = self.speed_walk
            self.animation = self.walk_der
            self.frame = 0
        elif (action == "walk_l"):
            self.move_x = -self.speed_walk
            self.animation = self.walk_izq
            self.frame = 0
        elif (action == "stay"):
            self.animation = self.stay
            self.move_x = 0
            self.move_y = 0
            self.frame = 0

    def update(self):
        if (self.frame < len(self.animation) - 1):
            self.frame += 1
        else:
            self.frame = 0

        self.rect.x += self.move_x  
        self.rect.y += self.move_y


    def draw(self, screen):
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        screen.blit(self.image, self.rect)
