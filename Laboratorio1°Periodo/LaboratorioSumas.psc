Algoritmo Sumas
	
	Definir numeroEntrada, suma Como Entero
	
	suma = 0 
	
	Escribir "Ingrese un número para sumar o (-1 para terminar): "
	Leer numeroEntrada 
	
	Mientras numeroEntrada <> -1 Hacer
		suma = suma + numeroEntrada
		Escribir "Su total es: " , suma 
		Escribir "Ingrese otro numero para sumar o (-1 si desea terminar): "
		Leer numeroEntrada 
	FinMientras
	
Escribir "El total de la suma realizada es: " , suma 
	
FinAlgoritmo
