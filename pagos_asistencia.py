
#### PAGOS DE CONSTRUCCION ####
from base_datos_conexion import *
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from openpyxl import Workbook
from typing import List

class Asistencia():
    def __init__(self,estado,fecha):
        self.estado = estado
        self.fecha = fecha

    def imprimir(self):
        print("los datos de la asistencia son: ")
        print(self.fecha)
        print(self.estado)

class ResultadoExcel():
    def __init__(self,num_semana,lista_dias,total):
        self.num_semana = num_semana
        self.lista_dias: List[Asistencia] = lista_dias
        self.total = total

    def obtener_lista_numero_semana(self):
        lista_dias_ = []

        for dia in self.lista_dias:
            dia_semana_num = dia.fecha.weekday()
            if dia.estado == 'si_trabajo':
                lista_dias_.append(dia_semana_num)

        return lista_dias_

class DiaNumeroSemana():
    def __init__(self, num_semana, fecha, estado):
        self.num_semana = num_semana
        self.fecha = fecha
        self.estado = estado

def registrar_si():
    fecha_actual = datetime.now().date()
    print("22222222222")
    print(fecha_actual)
    
    dia_semana = fecha_actual.weekday()

    if dia_semana == 5 or dia_semana == 6:
        print("No se puede registrar asistencia")
        return

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
    lista_resultado_excel = []
    lista_asistencias = []
    datos = obtener_todas_asistencias()


    for dato in datos:
        lista_asistencias.append(Asistencia(dato[2], dato[1]))

    for registro in lista_asistencias:
        fecha_registro = registro.fecha
        estado_ = registro.estado
        num_semana = obtener_numero_semana(fecha_registro)
        lista_tmp.append(DiaNumeroSemana(num_semana, fecha_registro,estado_))

    for num_sem in range(1,36):
        dias_semana = []
        dias_trabajados = 0

        for registro in lista_tmp:
            if registro.num_semana == num_sem:
                if registro.estado == 'si_trabajo':
                    dias_trabajados += 1
                dias_semana.append(Asistencia(registro.estado, registro.fecha))

        if len(dias_semana) > 0:
            suma_semana = dias_trabajados * 80
            lista_resultado_excel.append(ResultadoExcel(num_sem,dias_semana,suma_semana))
        
    exportar_excel(lista_resultado_excel)
    print("0000000000000000000")
    print(lista_resultado_excel)
    print("0000000000000000000")

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
        ws[f'A{cont}'] = registro.num_semana
        
        lista_dias_ = registro.obtener_lista_numero_semana()

        for i in range(0,6): # 0 es lunes, 1 es martes ...
            letra = chr(ord('A')+i+1)
            if i in lista_dias_:
                ws[f'{letra}{cont}'] = 'SI'
            else:
                ws[f'{letra}{cont}'] = 'NO'
        ws[f'G{cont}'] = registro.total

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



