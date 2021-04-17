import pygame
import sys

from text_rendering import *
from image_rendering import *
from constants import *

pygame.init()


class Game:
	def __init__(self):
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption(CAPTION)
		self.image_renderer = ImageRenderer()
		self.image1 = self.image_renderer.render_image("fish", (WIDTH//2, HEIGHT//2,), (128, 128,))
		self.image2 = self.image_renderer.render_image("fish", ((WIDTH//2)//2, (HEIGHT//2)//2,), (64, 64,))
		print(f'{self.image1}, {self.image2}')
		self.text_renderer = TextRenderer()
		self.text_renderer.render(x=WIDTH//2, y=HEIGHT//2, text="Lorem Ipsum", speed=0.1, static =True)
		self.clock = pygame.time.Clock()

	def event_handler(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == TEXT_UPDATE:
				self.text_renderer.tick()
			if event.type == pygame.MOUSEBUTTONDOWN:
				self.image_renderer.remove_image(self.image1)
				self.image_renderer.remove_image(self.image2)

	def key_handler(self):
		pass

	def graphics_handler(self):
		self.screen.fill((0,0,0))
		text_renders = self.text_renderer.get_render_requests()

		image_renders = self.image_renderer.get_render_requests()
		for image in image_renders:
			self.screen.blit(image["surface"], image["object"])
		pygame.event.post(pygame.event.Event(IMAGE_UPDATE))

		for text in text_renders:
			self.screen.blit(text["surface"], text["object"])
		pygame.event.post(pygame.event.Event(TEXT_UPDATE))
		pygame.display.update()

	def run(self):
		while True:
			self.event_handler()
			self.key_handler()

			self.graphics_handler()

			self.clock.tick(FPS)