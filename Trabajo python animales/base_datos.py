class base_datos:
    def __init__(self):
        self.lista_animales = []
        self.lista_animal_acuatico = []
        self.lista_animal_aereo = []
        self.lista_animal_anifibio = []
        self.lista_anima_terrestre = []
    def guardar_obj(self, nuevo_obj):
        self.lista_animales.append(nuevo_obj)

    def agregar_varios_obj(self, lista_nueva):
        self.lista_animales.extend(lista_nueva)

    def imprimir_info(self):
        for obj in self.lista_animales:
            print(obj)
