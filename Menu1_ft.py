# -*- coding: utf-8 -*-
"""
==========================================================
            CALCULADORA CON FLET
==========================================================

Este programa es una calculadora interactiva desarrollada con Flet.
Permite realizar operaciones básicas: suma, resta, multiplicación, 
división y cálculo de factorial. Se estructura en funciones para modularizar
cada operación y el flujo general del programa.

Características:
- Se utiliza Flet para crear una interfaz gráfica web/desktop.
- Se emplean AlertDialogs para solicitar datos y mostrar resultados.
- Se validan errores como división por cero y factorial de números negativos.
- La aplicación se cierra al presionar el botón "Salir".

Autor: [Tu Nombre]
Fecha: [Fecha Actual]
"""

# Importamos la función factorial desde el módulo math.
from math import factorial

# Importamos Flet y el módulo sys para poder salir de la aplicación.
import flet as ft
import sys

# ----------------------------------------------------------------
# Función: mostrar_dialogo
# ----------------------------------------------------------------
def mostrar_dialogo(page: ft.Page, titulo: str, contenido: ft.Control):
    """
    Muestra un AlertDialog con el título y contenido proporcionados.
    
    Parámetros:
    - page (ft.Page): Página principal de la aplicación.
    - titulo (str): Título del diálogo.
    - contenido (ft.Control): Contenido que se mostrará en el diálogo.
    """
    dialogo = ft.AlertDialog(
        title=ft.Text(titulo),
        content=contenido,
        actions=[
            ft.TextButton("Cerrar", on_click=lambda e: cerrar_dialogo(page))
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    page.dialog = dialogo
    dialogo.open = True
    page.update()

# ----------------------------------------------------------------
# Función: cerrar_dialogo
# ----------------------------------------------------------------
def cerrar_dialogo(page: ft.Page):
    """
    Cierra el diálogo actual de la página.
    
    Parámetros:
    - page (ft.Page): Página principal de la aplicación.
    """
    page.dialog.open = False
    page.update()

# ----------------------------------------------------------------
# Función: operacion_suma
# ----------------------------------------------------------------
def operacion_suma(page: ft.Page):
    """
    Solicita dos números al usuario mediante AlertDialog, calcula su suma y muestra el resultado.
    
    Parámetros:
    - page (ft.Page): Página principal de la aplicación.
    """
    tf_num1 = ft.TextField(label="Primer número", width=200)
    tf_num2 = ft.TextField(label="Segundo número", width=200)
    
    def calcular_suma(e):
        try:
            num1 = float(tf_num1.value)
            num2 = float(tf_num2.value)
            resultado = num1 + num2
            mostrar_dialogo(page, "Resultado de la Suma", ft.Text(f"El resultado de la suma es: {resultado}"))
        except ValueError:
            mostrar_dialogo(page, "Error", ft.Text("Por favor ingrese números válidos."))
    
    contenido = ft.Column(
        [
            tf_num1,
            tf_num2,
            ft.ElevatedButton("Calcular", on_click=calcular_suma),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )
    mostrar_dialogo(page, "Suma", contenido)

# ----------------------------------------------------------------
# Función: operacion_resta
# ----------------------------------------------------------------
def operacion_resta(page: ft.Page):
    """
    Solicita dos números al usuario, calcula la resta (primer número - segundo) y muestra el resultado.
    
    Parámetros:
    - page (ft.Page): Página principal de la aplicación.
    """
    tf_num1 = ft.TextField(label="Primer número", width=200)
    tf_num2 = ft.TextField(label="Segundo número", width=200)
    
    def calcular_resta(e):
        try:
            num1 = float(tf_num1.value)
            num2 = float(tf_num2.value)
            resultado = num1 - num2
            mostrar_dialogo(page, "Resultado de la Resta", ft.Text(f"El resultado de la resta es: {resultado}"))
        except ValueError:
            mostrar_dialogo(page, "Error", ft.Text("Por favor ingrese números válidos."))
    
    contenido = ft.Column(
        [
            tf_num1,
            tf_num2,
            ft.ElevatedButton("Calcular", on_click=calcular_resta),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )
    mostrar_dialogo(page, "Resta", contenido)

# ----------------------------------------------------------------
# Función: operacion_multiplicacion
# ----------------------------------------------------------------
def operacion_multiplicacion(page: ft.Page):
    """
    Solicita dos números al usuario, calcula su producto y muestra el resultado.
    
    Parámetros:
    - page (ft.Page): Página principal de la aplicación.
    """
    tf_num1 = ft.TextField(label="Primer número", width=200)
    tf_num2 = ft.TextField(label="Segundo número", width=200)
    
    def calcular_multiplicacion(e):
        try:
            num1 = float(tf_num1.value)
            num2 = float(tf_num2.value)
            resultado = num1 * num2
            mostrar_dialogo(page, "Resultado de la Multiplicación", ft.Text(f"El resultado es: {resultado}"))
        except ValueError:
            mostrar_dialogo(page, "Error", ft.Text("Por favor ingrese números válidos."))
    
    contenido = ft.Column(
        [
            tf_num1,
            tf_num2,
            ft.ElevatedButton("Calcular", on_click=calcular_multiplicacion),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )
    mostrar_dialogo(page, "Multiplicación", contenido)

# ----------------------------------------------------------------
# Función: operacion_division
# ----------------------------------------------------------------
def operacion_division(page: ft.Page):
    """
    Solicita dos números al usuario, realiza la división del primero entre el segundo,
    valida que el divisor no sea cero y muestra el resultado.
    
    Parámetros:
    - page (ft.Page): Página principal de la aplicación.
    """
    tf_num1 = ft.TextField(label="Dividendo", width=200)
    tf_num2 = ft.TextField(label="Divisor", width=200)
    
    def calcular_division(e):
        try:
            num1 = float(tf_num1.value)
            num2 = float(tf_num2.value)
            if num2 == 0:
                mostrar_dialogo(page, "Error en División", ft.Text("No se puede dividir por cero."))
            else:
                resultado = num1 / num2
                mostrar_dialogo(page, "Resultado de la División", ft.Text(f"El resultado es: {resultado}"))
        except ValueError:
            mostrar_dialogo(page, "Error", ft.Text("Por favor ingrese números válidos."))
    
    contenido = ft.Column(
        [
            tf_num1,
            tf_num2,
            ft.ElevatedButton("Calcular", on_click=calcular_division),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )
    mostrar_dialogo(page, "División", contenido)

# ----------------------------------------------------------------
# Función: operacion_factorial
# ----------------------------------------------------------------
def operacion_factorial(page: ft.Page):
    """
    Solicita al usuario un número entero, valida que no sea negativo y calcula su factorial.
    Muestra el resultado o un mensaje de error si el número es negativo.
    
    Parámetros:
    - page (ft.Page): Página principal de la aplicación.
    """
    tf_num = ft.TextField(label="Número entero", width=200)
    
    def calcular_factorial_local(e):
        try:
            num = int(tf_num.value)
            if num < 0:
                mostrar_dialogo(page, "Error en Factorial", ft.Text("El factorial no está definido para números negativos."))
            else:
                resultado = factorial(num)
                mostrar_dialogo(page, "Resultado del Factorial", ft.Text(f"El factorial de {num} es: {resultado}"))
        except ValueError:
            mostrar_dialogo(page, "Error", ft.Text("Por favor ingrese un número entero válido."))
    
    contenido = ft.Column(
        [
            tf_num,
            ft.ElevatedButton("Calcular", on_click=calcular_factorial_local),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )
    mostrar_dialogo(page, "Factorial", contenido)

# ----------------------------------------------------------------
# Función: main
# ----------------------------------------------------------------
def main(page: ft.Page):
    """
    Función principal que crea la interfaz de la calculadora con Flet.
    Se crea un layout con botones para cada operación y uno para salir.
    
    Parámetros:
    - page (ft.Page): Página principal de la aplicación.
    """
    page.title = "Calculadora con Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Título de la aplicación.
    titulo = ft.Text("Calculadora", style="headlineMedium")
    
    # Botones para cada operación, cada uno llama a su función mediante lambda.
    boton_suma = ft.ElevatedButton("Suma", on_click=lambda e: operacion_suma(page), width=150)
    boton_resta = ft.ElevatedButton("Resta", on_click=lambda e: operacion_resta(page), width=150)
    boton_multiplicacion = ft.ElevatedButton("Multiplicación", on_click=lambda e: operacion_multiplicacion(page), width=150)
    boton_division = ft.ElevatedButton("División", on_click=lambda e: operacion_division(page), width=150)
    boton_factorial = ft.ElevatedButton("Factorial", on_click=lambda e: operacion_factorial(page), width=150)
    # Para salir de la aplicación, se utiliza sys.exit(0).
    boton_salir = ft.ElevatedButton("Salir", on_click=lambda e: sys.exit(0), width=150, bgcolor=ft.Colors.RED, color=ft.Colors.WHITE)

    # Layout principal, organizando los botones en filas y columnas.
    layout = ft.Column(
        [
            titulo,
            ft.Row([boton_suma, boton_resta], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([boton_multiplicacion, boton_division], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([boton_factorial, boton_salir], alignment=ft.MainAxisAlignment.CENTER),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20,
    )
    
    page.add(layout)

# ----------------------------------------------------------------
# Punto de entrada de la aplicación
# ----------------------------------------------------------------
if __name__ == "__main__":
    # Inicia la aplicación Flet usando main como función de inicio.
    ft.app(target=main)
