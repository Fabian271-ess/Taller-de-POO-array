from modelo_vehiculoo import modelo_vehiculo
class vehiculo_deportivo(modelo_vehiculo):
    def __init__ (self,modelo, color, num_puertas, capacidad_p, velocidad_min, velocidad_max):
        super().__init__(modelo, color, num_puertas, capacidad_p)
        self.velocidad_min = velocidad_min
        self.velocidad_max = velocidad_max
    
    def velocidadmax(self):
        print("La velocidad maxima es: {self.velocidad_max}")
    
    def velocidadmin(self):
        print("La velocidad minima es {self.valocidad_min}")
    
    def info_deportivo(self):
        print(f"La velocidad maxima es: {self.velocidad_max}")
        print(f"La velocidad minima es: {self.velocidad_min}")
        super().info()
        print(f"El modelo padre es: {self.modelo}")
        return "Información encontrada"