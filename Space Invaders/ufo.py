import pygame
import os

class UFO:
    def __init__(self):
        ufowidth = 64
        ufoheight = 64
        ufoimage = pygame.image.load(os.path.join("images", "ufo-64px.png"))