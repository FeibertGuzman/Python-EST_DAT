# Importar las clases necesarias de tkinter
from tkinter import Tk, Label, Button, Entry

"""
Descripción de los widgets utilizados en Tkinter:
    Tk: Es el widget raíz de una aplicación Tkinter. Es la ventana principal de la aplicación y contiene todos los demás widgets.
    Label: Un Label (etiqueta) muestra texto o una imagen en la pantalla. Es información estática que no interactúa con el usuario.
    Button: Un Button (botón) permite al usuario interactuar con la aplicación. Al hacer clic, se activa una función asociada.
    Entry: Un Entry (entrada) permite al usuario ingresar texto o números. Es un campo de texto editable comúnmente usado en formularios.
"""

# Crear la ventana principal
def crear_ventana():
    vent = Tk()
    vent.title("Ejemplo de place")  # Título de la ventana
    vent.geometry("400x200")  # Dimensiones de la ventana

    # Definir la función que se ejecutará al presionar el botón "Sumar"
    def fnSuma():
        # Obtener los valores de los campos de texto
        n1 = txt1.get()
        n2 = txt2.get()
        # Realizar la suma y mostrar el resultado
        r = float(n1) + float(n2)
        txt3.delete(0, 'end')  # Limpiar el campo de resultado
        txt3.insert(0, r)  # Insertar el resultado en el campo de texto

    # Definir la función que se ejecutará al presionar el botón "Restar"
    def fnResta():
        # Obtener los valores de los campos de texto
        n1 = txt1.get()
        n2 = txt2.get()
        # Realizar la resta y mostrar el resultado
        r = float(n1) - float(n2)
        txt3.delete(0, 'end')  # Limpiar el campo de resultado
        txt3.insert(0, r)  # Insertar el resultado en el campo de texto

    # Crear los elementos de la interfaz de usuario
    # Etiqueta y campo de texto para el primer número
    lbl1 = Label(vent, text="Primer número")
    lbl1.place(relx=0.03, rely=0.04, relwidth=0.23, relheight=0.1)
    txt1 = Entry(vent)  # Campo de entrada para el primer número
    txt1.place(relx=0.5, rely=0.1, anchor='center')

    # Etiqueta y campo de texto para el segundo número
    lbl2 = Label(vent, text="Segundo número", fg="white", bg="blue", font=("Arial", 11, "bold"))
    lbl2.place(relx=0.5, rely=0.3, anchor='center')
    txt2 = Entry(vent, bg="#FFC0CB")  # Campo de entrada para el segundo número (color rosa)
    txt2.place(relx=0.5, rely=0.5, anchor='center')

    # Etiqueta y campo de texto para el resultado
    lbl3 = Label(vent, text="Resultado")
    lbl3.place(relx=0.5, rely=0.6, anchor='center')
    txt3 = Entry(vent, bg="#FFC0CB")  # Campo de entrada para el resultado (color rosa)
    txt3.place(relx=0.5, rely=0.7, anchor='center')

    # Botón "Sumar"
    btn1 = Button(vent, text="Sumar", command=fnSuma)
    btn1.place(relx=0.3, rely=0.9, anchor='center')

    # Botón "Restar"
    btn2 = Button(vent, text="Restar", command=fnResta)
    btn2.place(relx=0.7, rely=0.9, anchor='center')

    return vent  # Devolver la ventana creada

# Crear la ventana principal
vent = crear_ventana()

# Iniciar el bucle principal de la aplicación
vent.mainloop()
