class Comuna():
    def __init__(self, numero:int):
        self.numero = numero
    
    @property
    def numero(self):
        return self.__numero
        
    @numero.setter
    def numero(self, valor):
        self.__numero = valor

class Barrio():
    def __init__(self, nombre, comuna) -> None:
        self.nombre = nombre
        self.comuna = comuna

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def comuna(self):
        return self.__comuna
    
    @comuna.setter
    def comuna(self, numero):
        self.__comuna = numero