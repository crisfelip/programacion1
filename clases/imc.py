#constantes 
PREGUNTA_PESO = "cuanto pesas en kg"
PREGUNTA_ESTATURA = "cuanto mides en mts"
MESNSAJE_BIENBENIDA = "hola como estas? voy a calcular tu IMC"
MENSAJE_DESPEDIDA = "tu IMC es ..."


print(MESNSAJE_BIENBENIDA)
peso = float(input(PREGUNTA_PESO))
estatura = float(input(PREGUNTA_ESTATURA))
imc = peso/(estatura**2)
print (MENSAJE_DESPEDIDA, imc)
isobeso = imc >= 30
print ("el resultado de la prueba obesidad es ...", isobeso)
