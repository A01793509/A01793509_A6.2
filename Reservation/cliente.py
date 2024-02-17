"""
Definición de la clase Cliente con todos sus eventos requeridos
"""
import json
import os


class Cliente:
    """
    Esta clase permitirá gestionar la creación, borrado,
    visualización y modificación de clientes.
    """
    def __init__(self, id_cliente: int = 0,
                 nombre: str = "", nacionalidad: str = ""):
        """
        Inicializar objetos de la clase Cliente
        """
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.nombrearchivo = f"{id_cliente}_data.json"

    def crear_archivo_json(self):
        """
        Este método permite crear un archivo json haciendo el simil de una BD
        """
        datos = {
            'id_cliente': self.id_cliente,
            'nombre': self.nombre,
            'nacionalidad': self.nacionalidad
        }
        with open(self.nombrearchivo, 'w', encoding='utf-8') as archivo_json:
            json.dump(datos, archivo_json)

    def crear_cliente(self, id_cliente: int, nombre: str, nacionalidad: str):
        """
        Este método permite crear un cliente
        """
        if isinstance(id_cliente, int):
            cliente = Cliente(id_cliente, nombre, nacionalidad)
            cliente.crear_archivo_json()
            return Cliente
        return "Creando: La identificación debe ser un número."

    def eliminar_cliente(self, id_cliente: int):
        """
        Este método permite eliminar un cliente existente
        """
        nombre_json = str(id_cliente) + '_data.json'
        ruta_archivo_json = os.path.join("/content", nombre_json)
        if os.path.exists(ruta_archivo_json):
            os.remove(nombre_json)
            return "Eliminando: Cliente eliminado exitosamente."
        return f"El cliente con ID '{id_cliente}' no existe."

    def ver_info(self, id_cliente: str):
        """
        Este método permite visualizar la información del cliente
        """
        nombre_json = str(id_cliente) + '_data.json'
        ruta_archivo = os.path.join("/content", nombre_json)
        if os.path.exists(ruta_archivo):
            with open(ruta_archivo, "r", encoding='utf-8') as archivo_json:
                contenido_json = json.load(archivo_json)
                return f"Datos de cliente {id_cliente}: {contenido_json}"
        return f"El cliente con ID '{id_cliente}' no existe."

    def modificar_info_cliente(self, id_cliente: int,
                               nombre: str, nacionalidad: str):
        """
        Este método permite modificar información del cliente
        """
        nombre_json = str(id_cliente) + '_data.json'
        ruta_archivo = os.path.join("/content", nombre_json)
        if os.path.exists(ruta_archivo):
            with open(ruta_archivo, "r", encoding='utf-8') as archivo_json:
                contenido_json = json.load(archivo_json)
                contenido_json['nombre'] = nombre
                contenido_json['nacionalidad'] = nacionalidad

            with open(ruta_archivo, "w", encoding='utf-8') as archivo_json:
                json.dump(contenido_json, archivo_json, indent=2)

            return f"Información de cliente con ID {id_cliente} actualizada."
        return f"El cliente con ID '{id_cliente}' no existe."
