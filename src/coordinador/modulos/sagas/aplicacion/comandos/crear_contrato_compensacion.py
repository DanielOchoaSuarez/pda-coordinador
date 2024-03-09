from dataclasses import dataclass
from coordinador.seedwork.aplicacion.comandos import Comando
from coordinador.seedwork.aplicacion.comandos import ejecutar_commando as comando
from .base import CrearComandoBaseHandler

from coordinador.modulos.sagas.aplicacion.dto import *
from coordinador.seedwork.infraestructura import utils
from coordinador.modulos.sagas.infraestructura.despachadores import Despachador


@dataclass
class CrearContratoCompensacion(Comando):
    id_propiedad: str
    fecha_creacion: str


class CrearContratoCompensacionHandler(CrearComandoBaseHandler):

    def handle(self, comando: CrearContratoCompensacion):
        print('Ejecutando compensacion crear contrato')
        crear_contrato_fallido = CrearContratroFallidoDTO(
            id_propiedad=comando.id_propiedad)
        Despachador().publicar_comando(crear_contrato_fallido,
                                       utils.COMANDO_CREAR_CONTRATO_FALLIDO)


@comando.register(CrearContratoCompensacion)
def ejecutar_comando_crear_contrato(comando: CrearContratoCompensacion):
    handler = CrearContratoCompensacionHandler()
    handler.handle(comando)
