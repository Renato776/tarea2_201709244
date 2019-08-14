import pydot
import os
class Matrix:
	def __init__(self,d_x,d_y):
		self.x = d_x
		self.y = d_y
		content = [[],[]]
		self.posicion = 0
		self.true_x = 0
		self.true_y = 0
		self.fila = False
	def to_lineal(self,pos_x,pos_y,modo_fila):
		if(modo_fila):
			self.posicion = pos_x*self.x + pos_y
			self.true_x = pos_x
			self.true_y = pos_y
			self.fila = True
			return self.posicion
		else:
			self.posicion = pos_y*self.y + pos_x
			self.true_x = pos_x
			self.true_y = pos_y
			self.fila = False
			return self.posicion
	def getNode(self):
		return "({},{})".format(self.true_x,self.true_y)
	def get_valid_node(self,c_x,c_y,parentesis):
		if(c_x == self.true_x and c_y == self.true_y):
			if(parentesis):
				return "ren"
			return "og"
		if(parentesis):
			return "\"({},{})\"".format(c_x,c_y)
		return "\"{},{}\"".format(c_x,c_y)
	def get_row(self,index):
		c = 0
		is_first = True
		result = ""
		while(c<self.x):
			if(is_first):
				result = result + self.get_valid_node(index,c,False)
				is_first = False
			else:
				result = result + " -> " + self.get_valid_node(index,c,False)
			c+=1
		return result
	def get_column(self,index):
		c = 0
		is_first = True
		result = ""
		while(c<self.y):
			if(is_first):
				result = result + self.get_valid_node(c,index,False)
				is_first = False
			else:
				result = result + " -> " + self.get_valid_node(c,index,False)
			c+=1
		return result
	def get_matrix_as_linear(self):
		c = 0
		result = ""
		is_first = True
		if(self.fila):
			while(c<self.y):
				c4 = 0
				while(c4 < self.x):
					if(is_first):
						result = result + self.get_valid_node(c,c4,True)
						is_first = False
					else:
						result = result +" -> "+ self.get_valid_node(c,c4,True)
					c4 += 1
				c+=1
		else:
			while(c<self.x):
				c4 = 0
				while(c4 < self.y):
					if(is_first):
						result = result + self.get_valid_node(c4,c,True)
						is_first = False
					else:
						result = result +" -> "+ self.get_valid_node(c4,c,True)
					c4 += 1
				c+=1
		return result
	def graph(self):
		resultado = "digraph Matrix { node [shape=box] graph [ranksep=0.25 nodesep=0.25]"+"\n"
		resultado = resultado + "og[label = \""+self.getNode()+"\",style=filled, fillcolor=blue] ; " + "\n"
		resultado = resultado + "edge [dir=back] edge [style=invis weight=100]" + "\n"
		c = 0
		while(c<self.y):
			resultado = resultado + "rank=same {"+self.get_row(c)+"}"+"\n"
			c+=1
		c = 0
		while(c<self.x):
			resultado = resultado + self.get_column(c) + "\n"
			c+=1
		resultado = resultado + "subgraph cluster_0 {style=filled; color=lightgrey; node [style=filled,color=white];"+"\n"
		resultado = resultado + "ren [label = \""+self.getNode()+"\",style=filled, fillcolor=red] ;" + "\n"	
		resultado = resultado + self.get_matrix_as_linear()+";"+"\n"
		resultado = resultado + "label = \"Linear\";"+"\n"
		resultado = resultado + "}"+"\n"
		resultado = resultado + "}"
		grafos = pydot.graph_from_dot_data(resultado)
		(g,)=grafos
		g.write_jpg('matrix.jpg')
		os.system('matrix.jpg')
