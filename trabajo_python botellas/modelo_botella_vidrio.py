from modelo_botella import Botella
class botella_vidrio(Botella):
    def __init__ (self,marca, capacidad, tapa, tamaño, fragil):
        super().__init__(marca, capacidad, tapa)
        self.tamaño = tamaño  
        self.fragil = fragil
    
    def tamaño_vidrio(self):
        print("El tamaño de la botella es: {self.tamaño}")
    
    def fragilidad(self):
        print("¿La botella es frágil?: {self.fragil}")
    
    def info_vidrio(self):
        print(f"El tamaño de la botella es: {self.tamaño}")
        print(f"¿La botella es frágil?: {self.fragil}")
        super().imprimir_info()
        print(f"La marca padre es: {self.marca}")
        return "Información encontrada"