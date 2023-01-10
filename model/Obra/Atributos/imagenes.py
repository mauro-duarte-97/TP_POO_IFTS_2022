class Imagen():
    def __init__(self, link_imagen:str):
        self.link_imagen = link_imagen

    @property
    def nombre(self):
        return self.__link_imagen

    @nombre.setter
    def imagen(self, valor):
        self.__link_imagen = valor