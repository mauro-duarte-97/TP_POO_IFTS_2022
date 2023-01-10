class TipoContratacion():
    def __init__(self, tipo_contratacion):
        self.tipo_contratacion = tipo_contratacion
    
    @property
    def tipo_contratacion(self):
        return self.__tipo_contratacion
    
    @tipo_contratacion.setter
    def tipo_contratacion(self, valor):
        self.__tipo_contratacion = valor