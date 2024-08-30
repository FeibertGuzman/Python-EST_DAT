# Importar las Librerías necesarias de tkinter
from tkinter import Tk, Label, Button, Entry, Menu

"""
Descripción de los widgets utilizados en Tkinter:
    Tk: Es el widget raíz de una aplicación Tkinter. Es la ventana principal de la aplicación y contiene todos los demás widgets.
    Label: Un Label (etiqueta) muestra texto o una imagen en la pantalla. Es información estática que no interactúa con el usuario.
    Button: Un Button (botón) permite al usuario interactuar con la aplicación. Al hacer clic, se activa una función asociada.
    Entry: Un Entry (entrada) permite al usuario ingresar texto o números. Es un campo de texto editable comúnmente usado en formularios.
    Menu: Un Menu (menú) es un contenedor de opciones que permite la navegación y ejecución de funciones.
"""

# Definir las funciones para las operaciones
def fnSuma():
    n1 = txt1.get()
    n2 = txt2.get()
    r = float(n1) + float(n2)
    txt3.delete(0, 'end')  # Limpiar el campo de resultado
    txt3.insert(0, r)  # Insertar el resultado en el campo de texto

def fnResta():
    n1 = txt1.get()
    n2 = txt2.get()
    r = float(n1) - float(n2)
    txt3.delete(0, 'end')  # Limpiar el campo de resultado
    txt3.insert(0, r)  # Insertar el resultado en el campo de texto

# Definir la función que se ejecutará al presionar el botón "Salir"
def fnSalir():
    vent.destroy()  # Cierra la ventana principal

def crear_menu(vent):
    # Crear barra de menú
    barra_menu = Menu(vent)  # Crea una barra de menú principal en la ventana 'vent'
    vent.config(menu=barra_menu)  # Configura la ventana 'vent' para que use esta barra de menú
    
    # Menú "Inicio"
    menu_inicio = Menu(barra_menu, tearoff=0)  # Crea un submenú dentro de la barra de menú, llamado "Inicio"
    barra_menu.add_cascade(label="Inicio", menu=menu_inicio)  # Añade el submenú "Inicio" a la barra de menú
    menu_inicio.add_command(label="Salir", command=vent.destroy)  # Añade una opción al submenú "Inicio" para cerrar la ventana
    
    # Menú "Operación"
    menu_operacion = Menu(barra_menu, tearoff=0)  # Crea otro submenú dentro de la barra de menú, llamado "Operación"
    barra_menu.add_cascade(label="Operación", menu=menu_operacion)  # Añade el submenú "Operación" a la barra de menú
    menu_operacion.add_command(label="Sumar", command=fnSuma)  # Añade una opción al submenú "Operación" para realizar la suma
    menu_operacion.add_command(label="Restar", command=fnResta)  # Añade una opción al submenú "Operación" para realizar la resta


def crear_ventana():
    # Configuración de colores y fuentes
    bg_color = "#F0F0F0"  # Fondo claro
    fg_color = "#333"  # Texto oscuro
    font = ("Arial", 12)  # Fuente estándar

    # Crear la ventana principal
    vent = Tk()
    vent.title("Calculadora Simple")  # Título de la ventana
    vent.geometry("500x300")  # Dimensiones de la ventana
    vent.configure(bg=bg_color)  # Color de fondo de la ventana

    # Crear el menú
    crear_menu(vent)

    # Crear los elementos de la interfaz de usuario
    global txt1, txt2, txt3  # Declarar las entradas como globales para que las funciones puedan acceder a ellas

    # Etiqueta y campo de texto para el primer número
    lbl1 = Label(vent, text="Primer número", fg=fg_color, bg=bg_color, font=font)
    lbl1.place(relx=0.5, rely=0.1, anchor='center', relwidth=0.6, relheight=0.1)
    txt1 = Entry(vent, bg="#FFF")  # Campo de entrada para el primer número (fondo blanco)
    txt1.place(relx=0.5, rely=0.2, anchor='center', relwidth=0.6, relheight=0.1)

    # Etiqueta y campo de texto para el segundo número
    lbl2 = Label(vent, text="Segundo número", fg=fg_color, bg=bg_color, font=font)
    lbl2.place(relx=0.5, rely=0.35, anchor='center', relwidth=0.6, relheight=0.1)
    txt2 = Entry(vent, bg="#FFF")  # Campo de entrada para el segundo número (fondo blanco)
    txt2.place(relx=0.5, rely=0.45, anchor='center', relwidth=0.6, relheight=0.1)

    # Etiqueta y campo de texto para el resultado
    lbl3 = Label(vent, text="Resultado", fg=fg_color, bg=bg_color, font=font)
    lbl3.place(relx=0.5, rely=0.6, anchor='center', relwidth=0.6, relheight=0.1)
    txt3 = Entry(vent, bg="#FFF")  # Campo de entrada para el resultado (fondo blanco)
    txt3.place(relx=0.5, rely=0.7, anchor='center', relwidth=0.6, relheight=0.1)

    # Botón "Sumar"
    btn1 = Button(vent, text="Sumar", command=fnSuma, bg=bg_color, fg=fg_color, font=font)
    btn1.place(relx=0.3, rely=0.9, anchor='center', relwidth=0.2, relheight=0.1)

    # Botón "Restar"
    btn2 = Button(vent, text="Restar", command=fnResta, bg=bg_color, fg=fg_color, font=font)
    btn2.place(relx=0.7, rely=0.9, anchor='center', relwidth=0.2, relheight=0.1)

    # Botón "Salir"
    btnSalir = Button(vent, text="Salir", command=fnSalir, bg="#E74C3C", fg="#FFF", font=font)
    btnSalir.place(relx=0.5, rely=0.9, anchor='center', relwidth=0.2, relheight=0.1)

    return vent  # Devolver la ventana creada

# Crear la ventana principal
vent = crear_ventana()

# Iniciar el bucle principal de la aplicación
vent.mainloop()
