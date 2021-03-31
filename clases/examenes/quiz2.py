Temperatura_Corporal = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]

preguntamenu = '''buen dia espero te encuentres bien 
    1- conversion de temperatura 
    2- clasificacion de temperatura 
    3- temperatura max y min
    4- salir 
escoga una opcion para continuar '''

preguntaconversion = '''
    c- temperatura en celsius 
    k- temperatura en kelvin 
    f- temperatura en fahrenheit 
ingrese la letra dependiendo en que unidades quiera el resultado : '''

mensajecelsius= 'los datos estan en celsius por lo que no se requiere una conversion '
mensajeeleccion = 'elegiste la opcion {}'
mensajeerrormen = 'error, utilice una opcion permitida'
mensajesalida = 'feliz dia cualquiera que este sea'


#codigoooooo

opcion = int(input(preguntamenu))


#conversiones 
listafahrenheit  =[]
listakelin = []
for elemento in Temperatura_Corporal:
    fahrenheit = round (elemento*1.8)+ 32 
    listafahrenheit.append (fahrenheit)
for elemento in Temperatura_Corporal:
    kelvin = round (elemento + 273.15)
    listakelin.append(kelvin)

#clasificaciones 
listaclasificacion = []
for elemento in Temperatura_Corporal:
    clasificacion = ""
    if (elemento < 36): 
        clasificacion = 'hipotermia'
    elif (elemento >= 36 and elemento <=37.5):
        clasificacion= 'temperatura normal'
    elif (elemento >=37.6):
        clasificacion= 'fiebre'
    else:
        clasificacion= 'datos errados'
    listaclasificacion.append (clasificacion)


# temperatura max y min 

maxima = max(Temperatura_Corporal)
minima = min(Temperatura_Corporal)

# menu 

while (opcion !=4):
    if (opcion == 1):
        print(mensajeeleccion.format(1))
        conversion = input(preguntaconversion)
        if(conversion == 'c'):
            print (mensajecelsius)
            print (Temperatura_Corporal)
        elif(conversion == 'f'):
            print (listafahrenheit)
        elif (conversion == 'k'):
            print (listakelin)
        else:,
            print (mensajeerrormen)
    elif (opcion == 2):
        print (mensajeeleccion.format(2))
        (listaclasificacion)
    elif (opcion == 3):
        print (mensajeeleccion.format(3))
        print ('la temperatura maxima es', maxima)
        print ('la temperatura minima es', minima)
    else:
        print (mensajeerrormen)
    opcion = int (input (preguntamenu))
print (mensajesalida)