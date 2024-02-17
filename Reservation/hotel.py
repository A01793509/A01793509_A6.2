"""
Definición de la clase Hotel con todos sus eventos requeridos
"""
import json
import os


class Hotel:
    """
    Esta clase permitirá la gestión relacionada con la creación, borrado,
    visualización, modificación, reserva y cancelación de reserva para hoteles.
    """
    def __init__(self, nombre: str = "",
                 habitaciones: int = 0, disponibles: int = 0):
        """
        Inicializar objetos de la clase Hotel
        """
        self.nombre = nombre
        self.habitaciones = habitaciones
        self.disponibles = disponibles
        self.nombrearchivo = f"{nombre}.json"

    def crear_archivo_json(self):
        """
        Este método permite crear un archivo json haciendo el simil de una BD
        """
        datos = {
            'nombre': self.nombre,
            'habitaciones': self.habitaciones,
            'disponibles': self.disponibles
        }
        with open(self.nombrearchivo, 'w', encoding='utf-8') as f:
            json.dump(datos, f)

    def crear_hotel(self, nombre: str, habitaciones: int, disponibles: int):
        """
        Este método permite crear un hotel
        """
        if isinstance(habitaciones, int):
            hotel = Hotel(nombre, habitaciones, disponibles)
            Hotel.crear_archivo_json(self)
            return hotel
        return "Creando: El número de habitaciones debe ser un entero."

    def eliminar_hotel(self, nombre: str):
        """
        Este método permite eliminar un hotel existente
        """
        nombre_json = nombre + '.json'
        ruta_archivo_json = os.path.join("/content", nombre_json)
        if os.path.exists(ruta_archivo_json):
            os.remove(nombre_json)
            return "Eliminando: Hotel eliminado exitosamente."
        return f"Eliminando: El '{nombre}' no existe en la base de datos."

    def ver_info(self, nombre: str):
        """
        Este método permite visualizar la información del hotel
        """
        nombre_json = nombre + '.json'
        ruta_archivo_json = os.path.join("/content", nombre_json)
        if os.path.exists(ruta_archivo_json):
            with open(ruta_archivo_json, "r", encoding='utf-8') as archiv_json:
                contenido_json = json.load(archiv_json)
                return f"Visualizando: Datos de {nombre}: {contenido_json}"
        return f"Visualizando: El '{nombre}' no existe en la base de datos."

    def modificar_info_hotel(self, nombre: str,
                             habitaciones: int, disponibles: int):
        """
        Este método permite modificar información del hotel
        """
        nombre_json = nombre + '.json'
        ruta_archivo_json = os.path.join("/content", nombre_json)
        if os.path.exists(ruta_archivo_json):
            with open(ruta_archivo_json, "r", encoding='utf-8') as archiv_json:
                contenido_json = json.load(archiv_json)
                contenido_json['habitaciones'] = habitaciones
                contenido_json['disponibles'] = disponibles

            with open(ruta_archivo_json, "w", encoding='utf-8') as archiv_json:
                json.dump(contenido_json, archiv_json, indent=2)

            return f"Información de {nombre} actualizada exitosamente."
        return f"El '{nombre}' no existe en la base de datos."

    def reservar_habitacion(self, nombre: str,
                            id_cliente: int, num_habitaciones: int):
        """
        Este método permite reservas habitaciones
        """
        nombre_json = nombre + '.json'
        ruta_archivo = os.path.join("/content", nombre_json)
        if os.path.exists(ruta_archivo):
            with open(ruta_archivo, "r", encoding='utf-8') as archiv_json:
                contenido_json = json.load(archiv_json)
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
        return "No existe el hotel {nombre} en la base de datos."

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
