from dataclasses import dataclass
from coordinador.seedwork.aplicacion.comandos import Comando
from coordinador.seedwork.aplicacion.comandos import ejecutar_commando as comando
from .base import CrearComandoBaseHandler


@dataclass
class CrearPropiedadCompensacion(Comando):
    id_propiedad: str
    fecha_creacion: str


class CrearPropiedadCompensacionHandler(CrearComandoBaseHandler):

    def handle(self, comando: CrearPropiedadCompensacion):
        print('Ejecutando compensacion crear propiedad')


@comando.register(CrearPropiedadCompensacion)
def ejecutar_comando_crear_propiedad_compensacion(comando: CrearPropiedadCompensacion):
    handler = CrearPropiedadCompensacionHandler()
    handler.handle(comando)
