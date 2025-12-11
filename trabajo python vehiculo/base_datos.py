class base_datos:
    def __init__(self):
        self.lista_vehiculos = []
        self.lista_vehiculo_carga = []
        self.lista_vehiculo_deportivo = []
        self.lista_vehiculo_personal = []

    def guardar_obj(self, nuevo_obj):
        self.lista_vehiculos.append(nuevo_obj)

    def agregar_varios_obj(self, lista_nueva):
        self.lista_vehiculos.extend(lista_nueva)

    def imprimir_info(self):
        for obj in self.lista_vehiculos:
            print(obj)
