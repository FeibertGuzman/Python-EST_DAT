# -*- coding: utf-8 -*-
"""
==========================================================
            CALCULADORA CON TKINTER
==========================================================

Este programa es una calculadora interactiva con interfaz gráfica
desarrollada con Tkinter. Permite realizar operaciones básicas:
suma, resta, multiplicación, división y cálculo de factorial.
Cada operación se implementa en una función, y se utiliza la 
librería tkinter para crear ventanas, botones y diálogos de entrada.

Características:
- Se emplea Tkinter para crear una interfaz gráfica amigable.
- Se utilizan funciones para cada operación, siguiendo una estructura modular.
- Se validan errores como la división por cero y el factorial de números negativos.
- El programa se cierra al presionar el botón "Salir".

Autor: [Tu Nombre]
Fecha: [Fecha Actual]
"""

# Importamos la función factorial desde el módulo math para calcular factoriales.
from math import factorial

# Importamos Tkinter y algunos diálogos de entrada y mensajes.
import tkinter as tk
from tkinter import messagebox, simpledialog

# ----------------------------------------------------------------
# Función: suma
# ----------------------------------------------------------------


def suma():
    """
    Solicita dos números al usuario mediante diálogos, calcula su suma
    y muestra el resultado en un mensaje.
    """
    # Solicita el primer número (tipo float) mediante un diálogo.
    num1 = simpledialog.askfloat("Suma", "Ingrese el primer número:")
    if num1 is None:  # El usuario canceló la entrada.
        return

    # Solicita el segundo número.
    num2 = simpledialog.askfloat("Suma", "Ingrese el segundo número:")
    if num2 is None:
        return

    # Calcula la suma de ambos números.
    resultado = num1 + num2
    # Muestra el resultado en una ventana de mensaje.
    messagebox.showinfo("Resultado de la Suma",
                        f"El resultado de la suma es: {resultado}")

# ----------------------------------------------------------------
# Función: resta
# ----------------------------------------------------------------


def resta():
    """
    Solicita dos números al usuario, calcula la resta (primer número menos el segundo)
    y muestra el resultado en un mensaje.
    """
    num1 = simpledialog.askfloat("Resta", "Ingrese el primer número:")
    if num1 is None:
        return

    num2 = simpledialog.askfloat("Resta", "Ingrese el segundo número:")
    if num2 is None:
        return

    resultado = num1 - num2
    messagebox.showinfo("Resultado de la Resta",
                        f"El resultado de la resta es: {resultado}")

# ----------------------------------------------------------------
# Función: multiplicacion
# ----------------------------------------------------------------


def multiplicacion():
    """
    Solicita dos números al usuario, calcula su producto y muestra el resultado.
    """
    num1 = simpledialog.askfloat("Multiplicación", "Ingrese el primer número:")
    if num1 is None:
        return

    num2 = simpledialog.askfloat(
        "Multiplicación", "Ingrese el segundo número:")
    if num2 is None:
        return

    resultado = num1 * num2
    messagebox.showinfo("Resultado de la Multiplicación",
                        f"El resultado de la multiplicación es: {resultado}")

# ----------------------------------------------------------------
# Función: division
# ----------------------------------------------------------------


def division():
    """
    Solicita dos números al usuario, realiza la división del primero entre el segundo,
    valida que el divisor no sea cero y muestra el resultado o un mensaje de error.
    """
    num1 = simpledialog.askfloat("División", "Ingrese el primer número:")
    if num1 is None:
        return

    num2 = simpledialog.askfloat("División", "Ingrese el segundo número:")
    if num2 is None:
        return

    # Se valida que el divisor no sea cero.
    if num2 == 0:
        messagebox.showerror("Error en División",
                             "No se puede dividir por cero.")
    else:
        resultado = num1 / num2
        messagebox.showinfo("Resultado de la División",
                            f"El resultado de la división es: {resultado}")

# ----------------------------------------------------------------
# Función: calcular_factorial
# ----------------------------------------------------------------


def calcular_factorial():
    """
    Solicita al usuario un número entero, verifica que no sea negativo y
    calcula su factorial. Muestra el resultado o un mensaje de error si el número es negativo.
    """
    # Solicita un número entero mediante un diálogo.
    num = simpledialog.askinteger("Factorial", "Ingrese un número entero:")
    if num is None:
        return

    # Se valida que el número sea mayor o igual a cero.
    if num < 0:
        messagebox.showerror(
            "Error en Factorial", "El factorial no está definido para números negativos.")
    else:
        resultado = factorial(num)
        messagebox.showinfo("Resultado del Factorial",
                            f"El factorial de {num} es: {resultado}")

# ----------------------------------------------------------------
# Función: crear_interfaz
# ----------------------------------------------------------------


def crear_interfaz():
    """
    Crea la ventana principal de la calculadora con botones para cada operación.
    Cada botón llama a la función correspondiente.
    """
    # Se crea la ventana principal.
    ventana = tk.Tk()
    ventana.title("Calculadora con Tkinter")
    ventana.geometry("400x300")

    # Se crea un título o etiqueta para la calculadora.
    etiqueta_titulo = tk.Label(ventana, text="Calculadora", font=("Arial", 16))
    etiqueta_titulo.pack(pady=10)

    # Se crea un marco (frame) para organizar los botones.
    marco_botones = tk.Frame(ventana)
    marco_botones.pack(pady=10)

    # Botón para la suma.
    boton_suma = tk.Button(marco_botones, text="Suma", width=15, command=suma)
    boton_suma.grid(row=0, column=0, padx=5, pady=5)

    # Botón para la resta.
    boton_resta = tk.Button(marco_botones, text="Resta",
                            width=15, command=resta)
    boton_resta.grid(row=0, column=1, padx=5, pady=5)

    # Botón para la multiplicación.
    boton_multiplicacion = tk.Button(
        marco_botones, text="Multiplicación", width=15, command=multiplicacion)
    boton_multiplicacion.grid(row=1, column=0, padx=5, pady=5)

    # Botón para la división.
    boton_division = tk.Button(
        marco_botones, text="División", width=15, command=division)
    boton_division.grid(row=1, column=1, padx=5, pady=5)

    # Botón para calcular el factorial.
    boton_factorial = tk.Button(
        marco_botones, text="Factorial", width=15, command=calcular_factorial)
    boton_factorial.grid(row=2, column=0, padx=5, pady=5)

    # Botón para salir de la aplicación.
    boton_salir = tk.Button(marco_botones, text="Salir",
                            width=15, command=ventana.destroy)
    boton_salir.grid(row=2, column=1, padx=5, pady=5)

    # Se inicia el bucle principal de la interfaz.
    ventana.mainloop()


# ----------------------------------------------------------------
# Punto de entrada del programa
# ----------------------------------------------------------------
if __name__ == "__main__":
    # Se llama a la función que crea la interfaz gráfica.
    crear_interfaz()
