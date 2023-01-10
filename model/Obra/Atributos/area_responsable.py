class Area_responsable():
    def __init__(self, area_responsable) -> None:
        self.area_responsable = area_responsable
    
    @property
    def area_responsable(self):
        return self.__area_responsable
    
    @area_responsable.setter
    def area_responsable(self, valor):
        self.__area_responsable = valor