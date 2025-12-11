from modelo_animal import animal
from modelo_animal_terrestre import animal_terrestre
from modelo_animal_aereo import animal_aereo
from modelo_animal_acuatico import animal_acuatico
from modelo_animal_anfibio import animal_anfibio
from base_datos import base_datos

obj_base_datos = base_datos()

print("=== Animal Normal ===")
nombre = input("Nombre: ")
tamaño = input("Tamaño: ")
edad = input("Edad: ")
color = input("Color: ")
obj_animal = animal(nombre, tamaño, edad, color)
obj_base_datos.guardar_obj(obj_animal)
obj_base_datos.imprimir_info()

print("\n=== Animal Terrestre ===")
nombre = input("Nombre: ")
tamaño = input("Tamaño: ")
edad = input("Edad: ")
color = input("Color: ")
habitat = input("Habitat: ")
obj_animal_terrestre = animal_terrestre(nombre, tamaño, edad, color, habitat)
obj_base_datos.guardar_obj(obj_animal_terrestre)
obj_base_datos.imprimir_info()

print("\n=== Animal Aéreo ===")
nombre = input("Nombre: ")
tamaño = input("Tamaño: ")
edad = input("Edad: ")
color = input("Color: ")
envergadura = input("Envergadura: ")
obj_animal_aereo = animal_aereo(nombre, tamaño, edad, color, envergadura)
obj_base_datos.guardar_obj(obj_animal_aereo)
obj_base_datos.imprimir_info()

print("\n=== Animal Acuático ===")
nombre = input("Nombre: ")
tamaño = input("Tamaño: ")
edad = input("Edad: ")
color = input("Color: ")
profundidad = input("Profundidad: ")
obj_animal_acuatico = animal_acuatico(nombre, tamaño, edad, color, profundidad)
obj_base_datos.guardar_obj(obj_animal_acuatico)
obj_base_datos.imprimir_info()

print("\n=== Animal Anfibio ===")
nombre = input("Nombre: ")
tamaño = input("Tamaño: ")
edad = input("Edad: ")
color = input("Color: ")
tipo_agua = input("Tipo de agua: ")
obj_animal_anfibio = animal_anfibio(nombre, tamaño, edad, color, tipo_agua)
obj_base_datos.guardar_obj(obj_animal_anfibio)
obj_base_datos.imprimir_info()
