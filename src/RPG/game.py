import pygame
import sys

from graphics import *
from constants import *

pygame.init()


class Game:
	def __init__(self):
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption(CAPTION)
		self.text_renderer = TextRenderer()
		self.text_renderer.render(x=WIDTH//2, y=HEIGHT//2, text="Lorem Ipsum", speed=1)
		self.clock = pygame.time.Clock()

	def event_handler(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

	def key_handler(self):
		pass

	def graphics_handler(self):
		text_renders = self.text_renderer.get_render_requests()
		for text in text_renders:
			self.screen.blit(text["surface"], text["object"])
		pygame.display.update()

	def run(self):
		while True:
			self.event_handler()
			self.key_handler()

			self.graphics_handler()

			self.clock.tick(FPS)