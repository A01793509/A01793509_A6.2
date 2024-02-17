"""
Definición de la clase Reserva con todos sus eventos requeridos
"""
import json
import os


class Reserva:
    """
    Esta clase permitirá realizar la gestión relacionada con la
    reserva y cancelación de reserva para los hoteles.
    """
    def __init__(self, nombre: str = "",
                 id_cliente: int = 0, habitaciones: int = 0):
        """
        Inicializar objetos de la clase Reserva
        """
        self.nombre = nombre
        self.habitaciones = habitaciones
        self.id_cliente = id_cliente
        self.nombrearchivo = f"{nombre}.json"

    def crear_archivo_json(self):
        """
        Este método permite crear un archivo json haciendo el simil de una BD
        """
        datos = {
            'nombre': self.nombre,
            'id_cliente': self.id_cliente,
            'habitaciones': self.habitaciones
        }
        with open(self.nombrearchivo, 'w', encoding='utf-8') as f:
            json.dump(datos, f)

    def reservar_habitacion(self, nombre: str,
                            id_cliente: int, num_habitaciones: int):
        """
        Este método permite reservas habitaciones
        """
        nombre_json = nombre + '.json'
        ruta_archivo = os.path.join("/content", nombre_json)
        if os.path.exists(ruta_archivo):
            with open(ruta_archivo, "r", encoding='utf-8') as archivo_json:
                contenido_json = json.load(archivo_json)
                contenido_json['disponibles'] -= num_habitaciones
                disponibles = contenido_json['disponibles']

            if disponibles >= 0:
                # Creamos archivo con la reserva
                nombrearchivo = nombre + "_reserv_" + str(id_cliente) + '.json'
                datos = {
                          'nombre': nombre,
                          'cliente': id_cliente,
                          'habitaciones': num_habitaciones
                        }
                with open(nombrearchivo, 'w', encoding='utf-8') as f:
                    json.dump(datos, f)

                # Actualizamos habitaciones disponibles en hotel
                with open(ruta_archivo, "w", encoding='utf-8') as archivo_json:
                    json.dump(contenido_json, archivo_json, indent=2)
                return f"Reserva exitosa. Cuartos disponibles: {disponibles}"
            return "No se cuenta con habitaciones suficientes."
        return f"No existe el hotel {nombre} en la base de datos."

    def cancelar_reserva(self, nombre: str,
                         id_cliente: int, num_habitaciones: int):
        """
        Este método permite borrar reservas existentes
        """
        # Validamos si el hotel existe en la base de datos
        nombre_json = nombre + '.json'
        ruta_archivo = os.path.join("/content", nombre_json)
        if os.path.exists(ruta_archivo):
            with open(ruta_archivo, "r", encoding='utf-8') as archivo_json:
                contenido_json = json.load(archivo_json)
                contenido_json['disponibles'] += num_habitaciones
                disponibles = contenido_json['disponibles']

            # Actualizamos habitaciones disponibles en hotel
            with open(ruta_archivo, "w", encoding='utf-8') as archivo_json:
                json.dump(contenido_json, archivo_json, indent=2)

            # Buscamos archivo con la reserva
            nombrearchivo = nombre + "_reserv_" + str(id_cliente) + '.json'
            archivo_reserva = os.path.join("/content", nombrearchivo)
            # Si el archivo existe lo eliminamos
            if os.path.exists(archivo_reserva):
                os.remove(archivo_reserva)
                return f"Reserva cancelada. Cuartos disponibles: {disponibles}"
            return "No existe la reserva indicada."
        return f"No existe el hotel {nombre} en la base de datos."
