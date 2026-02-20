Algoritmo Sucesión_Fibonacci2
	// una sfb  es la suma de los
	// numeros que tenemos antes hasta llegar al numero 
	// que indicamos
	
	// entrada de datos 
	
	Escribir  " Escriba un numero para ejecutar el algoritmo" 
	leer numeroEntrada
	
	// sucecion logica 
	// and indica que ambos elementos deben ser true 
	// para que la respuesta sea verdadera 
	// or que indica que solo una de la expreciones necesita ser 
	// verdadera 
	// not niega una exprecion
	//  and y not !
	
	Definir  contador, suma, anterior Como Entero;
	contador = 0
	suma = 0;
	anterior = 0
	Mientras numeroEntrada > contador Hacer
		// guardar el estado del contador 
		// lo vamos a suar con su estado anterior
		anterior = contador
		contador = contador + 1
		suma = contador + anterior
		Escribir  contador ,"+" , anterior, "=", suma
	Fin Mientras
FinAlgoritmo
