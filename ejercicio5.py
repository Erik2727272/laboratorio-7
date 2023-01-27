#Escribir una función que determine la longitud de la
# subcadena más larga que contiene solo dígitos.

cadena="77577 44 7899  1123 334346 42 1 0 0 0"
lista=[]
palabras = []
recolectador =0
separador = 0
subcadena = cadena.split()
print("CADENA")
print(cadena)
longitud = list(map(len, subcadena))
print(longitud)

longitud_mayor=0
palabra_mas_larga=None

for palabra in subcadena:
    if len(palabra) >= longitud_mayor:
        longitud_mayor = len(palabra)
        palabra_mas_larga= palabra
print("La subcadena con mas digitos  es: ")
print(palabra_mas_larga)

