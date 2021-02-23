#constantes 
preguntaMedida = 'ingrese una medida en centimetros : '
preguntaUnidad = ''' ingrese  que unidades desea transformar :
      K - Kilometros
      M - Metros 
      mm -milimetros
'''

mensajeError = 'Entrada no válida'

medida = float(input(preguntaMedida))
unidad = input(preguntaUnidad)

metros = medida *10**-2
kilometros = medida *10**-5
milimetros = medida *10

if (unidad == 'K'):
  print (kilometros)
elif (unidad == 'M'):
  print (metros)
elif (unidad == 'mm'):
  print (milimetros)
else:
  print (mensajeError)
