#Escribir una función que determine la longitud de la
# subcadena más larga que no contiene ninguna letra
# repetida.

cadena="Nieva como hace mucho tiempo no lo hacía"
lista=[]
palabras = []
recolectador =0
separador = 0
subcadena = cadena.split()

longitud = list(map(len, subcadena))
print(longitud)

longitud_mayor=0
palabra_mas_larga=None

for palabra in subcadena:
    if len(palabra) >= longitud_mayor:
        longitud_mayor = len(palabra)
        palabra_mas_larga= palabra
print("La palabra con mas caracteres es: ")
print(palabra_mas_larga)