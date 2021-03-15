for iteracion in range (10):
    print (iteracion)
print ('#'*60)
#se ven los numeros desde el 0 al 9 
for iteracion in range (10):
    print (iteracion+1)
print ('#'*60)
# se ven los numeros del 1 al 10 
for iteracion in range (1,11):
    print(iteracion)
print ('#'*60)
#se ven del 1 al 10 
for iteracion in range (1,14,2):
    print (iteracion)
# se van a ver los numeros del 1 al 14 pero saltando de 2 en dos 1,,3,5,7...
residuo = 5%4
print (residuo)
residuo = 4%4
print (residuo)
print ('#'*60)
for iteracion in range (1,11):
    if (iteracion % 2 == 0):
        print(iteracion)
#asi podemos mostrar solo los numeros pares que se encuentran del 1 al 10 
print ('#'*60)
for iteracion in range (1,11):
    if (iteracion % 2 != 0):
        print(iteracion)
#asi podemos ver los impares solo manbio de ==0 a !=0 para los impares 
print ('#'*60)
for iteracion in range (1,11):
    if (iteracion % 2 == 0):
        print (iteracion, '--> Es un número par')
    else:
        print(iteracion, '--> Es un número impar')
print ('#'*60)
#asi mostramos cuales son los numeros pares e impares sin saltarse ninguno de ellos 
rango = int (input('ingrese el rango máximo : '))

opcion = int (input('''
    1- Ver solo impares
    2- Ver solo pares
    3- Ver las dos clasificaciones
    n- cualquier número para mostrar nada
'''))
print ('☺'*30)
if (opcion == 1 ):
    for iteracion in range (1,rango+1):
        if (iteracion % 2 != 0):
            print (iteracion)
elif (opcion == 2 ):
    for iteracion in range (1,rango+1):
        if (iteracion % 2 == 0):
            print (iteracion)
elif (opcion == 3):
    for iteracion in range (1,rango+1):
        if (iteracion % 2 == 0):
            print (iteracion, '--> Es un número par')
        else:
            print(iteracion, '--> Es un número impar')
else:
    print ('Mostrando nada')