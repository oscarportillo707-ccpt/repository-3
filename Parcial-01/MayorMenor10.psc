Algoritmo MayorMenor
	
	Definir num1, num2 Como Entero
	
	Escribir "Ingrese el primer número: "
	Leer num1
	
	Escribir "Ingrese el segundo número: "
	Leer num2
	
	Si num1 > num2 Entonces
		Escribir "El número mayor es: ", num1
		Escribir "El número menor es: ", num2
	SiNo
		Si num2 > num1 Entonces
			Escribir "El número mayor es: ", num2
			Escribir "El número menor es: ", num1
		SiNo
			Escribir "Ambos números son iguales"
		FinSi
	FinSi
	
FinAlgoritmo
