# -*- coding: utf-8 -*-

import commands

"""
* Código que se encarga de obtener las colocaciones, ya sea de un conjunto
* de tokens o de un query
"""

def get(st,query=False):
	if query:
		return commands.getoutput("corpquery fullcorpus "+st)
	else:
		return commands.getoutput("corpquery fullcorpus \'\""+st+"\"\'")
