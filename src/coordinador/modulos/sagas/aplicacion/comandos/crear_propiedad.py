from dataclasses import dataclass
from coordinador.seedwork.aplicacion.comandos import Comando
from coordinador.seedwork.aplicacion.comandos import ejecutar_commando as comando
from .base import CrearComandoBaseHandler


@dataclass
class CrearPropiedad(Comando):
    id_propiedad: str
    fecha_creacion: str


class CrearPropiedadHandler(CrearComandoBaseHandler):

    def handle(self, comando: CrearPropiedad):
        print('Ejecutando comando crear propiedad')


@comando.register(CrearPropiedad)
def ejecutar_comando_crear_propiedad(comando: CrearPropiedad):
    handler = CrearPropiedadHandler()
    handler.handle(comando)
