#Escribir una función que determine la frecuencia de cada
# carácter en una cadena dada y devuelva un diccionario

cadenaPalabras = "Había una conexión de corazón a corazón entre ellos z z z z t t t t t "


listaPalabras = cadenaPalabras.split()

frecuencia_palabra = []
for i in listaPalabras:
    frecuencia_palabra.append(listaPalabras.count(i))

print("oración\n" + cadenaPalabras +"\n")
print("palabras\n" + str(listaPalabras) + "\n")
print("Frecuencia_de repetición\n" + str(frecuencia_palabra) + "\n")
