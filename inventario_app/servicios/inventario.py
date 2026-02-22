# servicios/inventario.py

import os
from modelos.producto import Producto


class Inventario:
    """
    Clase encargada de gestionar los productos del inventario
    con persistencia en archivo.
    """

    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = []
        self.cargar_desde_archivo()

    # ===============================
    # MÉTODOS DE ARCHIVO
    # ===============================

    def cargar_desde_archivo(self):
        """
        Carga los productos desde el archivo.
        Si el archivo no existe, lo crea automáticamente.
        """
        try:
            if not os.path.exists(self.archivo):
                open(self.archivo, "w").close()
                print("📁 Archivo inventario.txt creado.")

            with open(self.archivo, "r") as file:
                for linea in file:
                    try:
                        id_producto, nombre, cantidad, precio = linea.strip().split(",")
                        producto = Producto(
                            id_producto,
                            nombre,
                            int(cantidad),
                            float(precio)
                        )
                        self.productos.append(producto)
                    except ValueError:
                        print("⚠ Línea corrupta ignorada:", linea.strip())

            print("✅ Inventario cargado correctamente.")

        except PermissionError:
            print("❌ Error: No tienes permisos para leer el archivo.")

    def guardar_en_archivo(self):
        """
        Guarda todos los productos en el archivo.
        """
        try:
            with open(self.archivo, "w") as file:
                for producto in self.productos:
                    file.write(
                        f"{producto.get_id()},"
                        f"{producto.get_nombre()},"
                        f"{producto.get_cantidad()},"
                        f"{producto.get_precio()}\n"
                    )
            print("💾 Cambios guardados en inventario.txt.")

        except PermissionError:
            print("❌ Error: No tienes permisos para escribir en el archivo.")

    # ===============================
    # MÉTODOS DE GESTIÓN
    # ===============================

    def añadir_producto(self, producto):
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("❌ Error: Ya existe un producto con ese ID.")
            return False

        self.productos.append(producto)
        self.guardar_en_archivo()
        print("✅ Producto añadido correctamente.")
        return True

    def eliminar_producto(self, id_producto):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                self.productos.remove(producto)
                self.guardar_en_archivo()
                print("🗑 Producto eliminado correctamente.")
                return True

        print("❌ Producto no encontrado.")
        return False

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)

                self.guardar_en_archivo()
                print("🔄 Producto actualizado correctamente.")
                return True

        print("❌ Producto no encontrado.")
        return False

    def buscar_por_nombre(self, nombre):
        resultados = [
            producto for producto in self.productos
            if nombre.lower() in producto.get_nombre().lower()
        ]

        if resultados:
            print("🔎 Resultados encontrados:")
            for producto in resultados:
                print(producto)
        else:
            print("❌ No se encontraron productos.")

    def mostrar_inventario(self):
        if not self.productos:
            print("📦 El inventario está vacío.")
        else:
            print("\n📋 Inventario actual:")
            for producto in self.productos:
                print(producto)