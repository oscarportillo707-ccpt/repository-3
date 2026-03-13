Algoritmo SUCESION_FIBONACCI
	Definir NumeroFinal, NumeroAnterior, NumeroActual, Siguiente, contador Como Entero
	Escribir '¿Cuantos numeros de Fibonacci desea ver?'
	Leer NumeroFinal
	NumeroAnterior <- 1
	NumeroActual <- 2
	contador <- 1
	Mientras contador<=NumeroFinal Hacer
		Escribir NumeroAnterior
		Siguiente <- NumeroAnterior+NumeroActual
		NumeroAnterior <- NumeroActual
		NumeroActual <- Siguiente
		contador <- contador+1
	FinMientras
FinAlgoritmo
