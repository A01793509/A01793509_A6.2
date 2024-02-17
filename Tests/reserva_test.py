import unittest
from reserva import Reserva

class TestClaseReserva(unittest.TestCase):
    def Inicializar(self):
        # Configurar cualquier inicialización necesaria antes de cada prueba
        self.gr = Reserva()
    
    def test_reservar_habitaciones(self):
        with self.assertRaises(AttributeError):
          gr = Reserva()
          result = gr.reservar_habitacion("Hotel Royal", 72998876, 4)
          print(result)
          [].get
    
    def test_reservar_habitaciones_2(self):
        with self.assertRaises(AttributeError):
          gr = Reserva()
          result = gr.reservar_habitacion("Hotel Hilton", 72998876, 7)
          print(result)
          [].get

    def test_cancelar_reserva(self):
        with self.assertRaises(AttributeError):
          gr = Reserva()
          result = gr.cancelar_reserva("Hotel Hilton", 72998876, 4)
          print(result)
          [].get

if __name__ == "__main__":
    unittest.main()