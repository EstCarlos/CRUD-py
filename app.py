import conexion as conn
from Crea_pdf import crear
import json

# Carga el archivo de configuración en un diccionario de Python
with open("config.json", "r") as f:
    config = json.load(f)


db = conn.DB()

def create():
    name = str(input("Ingrese su: " + config["campo"]["nombre"]["label"]))
    apellido = str(input("Ingrese su: " + config["campo"]["apellido"]["label"]))
    edad = int(input("Ingrese su: " + config["campo"]["edad"]["label"]))

    if len(name) > 0 and len(apellido) > 0:
        sql = 'INSERT INTO personas(nombre,apellido,edad) VALUES(?,?,?)'
        parametros = (name,apellido,edad)
        db.ejecutar_consulta(sql,parametros)
        
        nombre_completo = name + apellido
        crear(nombre_completo, f"{name} tiene la edad de {edad}")
        print('Insertados...')

def read():
    print("1 - Para mostrar una lista")
    print("2 - Para buscar por atributo")

    op = int(input("Elige una opcion: "))
    if op == 1:
        result = db.ejecutar_consulta("SELECT * FROM personas")
        for data in result:
            print(f"{data[0]} - {data[1]} - {data[2]} - {data[3]}")
    elif op == 2:
        search()
    
def update():
    id = int(input("Ingrese el ID: "))
    name = str(input("Ingrese el nombre: "))
    apellido = str(input("Ingrese su apellido: "))
    edad = int(input("Ingrese su edad: "))
    if id != 0: 
        sql = 'UPDATE personas SET nombre=?,apellido=?,edad=? WHERE id=?'
        parametros = (name, apellido, edad, id)
        db.ejecutar_consulta(sql, parametros)
        print("Actualizado!")

def delete():
    id = int(input("Ingrese el ID: "))
    if id != 0: 
        sql = 'DELETE FROM personas WHERE id=?'
        parametros = (id,)
        db.ejecutar_consulta(sql,parametros)
        print("Eliminado")

def search():
    print("Por que atributo quiere buscar: 1-Nombre || 2-Apellido || 3-Edad")
    atributo = int(input("Ingrese: "))
    
    if atributo == 1:
        nombreB = str(input("Ingrese el nombre: "))
        if len(nombreB) > 0:
            sql = "SELECT * FROM personas WHERE nombre LIKE ?"
            parametros = ('%{}%'.format(nombreB),)
            result = db.ejecutar_consulta(sql, parametros)
            for data in result:
                print(f"{data[0]} - {data[1]} - {data[2]} - {data[3]}")

    elif atributo == 2:
        apellidoB = str(input("Ingrese el apellido: "))
        if len(apellidoB) > 0:
            sql = "SELECT * FROM personas WHERE apellido LIKE ?"
            parametros = ('%{}%'.format(apellidoB),)
            result = db.ejecutar_consulta(sql, parametros)
            for data in result:
                print(f"{data[0]} - {data[1]} - {data[2]} - {data[3]}")

    elif atributo == 3:
        edadB = int(input("Ingrese el la edad: "))
        if len(edadB) > 0:
            sql = "SELECT * FROM personas WHERE edad LIKE ?"
            parametros = ('%{}%'.format(edadB),)
            result = db.ejecutar_consulta(sql, parametros)
            for data in result:
                print(f"{data[0]} - {data[1]} - {data[2]} - {data[3]}")

while True: 
    print("==================")
    print("\tMENU")
    print("==================")
    print("\t1 - Insertar registro")
    print("\t2 - Listar registro")
    print("\t3 - Actualizar registro")
    print("\t4 - Eliminar registro")
    print("\t5 - Salir")
    print("==================")

    try: 
        option = int(input("Seleccione una opcion: "))
        if option == 1:
            create()
        elif option == 2:
            read()
        elif option == 3: 
            update()    
        elif option == 4: 
            delete()    
        elif option == 5:
            break
    except: 
        print("Error en elegir opciones")


