neg = open("./corpus/Negativas.vrt",'r').read()
pos = open("./corpus/Positivas.vrt",'r').read()

file = open("./corpus/fullcorpus.vrt",'w')
file.write(neg+"\n")
file.write(pos)
file.close()