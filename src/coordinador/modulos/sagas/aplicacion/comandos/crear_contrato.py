from dataclasses import dataclass
from coordinador.seedwork.aplicacion.comandos import Comando
from coordinador.seedwork.aplicacion.comandos import ejecutar_commando as comando
from .base import CrearComandoBaseHandler
from coordinador.modulos.sagas.aplicacion.dto import *
from coordinador.seedwork.infraestructura import utils
from coordinador.modulos.sagas.infraestructura.despachadores import Despachador


@dataclass
class CrearContrato(Comando):
    id_propiedad: str
    fecha_creacion: str


class CrearContratoHandler(CrearComandoBaseHandler):

    def handle(self, comando: CrearContrato):
        print('Ejecutando comando crear contrato')
        crear_contrato = CrearContratroDTO(id_propiedad=comando.id_propiedad)
        Despachador().publicar_comando(crear_contrato, utils.COMANDO_CREAR_CONTRATO)


@comando.register(CrearContrato)
def ejecutar_comando_crear_contrato(comando: CrearContrato):
    handler = CrearContratoHandler()
    handler.handle(comando)
