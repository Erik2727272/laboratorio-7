#Escribir una función que reemplace todas las apariciones
# de una subcadena en una cadena dada con otra subcadena
# dada.

cadena=" Una palabra tras una palabra tras otra es poder"
subcadena= "pérdida"
separacion= cadena.split()
nueva_cadena = cadena.replace("palabra", "8989", 3)
nueva_separación=nueva_cadena.split()

print(separacion)

print(nueva_cadena)
