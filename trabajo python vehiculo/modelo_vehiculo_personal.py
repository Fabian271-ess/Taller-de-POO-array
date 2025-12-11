from modelo_vehiculoo import modelo_vehiculo
class vehiculo_personal(modelo_vehiculo):
    def __init__ (self,modelo, color, num_puertas, capacidad_p, motor, tipo_combustible):
        super().__init__(modelo, color, num_puertas, capacidad_p)
        self.motor = motor
        self.tipo_combustible = tipo_combustible
    
    def motor_personal(self):
        print("El motor del vehículo deportivo es: {self.motor}")
    
    def combustible(self):
        print("El tipo de combustible del vehículo es: {self.tipo_combustible}")
    
    def info_personal(self):
        print(f"El motor es: {self.motor}")
        print(f"El tipo de combustible es: {self.tipo_combustible}")
        super().info()
        print(f"El modelo padre es: {self.modelo}")
        return "Información encontrada"