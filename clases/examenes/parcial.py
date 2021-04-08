def separador ():
    print ('#'*30)

#---funciones calculadora---#

def sumar (valor1=0, valor2=0,valor3=0 ):
    return valor1 + valor2 + valor3
def restar (valor1=0, valor2=0, valor3=0 ):
    return valor1 - valor2 - valor3
def multiplicar (valor1=0, valor2=0, valor3=0 ):
    return valor1 * valor2 * valor3
def dividir (valor1=0, valor2=1, valor3=1 ):
    return valor1 / valor2 / valor3
def exponente (valor1=0, valor2=0, valor3=0 ):
    return valor1 ** valor2 ** valor3

def calculadora (accion, valor1, valor2, valor3):
    print (accion(valor1,valor2,valor3))

valor1=int (input('ingresar valor 1 porfavor : '))
valor2=int (input('ingresar valor 2 porfavor : '))
valor3=int (input('ingresar valor 3 porfavor : '))
separador ()
print ('realizando operaciones')
print ('sumando')
calculadora (sumar, valor1, valor2, valor3)
separador ()
print ('restando')
calculadora (restar, valor1, valor2, valor3)
separador ()
print ('multiplicando')
calculadora (multiplicar, valor1, valor2, valor3)
separador ()
print ('dividiendo')
calculadora (dividir, valor1, valor2, valor3)
separador ()
print ('exponencial')
calculadora (exponente, valor1, valor2, valor3)
separador ()

#--- listas en pantalla ---#
print ('lista nombres')
nombres = []
print (type(nombres))
print(nombres)
nombres = ['Santiago','Samuel','Aleja','camilo','pepito','carlos','juliana']
print (nombres)
separador()

print ('lista adultos')
adultos = []
print (type(adultos))
print(adultos)
adultos = ['dayana','laureano','fulano','sutano','pepito','manuela','juliana']
print (adultos)
separador()

print('lista mujeres')
nombres = []
print (type(nombres))
print(nombres)
nombres = ['Salome','Samanta','Alejandra','camila','pepita','carla','juliana']
print (nombres)
separador()

# --- calcular area del triangulo ---#

def area_triangulo (base=0, altura=0):
    return base * altura /2
Base = int(input('ingrese valor para la base : '))
Altura = int(input('ingrese valor para la altura : '))

print (area_triangulo(Base, Altura))
separador()

#--- dada la lista sacar promedio, maximo y minimo ---#

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

#--- serie fibonacci ---#
print ('la serie de fibonnaci es : ')
def fibo(n):
    if n < 2:
        return n
    return fibo(n-1)+fibo(n-2)

for x in range (20):
    print (fibo (x))

print ('profe puso muy duro ese ultimo punto jajajaja ')
print('solo me dio tiempo para hacer la sucesion :´(')