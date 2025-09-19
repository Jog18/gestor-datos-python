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