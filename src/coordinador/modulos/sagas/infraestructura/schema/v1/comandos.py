from pulsar.schema import *
from coordinador.seedwork.infraestructura.schema.v1.comandos import (
    ComandoIntegracion)


class ComandoCrearPropiedadPayload(ComandoIntegracion):
    id_propiedad = String()


class ComandoCrearPropiedad(ComandoIntegracion):
    data = ComandoCrearPropiedadPayload()
