

import mysql.connector
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'asistenciadb'
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
