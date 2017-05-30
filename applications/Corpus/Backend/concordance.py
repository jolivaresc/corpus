import commands

def get(st,query=False):
	if query:
		return commands.getoutput("corpquery fullcorpus "+st)
	else:
		return commands.getoutput("corpquery fullcorpus \'\""+st+"\"\'")
