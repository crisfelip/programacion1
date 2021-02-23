pruebav = True
pruebaf = False
print (pruebaf)
print(pruebav)
pruebav = pruebaf
print(pruebaf)
edad = 20
estatura = 1.71
peso = 65
NOMBRE = "cristian felipe bustamante"
# edad mayor o igual que 18 
print ("#"*15,"mayor Edad", "#"*15)
ismayorEdad = edad >= 18
print (ismayorEdad)
# estatura menor que 1.70
print ("#"*15,"estatura promedio", "#"*15)
ismayorestatura = estatura < 1.70
print(ismayorestatura)
# peso diferente de 65 
print ("#"*15,"peso diferente de 65", "#"*15)
ispesodiferente = peso != 65
print (ispesodiferente)
# el apellido esta en el nombre completo? 
apellido = "bustamante"
isapellido = apellido in NOMBRE 
print ("#"*15,"apellido en nombre", "#"*15)
print (isapellido)
