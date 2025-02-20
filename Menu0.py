# -*- coding: utf-8 -*-
"""
==========================================================
            CALCULADORA SIMPLE EN PYTHON
==========================================================

Este programa es una calculadora interactiva en consola que permite 
realizar operaciones básicas como suma, resta, multiplicación, 
división y cálculo de factorial.

Características:
- Funciona con entrada de usuario en un bucle continuo.
- Permite salir del programa al seleccionar la opción correspondiente.
- Implementa validaciones básicas, como evitar la división por cero.

Autor: [Tu Nombre]
Fecha: [Fecha Actual]
"""

# Importamos la función factorial desde la librería estándar math
# Esta función nos permite calcular el factorial de un número entero.
from math import factorial

# ===================== INICIO DEL PROGRAMA =====================

# El bucle while permite que el programa se ejecute de forma continua
# hasta que el usuario elija la opción de salir.
while True:
    # Mostrar el menú de opciones disponibles en la calculadora
    print("\n=== Calculadora ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Factorial")
    print("6. Salir")

    # Se solicita al usuario que elija una opción del menú
    opcion = input("Elija una opción (1-6): ")

    # ===================== OPERACIONES =====================

    # Opción 1: Suma
    if opcion == "1":
        # Se solicita al usuario que ingrese dos números
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        # Se calcula la suma
        resultado = num1 + num2
        # Se muestra el resultado en pantalla
        print(f"El resultado de la suma es: {resultado}")

    # Opción 2: Resta
    elif opcion == "2":
        # Se solicitan los números al usuario
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        # Se realiza la resta
        resultado = num1 - num2
        # Se muestra el resultado
        print(f"El resultado de la resta es: {resultado}")

    # Opción 3: Multiplicación
    elif opcion == "3":
        # Se solicitan los números al usuario
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        # Se calcula la multiplicación
        resultado = num1 * num2
        # Se muestra el resultado
        print(f"El resultado de la multiplicación es: {resultado}")

    # Opción 4: División
    elif opcion == "4":
        # Se solicitan los números al usuario
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        # Se verifica que el divisor no sea cero
        if num2 == 0:
            print("Error: No se puede dividir por cero.")
        else:
            # Se realiza la división
            resultado = num1 / num2
            # Se muestra el resultado
            print(f"El resultado de la división es: {resultado}")

    # Opción 5: Factorial
    elif opcion == "5":
        # Se solicita al usuario un número entero para calcular su factorial
        num = int(input("Ingrese un número entero para calcular su factorial: "))
        # Se verifica que el número sea positivo
        if num < 0:
            print("Error: El factorial no está definido para números negativos.")
        else:
            # Se calcula el factorial usando la función factorial() importada
            resultado = factorial(num)
            # Se muestra el resultado
            print(f"El factorial de {num} es: {resultado}")

    # Opción 6: Salir del programa
    elif opcion == "6":
        # Mensaje de despedida
        print("Gracias por usar la calculadora. ¡Hasta luego!")
        # El break termina el bucle while y finaliza la ejecución del programa.
        break

    # Caso de opción inválida
    else:
        print("Opción no válida. Por favor, elija una opción del 1 al 6.")

    # Se agrega una pausa antes de continuar para que el usuario pueda ver el resultado
    input("Presione Enter para continuar...")
