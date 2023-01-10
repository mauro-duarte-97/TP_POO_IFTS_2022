from dao.dao import DAO

#Clase concreta que implementa la interface Data Access Object
class Barrio_DAO(DAO):
    def __init__(self) -> None:
        super().__init__()
        self.nombre_tabla = "barrios"
    
    @property
    def nombre_tabla(self):
        return self.__nombre_tabla
    
    @nombre_tabla.setter
    def nombre_tabla(self, valor):
        self.__nombre_tabla = valor
    
    def crear_tabla(self):
        try:
            db, cursor = self.conectar_bd()
            # Crear una tabla
            cursor.execute(f'''CREATE TABLE IF NOT EXISTS {self.nombre_tabla} (
                "id"	INTEGER,
                "nombre"	TEXT UNIQUE,
                "nro_comuna"	INTEGER,
                PRIMARY KEY("id" AUTOINCREMENT)
            );''')
        except Exception as e:
            print(f"Ocurrió un error al crear la tabla. {e}")
        finally:
            db.close()
    
    def insertar_registro(self, objeto):
        try:
            db, cursor = self.conectar_bd()
            # Insertar un registro a la tabla
            cursor.execute(f'''INSERT INTO {self.nombre_tabla} (nombre,nro_comuna)
                VALUES
                ('{objeto.nombre}','{objeto.comuna.numero}');'''
            )
            # Guardar (commit) los cambios
            db.commit()
            #print("El registro se ha insertado correctamente")
            return cursor.lastrowid
        except Exception as e:
            print(f"Ocurrió un error al insertar un registro. {e}")
        finally:
            db.close()
    
    def insertar_varios_registros(self, lista):
        for objeto in lista:
            self.insertar_registro(objeto)

    def importar_registro_csv(self, elementos):
        try:
            db, cursor = self.conectar_bd()
            # Insertar un registro a la tabla
            cursor.execute(f'''INSERT INTO {self.nombre_tabla} (nombre,nro_comuna)
                VALUES
                ('{elementos[0]}','{elementos[1]}');'''
            )
            # Guardar (commit) los cambios
            db.commit()
            #print("El registro se ha insertado correctamente")
            return cursor.lastrowid
        except Exception as e:
            #print(f"Ocurrió un error al insertar un registro. {e}")
            return 0
        finally:
            db.close()
    
    def seleccionar_registro(self, objeto):
        try:
            db, cursor = self.conectar_bd()
            cursor.execute(f"SELECT * FROM {self.nombre_tabla} WHERE nombre='{objeto.nombre}'")
            print(cursor.fetchone())
        except Exception as e:
            print(f"Ocurrió un error al seleccionar el registro correspondiente al barrio={objeto.nombre}. {e}")
        finally:
            db.close()
    
    def seleccionar_todos_registros(self):
        try:
            db, cursor = self.conectar_bd()
            cursor.execute(f"SELECT * FROM {self.nombre_tabla}")
            print(cursor.fetchall())
        except Exception as e:
            print(f"Ocurrió un error al seleccionar todos los registros. {e}")
        finally:
            db.close()
    
    def eliminar_registro(self, objeto):
        try:
            db, cursor = self.conectar_bd()
            cursor.execute(f"DELETE FROM {self.nombre_tabla} WHERE nombre='{objeto.nombre}'", )
            # Guardar (commit) los cambios
            db.commit()
            print(f"El registro correspondiente al barrio {objeto.nombre} se ha eliminado correctamente")
        except Exception as e:
            print(f"Ocurrió un error al eliminar el registro correspondiente al barrio {objeto.nombre}. {e}")
        finally:
            db.close()

    def modificar_registro(self, objeto):
        try:
            db, cursor = self.conectar_bd()
            cursor.execute(f"UPDATE {self.nombre_tabla} SET nro_comuna='{objeto.nro_comuna}' WHERE nombre='{objeto.nombre}'", )
            # Guardar (commit) los cambios
            db.commit()
            print(f"El barrio {objeto.nombre} se ha actualizado correctamente")
        except Exception as e:
            print(f"Ocurrió un error al modificar el barrio {objeto.nombre}. {e}")
        finally:
            db.close()
    
    def obtener_registros(self):
        try:
            db, cursor = self.conectar_bd()
            cursor.execute(f"SELECT * FROM {self.nombre_tabla}")
            return cursor.fetchall()
        except Exception:
            return None
        finally:
            db.close()
    
    def obtener_registro(self, objeto):
        try:
            db, cursor = self.conectar_bd()
            cursor.execute(f"SELECT * FROM {self.nombre_tabla} WHERE nombre='{objeto.nombre}'")
            return cursor.fetchone()
        except Exception as e:
            #print(f"Ocurrió un error al seleccionar el barrio={objeto.nombre}. {e}")
            return 0
        finally:
            db.close()
    
    def obtener_registro_desde_csv(self, valor):
        try:
            db, cursor = self.conectar_bd()
            cursor.execute(f"SELECT * FROM {self.nombre_tabla} WHERE nombre='{valor}'")
            return cursor.fetchone()
        except Exception as e:
            #print(f"Ocurrió un error al seleccionar el barrio={valor}. {e}")
            return 0
        finally:
            db.close()

