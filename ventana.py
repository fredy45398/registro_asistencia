import tkinter as tk

def create_table(root, data, row, col, wide_col_index=None):
    # Crear un marco para la tabla
    frame = tk.Frame(root)
    frame.grid(row=row, column=col, padx=10, pady=10)

    # Crear un canvas para el desplazamiento
    canvas = tk.Canvas(frame)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Crear un scrollbar vertical
    scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configurar el canvas para el desplazamiento
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Crear un frame interno para contener la tabla
    table_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=table_frame, anchor="nw")

    # Llenar el frame interno con la tabla
    for i, row_data in enumerate(data):
        cell = tk.Label(table_frame, text=row_data[1], relief="solid", padx=5, pady=5)
        cell.grid(row=i, column=0, columnspan=10, sticky="nsew")  # Extiende la celda a 3 columnas
        cell_1 = tk.Label(table_frame, text=row_data[2], relief="solid", padx=5, pady=5)
        cell_1.grid(row=i, column=9, sticky="nsew")


    # Configurar pesos para que las celdas crezcan
    #for i in range(len(data[0]) + 2):  # Ajustar para el columnspan
        #table_frame.grid_columnconfigure(i, weight=1)

    #for i in range(len(data)):
        #table_frame.grid_rowconfigure(i, weight=1)

# Datos de ejemplo para la tabla
data = [
    ["A1", "Texto largo que ocupa más espacio", "C1", "D1", "E1"],
    ["A2", "Texto normal", "C2", "D2", "E2"],
    ["A3", "Otro texto largo que ocupa espacio", "C3", "D3", "E3"]
]

# Crear la ventana principal
root = tk.Tk()
root.title("Tabla con Columna Expandida")

# Crear la tabla, haciendo que la segunda columna ocupe el espacio de tres columnas
create_table(root, data, row=0, col=0, wide_col_index=1)

root.mainloop()

