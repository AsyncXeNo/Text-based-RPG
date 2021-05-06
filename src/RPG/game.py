import pygame
import sys

from logger import Logger
from graphics.text_rendering import *
from graphics.image_rendering import *
from constants import *
from logger import Logger

logger = Logger('game.py')


class Game(object):
    def __init__(self, application):

        self.application = application
        self.application.menus_handler.add_menu(self)

        self.running = True

        self.width = WIDTH
        self.height = HEIGHT

        logger.log_neutral('Setting up the surface.')
        self.surface = pygame.Surface((self.width, self.height,))

        logger.log_neutral('Sending 2 fish images for rendering.')
        self.image1id = self.application.image_renderer.render_image('fish', (self.width/2, self.height/2,), self.surface, (128, 128,))
        self.image2id = self.application.image_renderer.render_image('fish', (((self.width/2)/2), ((self.height/2)/2)), self.surface, (64, 64,))

        logger.log_neutral('Sending text for rendering')
        self.text1id = self.application.text_renderer.render(text="Lorem Ipsum", x=self.width/2, y=self.height/2, surface=self.surface, speed=0.1, static=True)

    def event_handler(self, events):
        for event in events:
            if event.type == TEXT_UPDATE:
                self.application.text_renderer.tick()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.application.image_renderer.remove_request(self.image1id)
                self.application.image_renderer.remove_request(self.image2id)
                self.application.text_renderer.remove_request(self.text1id)

    def graphics_handler(self):
        self.application.win.blit(self.surface, (0, 0))
        self.surface.fill(pygame.Color('gold'))

        # do stuff


        #

    def loop(self):
        self.event_handler(self.application.events)
        self.graphics_handler()
            
