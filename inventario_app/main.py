# main.py

from servicios.inventario import Inventario
from modelos.producto import Producto


def mostrar_menu():
    print("\n===== UNIVERSIDAD ESTATAL AMAZONICA =====")
    print("===== Autor Daniel Luzuriaga =====\n")
    print("\n===== SISTEMA DE GESTIÓN DE INVENTARIOS =====")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Listar inventario")
    print("6. Salir")


def main():
    inventario = Inventario()

    while True:
        mostrar_menu()

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("⚠️ Ingrese un número válido.")
            continue

        if opcion == 1:
            try:
                id_producto = input("ID: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))

                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.añadir_producto(producto)

            except ValueError:
                print("⚠️ Datos inválidos. Verifique cantidad y precio.")

        elif opcion == 2:
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == 3:
            id_producto = input("Ingrese ID del producto a actualizar: ")

            try:
                nueva_cantidad = input("Nueva cantidad (dejar vacío si no desea cambiar): ")
                nuevo_precio = input("Nuevo precio (dejar vacío si no desea cambiar): ")

                nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
                nuevo_precio = float(nuevo_precio) if nuevo_precio else None

                inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

            except ValueError:
                print("⚠️ Datos inválidos.")

        elif opcion == 4:
            nombre = input("Ingrese nombre a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == 5:
            inventario.mostrar_inventario()

        elif opcion == 6:
            print("👋 Saliendo del sistema...")
            break

        else:
            print("⚠️ Opción inválida.")


if __name__ == "__main__":
    main()
