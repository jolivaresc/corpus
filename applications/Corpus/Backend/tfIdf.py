# -*- coding: utf-8 -*-
from pickle import load

"""
* Clase que se encarga de evaluar mediante tfIdf una cadena para determinar
* los resultados de búsqueda dada esa cadena.
"""

class tfIdf:

	def __init__(self):
		self.idf = load(open("./models/idf.d",'r'))
		self.tf = load(open("./models/tf.d","r"))
		self.index = load(open("./models/index.d","r"))

	def eval(self,st,doc):
		if st in self.idf:
			k = self.idf[st]
		else:
			k = 1
		if st+"_"+str(doc) in self.tf:
			t = self.tf[st+"_"+str(doc)]
		else:
			t = 0
		return (float(t)/float(self.tf[str(doc)]))*float(k)

	def search(self,st):
		st = st.split(" ")
		l = []
		flg = True
		for i in st:
			for j in range(1,101):
				if flg:
					cad = self.index[j].replace("\t"," ")
					l.append((self.eval(i,j),cad))
				else:
					tmp = l.pop(j-1)
					val = tmp[0] + self.eval(i,j)
					l.insert(j,(val,tmp[1]))
			flg = False
		l.sort()
		l.reverse()
		return l

