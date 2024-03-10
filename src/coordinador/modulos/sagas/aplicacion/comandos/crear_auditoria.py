from dataclasses import dataclass
from coordinador.seedwork.aplicacion.comandos import Comando
from coordinador.seedwork.aplicacion.comandos import ejecutar_commando as comando
from .base import CrearComandoBaseHandler

from coordinador.modulos.sagas.aplicacion.dto import *
from coordinador.seedwork.infraestructura import utils
from coordinador.modulos.sagas.infraestructura.despachadores import Despachador


@dataclass
class CrearAuditoria(Comando):
    id_propiedad: str
    fecha_creacion: str


class CrearAuditoriaHandler(CrearComandoBaseHandler):

    def handle(self, comando: CrearAuditoria):
        print('Ejecutando comando crear auditoria')
        crear_auditoria = CrearAuditoriaDTO(id_propiedad=comando.id_propiedad)
        Despachador().publicar_comando(crear_auditoria, utils.COMANDO_CREAR_AUDITORIA)


@comando.register(CrearAuditoria)
def ejecutar_comando_crear_auditoria(comando: CrearAuditoria):
    handler = CrearAuditoriaHandler()
    handler.handle(comando)
