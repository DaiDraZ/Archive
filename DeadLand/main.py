
import pygame
import os
import configs




class DeadLand:
    def __init__(self) -> None:
        pygame.init()
        self.status = True
        self.screen = pygame.display.set_mode(
            (configs.WIDTH, configs.HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption('DeadLand <#>')
        pass

    def fps(self):
        FPS = pygame.time.Clock()
        FPS.tick(configs.FPS)

    def start(self):
        while self.status:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.status = False
            pygame.display.update()
        self.fps()
        pygame.quit()


if __name__ == '__main__':
    game = DeadLand()
    game.start()