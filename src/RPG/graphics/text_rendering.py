#graphics_helper.py
import pygame
import os

from utils import code_generator
from logger import Logger

dir_path = os.path.dirname(os.path.realpath(__file__))

logger = Logger('graphics/text_renderer.py')


class TextRenderer:
	def __init__(self):
		self.requests = []	
		pygame.font.init()

	#Adds a text message to the rendering queue
	def render(self, text:str, x:int, y:int, surface, size=16, speed=0.5, static=False, foreground=(255,255,255)):

		while True:
			id = code_generator(6)
			unique = True

			for request in self.requests:
				if request["id"] == id:
					unique = False

			if unique:
				break

		font = pygame.font.Font(dir_path + '/../../../res/fonts/EightBitDragon-anqx.ttf', size)
		self.requests.append({
			"message": text,
			"x": x,
			"y": y,
			"font": font,
			"str": "",
			"progress": 0,
			"speed": speed,
			"static": static,
			"foreground": foreground,
			"id": id,
			"surface": surface
		})

		return id

	#called every text update event
	def tick(self):
		for i in range(len(self.requests)):
			if (self.requests[i]["speed"] == 0):
				self.requests[i]["str"] = self.requests[i]["message"]
			self.requests[i]["progress"] += self.requests[i]["speed"]
			if(self.requests[i]["message"] != self.requests[i]["str"]):
				if(self.requests[i]["progress"] >= 1):
					self.requests[i]["progress"] -= 1
					self.requests[i]["str"] = self.requests[i]["message"][:len(self.requests[i]["str"])+1]
					if self.requests[i]["static"]:
						width,_ = self.requests[i]["font"].size(self.requests[i]["str"][-1])
						self.requests[i]["x"] += width/2


	#Return an array with all the surfaces to draw as well as their transforms(?)
	def get_render_requests(self):
		display = []
		for i in range(len(self.requests)):
			text = self.requests[i]["font"].render(self.requests[i]["str"], True, self.requests[i]["foreground"])
			textRect = text.get_rect()
			textRect.center = (self.requests[i]["x"], self.requests[i]["y"])
			blit_surface = self.requests[i]["surface"]
			display.append({
				"blit_surface": blit_surface,
				"surface": text, 
				"object": textRect
				})
		return display

	def remove_request(self, id):
		req_to_remove = None
		for request in self.requests:
			if request["id"] == id:
				req_to_remove = request
		
		if req_to_remove:
			self.requests.remove(req_to_remove)
			logger.log_neutral(f'{id} removed')
		else:
			logger.log_warning('no text renders with this id')

		for render in self.requests:
			logger.log_neutral(f'text {render}')

	def blit_requests(self):
		for image in self.get_render_requests():
			image["blit_surface"].blit(image["surface"], image["object"])
