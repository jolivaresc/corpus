# -*- coding: utf-8 -*-

"""file = open("/corpora/vert/fullcorpus.vrt","r").read()
file = file.replace(" ","	")

filew = open("/corpora/vert/fullcorpus.vrt","w")
filew.write(file)
"""

from Bayes import Bayes
from concordance import get
from MI import MI
from tfIdf import tfIdf

model = tfIdf()
l = model.search("La noche de terror va a empezar")
for i,j in l:
	print j

model = MI()
mi = model.eval("la","historia")
print mi

model = Bayes()
tmp = model.evalStr("La noche de terror va a empezar")
print tmp

res = get("México")
print res

print ">>>>>>>>>>>>>>>>>>"

res = get("\'\"México\"\'",query=True)
print res
