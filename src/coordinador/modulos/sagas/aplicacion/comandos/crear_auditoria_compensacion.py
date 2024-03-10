from dataclasses import dataclass
from coordinador.seedwork.aplicacion.comandos import Comando
from coordinador.seedwork.aplicacion.comandos import ejecutar_commando as comando
from .base import CrearComandoBaseHandler

from coordinador.modulos.sagas.aplicacion.dto import *
from coordinador.seedwork.infraestructura import utils
from coordinador.modulos.sagas.infraestructura.despachadores import Despachador


@dataclass
class CrearAuditoriaCompensacion(Comando):
    id_propiedad: str
    fecha_creacion: str


class CrearAuditoriaCompensacionHandler(CrearComandoBaseHandler):

    def handle(self, comando: CrearAuditoriaCompensacion):
        print('Ejecutando compensacion crear auditoria')
        crear_auditoria_fallida = CrearAuditoriaFallidaDTO(
            id_propiedad=comando.id_propiedad)
        Despachador().publicar_comando(crear_auditoria_fallida,
                                       utils.COMANDO_CREAR_AUDITORIA_FALLIDA)


@comando.register(CrearAuditoriaCompensacion)
def ejecutar_comando_crear_auditoria_compensacion(comando: CrearAuditoriaCompensacion):
    handler = CrearAuditoriaCompensacionHandler()
    handler.handle(comando)
