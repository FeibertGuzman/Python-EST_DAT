from tkinter import *  # Importa todos los componentes del módulo tkinter, que se utiliza para crear interfaces gráficas en Python.

def miFuncion():
    print("Este mensaje es del botón")  # Define una función que se ejecutará cuando se presione el botón. Imprime un mensaje en la consola.

# Crear la ventana principal
ventana = Tk()  # Crea la ventana principal de la aplicación.
ventana.title("Hola Mundo")  # Establece el título de la ventana.
ventana.geometry("400x200")  # Define las dimensiones de la ventana en píxeles (ancho x alto).

# Crear un label (etiqueta) en la ventana
lebel = Label(ventana, text="Este es un label")  # Crea una etiqueta con el texto "Este es un label".
lebel.config(bg="#FF00FF")  # Configura el color de fondo de la etiqueta a gris.
lebel.pack()  # Empaqueta la etiqueta en la ventana para que se muestre. `pack()` es un método que coloca el widget en la ventana.

# Crear un botón en la ventana
boton = Button(ventana, text="Presionar", command=miFuncion)  # Crea un botón con el texto "Presionar". Cuando se presiona, llama a la función `miFuncion`.
#btn.config(fg="red", bg="blue")  # Otra manera de configurar los colores, comentado aquí como ejemplo.
boton["fg"] = "#red"  # Configura el color del texto del botón a rojo.
boton["bg"] = "yellow"  # Configura el color de fondo del botón a amarillo.
boton.pack()  # Empaqueta el botón en la ventana para que se muestre.

# Inicia el bucle principal de la ventana
ventana.mainloop()  # Inicia el bucle principal de la ventana. Mantiene la ventana abierta y en espera de eventos (como clics de botón) hasta que se cierre.
