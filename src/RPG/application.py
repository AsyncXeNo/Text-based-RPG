import pygame
import time
import sys

from utils import Logger
from menus_handler import MenusHandler
from game import Game
from graphics.text_rendering import *
from graphics.image_rendering import *
from graphics.plot_rendering import *
from constants import *

logger = Logger('application.py')


class Application(object):
	def __init__(self):
		logger.log_neutral('Initializing pygame.')
		pygame.init()

		self.running = True

		self.width = WIDTH
		self.height = HEIGHT
		logger.log_neutral('Initializing application window.')
		self.win = pygame.display.set_mode((WIDTH, HEIGHT))
		logger.log_neutral('Setting window caption.') 
		pygame.display.set_caption(CAPTION)

		logger.log_neutral('Initializing image renderer.')
		self.image_renderer = ImageRenderer()
		logger.log_neutral('Initializing text renderer.')
		self.text_renderer = TextRenderer()    
		logger.log_neutral('Initializing plot renderer.')
		self.plot_renderer = PlotRenderer()

		logger.log_neutral('Initializing clock.')
		self.clock  = pygame.time.Clock()
		self.fps = FPS

		self.menus_handler = MenusHandler()

		self.events = []

		self.game = Game(self)

		logger.log_neutral('Starting the application.')
		self.run()

	def get_events(self):
		self.events = pygame.event.get()

	def clear_events(self):
		self.events = []

	def event_handler(self):
		for event in self.events:
			if event.type == pygame.QUIT:
				logger.log_alert('Quit all the menus too when you implement the stack.')
				logger.log_neutral('Quitting the application.')
				self.running = False    
				pygame.quit()
				sys.exit()
			
			if event.type == TEXT_UPDATE:
				self.text_renderer.tick()

			if event.type == IMAGE_UPDATE:
				pass

			if event.type == PLOT_UPDATE:
				pass

	def run(self):
		while self.running:
			self.get_events()
			self.event_handler()

			self.win.fill(pygame.Color('black'))

			# do game stuff
			self.menus_handler.get_menu().loop()

			pygame.event.post(pygame.event.Event(IMAGE_UPDATE))
			pygame.event.post(pygame.event.Event(TEXT_UPDATE))
			pygame.event.post(pygame.event.Event(PLOT_UPDATE))

			self.text_renderer.blit_requests()
			self.image_renderer.blit_requests()
			self.plot_renderer.blit_requests()

			self.clear_events()
			pygame.display.update()
			self.clock.tick(self.fps)


# Test
application = Application()

class A():
	def __init__(self):
		b = B(self)


class B():
	def __init__(self, a):
		self.a = a


a = A()
