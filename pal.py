frase = input("ingrese una frase: ") # No te ocupo explicar aqui.

frase_sin_espacios = frase.replace(" ","") # A .replace se le ha indicado hacer una accion, la cual es eliminar los espacios si es que se le a añadido una frase, esto para que el programa detecte si es un palindromo.

if frase_sin_espacios.islower() == False: # Ya que se eliminaron los espacios, se comprueba que el string sea solo en minusculas.
 frase_sin_espacios = frase_sin_espacios.islower() # La funcion .islower convierte el string a minusculas con el fin de que el programa no se confunda al realizar la comprobacion.

frase_invertida = frase_sin_espacios[::-1] # Para invertir la frase se usa ::-1 para asignar a la nueva variable el string comenzando de la ultima posicion menos lo que nos dara una cadena al reves.

if frase_invertida == frase_sin_espacios:
	print("la frase: "+str(frase)+" es un palindromo. owo") # if comprueba si la frase es un palindromo, str es una abreviacion de 'string'; si la condicion se cumple, entonces la funcion te lo confirmara.

else: print("la frase: "+str(frase)+"no es un palindromo. unu") # De lo contrario, si no se cumple la funcion anterior, automaticamente te indicara que no es un palindromo.



