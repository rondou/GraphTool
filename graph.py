from graph_tool.all import *
from itertools import izip
from numpy.random import randint

g = Graph()

g.add_vertex(10)

# insert some random links
for s,t in izip(randint(0, 10, 10), randint(0, 10, 10)):
        g.add_edge(g.vertex(s), g.vertex(t))

graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=18, output_size=(200, 200), output="two-nodes.png")
