# -*- coding: utf-8 -*-
from collections import defaultdict
from collections import Counter
from numpy import log10
from pickle import dump

def toFile(name,obj):
	file = open(name,'w')
	dump(obj,file)
	file.close()

def p(di,lenWords,classFrec=50,l=0.01):
	for i in di:
		di[i] = (float(di[i])+l)/(float(classFrec)+(float(lenWords)*l))
	return di

corpus = open("./corpus/fullcorpus.vrt",'r').read()
corpus = corpus.split("\n")

N = 100.0
dtf = defaultdict(set)
sarcFrec = set()
positivo = {}
negativo = {}
sarcasmo = {}
words = []
doc = 0
tf = {}
idf = {}
docs = {}

for i in corpus:
	if i.startswith('<doc'):
		doc +=1
		tmp = i.split("\"")
		docs[doc] = tmp[1]
		tf[str(doc)] = 0
	elif i.startswith('</doc'):
		nothing = ""
	else:
		tmp = i.split("\t")
		tf[str(doc)] += 1
		words.append(tmp[0])
		if doc < 51:
			if tmp[0] in negativo:
				negativo[tmp[0]] += 1
			else:
				negativo[tmp[0]] = 1
		else:
			if tmp[0] in positivo:
				positivo[tmp[0]] += 1
			else:
				positivo[tmp[0]] = 1
		if tmp[3].__eq__("Sarcasmo"):
			sarcFrec.add(doc)
			if tmp[0] in sarcasmo:
				sarcasmo[tmp[0]] += 1
			else:
				sarcasmo[tmp[0]] = 1
		dtf[tmp[0]].add(doc)
		if tmp[0]+'_'+str(doc) in tf:
			tf[tmp[0]+'_'+str(doc)] += 1
		else:
			tf[tmp[0]+'_'+str(doc)] = 1

ngrams = []
for i in range(0,len(words)-1):
	ngrams.append(words[i]+"_"+words[i+1])

for i in dtf:
	tmp = len(list(dtf[i]))
	idf[i] = log10(N/float(tmp))

l = len(list(set(words)))
ngrams = Counter(ngrams)
words = Counter(words)
positivo = p(positivo,l)
negativo = p(negativo,l)
sarcasmo = p(sarcasmo,l,classFrec=len(list(sarcFrec)))

toFile("./models/ngrams.d",ngrams)
toFile("./models/words.d",words)
toFile("./models/tf.d",tf)
toFile("./models/idf.d",idf)
toFile("./models/index.d",docs)
toFile("./models/pos.d",positivo)
toFile("./models/neg.d",negativo)
toFile("./models/sar.d",sarcasmo)