from dataclasses import dataclass
from coordinador.seedwork.aplicacion.comandos import Comando
from coordinador.seedwork.aplicacion.comandos import ejecutar_commando as comando
from .base import CrearComandoBaseHandler


@dataclass
class CrearContratoCompensacion(Comando):
    id_propiedad: str
    fecha_creacion: str


class CrearContratoCompensacionHandler(CrearComandoBaseHandler):

    def handle(self, comando: CrearContratoCompensacion):
        print('Ejecutando compennsacion crear contrato')


@comando.register(CrearContratoCompensacion)
def ejecutar_comando_crear_contrato(comando: CrearContratoCompensacion):
    handler = CrearContratoCompensacionHandler()
    handler.handle(comando)
