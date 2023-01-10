from dao.dao import DAO

#Clase concreta que implementa la interface Data Access Object
class TipoContratacion_DAO(DAO):
    def __init__(self) -> None:
        super().__init__()
        self.nombre_tabla = "tipos_contratacion"
    
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
                "descripcion"	TEXT UNIQUE,
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
            cursor.execute(f'''INSERT INTO {self.nombre_tabla} (descripcion)
                VALUES
                ('{objeto.descripcion}');'''
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
    
    def insertar_varios_registros(self, lista):
        for objeto in lista:
            self.insertar_registro(objeto)

    def importar_registro_csv(self, elementos):
        try:
            db, cursor = self.conectar_bd()
            # Insertar un registro a la tabla
            cursor.execute(f'''INSERT INTO {self.nombre_tabla} (descripcion)
                VALUES
                ('{elementos[0]}');'''
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
            cursor.execute(f"SELECT * FROM {self.nombre_tabla} WHERE descripcion='{objeto.descripcion}'")
            print(cursor.fetchone())
        except Exception as e:
            print(f"Ocurrió un error al seleccionar el registro correspondiente a la descripcion={objeto.descripcion}. {e}")
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
            cursor.execute(f"DELETE FROM {self.nombre_tabla} WHERE descripcion='{objeto.descripcion}'", )
            # Guardar (commit) los cambios
            db.commit()
            print(f"El registro correspondiente a {objeto.descripcion} se ha eliminado correctamente")
        except Exception as e:
            print(f"Ocurrió un error al eliminar el registro correspondiente a {objeto.descripcion}. {e}")
        finally:
            db.close()

    def modificar_registro(self, objeto):
        try:
            db, cursor = self.conectar_bd()
            cursor.execute(f"UPDATE {self.nombre_tabla} SET tipos_contratacion='{objeto.tipos_contratacion}' WHERE nombre='{objeto.nombre}'", )
            # Guardar (commit) los cambios
            db.commit()
            print(f"El tipo de contratacion {objeto.nombre} se ha actualizado correctamente")
        except Exception as e:
            print(f"Ocurrió un error al modificar el tipo de contratacion {objeto.nombre}. {e}")
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
            cursor.execute(f"SELECT * FROM {self.nombre_tabla} WHERE descripcion='{objeto.descripcion}'")
            return cursor.fetchone()
        except Exception as e:
            #print(f"Ocurrió un error al seleccionar el registro correspondiente a la descripcion={objeto.descripcion}. {e}")
            return 0
        finally:
            db.close()
    
    def obtener_registro_desde_csv(self, valor):
        try:
            db, cursor = self.conectar_bd()
            cursor.execute(f"SELECT * FROM {self.nombre_tabla} WHERE descripcion='{valor}'")
            return cursor.fetchone()
        except Exception as e:
            #print(f"Ocurrió un error al seleccionar el registro correspondiente a la descripcion={objeto.descripcion}. {e}")
            return 0
        finally:
            db.close()

