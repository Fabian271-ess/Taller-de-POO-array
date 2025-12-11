from modelo_botella import Botella
class Botella_plastico(Botella):
    def __init__(self, marca, capacidad, tapa, diseño, material, tinte):
        super().__init__(marca, capacidad, tapa)
        self.diseño = diseño
        self.material = material
        self.tinte = tinte
    
    def reutilizar_botella(self):
        print(f"La botella se va a reciclar: {self.material}")
    
    def imprimir_info(self):
        print(f"El diseño es: {self.diseño}")
        print(f"El material es: {self.material}")
        print(f"El color es: {self.tinte}")
        super().imprimir_info()
        print(f"La marca padre es: {self.marca}")
        return "Informacion encontrada"