class animal:
    def __init__(self, nombre, tamaño, edad, color):
        self.nombre = nombre
        self.tamaño = tamaño
        self.edad = edad
        self.color = color

    def nombre_animal(self):
        print(f"El nombre del animal es: {self.nombre}")
    
    def tamaño_animal(self):
        print(f"El tamaño del animal es: {self.tamaño}")

    def edad_animal(self):
        print(f"La edad del animal es: {self.edad}")

    def color_animal(self):
        print(f"El color del animal es: {self.color}")
    
    def info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Tamaño: {self.tamaño}")
        print(f"Edad: {self.edad}")
        print(f"Color: {self.color}")