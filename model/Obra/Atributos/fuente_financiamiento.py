class FuenteFinanciamiento():
    def __init__(self, fuente_financiamiento):
        self.fuente_financiamiento = fuente_financiamiento
    
    @property
    def fuente_financiamiento(self):
        return self.__fuente_financiamiento
    
    @fuente_financiamiento.setter
    def fuente_financiamiento(self, valor):
        self.__fuente_financiamiento = valor