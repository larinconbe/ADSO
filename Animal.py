class Animal:
    def __init__ (self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def mostrarInformacion(self):
        print(f"El nombre del animal es: {self.nombre}, la edad del animal es: {self.edad}")    
    def hacerSonido(self):
        pass
        
class Perro(Animal):
    def __init__(self, nombre, edad, raza, color):
        super().__init__(nombre, edad)
        self.raza = raza
        self.color = color
    def mostrarInformacion(self):
        print(f"El nombre del perro es: {self.nombre}, la edad del perro es {self.edad}, \
            la raza del perro es: {self.raza}, el color del perro es: {self.color}")
    def hacerSonido(self):
        print(f"El perro hace guau guau")
class Gato(Animal):
    def __init__(self, nombre, edad, raza, color, vacuna):
        super().__init__(nombre, edad)
        self.raza = raza
        self.color = color
        self.vacuna = vacuna
    def mostrarInformacion(self):
        print(f"El nombre del gato es: {self.nombre}, la edad del gato es {self.edad}, \
            la raza del gato es: {self.raza}, el color del gato es: {self.color}")
        if self.vacuna == False:
            print(f"El gato {self.nombre} no esta vacunado") 
        else:
            print(f"El gato {self.nombre} si esta vacunado")
    def hacerSonido(self):
        print (f"El gato {self.nombre} hace miauuuu")
class Pajaro (Animal):
    def __init__(self, nombre, edad, raza, tipoCanto):
        super().__init__(nombre, edad)
        self.raza = raza
        self.tipoCanto = tipoCanto        
    def mostrarInformacion(self):
        print(f"El nombre del pajaro es: {self.nombre}, la edad del pajaro es {self.edad}, \
            la raza del pajaro es: {self.raza}, el tipo de canto del pajaro es: {self.tipoCanto}")
        
perro1 = Perro("Tomas", 2, "Labrador", "Marron")
gato1 = Gato("Firus", 12, "Criollo", "Blanco", True)
pajaro1 = Pajaro("Henrrique", 5, "Turpial", "Melodioso")
perro2 = Perro ("Agustin", 5, "Chandis", "Marron")

perro1.mostrarInformacion() 

animales = [perro1, gato1, pajaro1, perro2] 
for animal in animales:
    animal.mostrarInformacion()
    animal.hacerSonido()                                   