from modelo_vehiculoo import modelo_vehiculo
from modelo_vehiculo_personal import vehiculo_personal
from modelo_vehiculo_deportivo import vehiculo_deportivo
from modelo_vehiculo_carga import vehiculo_carga
from base_datos import base_datos

obj_base_datos = base_datos()

print("=== Vehículo Normal ===")

modelo = input("Modelo: ")
color = input("Color: ")
num_puertas = input("Numero de puertas: ")
capacidad_p = input("Capacidad de personas: ")
obj_vehiculo = modelo_vehiculo(modelo, color, num_puertas, capacidad_p)
obj_base_datos.guardar_obj(obj_vehiculo)
obj_base_datos.imprimir_info()

print("\n=== Vehículo Personal ===")

modelo = input("Modelo: ")
color = input("Color: ")
num_puertas = input("Numero de puertas: ")
capacidad_p = input("Capacidad de personas: ")
motor = input("Motor: ")
tipo_combustible = input("Tipo de combustible: ")
obj_vehiculo_personal = vehiculo_personal(modelo, color, num_puertas, capacidad_p, motor, tipo_combustible)
obj_base_datos.guardar_obj(obj_vehiculo_personal)
obj_base_datos.imprimir_info()

print("\n=== Vehículo Deportivo ===")
modelo = input("Modelo: ")
color = input("Color: ")
num_puertas = input("Numero de puertas: ")
capacidad_p = input("Capacidad de personas: ")
velocidad_min = input("Velocidad minima: ")
velocidad_max = input("Velocidad maxima: ")
obj_vehiculo_deportivo = vehiculo_deportivo(modelo, color, num_puertas, capacidad_p, velocidad_min, velocidad_max)
obj_base_datos.guardar_obj(obj_vehiculo_deportivo)
obj_base_datos.imprimir_info()

print("\n=== Vehículo de Carga ===")
modelo = input("Modelo: ")
color = input("Color: ")
num_puertas = input("Numero de puertas: ")
capacidad_p = input("Capacidad de personas: ")
carga_maxima = input("Carga máxima: ")
tipo_carga = input("Tipo de carga: ")
obj_vehiculo_carga = vehiculo_carga(modelo, color, num_puertas, capacidad_p, carga_maxima, tipo_carga)
obj_base_datos.guardar_obj(obj_vehiculo_carga)
obj_base_datos.imprimir_info()