from modelo_animal import animal
class animal_acuatico(animal):
    def __init__(self, nombre, tamaño, edad, color, profundidad):
        super().__init__(nombre, tamaño, edad, color)
        self.profundidad = profundidad

    def profundidad_animal(self):
        print(f"La profundidad a la que vive el animal es: {self.profundidad}")

    def info(self):
        print(f"Profundidad: {self.profundidad}")
        super().info()
        return ("Informacion encontrada")
        