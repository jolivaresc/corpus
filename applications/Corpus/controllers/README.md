## Proyecto Final de Procesamiento de Corpus Textuales y Orales


Los archivos *.py para realizar el análisis del corpus se encuentran dentro de el directorio "corpus/applications/Corpus/controllers", es necesario contar con las siguientes herramientas: 

	Python 2.7: https://www.python.org/
	Freeling: http://nlp.lsi.upc.edu/freeling/node/1
	Manatee: https://nlp.fi.muni.cz/trac/noske/wiki/Downloads

Adicional a los programas para analizar el corpus, en la misma carpeta se encuentran los archivos que se utilizan para generar la página web que despliega los resultados del análisis. 
Estos archivos son:

	appadmin.py
	default.py
	httpserver.log

## Proceso de compilación
Una vez que se cuenta con las herramientas antes mencionadas, es necesario compilar el corpus, para esto,
será necesario realizar los siguientes pasos:

	python freeling.py -i ./corpus/Positivas -o ./corpus/PositivasPOS
	python freeling.py -i ./corpus/Negativas -o ./corpus/NegativasPOS

con esto obtendremos el valor POS de los tokens dentro de nuestros archivos.

Posteriormente se etiquetarán todos nuestros archivos, generando así un archivo vertical

	python join.py -i ./corpus/PositivasPOS -o Positivas.vrt -f Positivo
	python join.py -i ./corpus/NegativasPOS -o Negativas.vrt -f Negativo

Ahora será necesario juntar ambos archivos etiquetados en uno solo, para esto se ejecuta

	python fulljoin.py

Con esto se nos generará el archivo "fullcorpus.vrt", dicho archivo debe ser copiado (no se debe mover) al directorio "./corpora/vert"
que se encuentra dentro de este repositorio. Una vez que se copia el archivo, se deberá copiar o mover el directorio "corpora" a la
raíz del equipo, quedando localizado en "/corpora".

Nota: si se quieren hacer análisis con otro tipo de sentimientos tales como Sarcasmo, se deberá ingresar al archivo
fullcorpus.vrt y cambiar el sentimiento de forma manual.

Para compilar el corpus mediante manatee, dentro de la terminal del equipo se debe ejecutar el siguiente comando:
	
	compilecorp fullcorpus

Con esto, manatee nos permitirá obtener las concordancias en nuestro corpus.

## Proceso de Entrenamiento
Una vez que compilamos nuestro corpus, es necesario generar los modelos que nos van a permitir hacer el análisis
de sentimientos, la búsqueda de términos y las posibles colocaciones entre dos palabras.

	python trainer.py

## Proceso de Evaluación
Primero es necesario importar los códigos y clases que se encargan de hacer las evaluaciones de los modelos generados
durante el entrenamiento

	from Bayes import Bayes
	from concordance import get
	from MI import MI
	from tfIdf import tfIdf

A continuación se pondrán algunos ejemplos de prueba de los modelos.

Para ver cómo se indexaría una búsqueda mediante tfIdf, se utilizaría lo siguiente:

	model = tfIdf()
	l = model.search("La noche de terror va a empezar")
	for i,j in l:
		print j

El método search, nos regresa una lista de tuplas, en las cuales se tiene el valor obtenido mediante tfIdf y el título del texto

Para ver si hay colocación entre dos tokens se haría de la siguiente forma:

	model = MI()
	mi = model.eval("la","historia")
	print mi

El método eval retorna el valor de la información mutua entre dos tokens

Para realizar el análisis de sentimientos

	model = Bayes()
	tmp = model.evalStr("La noche de terror va a empezar")
	print tmp

El método evalStr nos retorna una lista con los valores de las probabilidades de que la cadena evaluada sea positiva, negativa y sarcasmo en ese orden.

Finalmente, para hacer uso de manatee y ver las concordancias que puede haber dentro del corpus se podría realizar de las siguientes maneras:

	res = get("México")
	print res

De esta forma sólo se está evaluando una cadena de texto simple, si se quisiera enviar una query, se tendría que hacer de la siguiente manera:

	res = get("\'\"México\"\'",query=True)
	print res

Donde \'\"México\"\' es nuestra query a evaluar

Se puede ejecutar el archivo prueba.py, ahí están implementadas las líneas de código antes mencionadas.
