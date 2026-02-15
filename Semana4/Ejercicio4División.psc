Algoritmo DIVISION
	Definir num1, num2, resultado Como Real
	Escribir 'Ingrese el primer número: '
	Leer num1
	Escribir 'Ingrese el segundo número: '
	Leer num2
	Si num2<>0 Entonces
		resultado <- num1/num2
		Escribir ' El resultado de la división es: ', resultado
	SiNo
		Escribir ' Error: no se puede dividir entre cero '
	FinSi
FinAlgoritmo
