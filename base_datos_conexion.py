

import mysql.connector
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'db_asistenciadb'
}


def insertar(nueva_asistencia):
    try:
        conn = mysql.connector.connect(**config)
        if conn.is_connected():
            print('Conexión exitosa a la base de datos')
            cursor = conn.cursor()
            query = "INSERT INTO asistencia_registro (estado, fecha) VALUES (%s, %s)"
            values = (nueva_asistencia.estado, nueva_asistencia.fecha)
            cursor.execute(query, values)
            conn.commit()
            print(f'{cursor.rowcount} registro(s) insertado(s).')
    except mysql.connector.Error as err:
        print(f'Error: {err}')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print('Conexión cerrada')

def insertar_pago(nuevo_pago):
    try:
        conn = mysql.connector.connect(**config)
        if conn.is_connected():
            print('Conexión exitosa a la base de datos')
            cursor = conn.cursor()
            query = "INSERT INTO semanas_pagadas (numero_semana, estado_pago) VALUES (%s, %s)"
            values = (nuevo_pago.numero_semana, nuevo_pago.estado_pago)
            cursor.execute(query, values)
            conn.commit()
            print(f'{cursor.rowcount} registro(s) insertado(s).')
    except mysql.connector.Error as err:
        print(f'Error: {err}')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print('Conexión cerrada')

def obtener_semanas_pagadas(flag_pagado=None):
    try:
        conn = mysql.connector.connect(**config)
        if conn.is_connected():
            print('Conexión exitosa a la base de datos')
            cursor = conn.cursor()
            query = "SELECT * FROM semanas_pagadas"
            if flag_pagado != None:
                if flag_pagado == True:
                    query += " Where estado_pago = 'si_pagado'"
                else:
                    query += " Where estado_pago = 'no_pagado'"
                    
            print(query)
            cursor.execute(query,)
            results = cursor.fetchall()
            return results
            
    except mysql.connector.Error as err:
        print(f'Error: {err}')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print('Conexión cerrada')


def actualizar_estado_pagado(registro_de_pago):
    try:
        conn = mysql.connector.connect(**config)
        if conn.is_connected():
            print('Conexión exitosa a la base de datos')
            cursor = conn.cursor()
            query = "UPDATE semanas_pagadas SET estado_pago = 'si_pagado', fecha_pago = %s where id = %s"
            values = (registro_de_pago.fecha_registro_pago, registro_de_pago.id)
            cursor.execute(query, values)
            conn.commit()
            print(f'{cursor.rowcount} registro(s) actualizado(s).')
    except mysql.connector.Error as err:
        print(f'Error: {err}')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print('Conexión cerrada')

def buscar_asistencia_por_fecha(fecha):
    try:
        conn = mysql.connector.connect(**config)
        if conn.is_connected():
            print('Conexión exitosa a la base de datos')
            cursor = conn.cursor()
            query = "SELECT * FROM asistencia_registro where fecha = %s"
            print(query)
            cursor.execute(query, (fecha,))
            results = cursor.fetchall()
            return results
            
    except mysql.connector.Error as err:
        print(f'Error: {err}')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print('Conexión cerrada')

def obtener_todas_asistencias():
    try:
        conn = mysql.connector.connect(**config)
        if conn.is_connected():
            print('Conexión exitosa a la base de datos')
            cursor = conn.cursor()
            query = "SELECT * FROM asistencia_registro"
            print(query)
            cursor.execute(query)
            results = cursor.fetchall()
            return results
            
    except mysql.connector.Error as err:
        print(f'Error: {err}')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print('Conexión cerrada')

def buscar_estado():
    try:
        conn = mysql.connector.connect(**config)
        if conn.is_connected():
            print('Conexión exitosa a la base de datos')
            cursor = conn.cursor()
            query = "SELECT COUNT(*) AS total_presentes FROM `asistencia_registro` WHERE estado= 'si_trabajo'"
            cursor.execute(query)
            results = cursor.fetchall()
            return results
            
    except mysql.connector.Error as err:
        print(f'Error: {err}')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print('Conexión cerrada')

def buscar_fecha_minima():
    try:
        conn = mysql.connector.connect(**config)
        if conn.is_connected():
            print('Conexión exitosa a la base de datos')
            cursor = conn.cursor()
            query = "SELECT MIN(fecha) AS fecha_minima FROM asistencia_registro"
            cursor.execute(query)
            results = cursor.fetchall()
            return results
            
    except mysql.connector.Error as err:
        print(f'Error: {err}')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print('Conexión cerrada')

def buscar_fecha_maxima():
    try:
        conn = mysql.connector.connect(**config)
        if conn.is_connected():
            print('Conexión exitosa a la base de datos')
            cursor = conn.cursor()
            query = "SELECT MAX(fecha) AS fecha_maxima FROM asistencia_registro"
            cursor.execute(query)
            results = cursor.fetchall()
            return results
            
    except mysql.connector.Error as err:
        print(f'Error: {err}')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print('Conexión cerrada')

