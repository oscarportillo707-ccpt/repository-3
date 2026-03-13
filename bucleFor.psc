Funcion respuesta <- validar ( usuario, pass )
	respuesta = Falso
	Escribir "validar usuario"
	
	Si usuario == "EverSorto" Entonces
		Si pass == "ever" Entonces
			Escribir  "Bienvenido"
			respuesta = Verdadero
		SiNo
			Escribir  "fallo de password"
		Fin Si
	SiNo
		Escribir  "fallo de usuario"
	Fin Si
Fin Funcion
// funcion 
// encapsulacion -> siempre me va a dar la misma salidad 
// va a crear algo que se llama scope 


// las variable siempre tiene que tener sentido
//  edad =32  funcion entero <- registrarpersona(edad)
//  funcion entero <- registrarpersona(xw)
//  nombre en clave de las variables nombre de ex, nombres persojes, fechas.....
//   xw = "Hola como estas"
//   nomeclatura   camelCase  sneskCase
//  glosario 
//  ADN 
// ARN
// femur
Algoritmo bucleFor
	// indica que vamos a repetir los pasos o un algoiritmo en un numero de pasos definido
	
	// yo quiero utilizar la cuenta de correo 
	//pero si me equivoco mas de 4 veces 
	// se nloquea momentaneamente
	
	
	
	Escribir  "registrar usuario"
	leer usuario
	
	Escribir  "registrar PASS"
	leer pass
	
	Definir  i Como Entero
	resultado = validar ( usuario, pass )
	Para i <- 1 Hasta 5 Con Paso  1 Hacer
		si resultado == Verdadero
			Escribir  "Bienvenida"
			Escribir  "Indicaciones" 
		FinSi
		resultado = false
	Fin Para
	
	// for  i = 0 ; instruccionLogica  i> 20 ;
	// i = i + 1  ....19 detener el bucle 
	
	
	
	// funcion es una estructura de codigo
	// que se puede repetir pero simpre se llama a la misma instancia 
	// vajo el mismi nombre
	
	// palabra re.    si nos devuelve algo   () 
	// argumentos: son las entradas de las funcines van entre parentesis y puede ser 
	// mas de una o ninguna. 
	// carateristicas  -> el carro es rojo 
	//                    nosotros somos feos 
	// 						edad 				32
	// 						boolean             Verdad o Falso
	//						objeto :  un objeto es aquella entidad
	//                      en progrmacion que modela en base a las clases 
	//                      las caracteristicas de un objeto de la vida real
	
	
	
	
FinAlgoritmo