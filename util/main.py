from abc import ABC
from util.gestionar_dao import *
from .gestionar_modelo import *
from model.Obra.Atributos.imagenes import Imagen
from model.Obra.Obra import Obra
from dao.etapa_dao import Etapa_DAO
from datetime import *

id_financiamiento = 0

class Main(ABC):
    
    @classmethod
    def main(cls):
        #importar dataset .csv a la base de datos
        archivo_csv = "observatorio-de-obras-urbanas.csv"
        #archivo_csv = "https://cdn.buenosaires.gob.ar/datosabiertos/datasets/secretaria-general-y-relaciones-internacionales/ba-obras/observatorio-de-obras-urbanas.csv"
        GestionarDAO.importar_csv(archivo_csv)
#2 y 4
        obj_1_etapa_dao = Etapa_DAO()
        desc_etapa = "Proyecto"#input("Ingrese la etapa de la obra: ")
        id_etapa = 0
        for row in obj_1_etapa_dao.obtener_registros():
            if (row[1] == desc_etapa):
                id_etapa = int(row[0])
                obj_1_etapa_model = GestionarModelo.nueva_etapa(row[1])
                break
        if id_etapa == 0:
            obj_1_etapa_model = GestionarModelo.nueva_etapa("Proyecto")
            id_etapa = GestionarDAO.insertar_registro(obj_1_etapa_dao,obj_1_etapa_model)
#4b
        while True:
            obj_tipo_obra_model = TipoObra_DAO()
            desc_tipo_obra = "Arquitectura" #input("Ingrese el tipo de obra: ")
            id_tipo_obra = 0
            for tipo in obj_tipo_obra_model.obtener_registros():
                if (tipo[1] == desc_tipo_obra):
                    id_tipo_obra = int(tipo[0])
                    break

            if id_tipo_obra > 0:
                obj_tipo_obra_model = GestionarModelo.nuevo_tipo_obra(desc_tipo_obra)
                break
            else:
                print("El tipo de obra ingresado no existe en la BD")
  
        while True:
            obj_area_model = Area_DAO()
            desc_area_responsable = "Secretarí­a de Transporte y Obras Públicas" #input("Ingrese el area: ")
            id_area = 0
            for tipo in obj_area_model.obtener_registros():
                if (tipo[1] == desc_area_responsable):
                    id_area = int(tipo[0])
                    break
            if id_area > 0:
                obj_area_model = GestionarModelo.nueva_area(desc_area_responsable)
                break
            else:
                print("El area ingresada no existe en la BD")
            
        while True:
            obj_barrio_model = Barrio_DAO()
            desc_barrio = "La Boca" #input("Ingrese el barrio: ")
            comuna = 1 #input("Ingrese el numero de comuna: ")
            id_barrio = 0
            for tipo in obj_barrio_model.obtener_registros():
                if (tipo[1] == desc_barrio):
                    id_barrio = int(tipo[0])
                    break
            if id_barrio > 0:
                obj_barrio_model = GestionarModelo.nuevo_barrio(desc_barrio,comuna)
                break
            else:
                print("El barrio ingresado no existe en la BD")
#3 Ingreso de obras         
        seguir_ingresando_obras= "S"       
        while seguir_ingresando_obras == "S" or seguir_ingresando_obras == "s":
            obj_obra_dao = Obra_DAO()
            obj_obra_model = GestionarModelo.nueva_obra(
            "Buenos Aires Playa 2019",#input("Ingrese un entorno: "),
            "Buenos Aires Playa 2019: Parque Indoamericano- Mantenimiento",#input("Ingrese nombre: "),
            obj_1_etapa_model, obj_tipo_obra_model, obj_area_model,
            "1ra Etapa: La Obra De Seguridad Consiste En Trabajos Varios Como Puerta De Seguridad En Terraza, Cierre Sector Próximo A Hemodinamia, Casilla De Gas, Sector De Centro Médico Clí­nico, Rejas En Laboratorio E Iluminación.",#str(input("Ingrese una descripcion: ")),
            100,#int(input("Ingrese el monto del contrato: ")),
            obj_barrio_model,
            "MIRAVE Y LUNA", #str(input("Ingrese una direccion: ")), 
            2016, #int(input("Ingrese una licitacion de año: ")),
            "usuarios") #str(input("Ingrese los beneficiarios: ")))

            seguir_ingresando_obras = input("Desea seguir ingresando obras? si o no S/N: ")
            GestionarModelo.listado_obra(obj_obra_model)

#5
        
        while True:     
            obj_tipo_contratacion_dao = TipoContratacion_DAO()
            desc_tipo_contratacion = "Contratación Directa"#str(input("Ingrese un tipo de contratacion: "))
            nro_contratacion = "62-CBAS-2018"#str(input("Ingrese un nro de contratacion: "))
            id_tipo_contratacion = 0
            for tipo in obj_tipo_contratacion_dao.obtener_registros():
                if (tipo[1] == desc_tipo_contratacion):
                    id_tipo_contratacion = int(tipo[0])
                    break
            if id_tipo_contratacion > 0:
                obj_tipo_contratacion_model = GestionarModelo.nuevo_tipo_contratacion(desc_tipo_contratacion)
                break
            else:
                print("El tipo de contratacion seleccionada no existe en la BD: ")
        obj_obra_model.iniciar_contratacion(obj_tipo_contratacion_model,nro_contratacion)
        
