class modelo_vehiculo:
    def __init__(self, modelo, color, num_puertas, capacidad_p):
        self.modelo = modelo
        self.color = color
        self.num_puertas = num_puertas
        self.capacidad_p = capacidad_p
        
    def arrancar(self):
        print("El vehículo {self.modelo} está arrancando.")
    
    def apagar(self):
        print("El vehículo de  {self.modelo} se ha apagado.")
    
    def cantidad_puertas(self):
        print("El vehículo tiene {self.num_puertas} puertas.")
    
    def capacidad_personas(self):
        print("El vehículo tiene una capacidad para {self.capacidad_p} personas.")
    
    def info(self):
        print(f"El modelo es: {self.modelo}")
        print(f"El color es: {self.color}")
        print(f"El número de puertas es: {self.num_puertas}")
        print(f"La capacidad de personas es: {self.capacidad_p}")

        