#graphics_helper.py
import pygame
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

class TextRenderer:
	def __init__(self):
		self.requests = []	
		pygame.font.init()

	#Adds a text message to the rendering queue
	def render(self, text:str, x:int, y:int, size=16, speed=0.5, static=False, foreground=(255,255,255), background=(0,0,0)):
		font = pygame.font.Font(dir_path + '/../../res/fonts/EightBitDragon-anqx.ttf', size)
		self.requests.append({
			"message": text,
			"x": x,
			"y": y,
			"font": font,
			"str": "",
			"progress": 0,
			"speed": speed,
			"static": static,
			"background": background,
			"foreground": foreground
		})

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
			text = self.requests[i]["font"].render(self.requests[i]["str"], True, self.requests[i]["foreground"], self.requests[i]["background"])
			textRect = text.get_rect()
			textRect.center = (self.requests[i]["x"], self.requests[i]["y"])
			display.append({
				"surface": text, 
				"object": textRect
				})
		return display