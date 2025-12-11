from modelo_vehiculoo import modelo_vehiculo
class vehiculo_carga(modelo_vehiculo):
    def __init__ (self,modelo, color, num_puertas, capacidad_p, carga_maxima, tipo_carga):
        super().__init__(modelo, color, num_puertas, capacidad_p)
        self.carga_maxima = carga_maxima
        self.tipo_carga = tipo_carga
    
    def carga_maxima_vehiculo(self):
        print("La carga máxima del vehículo es: {self.carga_maxima}")
    
    def tipo_carga_vehiculo(self):
        print("El tipo de carga del vehículo es: {self.tipo_carga}")
    
    def info_carga(self):
        print(f"La carga máxima es: {self.carga_maxima}")
        print(f"El tipo de carga es: {self.tipo_carga}")
        super().info()
        print(f"El modelo padre es: {self.modelo}")
        return "Información encontrada"