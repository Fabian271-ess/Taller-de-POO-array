from modelo_botella import Botella
from modelo_botella_plastico import Botella_plastico
from modelo_botella_vidrio import botella_vidrio
from base_datos import base_datos

obj_base_datos = base_datos()


print("=== Botella Normal ===")
marca = input("Marca: ")
capacidad = input("Capacidad: ")
tapa = input("Tipo de tapa: ")
obj_botella = Botella(marca, capacidad, tapa)
obj_base_datos.guardar_obj(obj_botella)
obj_base_datos.imprimir_info()

print("\n=== Botella Plástica ===")
marca = input("Marca: ")
capacidad = input("Capacidad: ")
tapa = input("Tipo de tapa: ")
diseño = input("Diseño: ")
material = input("Material: ")
tinte = input("Tinte: ")
obj_botella_plastico = Botella_plastico(marca, capacidad, tapa, diseño, material, tinte)
obj_base_datos.guardar_obj(obj_botella_plastico)
obj_base_datos.imprimir_info()

print("\n=== Botella de Vidrio ===")
marca = input("Marca: ")
capacidad = input("Capacidad: ")
tapa = input("Tipo de tapa: ")
tamaño = input("Tamaño: ")
fragil = input("¿Es frágil? (Si/No): ")
obj_botella_vidrio = botella_vidrio(marca, capacidad, tapa, tamaño, fragil)
obj_base_datos.guardar_obj(obj_botella_vidrio)
obj_base_datos.imprimir_info()



