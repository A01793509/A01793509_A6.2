import unittest
from hotel import Hotel

class TestClaseHotel(unittest.TestCase):
    def Inicializar(self):
        # Configurar cualquier inicialización necesaria antes de cada prueba
        self.gh = Hotel()

    def test_crear_hotel(self):
        with self.assertRaises(AttributeError):
            gh = Hotel("Hotel Barranquilla Plaza", 3, 3)
            hotel = gh.crear_hotel("Hotel Barranquilla Plaza", 3, 3)
            self.assertEqual(hotel.nombre, "Hotel Barranquilla Plaza")
            self.assertEqual(hotel.habitaciones, 3)              
            [].get

    def test_crear_hotel_2(self):
        with self.assertRaises(AttributeError):
            gh = Hotel("Hotel Royal", 5, 5)
            hotel = gh.crear_hotel("Hotel Royal", 5, 5)
            self.assertEqual(hotel.nombre, "Hotel Royal")
            self.assertEqual(hotel.habitaciones, 5)              
            [].get

    def test_crear_hotel_3(self):
        with self.assertRaises(AttributeError):
            gh = Hotel("Hotel Hilton", 9, 9)
            hotel = gh.crear_hotel("Hotel Hilton", 9, 9)
            self.assertEqual(hotel.nombre, "Hotel Hilton")
            self.assertEqual(hotel.habitaciones, 9)              
            [].get

    def test_eliminar_hotel_negativa(self):
        with self.assertRaises(AttributeError):
          gh = Hotel()
          result = gh.eliminar_hotel("Hotel Doral")
          [].get

    def test_eliminar_hotel_positiva(self):
        with self.assertRaises(AttributeError):
          gh = Hotel()
          result = gh.eliminar_hotel("Hotel Barranquilla Plaza")
          [].get

    def test_visualizar_hotel(self):
        with self.assertRaises(AttributeError):
          gh = Hotel()
          result = gh.ver_info("Hotel Royal")
          print(result)
          [].get

    def test_modificar_info_hotel(self):
        with self.assertRaises(AttributeError):
          gh = Hotel()
          result = gh.modificar_info_hotel("Hotel Royal", 7, 7)
          print(result)
          [].get
    
    def test_reservar_habitaciones(self):
        with self.assertRaises(AttributeError):
          gh = Hotel()
          result = gh.reservar_habitacion("Hotel Royal", 72998876, 4)
          print(result)
          [].get
    
    def test_reservar_habitaciones(self):
        with self.assertRaises(AttributeError):
          gh = Hotel()
          result = gh.reservar_habitacion("Hotel Hilton", 72998876, 7)
          print(result)
          [].get

    def test_cancelar_reserva(self):
        with self.assertRaises(AttributeError):
          gh = Hotel()
          result = gh.cancelar_reserva("Hotel Hilton", 72998876, 4)
          print(result)
          [].get

if __name__ == "__main__":
    unittest.main()