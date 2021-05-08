import pygame
import sys

from dialogue_manager import DialogueManager
from utils import Logger 

logger = Logger('dialogue/game.py')


class Game:
    def __init__(self):
        pygame.init()

        self.SCREEN_WIDTH = 500
        self.SCREEN_HEIGHT = 600
        self.CAPTION = 'dialogue_test'
        self.FPS = 60

        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT,))
        pygame.display.set_caption(self.CAPTION)

        self.clock = pygame.time.Clock()

        self.dialogue_manager = DialogueManager()
        logger.log_neutral("Activated")
        self.dialogue_manager.activate()
        self.dialogue_manager.set_active_dialogue("person1")

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.dialogue_manager.trigger_dialogue()

    def key_handler(self):
        pass

    def graphics_handler(self):
        self.screen.fill(pygame.Color('gold'))

        # draw stuff here


        pygame.display.update()
        self.clock.tick(self.FPS)

    def run(self):
        while True:
            self.event_handler()
            self.key_handler()
            self.graphics_handler()

if __name__ == "__main__":
    game = Game()
    game.run()
