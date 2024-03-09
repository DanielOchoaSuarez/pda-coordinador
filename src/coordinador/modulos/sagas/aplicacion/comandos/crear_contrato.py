from dataclasses import dataclass
from coordinador.seedwork.aplicacion.comandos import Comando
from coordinador.seedwork.aplicacion.comandos import ejecutar_commando as comando
from .base import CrearComandoBaseHandler


@dataclass
class CrearContrato(Comando):
    id_propiedad: str
    fecha_creacion: str


class CrearContratoHandler(CrearComandoBaseHandler):

    def handle(self, comando: CrearContrato):
        print('Ejecutando comando crear contrato')


@comando.register(CrearContrato)
def ejecutar_comando_crear_contrato(comando: CrearContrato):
    handler = CrearContratoHandler()
    handler.handle(comando)
