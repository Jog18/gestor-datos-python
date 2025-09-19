# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 11:53:10 2025

@author: oreaj
"""

import re

# Lista para almacenar los registros
registros = []

# Función para ingresar una fecha válida en formato xx-xx-xx
def ingresarFecha(cadena):
    while True:
        fecha = input(cadena)
        if re.fullmatch(r"\d{2}-\d{2}-\d{2}", fecha):
            return fecha
        else:
            print("Formato incorrecto. Use xx-xx-xx.")
            
def ingresarEdad(cadena):
    while True:
        try:
            retorno = int(input(cadena))  # pedimos dato y lo convertimos a entero
            return retorno
        except ValueError:                # capturamos error si no es número
            print("Solo se admiten valores numéricos.")
            retorno = None                # devolvemos None si falló
        

# Función para agregar un registro
def agregarRegistro():
    nombre = input("Ingrese nombre: ")
    fecha = ingresarFecha("Ingrese fecha (xx-xx-xx): ")
    edad = ingresarEdad("Ingrese edad: ")
    matricula = input("Ingrese matricula: ")
    registros.append({"nombre": nombre, "fecha": fecha, "edad": edad, "matricula": matricula})
    print("Registro agregado correctamente.")

# Función para listar registros
def listarRegistros():
        print("\n Lista de registros:")
        for i, reg in enumerate(registros, start=1):
            print(f"{i}. Nombre: {reg['nombre']}, Fecha: {reg['fecha']}, Edad: {reg['edad']}, Matricula: {reg['matricula']}")

# Función para buscar por nombre
def buscarRegistro():
    nombre = input("Ingrese el nombre a buscar: ")
    encontrados = [reg for reg in registros if reg["nombre"].lower() == nombre.lower()]
    for reg in encontrados:
            print(f"Encontrado: Nombre: {reg['nombre']}, Fecha: {reg['fecha']}, Edad: {reg['edad']}, Matricula: {reg['matricula']}")

# Función para eliminar un registro
def eliminarRegistro():
    nombre = input("Ingrese el nombre a eliminar: ")
    for reg in registros:
        if reg["nombre"].lower() == nombre.lower():
            registros.remove(reg)
            print("Registro eliminado correctamente.")
            return


# Menú principal
def menu():
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Agregar registro")
        print("2. Listar registros")
        print("3. Buscar por nombre")
        print("4. Eliminar registro")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregarRegistro()
        elif opcion == "2":
            listarRegistros()
        elif opcion == "3":
            buscarRegistro()
        elif opcion == "4":
            eliminarRegistro()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar programa
menu()
