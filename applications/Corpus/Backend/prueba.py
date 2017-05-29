# -*- coding: utf-8 -*-

"""file = open("/corpora/vert/fullcorpus.vrt","r").read()
file = file.replace(" ","	")

filew = open("/corpora/vert/fullcorpus.vrt","w")
filew.write(file)
"""

from tfIdf import tfIdf
from Bayes import Bayes

model = tfIdf()
l = model.search("La noche de terror va a empezar")
for i,j in l:
	print j

model = Bayes()
print model.neg["terror"]
tmp = model.evalStr("La noche de terror va a empezar")
print tmp
