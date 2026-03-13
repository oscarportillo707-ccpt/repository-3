Algoritmo Divisibles
	
	Definir numEntrada Como Entero
	
	Escribir "Ingrese un número para operar: "
	Leer numEntrada
	
	Si numEntrada MOD 3 = 0 O numEntrada MOD 5 = 0 Entonces
		
		Si numEntrada MOD 3 = 0 Entonces
			Escribir "Verdadero"
			Escribir "Es divisible entre 3"
		FinSi
		
		Si numEntrada MOD 5 = 0 Entonces
			Escribir "Verdadero"
			Escribir "Es divisible entre 5"
		FinSi
		
	SiNo
		Escribir "Falso"
		Escribir "No es divisible ni por 3 ni por 5"
	FinSi
	
FinAlgoritmo

// el algoritmo se ha ejecutado asi para que este mas explicado 
// el or siempre se respeta ya que el programa se cumple con que se ejecute solo alguna de las 2 
// solo se le añadieron mas detalles y a la hora de poner un numero divisible entre ambos 
// se cumpliran ambas 
// pero el objetivo se cumple poruqe siempre se utiliza el or 
// poruqe siempre se ejecutara mientras se cumpla alguna de las 2 
