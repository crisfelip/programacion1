#constantes
preguntaNumeroA = 'Ingrese el número  A : '
preguntaNumeroB = 'Ingrese el número  b : '
mensajeMayor = 'El numero {} es mayor que el numero {} pues {} > {}'
mensajeIguales = 'El numero {} es iguales que el numero {} pues {} == {}'


#Entradas
numeroA = int (input (preguntaNumeroA))
numeroB = int (input (preguntaNumeroB))
if (numeroA > numeroB) :
  print (mensajeMayor.format('A','B',numeroA, numeroB)) 
elif (numeroB > numeroA) :
  print (mensajeMayor.format('B','A',numeroB, numeroA)) 
else :
  print (mensajeIguales.format('A','B',numeroA, numeroB))
