#graphics_helper.py
import pygame
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

class TextRenderer:
	def __init__(self):
		self.requests = []	
		pygame.font.init()
		self.main_font = pygame.font.Font(dir_path + '/../../res/fonts/EightBitDragon-anqx.ttf', 28)

	#Adds a text message to the rendering queue
	def render(self, text:str, x:int, y:int, speed=1):
		self.requests.append({
			"message": text,
			"x": x,
			"y": y,
			"str": "",
			"speed": speed,
			"background": (0,0,0),
			"foreground": (255,255,255)
		})

	#Return an array with all the surfaces to draw as well as their transforms(?)
	def get_render_requests(self):
		display = []
		for i in range(len(self.requests)):
			if len(self.requests[i]["str"]) < len(self.requests[i]["message"]):
				self.requests[i]["str"] = self.requests[i]["message"][:len(self.requests[i]["str"])+self.requests[i]["speed"]] 
			text = self.main_font.render(self.requests[i]["str"], True, self.requests[i]["foreground"], self.requests[i]["background"])
			textRect = text.get_rect()
			textRect.center = (self.requests[i]["x"], self.requests[i]["y"])
			display.append({
				"surface": text, 
				"object": textRect
				})
		return display