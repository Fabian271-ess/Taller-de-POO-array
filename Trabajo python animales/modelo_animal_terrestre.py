from modelo_animal import animal
class animal_terrestre(animal):
    def __init__(self, nombre, tamaño, edad, color, habitat):
        super().__init__(nombre, tamaño, edad, color)
        self.habitat = habitat

    def habitat_animal(self):
        print(f"El tipo de terreno del animal es: {self.habitat}")

    def info(self):
        print(f"Tipo de Terreno: {self.habitat}")
        super().info()
        return ("Informacion encontrada")