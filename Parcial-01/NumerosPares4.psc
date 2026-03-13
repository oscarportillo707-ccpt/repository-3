Algoritmo NumerosPares
	
	Definir N, contador, numero Como Entero
	
	Escribir "Ingrese cuantos numeros pares desea ver:"
	Leer N
	
	contador = 0
	
	Para numero = 1 Hasta N * 2 Hacer
		
		Si numero MOD 2 = 0 Entonces
			Escribir numero
			contador = contador + 1
		FinSi
		
	FinPara
	
FinAlgoritmo