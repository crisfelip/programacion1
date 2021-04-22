# class Humano():
#     def __init__(self, nombreEntrada,edadEntrada,estaturaEntrada):
#         print('hola sou un humano nuevo')
#         self.raza = 'humano'
#         self.nombre = nombreEntrada
#         self.edad = edadEntrada
#         self.estatura = estaturaEntrada
    
#     def hablar (self,mensaje):
#         print('hola tengo un mensaje que decirte...', mensaje)
#     def MostrarAtributos (self):
#         print(f'''mi nombre es{self.nombre} mi estatura es{self.estatura}
#         mi edad es {self.edad}''')

# humano1 = Humano('cristian',20, 1.74) 
# humano2 = Humano('sara', 13,1.61 ) 

# humano1.hablar('estoy vivo')
# humano2.hablar('yo tambien lo estoy')

# humano1.MostrarAtributos()
# humano2.MostrarAtributos()
# print (humano1.nombre)
# print (humano1.edad)
# print (humano2.nombre)
# print (humano2.edad)



class Personas ():
    def __init__(self, nombreEntrada,edadEntrada,idEntrada):
        print('hola soy una persona y estos son mis atributos')
        self.nombre = nombreEntrada
        self.edad = edadEntrada
        self.id = idEntrada
    def Hablar (self,mensaje):
        print(f'me llamo {self.nombre} y tengo un mensaje', mensaje)
    def recorrerDistancia(self,distanciaMetros):
        for i in range (distanciaMetros):
            print(f'Hola soy {self.nombre} y he recorrido {i+1} metros')


class Doctor (Personas):

    def __init__(self,nombreEntrada,edadEntrada,idEntrada,cargoEntrada):
        Personas.__init__(self,nombreEntrada,edadEntrada,idEntrada)
        self.cargo = cargoEntrada

    def atender (self,especialidad):
        print (f'me gradue de {especialidad} y estoy feliz por eso')


class Nutricionista (Personas):

    def __init__(self,nombreEntrada,edadEntrada,idEntrada,cargoEntrada, NutricionistaEntrada):
        Personas.__init__(self,nombreEntrada,edadEntrada,idEntrada)
        self.Nutricionista = NutricionistaEntrada 

    def egresado(self,universidad):
        print(f'soy un egresesado de la {universidad} de la carrera nutrcionista')

PREGUNTA_PESO = "cuanto pesas en kg"
PREGUNTA_ESTATURA = "cuanto mides en mts"

peso = float(input(PREGUNTA_PESO))
estatura = float(input(PREGUNTA_ESTATURA))
imc = peso/(estatura**2)
print (imc)
isobeso = imc >= 30
print ("el resultado de la prueba obesidad es ...", isobeso)




persona1 = Personas ('cristian', 20, 720)
persona1.Hablar ('soy nuevo en esto')
print (persona1.nombre)
print (persona1.edad)
print (persona1.id)
persona1.recorrerDistancia(8)
doctor1 =Doctor('luis',35,730,'gefe encargado')
doctor1.Hablar ('soy un doctor')
doctor1.atender('urgenciologo')
nutricionista1 =Nutricionista('sara',13,579,'doctor','nutricionista')
nutricionista1.Hablar ('soy una nutricionista')
nutricionista1.egresado('CES')