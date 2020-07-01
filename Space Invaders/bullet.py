import pygame
import os

class Bullet:
    def __init__(self):
        bulletwidth = 32
        bulletheight = 32
        bulletimage = pygame.image.load(os.path.join("images", "bullet-32px"))