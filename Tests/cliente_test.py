import unittest
from cliente import Cliente

class TestClaseCliente(unittest.TestCase):
    def Inicializar(self):
        # Configurar cualquier inicialización necesaria antes de cada prueba
        self.gc = Cliente()

    def test_crear_cliente(self):
        with self.assertRaises(AttributeError):
            gc = Cliente(72998876, "Alberto Garcia", "Colombiano")
            cliente = gc.crear_cliente(72998876, "Alberto Garcia", "Colombiano")
            self.assertEqual(Cliente.id_cliente, 72998876)          
            [].get

    def test_crear_cliente_2(self):
        with self.assertRaises(AttributeError):
            gc = Cliente(103456789, "Maria Perez", "Colombiano")
            cliente = gc.crear_cliente(103456789, "Maria Perez", "Colombiano")
            self.assertEqual(Cliente.id_cliente, 103456789)          
            [].get

    def test_eliminar_cliente(self):
        with self.assertRaises(AttributeError):
          gc = Cliente()
          result = gc.eliminar_cliente(72998877)
          [].get

    def test_eliminar_cliente_2(self):
        with self.assertRaises(AttributeError):
          gc = Cliente()
          result = gc.eliminar_cliente(103456789)
          [].get

    def test_visualizar_cliente(self):
        with self.assertRaises(AttributeError):
          gc = Cliente()
          result = gc.ver_info(72998876)
          print(result)
          [].get

    def test_modificar_info_cliente(self):
        with self.assertRaises(AttributeError):
          gc = Cliente()
          result = gc.modificar_info_cliente(72998876, "Juan Perez", "Mexicano")
          print(result)
          [].get

if __name__ == "__main__":
    unittest.main()