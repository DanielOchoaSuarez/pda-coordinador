from dataclasses import dataclass
from coordinador.seedwork.aplicacion.comandos import Comando
from coordinador.seedwork.aplicacion.comandos import ejecutar_commando as comando
from .base import CrearComandoBaseHandler

from coordinador.modulos.sagas.aplicacion.dto import *
from coordinador.seedwork.infraestructura import utils
from coordinador.modulos.sagas.infraestructura.despachadores import Despachador


@dataclass
class CrearPropiedadCompensacion(Comando):
    id_propiedad: str
    fecha_creacion: str


class CrearPropiedadCompensacionHandler(CrearComandoBaseHandler):

    def handle(self, comando: CrearPropiedadCompensacion):
        print('Ejecutando compensacion crear propiedad')
        crear_propiedad_fallida = CrearPropiedadFallidaDTO(
            id_propiedad=comando.id_propiedad)
        Despachador().publicar_comando(crear_propiedad_fallida,
                                       utils.COMANDO_CREAR_PROPIEDAD_FALLIDA)


@comando.register(CrearPropiedadCompensacion)
def ejecutar_comando_crear_propiedad_compensacion(comando: CrearPropiedadCompensacion):
    handler = CrearPropiedadCompensacionHandler()
    handler.handle(comando)
