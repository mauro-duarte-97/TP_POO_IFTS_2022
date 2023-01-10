class Obra():
    #SV: Sin Valor, no esta seteado.
    def __init__(self, entorno:str, nombre:str, etapa, tipo_obra, area_responsable, descripcion:str,  
        monto_contrato:float, barrio, direccion:str, licitacion_anio:int, beneficiarios:str):
       
        self.entorno = entorno
        self.nombre = nombre
        self.etapa = etapa
        self.tipo_obra = tipo_obra
        self.area_responsable = area_responsable
        self.descripcion = descripcion
        self.monto_contrato = monto_contrato
        self.barrio = barrio
        self.direccion = direccion
        self.fecha_inicio = "SV" 
        self.fecha_fin_inicial = "SV"
        self.plazo_meses = 0
        self.porcentaje_avance = 0
        self.imagenes = []
        self.empresa = "SV"
        self.licitacion_anio = licitacion_anio
        self.tipo_contratacion = "SV"
        self.nro_contratacion = "SV"
        self.beneficiarios = beneficiarios
        self.mano_obra = "SV"
        self.destacada = "SV"
        self.expediente_numero = "SV"
        self.fuente_financiamiento = "SV"
    
    @property
    def entorno(self):
        return self.__entorno
    
    @entorno.setter
    def entorno(self, valor):
        self.__entorno = valor
    
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def etapa(self):
        return self.__etapa
    @etapa.setter
    def etapa(self, valor):
        self.__etapa = valor
    
    @property
    def tipo_obra(self):
        return self.__tipo_obra
    @tipo_obra.setter
    def tipo_obra(self, valor):
        self.__tipo_obra = valor
    
    @property
    def area_responsable(self):
        return self.__area_responsable
    @area_responsable.setter
    def area_responsable(self, valor):
        self.__area_responsable = valor
    
    @property
    def descripcion(self):
        return self.__descripcion
    @descripcion.setter
    def descripcion(self, valor):
        self.__descripcion = valor
    
    @property
    def monto_contrato(self):
        return self.__monto_contrato
    @monto_contrato.setter
    def monto_contrato(self, valor):
        self.__monto_contrato = valor
    
    @property
    def barrio(self):
        return self.__barrio
    @barrio.setter
    def barrio(self, valor):
        self.__barrio = valor
    
    @property
    def direccion(self):
        return self.__direccion
    @direccion.setter
    def direccion(self, valor):
        self.__direccion = valor
    
    @property
    def fecha_inicio(self):
        return self.__fecha_inicio
    @fecha_inicio.setter
    def fecha_inicio(self, valor):
        self.__fecha_inicio = valor
    
    @property
    def fecha_fin_inicial(self):
        return self.__fecha_fin_inicial
    @fecha_fin_inicial.setter
    def fecha_fin_inicial(self, valor):
        self.__fecha_fin_inicial = valor
    
    @property
    def plazo_meses(self):
        return self.__plazo_meses
    @plazo_meses.setter
    def plazo_meses(self, valor):
        self.__plazo_meses = valor
    
    @property
    def porcentaje_avance(self):
        return self.__porcentaje_avance
    @porcentaje_avance.setter
    def porcentaje_avance(self, valor):
        self.__porcentaje_avance = valor
    
    @property
    def imagenes(self):
        return self.__imagenes
    @imagenes.setter
    def imagenes(self,valor):
        self.__imagenes = valor
    
    @property
    def empresa(self):
        return self.__empresa
    @empresa.setter
    def empresa(self, valor):
        self.__empresa = valor
    
    @property
    def licitacion_anio(self):
        return self.__licitacion_anio
    @licitacion_anio.setter
    def licitacion_anio(self, valor):
        self.__licitacion_anio = valor

    @property
    def tipo_contratacion(self):
        return self.__tipo_contratacion
    @tipo_contratacion.setter
    def tipo_contratacion(self, valor):
        self.__tipo_contratacion = valor

    @property
    def nro_contratacion(self):
        return self.__nro_contratacion
    @nro_contratacion.setter
    def nro_contratacion(self, valor):
        self.__nro_contratacion = valor
    
    @property
    def beneficiarios(self):
        return self.__beneficiarios
    @beneficiarios.setter
    def beneficiarios(self, valor):
        self.__beneficiarios = valor
    
    @property
    def mano_obra(self):
        return self.__mano_obra
    @mano_obra.setter
    def mano_obra(self, valor):
        self.__mano_obra = valor
    
    @property
    def destacada(self):
        return self.__destacada
    @destacada.setter
    def destacada(self, valor):
        self.__destacada = valor
    
    @property
    def expediente_numero(self):
        return self.__expediente_numero
    @expediente_numero.setter
    def expediente_numero(self, valor):
        self.__expediente_numero = valor
    
    @property
    def fuente_financiamiento(self):
        return self.__fuente_financiamiento
    @fuente_financiamiento.setter
    def fuente_financiamiento(self, valor):
        self.__fuente_financiamiento = valor

    ###################################     METODOS     ####################################################
    #5
    def iniciar_contratacion(self, tipo_contratacion, nro_contratacion):
        self.tipo_contratacion = tipo_contratacion
        self.nro_contratacion = nro_contratacion
    #6
    def adjudicar_obra(self, empresa, nro_expediente):
        self.empresa = empresa
        self.nro_expediente = nro_expediente

    #7
    def iniciar_obra(self, destacada, fecha_inicio, fecha_fin, financiamiento, mano_obra):
        self.destacada = destacada
        self.fecha_inicio = fecha_inicio
        self.fecha_fin_inicial = fecha_fin
        self.financiamiento = financiamiento
        self.mano_obra = mano_obra

    #8
    def actualizar_porcentaje_avance(self, porc_incremento):
        self.porcentaje_avance = self.porcentaje_avance + porc_incremento

    #9
    def incrementar_plazo(self, meses):
        self.plazo_meses = self.plazo_meses + meses

    #10
    def agregar_imagenes(self, obj):
        self.imagenes.append(obj)

    #11
    def incrementar_mano_obra(self, cantidad):
        self.mano_obra = self.mano_obra + cantidad

    #12
    def finalizar_obra(self):
        self.etapa = "Finalizada"
        self.porcentaje_avance = "100"

    #13 
    def rescindir_obra(self):
        self.etapa = "Rescindida"
    
