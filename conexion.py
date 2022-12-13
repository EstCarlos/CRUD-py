import sqlite3	

database = 'database.db'

class DB:
    def ejecutar_consulta(self, consulta, parametros = ()):
        with sqlite3.connect(database) as conn:
            self.cursor = conn.cursor()
            result = self.cursor.execute(consulta, parametros)
            conn.commit()
            return result

db = DB()
result = db.ejecutar_consulta("SELECT * FROM personas")
print(result.fetchall())
