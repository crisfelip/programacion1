#-----mostrar listas------# 
def mostrarLista (lista):
  for elemento in lista :
    print (elemento)

edades = [13,25,18,45,20,15,77,18]
nombres = ['sara','alberto','ximena','maria jose','karla','cristian']
mostrarLista(edades)
mostrarLista(nombres)


print ('#'*20)
# Dada una lista de números enteros muestre en pantalla el número más grande, 
# el más pequeño y el promedio de la lista
def infoList(lista):
  mayor = max (lista)
  menor = min (lista)
  acumulador = 0
  for elemento in lista :
    acumulador += elemento
  sizeList =   len (lista)
  promedio = acumulador / sizeList
  print (f'el número mayor en la lista es el {mayor}, el menor {menor} y el promedio {promedio}')
edades = [23,22,12,45,17,33,77,18]
infoList(edades)
print('#'*20)

#saludar n veces 

def saludar (cantidad = 0):
    print ('hola'* cantidad)
saludar (3)

print ('#'*20)

#Que devuelva todos los números pares de una lista de números enteros
#para los impares de una lista solo es cambiar en la linea 41 2==0 a 2==1 
def paresLista(lista):
  pares = []
  for elemento in lista:
    if elemento % 2 == 0 :
      pares.append (elemento)
  return pares

edades = [23,22,12,45,17,33,77,18]
edadesPares = paresLista(edades)
print (edadesPares)

print ('#'*20)

#Que devuelva únicamente los elementos mayores a 24
def mayoresLista(lista):
  mayores = []
  for elemento in lista:
    if elemento > 24 :
      mayores.append (elemento)
  return mayores
edades = [23,22,12,45,17,33,77,18]
edadesMayores = mayoresLista(edades)
print (f'las edades mayores de 24 son : {edadesMayores} ')

print ('#'*20)
#Se sabe que el IMC se calcula dividiendo el peso por la altura al cuadrado, 
#realice una función que lo calcule.
def calcularIMC (peso, altura):
  return peso /(altura**2)
imc = calcularIMC(67, 1.74)
print (imc)


print ('#'*20)

# Crea una función que sirva para despedirte del que esta ejecutando el código
def chao():
  print ("fue un gusto tenerte aprendiendo!!")
chao()

print ('#'*20)

print(f'nombre la función: {chao.__name__}')