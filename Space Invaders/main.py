import pygame
import os

class Main:
    def __init__(self):
        self.width = 1024
        self.height = 768
        self.display = pygame.display.set_mode((self.width, self.height))
        self.bgwidth = 1024
        self.bgheight = 768
        self.bgimage = pygame.image.load(os.path.join("images", "background-image-1024x768.jpg"))

    def main_loop(self):
        FPS = 60
        run = True
        clock = pygame.time.Clock()

        while run:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.update_display()

        pygame.quit()

    def update_display(self):
        self.display.blit(self.bgimage, (0, 0, self.bgwidth, self.bgheight))

        pygame.display.update()

game = Main()
game.main_loop()