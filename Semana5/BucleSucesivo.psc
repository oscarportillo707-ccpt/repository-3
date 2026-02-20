Algoritmo Bucle 
	// bucle es algo que se repite hasta que una condición logica lo rompe 
	
	Definir contador Como Entero
	Escribir " Número del 0 al 100 "
	leer numeroEntrada 
	
	contador = 0
	resultado = 0 
	
	Mientras contador < numeroEntrada
		resultado = contador + contador 
		
		Escribir " El resultado es: ", contador ," = ", resultado 
		contador = contador  + 1 
	FinMientras
	
	Escribir  "password "
	leer pass
	
	
	Mientras pass <> "nombre de ella + fecha especial"   // ! = <> < >
		Escribir  " Romper bucle infinito opciones, 1:si 2:no "
		leer respuesta
		si respuesta == "2"
		FinSi
		si respuesta == "1"
			pass = "nombre de ella + fecha especial"
		FinSi
	FinMientras
	
	Escribir  " Final " 
	
	// exponentes
	// radicales 
	// parentesis
	// di y mul
	// suma yesta
	// contador  i  i++ i--   contador =+  contador = contador + contador
FinAlgoritmo 
