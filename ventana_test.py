import tkinter as tk
from tkinter import ttk

# Ventana principal
root = tk.Tk()
root.title("Dos Formularios en una Tabla General")
root.geometry("600x400")

# Canvas para contener los formularios
canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Scrollbar para el Canvas
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.configure(yscrollcommand=scrollbar.set)

# Frame dentro del Canvas que contendrá los formularios
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

# Función para ajustar el tamaño del Canvas según el contenido
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

frame.bind("<Configure>", on_frame_configure)

# Función para crear un formulario
def crear_formulario(parent, titulo):
    form_frame = ttk.LabelFrame(parent, text=titulo, padding=(10, 10))
    form_frame.pack(fill=tk.BOTH, expand=True, pady=(10, 5))

    # Ejemplo de entradas de texto y etiquetas
    ttk.Label(form_frame, text="Nombre:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
    ttk.Entry(form_frame).grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(form_frame, text="Apellido:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
    ttk.Entry(form_frame).grid(row=1, column=1, padx=5, pady=5)

    ttk.Label(form_frame, text="Correo Electrónico:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
    ttk.Entry(form_frame).grid(row=2, column=1, padx=5, pady=5)

    ttk.Label(form_frame, text="Teléfono:").grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
    ttk.Entry(form_frame).grid(row=3, column=1, padx=5, pady=5)

    ttk.Button(form_frame, text="Enviar").grid(row=4, columnspan=2, pady=10)

# Crear dos formularios, uno debajo del otro
crear_formulario(frame, "Formulario 1")
crear_formulario(frame, "Formulario 2")

# Ajustar el tamaño del Canvas al contenido
frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Inicia el bucle principal
root.mainloop()
