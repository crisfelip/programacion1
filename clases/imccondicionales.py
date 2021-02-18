#constantes 
PREGUNTA_PESO = "cuanto pesas en kg"
PREGUNTA_ESTATURA = "cuanto mides en mts"
MESNSAJE_BIENBENIDA = "hola como estas? voy a calcular tu IMC"
MENSAJE_DESPEDIDA = "tu IMC es ..."
MENSAJE_BAJO_PESO = "tu eres peso pluma"
MENSAJE_PESO_NORMAL = "estas en forma"
MENSAJE_SOBRE_PESO = "OJO a pagar gym"
MENSAJE_OBESO = "ocupas dos acientos en el bus "


print(MESNSAJE_BIENBENIDA)
peso = float(input(PREGUNTA_PESO))
estatura = float(input(PREGUNTA_ESTATURA))
imc = peso/(estatura**2)
isbajopeso = imc < 18.5 
isnormal = imc >= 18.5 and imc <25
issobrepeso = imc >=25 and imc < 30 
resultado = ""
if (isbajopeso):
    resultado = MENSAJE_BAJO_PESO
elif(isnormal): 
    resultado =MENSAJE_PESO_NORMAL
elif(issobrepeso):
    resultado = MENSAJE_SOBRE_PESO
else: 
    resultado = MENSAJE_OBESO
print(MENSAJE_DESPEDIDA)
print(resultado)
