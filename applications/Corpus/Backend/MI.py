# -*- coding: utf-8 -*-
from numpy import log2
from pickle import load

class MI:

	def __init__(self):
		self.words = load(open("./models/words.d",'r'))
		self.ngrams = load(open("./models/ngrams.d","r"))
		self.count = self.count()

	def count(self):
		cnt = 0
		for i in self.words:
			cnt += self.words[i]
		return cnt

	def eval(self,str1,str2):
		try:
			sup = float(self.ngrams[str1+"_"+str2])/float(self.count)
			inf = float(self.words[str1]) * float(self.words[str2])
			inf = inf/(float(self.count)*float(self.count))
			return log2(sup/inf)
		except:
			return 0 
