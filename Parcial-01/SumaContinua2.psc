Algoritmo SumaContinua
	
	Definir numeroEntrada, suma Como Entero
	
	suma = 0 
	
	Escribir "Ingrese un número positivo para sumar o negativo para terminar: "
	Leer numeroEntrada 
	
	Mientras numeroEntrada >= 0 Hacer
		suma = suma + numeroEntrada
		Escribir "Su total es: " , suma 
		Escribir "Ingrese otro número positivo para sumar o negativo si desea terminar: "
		Leer numeroEntrada 
	FinMientras
	
Escribir "El total de la suma de los números positivos es: " , suma 
	
FinAlgoritmo
