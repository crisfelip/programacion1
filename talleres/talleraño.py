# constantes 
preguntaActual = 'Ingrese el año actual : '
preguntaOtro = 'Ingrese un año cualquiera : '

mensaje = '{} {} años'
mensajeIguales = 'los años ingresados son iguales'

currentYear = int (input(preguntaActual))
randomYear = int (input(preguntaOtro))

if (currentYear>randomYear):
  resta = currentYear - randomYear
  print (mensaje.format('han pasado', resta))
elif (randomYear > currentYear) :
  resta = randomYear - currentYear
  print (mensaje.format('Faltan', resta))
else :
  print(mensajeIguales)
