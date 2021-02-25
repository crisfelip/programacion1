#constantes 

preguta_nivel_de_trigliceridos = "cual es el valor de trigliceridos "
mensaje_optimo = "estas en un rango optimo de trigliceridos "
mensaje_alto ="estan altos tus trigliceridos "
mensaje_limiteoptico = "estas entre el limite adecuado de trigliceridos "
pregunta_valor_homocisteina = "cual es el valor de homocisteina "
MESNSAJE_BIENBENIDA = "Bienvenido te ayudaremos con el calculo de trigliceridos "
mensaje_optimo1 = "tu nivel es optimo de homocisteina"
mensaje_limiteoptico1 = "tu nivel esta en el limite adecuado de homocisteina"
mensaje_alto1 = "tu nivel es algo alto de homocisteina"
mensaje_muy_alto = "tu nivel es MUY alto de homocisteina"
print(MESNSAJE_BIENBENIDA)
valor = int(input(preguta_nivel_de_trigliceridos))
valorHS = int(input(pregunta_valor_homocisteina))
homocisteina = valorHS*1 
isoptimo1 = valorHS>=2 and valorHS<= 15
islimiteoptimo1=valorHS>=16 and valorHS<= 30
isalto1 = valorHS>=31 and valorHS<= 100
ismuyalto1 =valorHS>101
resultado1 = ""
if (isoptimo1): 
    resultado= mensaje_optimo1
elif(islimiteoptimo1):
    resultado= mensaje_limiteoptico1
elif (isalto1):
    resultado = mensaje_alto1
print(resultado)
trigliceridos = valor*1
isoptimo = trigliceridos == 150 
islimiteoptimo = trigliceridos>151 and trigliceridos<199
isalto  = trigliceridos >= 200 and trigliceridos< 499 
ismuyalto = trigliceridos>500
resultado = ""
if (isoptimo): 
    resultado= mensaje_optimo
elif(islimiteoptimo):
    resultado= mensaje_limiteoptico
elif (isalto):
    resultado = mensaje_alto
print(resultado)