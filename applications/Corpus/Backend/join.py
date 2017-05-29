# -*- coding: utf-8 -*-
import os
import argparse

"""
* Modo de uso: python join.py -i Textos_Originales -o Textos_Fl -f Negativo
"""

parser = argparse.ArgumentParser()
parser.add_argument("-i","--input",help="Carpeta con los archivos de entrada")
parser.add_argument("-o","--output",help="Carpeta donde se guardarán los archivos de salida")
parser.add_argument("-f","--felling",help="Tipo de sentimiento que se expresa en el corpus")
args = parser.parse_args()

if args.input:
    docs = os.listdir("./"+args.input)
    if args.output:
        ex = args.output
    else:
        ex = "corpus.vrt"
    try:
        file2 = open(ex,"w")
        for i in docs:
            print("Procesando: "+i)
            file2.write("<doc name=\""+i+"\">\n")
            file = open("./"+args.input+"/"+i,"r").read()
            file = file.split("\n")
            for j in file:
                if len(j)>0:
                    row = j.split(" ")
                    for k in row[0:3]:
                        file2.write(k+" ")
                    file2.write(args.felling+"\n")
            file2.write("</doc>\n")
        file2.close()
    except:
        print("Ocurrió un problema durante la unión")
else:
    print("No se ingresó un archivo para procesar")
