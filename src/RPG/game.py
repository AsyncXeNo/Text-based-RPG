import pygame
import sys
import numpy as np
import math

from graphics.text_rendering import *
from graphics.image_rendering import *
from graphics.plot_rendering import *
from constants import *


pygame.init()



class Game:
	def __init__(self):
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		self.plot_renderer = PlotRenderer()
		x1 = np.arange(0,12, 0.1)
		print(list(x1)[:7])
		freq = lambda x: (20/(2*np.pi))*x
		print(list(map(freq,x1))[:7])
		y1 = 5*np.sin(list(map(freq,x1)))
		self.plot = self.plot_renderer.create_canvas(x1, y1, (400,400), (0,0), self.screen)
		x2 = np.arange(0,10, 0.01)
		def triangle(p): return lambda x: ((4/p))*(x-((p/2)*math.floor(((2*x)/p)+(1/2))))*(-1)**(math.floor(((2*x)/p)+(1/2)))
		trig = triangle(5)
		y2 = np.array(list(map(trig, x2)))
		self.plot_tan = self.plot_renderer.create_canvas(x2,y2, (400,400), (500,0), self.screen)
		pygame.display.set_caption(CAPTION)
		# self.image_renderer = ImageRenderer()
		# self.image1id = self.image_renderer.render_image("fish", (WIDTH//2, HEIGHT//2,), (128, 128,))
		# self.image2id = self.image_renderer.render_image("fish", ((WIDTH//2)//2, (HEIGHT//2)//2,), (64, 64,))
		# print(f'{self.image1id}, {self.image2id}')
		# self.text_renderer = TextRenderer()
		# self.text1id = self.text_renderer.render(x=WIDTH//2, y=HEIGHT//2, text="Lorem Ipsum", speed=0.1, static =True)
		self.clock = pygame.time.Clock()

	def event_handler(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == TEXT_UPDATE:
				self.text_renderer.tick()
			if event.type == pygame.MOUSEBUTTONDOWN:
				# self.image_renderer.remove_image(self.image1id)
				# self.image_renderer.remove_image(self.image2id)
				# self.text_renderer.remove_request(self.text1id)
				self.plot_renderer.remove_request(self.plot)

	def key_handler(self):
		pass

	def graphics_handler(self):
		self.screen.fill((0,0,0))
		self.plot_renderer.blit_graphs()

		# image_renders = self.image_renderer.get_render_requests()
		# for image in image_renders:
		# 	self.screen.blit(image["surface"], image["object"])
		# pygame.event.post(pygame.event.Event(IMAGE_UPDATE))

		# for text in text_renders:
		# 	self.screen.blit(text["surface"], text["object"])
		# pygame.event.post(pygame.event.Event(TEXT_UPDATE))
		pygame.display.update()
		pass

	def run(self):
		while True:
			self.event_handler()
			self.key_handler()

			self.graphics_handler()

			self.clock.tick(FPS)