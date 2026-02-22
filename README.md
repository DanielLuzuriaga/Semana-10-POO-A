# Semana-10-POO-A
Universidad Estatal Amazónica
Autor: Daniel Luzuriaga

Descripción del Proyecto

El presente proyecto consiste en un Sistema de Gestión de Inventarios en Python, desarrollado bajo el paradigma de Programación Orientada a Objetos (POO).

El sistema permite:

-Añadir productos
-Eliminar productos
-Actualizar productos
-Buscar productos por nombre
-Listar inventario completo
-Persistir datos en archivo de texto
-Manejar excepciones durante operaciones de archivo

Objetivo Académico

El objetivo es mejorar el sistema original entregado en la semana 9 agregando:

📂 Almacenamiento persistente en archivo inventario.txt
🔄 Recuperación automática de datos al iniciar el programa
⚠ Manejo robusto de excepciones (FileNotFoundError, PermissionError)
🧱 Código organizado en módulos (modelo, servicio y controlador)

Estructura del Proyecto
inventario_app/
│
├── main.py
├── inventario.txt
│
├── modelos/
│   ├── __init__.py
│   └── producto.py
│
└── servicios/
    ├── __init__.py
    └── inventario.py