#6  
        while True:
            obj_empresa_dao = Empresa_DAO()
            cuit = "20-18272109-4"#str(input("Ingrese cuit: "))
            razon_social = "Ecosan S.A"#str(input("Ingrese razon social: "))
            nro_expediente = "2018-604-MDUYTGC"#str(input("Ingrese un nro de expediente: "))
            id_empresa = 0
            empresa = GestionarModelo.nueva_empresa(cuit, razon_social)
            obj_empresa_dao.obtener_registro(cuit)
            if (obj_empresa_dao.obtener_registro(cuit) == 0):
                id_empresa = int(tipo[0])
                obj_empresa_dao.insertar_registro(empresa)
            if id_empresa > 0:
                obj_obra_model.adjudicar_obra(empresa, nro_expediente)
                break
            else:
                print("La empresa seleccionada no existe en la BD, si es una nueva porfavor ingresela de nuevo")
#7       
        obj_fuente_financiamiento_dao = FuenteFinanciamiento_DAO()
        destacada = bool(input("¿la obra es destacada Si/No (S/N): "))
        if destacada == "S" or destacada == "s":
            destacada = True
            print(destacada)
        elif destacada == "N" or destacada == "n":
            destacada = False
            print(destacada)
        fecha_inicio = str(input("ingrese fecha de inicio d/m/Y H:M: "))
        fecha_inicio = datetime.strptime(fecha_inicio, "%d/%m/%Y %H:%M")
        fecha_fin = str(input("ingrese fecha de fin d/m/Y H:M: "))
        fecha_fin = datetime.strptime(fecha_fin, "%d/%m/%Y %H:%M")
        mano_obra = int(input("Ingrese la cantidad de mano de obra: "))
        financiamiento = "Nación"#str(input("Ingrese fuente financiamiento: "))        
        while True:
        
            for tipo in obj_fuente_financiamiento_dao.obtener_registros():
                if (tipo[1] == financiamiento):
                    id_fuente_financiamiento = int(tipo[0])
                    break
            if id_fuente_financiamiento > 0:
                obj_fuente_financiamiento_model = FuenteFinanciamiento(financiamiento)
                break
            else:
                print("La fuente financiamiento seleccionada no existe en la BD")
        obj_obra_model.iniciar_obra(destacada, fecha_inicio, fecha_fin, obj_fuente_financiamiento_model, mano_obra)

#8              
        inc_porc_avanze = str(input("Desea incrementar el porcentaje de avanze de la obra? S/N (Si o No): "))
        if inc_porc_avanze == "S" or inc_porc_avanze  =="s":
            porc_incremento = int(input("Ingrese el porcentaje de avance: "))
            obj_obra_model.actualizar_porcentaje_avance(porc_incremento)
        print(obj_obra_model.porcentaje_avance)

#9
        inc_plazo_obra = str(input("Desea incrementar el plazo de la obra? S/N (Si o No): "))
        if inc_plazo_obra == "S" or inc_plazo_obra =="s":
            meses= int(input("Ingrese la cantidad de meses a agregar al plazo: "))
            obj_obra_model.incrementar_plazo(meses)
        print(obj_obra_model.plazo_meses)

#10
        agregar_imagenes = "S"
        while agregar_imagenes == "S" or agregar_imagenes == "s":
            agregar_imagenes = str(input("Desea agregar imagenes? S/N (Si o No): "))
            if agregar_imagenes == "S" or agregar_imagenes == "s":
                link_imagen = str(input("Ingrese el link de la imagen: "))
                img = Imagen(link_imagen)
                obj_obra_model.agregar_imagenes(img)
        for item in obj_obra_model.imagenes:
            print(item.link_imagen)

#11     
        extra_empleados = input("Desea ingresar nuevos empleados? S/N (Si o No): ")
        if extra_empleados == "S" or extra_empleados == "s": 
            cantidad = int(input("Ingrese la cantidad de nuevos empleados: "))
            obj_obra_model.incrementar_mano_obra(cantidad)
        print(obj_obra_model.mano_obra)
#12 y #13  
        etapa = str(input("Desea finalizar la obra o rescindirla? F = finalizar; R = rescindir: "))
        if etapa == "F" or etapa == "f":
            obj_obra_model.finalizar_obra()
            print("La obra se finalizo")
            print(obj_obra_model.etapa)
        elif etapa == "R" or etapa == "r":
            obj_obra_model.rescindir_obra()
            print("La obra se rescindio")
            print(obj_obra_model.etapa)

#14
        lista_id = (id_etapa,id_empresa,id_tipo_obra,id_area,id_barrio,id_tipo_contratacion,id_fuente_financiamiento)
        insertar_ok = obj_obra_dao.insertar_registro(obj_obra_model, lista_id)
        print(lista_id)
        if (insertar_ok == 0):
            print("Ocurrió un error al insertar la nueva obra en la BD")
        else:
            print(f"La nueva obra se ha insertado correctamente en la BD")
        #for obra in GestionarModelo.__listado_obras():
        #    print("Obra: ", obra.descripcion)
