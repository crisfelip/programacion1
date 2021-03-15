#constantes 
MESNSAJE_SALUDO = "Bienvenido a este programa"
PREGUNTAR_NUMERO ="en este juego esta un numero del 1-10 intentalo tres veces maximo suerte,ingresa tu numero: "
PREGUNTA_FALLIDA = "no no no, fallaste, ingresa otro numero :"
MENSAJE_ganaste = "Felicitaciones ganaste "
MENSAJE_perdiste = "lo siento intentalo luego  "


#codigo 
numero_oculto = 7 
vidas = 5 
print (MESNSAJE_SALUDO)
numeroIngresado = int(input(PREGUNTAR_NUMERO))
if (numeroIngresado != numero_oculto):
    vidas -=1
while (numero_oculto != numeroIngresado and vidas > 0):
    numeroIngresado = int(input(PREGUNTA_FALLIDA))
    vidas -=1 

if (vidas >= 0 and numero_oculto == numeroIngresado ):
    print (MENSAJE_ganaste)
    print (vidas)
else:
    print(MENSAJE_perdiste, "el numero era", numero_oculto)

