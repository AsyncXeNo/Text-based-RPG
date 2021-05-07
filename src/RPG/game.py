import pygame
import sys
import numpy as np
import math

from logger import Logger
from graphics.text_rendering import *
from graphics.image_rendering import *
from graphics.plot_rendering import *
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


	def event_handler(self, events):
		for event in events:
			
			if event.type == pygame.MOUSEBUTTONDOWN:

				if event.button == 1:
					logger.log_neutral('Sending 2 fish images for rendering.')
					self.image1id = self.application.image_renderer.render_image('fish', (self.width/2, self.height/2,), self.surface, (128, 128,))
					self.image2id = self.application.image_renderer.render_image('fish', (((self.width/2)/2), ((self.height/2)/2)), self.surface, (64, 64,))


					logger.log_neutral('Sending text for rendering')
					self.text1id = self.application.text_renderer.render(text="Lorem Ipsum", x=self.width/2, y=self.height/2, surface=self.surface, speed=0.1, static=True)


					logger.log_neutral('Sending 2 plots for rendering.')
					x1 = np.arange(0,12, 0.1)
					# logger.log_warning(list(x1)[:7])
					freq = lambda x: (20/(2*np.pi))*x
					# logger.log_warning(list(map(freq,x1))[:7])
					y1 = 5*np.sin(list(map(freq,x1)))
					self.plot = self.application.plot_renderer.create_canvas(x1, y1, (200, 200), (0,0), self.surface)
					x2 = np.arange(0,10, 0.01)
					def triangle(p): return lambda x: ((4/p))*(x-((p/2)*math.floor(((2*x)/p)+(1/2))))*(-1)**(math.floor(((2*x)/p)+(1/2)))
					trig = triangle(5)
					y2 = np.array(list(map(trig, x2)))
					self.plot_tan = self.application.plot_renderer.create_canvas(x2,y2, (200,200), (500,0), self.surface)
								
				if event.button == 3:
					self.application.image_renderer.remove_request(self.image1id)
					self.application.image_renderer.remove_request(self.image2id)
					self.application.text_renderer.remove_request(self.text1id)
					self.application.plot_renderer.remove_request(self.plot)

	def graphics_handler(self):
		self.application.win.blit(self.surface, (0, 0))
		self.surface.fill(pygame.Color('gold'))

		# do stuff


		#

	def loop(self):
		self.event_handler(self.application.events)
		self.graphics_handler()
			
