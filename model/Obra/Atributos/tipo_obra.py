class Tipo_Obra():
    def __init__(self, tipo):
        self.tipo = tipo
    
    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, valor):
        self.__tipo = valor 