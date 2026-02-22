# modelos/producto.py

class Producto:
    """
    Clase que representa un producto dentro del inventario.
    """

    def __init__(self, id_producto, nombre, cantidad, precio):
        """
        Constructor de la clase Producto.
        :param id_producto: Identificador único del producto
        :param nombre: Nombre del producto
        :param cantidad: Cantidad disponible en inventario
        :param precio: Precio unitario del producto
        """
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # Setters
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self._cantidad = cantidad
        else:
            print("⚠️ La cantidad no puede ser negativa.")

    def set_precio(self, precio):
        if precio >= 0:
            self._precio = precio
        else:
            print("⚠️ El precio no puede ser negativo.")

    def __str__(self):
        """
        Representación en texto del producto.
        """
        return f"ID: {self._id} | Nombre: {self._nombre} | Cantidad: {self._cantidad} | Precio: ${self._precio:.2f}"
