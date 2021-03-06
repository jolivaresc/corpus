# -*- coding: utf-8 -*-
import os
import argparse

"""
* Modo de uso: python freeling.py -i Textos_Originales -o Textos_Fl
*
* Código que se encarga de generar el etiquetado POS de un conjunto de textos 
* que formaran parte del corpus, se debe de ingresar el directorio con los archivos
* de entrada y de manera opcional el directorio donde se almacenarán los textos
* con su notación POS
"""

parser = argparse.ArgumentParser()
parser.add_argument("-i","--input",help="Directorio con los archivos de entrada")
parser.add_argument("-o","--output",help="Directorio donde se guardarán los archivos de salida")
args = parser.parse_args()

if args.input:
    docs = os.listdir("./"+args.input)
    for i in docs:
        if not i.__eq__("tmp"):
            print("Procesando: "+i)
            file = open("./"+args.input+"/"+i,"r").read()
            file = file.split("\n")
            file2 = open("./"+args.input+"/tmp","w")
            for j in file[5:]:
                file2.write(j+"\n")
            file2.close()
            st = "FREELINGSHARE=/usr/local/share/freeling/ analyzer -f /usr/local/share/freeling/config/es.cfg "
            st += "--outlv tagged "
            st+=" < "+"./"+args.input+"/tmp"
            if args.output:
                ex = args.output
            else:
                ex = "exit"
            try:
                os.mkdir(ex)
            except:
                pass
            st+=" > \""+"./"+ex+"/"+i+"\""
            os.system(st)
        
else:
    print("No se ingresó un archivo para procesar")
