# entradas 
PREGUNTA_EDAD = "cuantos años tienes?"
BIENVENIDO = "BIENBENIDO te preguntaremos tu edad "
MENSAJE_MAYOR_EDAD = "eres mayor de edad puedes seguir"
MENSAJE_MENOR_EDAD = "eres menor de edad no puedes seguir"


print (BIENVENIDO)
edad = int (input(PREGUNTA_EDAD))
ismayor = edad >= 18
if (ismayor): 
    resultado = MENSAJE_MAYOR_EDAD
else :
    resultado = MENSAJE_MENOR_EDAD

print (resultado)