#constantes
PREGUNTA_NUMERO_A = "dime un numero cualquiera"
PREGUNTA_NUMERO_B = "dime otro numero que quieras "
MESNSAJE_BIENBENIDA = "hola como estas? voy a calcular lo que me digas"
MENSAJE_DESPEDIDA = "me gusto ayudarte, aqui estoy para servirte nuevamente cuando gustes "
MENSAJE_AMISTOSO1 = "Muy bien, me gusta tu eleccion "
MENSAJE_AMISTOSO2 = "interesante "
MENSAJE_AMISTOSO3 = "primero los sumare y luego los multiplicare por ti"
MENSAJE_AMISTOSO4 = "ya ves, si soy capaz de hacerlo jejeje"
MENSAJE_AMISTOSO5 = "ponme a prueba, dividamos dos numeros y veamos que resulta"


#codigo espero que funcional jejeje
print(MESNSAJE_BIENBENIDA)
numeroA = float(input(PREGUNTA_NUMERO_A))
print(MENSAJE_AMISTOSO1)
numeroB = float(input(PREGUNTA_NUMERO_B))
print(MENSAJE_AMISTOSO2)
print(MENSAJE_AMISTOSO3)
sumar = numeroA + numeroB
print ("el resultado de la suma es" , sumar)
multiplicar = numeroA * numeroB
print("el resultado de la multiplicacion es", multiplicar)
print(MENSAJE_AMISTOSO4)
print(MENSAJE_AMISTOSO5)
numero1 = float(input(PREGUNTA_NUMERO_A))
numero2 = float(input(PREGUNTA_NUMERO_B))
dividir = numero1 /(numero2)
print ("el resultado de la division es", dividir)
print (MENSAJE_DESPEDIDA)
