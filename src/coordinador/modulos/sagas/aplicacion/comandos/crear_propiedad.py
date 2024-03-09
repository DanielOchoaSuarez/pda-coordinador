from dataclasses import dataclass
from coordinador.seedwork.aplicacion.comandos import Comando
from coordinador.seedwork.aplicacion.comandos import ejecutar_commando as comando
from .base import CrearComandoBaseHandler

from coordinador.modulos.sagas.aplicacion.dto import *
from coordinador.seedwork.infraestructura import utils
from coordinador.modulos.sagas.infraestructura.despachadores import Despachador


@dataclass
class CrearPropiedad(Comando):
    id_propiedad: str
    fecha_creacion: str


class CrearPropiedadHandler(CrearComandoBaseHandler):

    def handle(self, comando: CrearPropiedad):
        print('Ejecutando comando crear propiedad')
        crear_propiedad = CrearPropiedadDTO(id_propiedad=comando.id_propiedad)
        Despachador().publicar_comando(crear_propiedad, utils.COMANDO_CREAR_PROPIEDAD)


@comando.register(CrearPropiedad)
def ejecutar_comando_crear_propiedad(comando: CrearPropiedad):
    handler = CrearPropiedadHandler()
    handler.handle(comando)
