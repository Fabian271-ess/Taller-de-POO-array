from modelo_animal import animal
class animal_aereo(animal):
    def __init__(self, nombre, tamaño, edad, color, envergadura):
        super().__init__(nombre, tamaño, edad, color)
        self.envergadura = envergadura

    def envergadura_animal(self):
        print(f"La envergadura del animal es: {self.envergadura}")

    def info(self):
        print(f"Envergadura: {self.envergadura}")
        super().info()
        return ("Informacion encontrada")
        