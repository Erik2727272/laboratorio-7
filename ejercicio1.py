#Escribir una función que determine si una cadena es un
# palíndromo (se lee igual en ambos sentidos) o no:

variable1 = 0
variable2 = 0
texto = input("Ingrese la palabra que desea evaluar: ")
for i in reversed(range(0, len(texto))):
  if texto[i].lower() == texto[variable2].lower():
    variable1 += 1
  variable2 += 1
if len(texto) == variable1:
  print("LA PALABRA ES PALÍNDROMO")
else:
  print("LA PALABRA NO ES PALÍNDROMO")
