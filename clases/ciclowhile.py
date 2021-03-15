# entradas 
saludo = "hola bienvenido"
mensaje_ahorro = "llevas ahorrado..."
pregunta_valor_computadora = "cuanto vale el computador? :"
pregunta_cuanto_tienes = "cuanto llevas ahorrado? : "
#entradas 
print(saludo)
valor = float(input(pregunta_valor_computadora))
ahorrado = float(input(pregunta_cuanto_tienes))

while (valor > ahorrado):
    print(mensaje_ahorro,ahorrado, "te falta...",valor - ahorrado)
    ahorrado = ahorrado + 1000 

print(valor == ahorrado)