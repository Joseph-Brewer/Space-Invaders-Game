import pygame
import os

class SpaceShip:
    def __init__(self):
        spaceshipwidth = 64
        spaceshipheight = 64
        spaceshipimage = pygame.image.load(os.path.join("images", "spaceship-64px.png"))