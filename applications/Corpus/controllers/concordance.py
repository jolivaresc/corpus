# -*- coding: utf-8 -*-

import commands

"""
* Código que se encarga de obtener las colocaciones, ya sea de un conjunto
* de tokens o de un query
"""

def get(st):
	if st.startswith("q"):
		print "query"
		st = st[1:]
		return commands.getoutput("corpquery fullcorpus "+st)
	else:
		print "string"
		return commands.getoutput("corpquery fullcorpus \'\""+st+"\"\'")
