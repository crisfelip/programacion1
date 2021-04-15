class Perros():
    '''esta es la clase perros puedes ver muchas caracteristicas 
    de cada perro que este en la pase de datos '''


    def __init__(self, razaentrada,tipodepeloentrada,estaturaEntrada,nombreEntrada,pesoentrada,edadEntrada):
        print (' soy un perro nuevo que habla con tigo jejeje...')
        self.raza = razaentrada
        self.tipodepelo = tipodepeloentrada
        self.estatura = estaturaEntrada
        self.nombre = nombreEntrada
        self.peso = pesoentrada
        self.edad = edadEntrada

    
    def hablar (self,mensaje):
        print (f'asi es soy un perro puedo hablar me llamo {self.nombre} y mi raza es {self.raza}', mensaje)
    def mostrarAtributos (self):
        print (f'''mi nombre es {self.nombre}
            me gusta mucho correr a pesar de ser pequeño 
            porque soy un perro {self.raza}
            pero eso no me importa porque soy muy alto 
            mido {self.estatura}cm
            y todavia tengo muchos años para jugar porque 
            tengo apenas {self.edad} años ''')




perro1 = Perros('pincher', 'liso', 40,'paco', 6,12)
perro1.hablar('no te preocupes no estas loco')
perro1.hablar('ya me voy me llama mi amo, chao')

print (perro1.nombre)
print (perro1.peso)
print (perro1.raza)
perro1.mostrarAtributos()
