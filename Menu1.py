# -*- coding: utf-8 -*-
"""
==========================================================
            CALCULADORA CON FUNCIONES EN PYTHON
==========================================================

Este programa es una calculadora interactiva que permite realizar
operaciones básicas: suma, resta, multiplicación, división y cálculo
de factorial. Se estructura en funciones para modularizar cada
operación y el flujo general del programa.

Características:
- Se utilizan funciones para cada operación y para mostrar el menú.
- Se valida la división por cero y el cálculo del factorial para números negativos.
- El programa se ejecuta en un bucle hasta que el usuario decide salir.

Autor: [Tu Nombre]
Fecha: [Fecha Actual]
"""

# Importamos la función factorial desde el módulo math.
# Esta función se utiliza para calcular el factorial de un número entero.
from math import factorial

# ----------------------------------------------------------------
# Función: mostrar_menu
# ----------------------------------------------------------------
def mostrar_menu():
    """
    Muestra en pantalla el menú de opciones disponibles en la calculadora.
    """
    print("=== Calculadora ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Factorial")
    print("6. Salir")

# ----------------------------------------------------------------
# Función: suma
# ----------------------------------------------------------------
def suma():
    """
    Solicita dos números al usuario, calcula su suma y muestra el resultado.
    """
    # Solicita el primer número y lo convierte a float.
    num1 = float(input("Ingrese el primer número: "))
    # Solicita el segundo número y lo convierte a float.
    num2 = float(input("Ingrese el segundo número: "))
    # Realiza la suma de ambos números.
    resultado = num1 + num2
    # Imprime el resultado de la suma.
    print(f"El resultado de la suma es: {resultado}")

# ----------------------------------------------------------------
# Función: resta
# ----------------------------------------------------------------
def resta():
    """
    Solicita dos números al usuario, calcula la resta (primer número menos segundo) y muestra el resultado.
    """
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 - num2
    print(f"El resultado de la resta es: {resultado}")

# ----------------------------------------------------------------
# Función: multiplicacion
# ----------------------------------------------------------------
def multiplicacion():
    """
    Solicita dos números al usuario, calcula su producto y muestra el resultado.
    """
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 * num2
    print(f"El resultado de la multiplicación es: {resultado}")

# ----------------------------------------------------------------
# Función: division
# ----------------------------------------------------------------
def division():
    """
    Solicita dos números al usuario, realiza la división del primero entre el segundo
    y muestra el resultado. Valida que el divisor no sea cero para evitar errores.
    """
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    # Verifica que el divisor no sea cero.
    if num2 == 0:
        print("Error: No se puede dividir por cero.")
    else:
        resultado = num1 / num2
        print(f"El resultado de la división es: {resultado}")

# ----------------------------------------------------------------
# Función: calcular_factorial
# ----------------------------------------------------------------
def calcular_factorial():
    """
    Solicita al usuario un número entero, verifica que no sea negativo y
    calcula su factorial, mostrando el resultado.
    """
    num = int(input("Ingrese un número entero para calcular su factorial: "))
    # Verifica que el número sea no negativo.
    if num < 0:
        print("Error: El factorial no está definido para números negativos.")
    else:
        resultado = factorial(num)
        print(f"El factorial de {num} es: {resultado}")

# ----------------------------------------------------------------
# Función: main
# ----------------------------------------------------------------
def main():
    """
    Función principal que controla el flujo del programa.
    Muestra el menú, solicita la opción al usuario y llama a la función correspondiente.
    El bucle se repite hasta que el usuario decide salir.
    """
    while True:
        mostrar_menu()  # Muestra el menú de opciones.
        opcion = input("Elija una opción (1-6): ")  # Solicita la opción al usuario.

        # Evaluamos la opción ingresada por el usuario:
        if opcion == "1":
            suma()  # Llama a la función que realiza la suma.
        elif opcion == "2":
            resta()  # Llama a la función que realiza la resta.
        elif opcion == "3":
            multiplicacion()  # Llama a la función que realiza la multiplicación.
        elif opcion == "4":
            division()  # Llama a la función que realiza la división.
        elif opcion == "5":
            calcular_factorial()  # Llama a la función que calcula el factorial.
        elif opcion == "6":
            # Muestra un mensaje de despedida y rompe el bucle para terminar el programa.
            print("Gracias por usar la calculadora. ¡Hasta luego!")
            break
        else:
            # Se muestra un mensaje si la opción ingresada no es válida.
            print("Opción no válida. Por favor, elija una opción del 1 al 6.")

        # Pausa para que el usuario pueda ver el resultado antes de continuar.
        input("Presione Enter para continuar...")

# ----------------------------------------------------------------
# Punto de entrada del programa
# ----------------------------------------------------------------
if __name__ == "__main__":
    # Ejecuta la función principal solo si este script se ejecuta directamente.
    main()
