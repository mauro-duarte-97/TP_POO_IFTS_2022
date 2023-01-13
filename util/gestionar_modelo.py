from abc import ABC
import sys
sys.path.append("..")

from model.Obra.Atributos.area_responsable import Area_responsable
from model.Obra.Atributos.etapa import Etapa
from model.Obra.Obra import Obra
from model.Obra.Atributos.tipo_obra import Tipo_Obra
from model.Obra.Atributos.barrio import Barrio, Comuna
from model.Obra.Atributos.tipo_contratacion import TipoContratacion
from model.Obra.Atributos.empresa import Empresa
from model.Obra.Atributos.fuente_financiamiento import FuenteFinanciamiento
from dao.etapa_dao import Etapa_DAO
from dao.tipo_obra_dao import TipoObra_DAO
from dao.area_dao import Area_DAO



class GestionarModelo(ABC):
    __listado_etapas = []
    __listado_obras = []
    __listado_tipo_obra = []
    __listado_areas = []
    __listado_comunas =[]
    __listado_barrios =[]
    __listado_tipos_contratacion =[]
    __listado_empresas = []
    __listado_fuentes_financiamiento = []
    
       
    @classmethod
    def nueva_obra(cls, entorno:str, nombre:str, etapa, tipo_obra, area_responsable, descripcion:str, monto_contrato:float, barrio, direccion, licitacion_anio:int, beneficiarios:str) -> Obra:
        obj = Obra(entorno, nombre, etapa, tipo_obra, area_responsable, descripcion, monto_contrato, barrio, direccion, licitacion_anio, beneficiarios)
        return obj
        
    
    @classmethod
    def listado_obra(cls,obj):
        cls.__listado_obras.append(obj)
        
    @classmethod
    def nueva_etapa(cls,nombre) -> Etapa:
        obj = Etapa(nombre)
        cls.__listado_etapas.append(obj)
        return obj

    @classmethod
    def nuevo_tipo_obra(cls,tipo_obra) -> Tipo_Obra:
        obj = Tipo_Obra(tipo_obra)
        return obj

    @classmethod
    def nueva_area(cls,area_responsable):
        obj = Area_responsable(area_responsable)
        cls.__listado_areas.append(area_responsable)
        return obj
    
    @classmethod
    def nueva_comuna(cls,numero) -> Comuna:
        obj = Comuna(numero)
        cls.__listado_comunas.append(obj)
        return obj

    @classmethod
    def nuevo_barrio(cls,nombre, comuna) -> Barrio:
        obj = Barrio(nombre, comuna)
        cls.__listado_tipos_contratacion.append(obj)
        return obj

    @classmethod
    def nuevo_tipo_contratacion(cls,tipo_contratacion) -> TipoContratacion:
        obj = TipoContratacion(tipo_contratacion)
        cls.__listado_barrios.append(obj)
        return obj
    
    @classmethod
    def nueva_empresa(cls,cuit, razon_social) -> Empresa:
        obj = Empresa(cuit, razon_social)
        cls.__listado_empresas.append(obj)
        return obj
    
    @classmethod
    def nueva_fuente_financiamiento(cls,fuente_financiamiento) -> FuenteFinanciamiento:
        obj = FuenteFinanciamiento(fuente_financiamiento)
        cls.__listado_fuentes_financiamiento.append(obj)
        return obj
  
   