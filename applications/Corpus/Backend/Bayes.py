# -*- coding: utf-8 -*-
from pickle import load

class Bayes:

	def __init__(self):
		self.pos = load(open("./models/pos.d",'r'))
		self.neg = load(open("./models/neg.d","r"))
		self.sar = load(open("./models/sar.d","r"))

	def eval(self,st):
		if st in self.pos:
			p = self.pos[st]
		else:
			p = 1
		if st in self.neg:
			n = self.neg[st]
		else:
			n = 1
		if st in self.sar:
			s = self.sar[st]
		else:
			s = 1
		return [p,n,s]

	def evalStr(self,st):
		st = st.split(" ")
		p = 0.5
		s = 1.0
		n = 0.5
		for i in st:
			print i
			tmp = self.eval(i)
			print p
			print n
			print s
			p *= float(tmp[0])
			n *= float(tmp[1])
			s *= float(tmp[2])
		return [p,n,s]