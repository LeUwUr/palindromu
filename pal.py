frase = input("ingrese una frase: ")

frase_sin_espacios = frase.replace(" ","")

if frase_sin_espacios.islower() == False:
 frase_sin_espacios = frase_sin_espacios.lower()

frase_invertida = frase_sin_espacios[::-1]

if frase_invertida == frase_sin_espacios:
	print("la frase: "+str(frase)+" es un palindromo. owo")

else: print("la frase: "+str(frase)+"no es un palindromo. unu")



