from abc import ABC, abstractmethod
import sqlite3

#Interfaces y clases Data Access Object

#Interface DAO
class DAO(ABC):
    def __init__(self) -> None:
        self.nombre_bd = "obras_urbanas_caba.db"
    
    @property
    def nombre_bd(self):
        return self.__nombre_bd
    
    @nombre_bd.setter
    def nombre_bd(self, valor):
        self.__nombre_bd = valor

    def conectar_bd(self):
        try:
            db = sqlite3.connect("db/" + self.nombre_bd)
            #print("La conexion a la bd se ha realizado correctamente")
            return db, db.cursor()
        except Exception as e:
            print(f"Ocurrió un error al crear la tabla. {e}")
            return None

    @abstractmethod
    def crear_tabla(self):
        pass

    @abstractmethod
    def insertar_registro(self, objeto):
        pass

    @abstractmethod
    def seleccionar_registro(self, objeto):
        pass

    @abstractmethod
    def seleccionar_todos_registros(self):
        pass

    @abstractmethod
    def eliminar_registro(self, objeto):
        pass

    @abstractmethod
    def modificar_registro(self, objeto):
        pass
    
    @abstractmethod
    def obtener_registro_desde_csv(self, valor):
        pass