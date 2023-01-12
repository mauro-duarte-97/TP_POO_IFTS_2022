from abc import ABC
import numpy as np
import pandas as pd
from dao.dao import *
from dao.etapa_dao import Etapa_DAO
from dao.empresa_dao import Empresa_DAO
from dao.obra_dao import Obra_DAO
from dao.tipo_obra_dao import TipoObra_DAO
from dao.area_dao import Area_DAO
from dao.comuna_dao import Comuna_DAO
from dao.barrio_dao import Barrio_DAO
from dao.tipo_contratacion_dao import TipoContratacion_DAO
from dao.fuente_financiamiento_dao import FuenteFinanciamiento_DAO
from dao.imagen_dao import Imagen_DAO



class GestionarDAO(ABC):

    @classmethod
    def importar_csv(cls, archivo_csv: str):
        df = pd.read_csv(archivo_csv, sep=';', encoding='utf8')
        # print(df.head())
        # print(df.count())
        # print(df.columns)
        """
        for x in df['etapa']:
            print(f"{x}")
        """
        etapa_dao = cls.crear_objeto_dao("Etapa_DAO")
        cls.crear_tabla(etapa_dao)
        empresa_dao = cls.crear_objeto_dao("Empresa_DAO")
        cls.crear_tabla(empresa_dao)
        tipo_obra_dao = cls.crear_objeto_dao("TipoObra_DAO")
        cls.crear_tabla(tipo_obra_dao)
        area_dao = cls.crear_objeto_dao("Area_DAO")
        cls.crear_tabla(area_dao)
        comuna_dao = cls.crear_objeto_dao("Comuna_DAO")
        cls.crear_tabla(comuna_dao)
        barrio_dao = cls.crear_objeto_dao("Barrio_DAO")
        cls.crear_tabla(barrio_dao)
        tipo_contratacion_dao = cls.crear_objeto_dao("TipoContratacion_DAO")
        cls.crear_tabla(tipo_contratacion_dao)
        financiamiento_dao = cls.crear_objeto_dao("FuenteFinanciamiento_DAO")
        cls.crear_tabla(financiamiento_dao)
        imagen_dao = cls.crear_objeto_dao("Imagen_DAO")
        cls.crear_tabla(imagen_dao)
        obra_dao = cls.crear_objeto_dao("Obra_DAO")
        cls.crear_tabla(obra_dao)

        # Eliminar valores NA o NaN (nulos o no disponibles)
        df.dropna(subset=["etapa", "tipo", "area_responsable", "descripcion",
                  "monto_contrato", "comuna", "barrio", "direccion"], axis=0, inplace=True)
        # print(df.count())

        # Obtener los valores únicos (no repetidos) de la tupla
        obras = list(set(zip(df['etapa'], df['tipo'], df['area_responsable'], df['cuit_contratista'], df['licitacion_oferta_empresa'], df['entorno'], df['nombre'], df['descripcion'], df['monto_contrato'], df['comuna'], df['barrio'], df['contratacion_tipo'], df['financiamiento'], df['imagen_1'],
                     df['imagen_2'], df['imagen_3'], df['imagen_4'], df['direccion'], df['fecha_inicio'], df['fecha_fin_inicial'], df['plazo_meses'], df['porcentaje_avance'], df['licitacion_anio'], df['nro_contratacion'], df['beneficiarios'], df['mano_obra'], df['destacada'], df['expediente-numero'])))
        # print(obras)
        print("Importando datos del archivo .csv a una base de datos SQLite")
        cargando = ""
        for elem in obras:
            cargando = cargando + "..."
            print(cargando)

            # Insertar datos en la tabla etapas
            # columna: etapa
            id_etapa = 0
            if elem[0] is not np.nan:
                lista = []
                lista.append(elem[0])
                # print(lista)
                id_etapa = etapa_dao.importar_registro_csv(lista)
                # En caso que el registro ya exista en la bd
                if id_etapa == 0:
                    registro = etapa_dao.obtener_registro_desde_csv(elem[0])
                    if isinstance(registro, tuple):
                        id_etapa = registro[0]

            # Insertar datos en la tabla empresas
            # columnas: cuit_contratista y licitacion_oferta_empresa
            id_empresa = 0
            if elem[3] is not np.nan and elem[4] is not np.nan:
                lista = (elem[3], elem[4])
                # print(lista)
                id_empresa = empresa_dao.importar_registro_csv(lista)
                # En caso que el registro ya exista en la bd
                if id_empresa == 0:
                    registro = empresa_dao.obtener_registro_desde_csv(elem[3])
                    # print(registro)
                    if isinstance(registro, tuple):
                        id_empresa = registro[0]

            # Insertar datos en la tabla tipos_obras
            # columna: tipo
            id_tipo_obra = 0
            if elem[1] is not np.nan:
                lista = []
                lista.append(elem[1])
                # print(lista)
                id_tipo_obra = tipo_obra_dao.importar_registro_csv(lista)
                # En caso que el registro ya exista en la bd
                if id_tipo_obra == 0:
                    registro = tipo_obra_dao.obtener_registro_desde_csv(
                        elem[1])
                    if isinstance(registro, tuple):
                        id_tipo_obra = registro[0]

            # Insertar datos en la tabla areas
            # columna: area_responsable
            id_area = 0
            if elem[2] is not np.nan:
                lista = []
                lista.append(elem[2])
                # print(lista)
                id_area = area_dao.importar_registro_csv(lista)
                # En caso que el registro ya exista en la bd
                if id_area == 0:
                    registro = area_dao.obtener_registro_desde_csv(elem[2])
                    if isinstance(registro, tuple):
                        id_area = registro[0]

            # Insertar datos en la tabla comunas
            # columna: comuna
            if elem[2] is not np.nan:
                lista = []
                lista.append(elem[9])
                # print(lista)
                comuna_dao.importar_registro_csv(lista)

            # Insertar datos en la tabla barrios
            # columnas: comuna y barrio
            id_barrio = 0
            if elem[9] is not np.nan and elem[10] is not np.nan:
                lista = (elem[10], elem[9])
                # print(lista)
                id_barrio = barrio_dao.importar_registro_csv(lista)
                # En caso que el registro ya exista en la bd
                if id_barrio == 0:
                    registro = barrio_dao.obtener_registro_desde_csv(elem[10])
                    # print(registro)
                    if isinstance(registro, tuple):
                        id_barrio = registro[0]

            # Insertar datos en la tabla tipos_contratacion
            # columna: contratacion_tipo
            id_tipo_contratacion = 0
            if elem[11] is not np.nan:
                lista = []
                lista.append(elem[11])
                # print(lista)
                id_tipo_contratacion = tipo_contratacion_dao.importar_registro_csv(
                    lista)
                # En caso que el registro ya exista en la bd
                if id_tipo_contratacion == 0:
                    registro = tipo_contratacion_dao.obtener_registro_desde_csv(
                        elem[11])
                    if isinstance(registro, tuple):
                        id_tipo_contratacion = registro[0]

            # Insertar datos en la tabla fuentes_financiamiento
            # columna: financiamiento
            id_financiamiento = 0
            if elem[12] is not np.nan:
                lista = []
                lista.append(elem[12])
                # print(lista)
                id_financiamiento = financiamiento_dao.importar_registro_csv(
                    lista)
                # En caso que el registro ya exista en la bd
                if id_financiamiento == 0:
                    registro = financiamiento_dao.obtener_registro_desde_csv(
                        elem[12])
                    if isinstance(registro, tuple):
                        id_financiamiento = registro[0]

            # Insertar datos en la tabla Obras
            """columnas: entorno,nombre,descripcion,monto_contrato,direccion,fecha_inicio
                        ,fecha_fin_inicial,plazo_meses,porcentaje_avance,licitacion_anio
                        ,nro_contratacion,beneficiarios,mano_obra,destacada,expediente-numero
                        ,id_etapa,id_empresa,id_tipo_obra,id_area,id_barrio,id_tipo_contratacion,id_financiamiento"""
            id_obra = 0
            lista_id = [id_etapa, id_empresa, id_tipo_obra, id_area,
                        id_barrio, id_tipo_contratacion, id_financiamiento]
            # descripcion
            if elem[7] is not np.nan:
                lista = [elem[5], elem[6], elem[7]]
                # monto_contrato
                if elem[8] is not np.nan:
                    valor = elem[8]
                else:
                    valor = ""
                lista.append(valor)
                # direccion
                if elem[17] is not np.nan:
                    valor = elem[17]
                else:
                    valor = ""
                lista.append(valor)
                # fecha_inicio
                if elem[18] is not np.nan:
                    valor = elem[18]
                else:
                    valor = ""
                lista.append(valor)
                # fecha_fin_inicial
                if elem[19] is not np.nan:
                    valor = elem[19]
                else:
                    valor = ""
                lista.append(valor)
                # plazo_meses
                if elem[20] is not np.nan:
                    valor = elem[20]
                else:
                    valor = ""
                lista.append(valor)
                # porcentaje_avance
                if elem[21] is not np.nan:
                    valor = elem[21]
                else:
                    valor = ""
                lista.append(valor)
                # licitacion_anio
                if elem[22] is not np.nan:
                    valor = elem[22]
                else:
                    valor = ""
                lista.append(valor)
                # nro_contratacion
                if elem[23] is not np.nan:
                    valor = elem[23]
                else:
                    valor = ""
                lista.append(valor)
                # beneficiarios
                if elem[24] is not np.nan:
                    valor = elem[24]
                else:
                    valor = ""
                lista.append(valor)
                # mano_obra
                if elem[25] is not np.nan:
                    valor = elem[25]
                else:
                    valor = ""
                lista.append(valor)
                # destacada
                if elem[26] is not np.nan:
                    valor = elem[26]
                else:
                    valor = ""
                lista.append(valor)
                # expediente_numero
                if elem[27] is not np.nan:
                    valor = elem[27]
                else:
                    valor = ""
                lista.append(valor)
                # print(lista)
                id_obra = obra_dao.importar_registro_csv(lista, lista_id)

            # Insertar datos en la tabla imagenes
            # columna: imagen_1
            if elem[13] is not np.nan and id_obra > 0:
                lista = []
                lista.append(elem[13])
                # print(lista)
                id_imagen = imagen_dao.importar_registro_csv(lista, id_obra)
            # columna: imagen_2
            if elem[14] is not np.nan and id_obra > 0:
                lista = []
                lista.append(elem[14])
                # print(lista)
                id_imagen = imagen_dao.importar_registro_csv(lista, id_obra)
            # columna: imagen_3
            if elem[15] is not np.nan and id_obra > 0:
                lista = []
                lista.append(elem[15])
                # print(lista)
                id_imagen = imagen_dao.importar_registro_csv(lista, id_obra)
            # columna: imagen_4
            if elem[16] is not np.nan and id_obra > 0:
                lista = []
                lista.append(elem[16])
                # print(lista)
                id_imagen = imagen_dao.importar_registro_csv(lista, id_obra)
        print("Los datos se han importado correctamente")

    @classmethod
    def crear_objeto_dao(cls, tipo_dao: str) -> DAO:
        if tipo_dao == "Etapa_DAO":
            return Etapa_DAO()
        if tipo_dao == "Empresa_DAO":
            return Empresa_DAO()
        if tipo_dao == "TipoObra_DAO":
            return TipoObra_DAO()
        if tipo_dao == "Area_DAO":
            return Area_DAO()
        if tipo_dao == "Comuna_DAO":
            return Comuna_DAO()
        if tipo_dao == "Barrio_DAO":
            return Barrio_DAO()
        if tipo_dao == "TipoContratacion_DAO":
            return TipoContratacion_DAO()
        if tipo_dao == "FuenteFinanciamiento_DAO":
            return FuenteFinanciamiento_DAO()
        if tipo_dao == "Imagen_DAO":
            return Imagen_DAO()
        if tipo_dao == "Obra_DAO":
            return Obra_DAO()

    @classmethod
    def crear_tabla(cls, objeto: DAO):
        objeto.crear_tabla()

    @classmethod
    def insertar_registro(cls, objeto: DAO, objeto_modelo):
        objeto.insertar_registro(objeto_modelo)

    @classmethod
    def insertar_varios_registros(cls, objeto: DAO, listado):
        pass

    @classmethod
    def seleccionar_registro(cls, objeto: DAO, objeto_modelo):
        pass

    @classmethod
    def seleccionar_todos_registros(cls, objeto: DAO):
        pass

    @classmethod
    def eliminar_registro(cls, objeto: DAO, objeto_modelo):
        pass

    @classmethod
    def modificar_registro(cls, objeto: DAO, objeto_modelo):
        pass

    @classmethod
    def obtener_registros(cls, objeto: DAO, objeto_modelo) -> list:
        pass
