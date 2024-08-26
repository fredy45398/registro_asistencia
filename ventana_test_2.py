import tkinter as tk
from tkinter import ttk

# Función para el evento del botón
def on_button_click(index):
    print(f"Botón en la fila {index + 1} fue presionado")

# Crear la ventana principal
root = tk.Tk()
root.title("Tabla en Ventana Principal")

# Definir el tamaño de la ventana principal
ancho_ventana = 500
alto_ventana = 300
root.geometry(f"{ancho_ventana}x{alto_ventana}")

# Crear un frame para contener el Canvas y el Scrollbar, y centrarlo
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")
frame.grid(row=0, column=0)

# Crear un Canvas para simular la tabla y permitir el desplazamiento
canvas = tk.Canvas(frame)
canvas.pack(side="left", fill="both", expand=True)

# Crear un Scrollbar vertical para el Canvas
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

# Configurar el Canvas para usar el Scrollbar
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Crear un frame secundario dentro del Canvas, con borde
frame_in_canvas = tk.Frame(canvas, bd=2, relief="solid")  # Añadir borde y estilo
canvas.create_window((0, 0), window=frame_in_canvas, anchor="nw")

# Lista de valores a mostrar en la primera columna
valores = [f"Valor {i+1}" for i in range(5)]

# Añadir filas con texto y un botón a cada una
for i, valor in enumerate(valores):
    # Crear etiqueta para el valor de la primera columna
    label = tk.Label(frame_in_canvas, text=valor, width=30, anchor="w")
    label.grid(row=i, column=0, padx=5, pady=2)

    # Crear botón para la segunda columna
    boton = tk.Button(frame_in_canvas, text="Click Me", command=lambda i=i: on_button_click(i))
    boton.grid(row=i, column=1, padx=5, pady=2)

# Ajustar el tamaño del frame_in_canvas al contenido
frame_in_canvas.update_idletasks()

###################
frame_2 = tk.Frame(root)
frame_2.place(relx=1.5, rely=1.5, anchor="center")
frame_2.grid(row=1, column=0)

# Crear un Canvas para simular la tabla y permitir el desplazamiento
canvas_2 = tk.Canvas(frame_2)
canvas_2.pack(side="left", fill="both", expand=True)

# Crear un Scrollbar vertical para el Canvas
scrollbar_2 = ttk.Scrollbar(frame_2, orient="vertical", command=canvas_2.yview)
scrollbar_2.pack(side="right", fill="y")

# Configurar el Canvas para usar el Scrollbar
canvas_2.configure(yscrollcommand=scrollbar_2.set)
canvas_2.bind('<Configure>', lambda e: canvas_2.configure(scrollregion=canvas_2.bbox("all")))

# Crear un frame secundario dentro del Canvas, con borde
frame_in_canvas_2 = tk.Frame(canvas_2, bd=2, relief="solid")  # Añadir borde y estilo
canvas_2.create_window((0, 0), window=frame_in_canvas_2, anchor="nw")

# Lista de valores a mostrar en la primera columna
valores = [f"Item {i+1}" for i in range(5)]

# Añadir filas con texto y un botón a cada una
for i, valor in enumerate(valores):
    # Crear etiqueta para el valor de la primera columna
    label = tk.Label(frame_in_canvas_2, text=valor, width=30, anchor="w")
    label.grid(row=i, column=0, padx=5, pady=2)

    # Crear botón para la segunda columna
    boton = tk.Button(frame_in_canvas_2, text="Click Me", command=lambda i=i: on_button_click(i))
    boton.grid(row=i, column=1, padx=5, pady=2)

# Ajustar el tamaño del frame_in_canvas al contenido
frame_in_canvas_2.update_idletasks()

###################





# Ejecutar el bucle principal de la ventana
root.mainloop()
