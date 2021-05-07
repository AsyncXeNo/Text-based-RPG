#plot_rendering
import pygame
import matplotlib as plot
plot.use("Agg")
import pylab
import utils
import matplotlib.backends.backend_agg as agg


class PlotRenderer: #Math plot, tho, chill

	def __init__(self):
		self.requests = []

	def create_canvas (self,rang,function, size, pos, surface):
		fig = pylab.figure(figsize=list(size), # Inches
			  dpi=1, facecolor=(0.0,0.0,0.0,1.0)    # 100 dots per inch, so the resulting buffer is 400x400 pixels
			  )
		ax = fig.gca()
		ax.set_axis_off()
		ax.set_facecolor((0.0,1.0,0.0,1.0))
		ax.plot(rang,function,linewidth=100)

		canvas = agg.FigureCanvasAgg(fig)
		canvas.draw()
		s = canvas.get_width_height()
		renderer = canvas.get_renderer()
		raw_data = renderer.tostring_argb()
		id_ =  utils.code_generator(6)
		self.requests.append({"data":raw_data, "size": s, "pos": pos, "id": id_, "surface": surface})
		return id_

	def get_render_requests(self):
		return self.requests


	def remove_request(self, id_arg):
		req_to_remove = None
		for request in self.requests:
			if request["id"] == id_arg:
				req_to_remove = request
		
		if req_to_remove:
			self.requests.remove(req_to_remove)
			print(f'{id} removed')
		else:
			print('no graph with this id')

	def blit_graphs(self):
		for render in self.get_render_requests():
			#print(render["data"])
			surf = pygame.image.fromstring(render["data"], render["size"], "ARGB")
			render["surface"].blit(surf, render["pos"])

