
#### PAGOS DE CONSTRUCCION ####
from base_datos_conexion import *
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from openpyxl import Workbook

class Asistencia():
    def __init__(self,estado,fecha):
        self.estado = estado
        self.fecha = fecha

    def imprimir(self):
        print("los datos de la asistencia son: ")
        print(self.fecha)
        print(self.estado)

def registrar_si():
    fecha_actual = datetime.now().date()
    nueva_asistencia = Asistencia('si_trabajo',fecha_actual)
    fecha_coincidencias = buscar_asistencia_por_fecha(fecha_actual)
    if not fecha_coincidencias:
        insertar(nueva_asistencia)
        nueva_asistencia.imprimir()
    else:
        print("Ya hay un registro")

def registrar_no():
    fecha_actual = datetime.now().date()
    nueva_asistencia = Asistencia('no_trabajo',fecha_actual)
    fecha_coincidencias = buscar_asistencia_por_fecha(fecha_actual)
    if not fecha_coincidencias:
        insertar(nueva_asistencia)
        nueva_asistencia.imprimir()
    else:
        print("Ya hay un registro")

def obtener_numero_semana(fecha):
    fecha_str = str(fecha)
    fechas_dt = datetime.strptime(fecha_str, '%Y-%m-%d')
    semana = fechas_dt.isocalendar()
    numero_semana = semana[1]
    return numero_semana

def generar_reporte():
    lista_tmp = []
    lista_final = []
    lista_asistencias = obtener_todas_asistencias_ok()
    for registro in lista_asistencias:
        fecha_registro = registro[1]
        num_semana = obtener_numero_semana(fecha_registro)
        lista_tmp.append([num_semana,fecha_registro])
        print(num_semana," ",fecha_registro)
    for num_sem in range(1,36):
        dias_semana = []
        for registro in lista_tmp:
            if registro[0] == num_sem:
                dias_semana.append(registro)
        if len(dias_semana) > 0:
            suma_semana = len(dias_semana) * 80
            lista_final.append([num_sem,dias_semana,suma_semana])
            print([num_sem,dias_semana,suma_semana])
            print("4444444444444444444")
            #print(num_sem, suma_semana)
    exportar_excel(lista_final)

def obtener_dia_de_semana(fecha):
    fecha_obj = datetime.strptime(fecha, '%Y-%m-%d').date()
    dia_semana_num = fecha_obj.weekday()
    return dia_semana_num



def exportar_excel(datos):
    cont = 2
    wb = Workbook()
    ws = wb.active
    ws['A1'] = "SEMANA"
    ws['B1'] = "LUNES"
    ws['C1'] = "MARTES"
    ws['D1'] = "MIERCOLES"
    ws['E1'] = "JUEVES"
    ws['F1'] = "VIERNES"
    ws['G1'] = "TOTAL"
    
    for registro in datos:
        ws[f'A{cont}'] = registro[0]
        lista_dias = []
        for dato in registro[1]:
            dia_semana_num = obtener_dia_de_semana(str(dato[1]))
            lista_dias.append(dia_semana_num)
        for i in range(0,6): # 0 es lunes, 1 es martes ...
            letra = chr(ord('A')+i+1)
            if i in lista_dias:
                ws[f'{letra}{cont}'] = 'SI'
            else:
                ws[f'{letra}{cont}'] = 'NO'
        ws[f'G{cont}'] = registro[2]

        cont += 1


    wb.save("dias_semana.xlsx")
    print("Archivo 'dias_semana.xlsx' generado exitosamente.")



ventana = tk.Tk()
ventana.title("Formulario de Registro")
ventana.geometry("600x600")


tk.Label(ventana, text="Se trabajo hoy?").grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

boton_registrar_si = tk.Button(ventana, text="Si", command=registrar_si)
boton_registrar_si.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

boton_registrar_no = tk.Button(ventana, text="No", command=registrar_no)
boton_registrar_no.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")

boton_generar_reporte = tk.Button(ventana, text="Generar Reporte", command=generar_reporte)
boton_generar_reporte.grid(row=2, column=3, padx=10, pady=10, sticky="nsew")


ventana.mainloop()



