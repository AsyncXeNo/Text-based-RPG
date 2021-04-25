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

	def create_canvas (self,rang,function, size, pos):
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
		self.requests.append({"data":raw_data, "size": s, "pos": pos, "id": id_})
		return id_

	def get_render_requests(self):
		return self.requests


	def remove_request(self, id_arg):
		for r in  range(len(self.requests)):
			if self.requests[r]["id"] == id_arg:
				self.requests.pop(r)
				#print(self.requests)

