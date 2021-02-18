#constantes 
MESNSAJE_BIENBENIDA = "HOLA me alegra verte"
PREGUNTA_NUMERO_A = "ingrese numero A"
PREGUNTA_NUMERO_B = "ingrese numero B"
MENSAJE_MAYOR = "numero A es mayor que B"
MENSAJE_MENOR = "numero A es menor que B"
MENSAJE_IGUAL = "A y B son iguales"

#---entrada al codigo ---#
print(MESNSAJE_BIENBENIDA)
numeroA = int(input(PREGUNTA_NUMERO_A))
numeroB = int(input(PREGUNTA_NUMERO_B))
ismayor = numeroA > numeroB
ismenor = numeroA < numeroB

if(ismayor):
    print(MENSAJE_MAYOR)
elif(ismenor) :
    print(MENSAJE_MENOR)
else:
    print(MENSAJE_IGUAL)
