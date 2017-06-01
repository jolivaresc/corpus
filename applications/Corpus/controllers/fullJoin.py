"""
* Código que se encarga de juntar los archivos verticales que se tengan por separado
"""

neg = open("./corpus/Negativas.vrt",'r').read()
pos = open("./corpus/Positivas.vrt",'r').read()

file = open("./corpus/fullcorpus.vrt",'w')
file.write(neg+"\n")
file.write(pos)
file.close()