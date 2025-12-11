from modelo_animal import animal
class animal_anfibio(animal):
    def __init__(self, nombre, tamaño, edad, color, tipo_agua):
        super().__init__(nombre, tamaño, edad, color)
        self.tipo_agua = tipo_agua

    def tipo_agua_animal(self):
        print(f"El tipo de agua del animal es: {self.tipo_agua}")

    def info(self):
        print(f"Tipo de Agua: {self.tipo_agua}")
        super().info()
        return ("Informacion encontrada")