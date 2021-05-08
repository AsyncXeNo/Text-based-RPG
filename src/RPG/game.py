import pygame
import sys
import numpy as np
import math

from graphics.text_rendering import *
from graphics.image_rendering import *
from graphics.plot_rendering import *
from constants import *
from utils import Logger

logger = Logger('game.py')


class Game(object):
	def __init__(self, application):

		self.application = application
		self.application.menus_handler.add_menu(self)

		self.running = True

		self.width = WIDTH
		self.height = HEIGHT

		logger.log_neutral('Setting up the game surface.')
		self.surface = pygame.Surface((self.width, self.height,))

		logger.log_neutral('Activating dialogue manager.')
		self.application.dialogue_manager.activate()
		logger.log_neutral('Setting active conversation "person1"')
		self.application.dialogue_manager.set_active_dialogue("person1")

		self.render_requests = []

	def add_render_request(self, id_arg, name):
		self.render_requests.append((id_arg, name,))

	def get_request_id_and_delete(self, name):
		req = None
		for request in self.render_requests:
			if request[1] == name:
				req = request

		if req:
			self.render_requests.remove(req)
			return req[0]

	def event_handler(self, events):
		for event in events:

			if event.type == pygame.MOUSEBUTTONDOWN:

				if event.button == 1:

					logger.log_neutral('Sending 2 fish images for rendering.')
					self.add_render_request(self.application.image_renderer.render_image('fish', (self.width/2, self.height/2,), self.surface, (128, 128,)), 'fish1')
					
					self.add_render_request(self.application.image_renderer.render_image('fish', (((self.width/2)/2), ((self.height/2)/2)), self.surface, (64, 64,)), 'fish2')


					logger.log_neutral('Sending text for rendering')
					self.add_render_request(self.application.text_renderer.render(text="Lorem Ipsum", x=self.width/2, y=self.height/2, surface=self.surface, speed=0.1, static=True), 'lorem1')


					logger.log_neutral('Sending 2 plots for rendering.')
					x1 = np.arange(0,12, 0.1)
					# logger.log_warning(list(x1)[:7])
					freq = lambda x: (20/(2*np.pi))*x
					# logger.log_warning(list(map(freq,x1))[:7])
					y1 = 5*np.sin(list(map(freq,x1)))
					self.add_render_request(self.application.plot_renderer.create_canvas(x1, y1, (200, 200), (0,0), self.surface), 'plot1')
					x2 = np.arange(0,10, 0.01)
					def triangle(p): return lambda x: ((4/p))*(x-((p/2)*math.floor(((2*x)/p)+(1/2))))*(-1)**(math.floor(((2*x)/p)+(1/2)))
					trig = triangle(5)
					y2 = np.array(list(map(trig, x2)))
					self.add_render_request(self.application.plot_renderer.create_canvas(x2,y2, (200,200), (500,0), self.surface), 'plot tan')
				
				if event.button == 2:
					self.application.dialogue_manager.trigger_dialogue()

				if event.button == 3:
					self.application.image_renderer.remove_request(self.get_request_id_and_delete('fish1'))
					self.application.image_renderer.remove_request(self.get_request_id_and_delete('fish2'))
					self.application.text_renderer.remove_request(self.get_request_id_and_delete('lorem1'))
					self.application.plot_renderer.remove_request(self.get_request_id_and_delete('plot1'))
					self.application.plot_renderer.remove_request(self.get_request_id_and_delete('plot tan'))

	def graphics_handler(self):
		self.application.win.blit(self.surface, (0, 0))
		self.surface.fill(pygame.Color('gold'))

		# do stuff


		#

	def loop(self):
		self.event_handler(self.application.events)
		self.graphics_handler()
			
