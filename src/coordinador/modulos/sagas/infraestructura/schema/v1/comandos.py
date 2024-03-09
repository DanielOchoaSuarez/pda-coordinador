from pulsar.schema import *
from coordinador.seedwork.infraestructura.schema.v1.comandos import (
    ComandoIntegracion)


#####################
# Comandos Catastro #
#####################

class ComandoCrearPropiedadPayload(ComandoIntegracion):
    id_propiedad = String()


class ComandoCrearPropiedad(ComandoIntegracion):
    data = ComandoCrearPropiedadPayload()


class ComandoCrearPropiedadFallidoPayload(ComandoIntegracion):
    id_propiedad = String()


class ComandoCrearPropiedadFallido(ComandoIntegracion):
    data = ComandoCrearPropiedadFallidoPayload()


########################
# Comandos Contractual #
########################

class ComandoCrearContratoPayload(ComandoIntegracion):
    id_propiedad = String()


class ComandoCrearContrato(ComandoIntegracion):
    data = ComandoCrearContratoPayload()


class ComandoCrearContratoFallidoPayload(ComandoIntegracion):
    id_propiedad = String()


class ComandoCrearContratoFallido(ComandoIntegracion):
    data = ComandoCrearContratoFallidoPayload()
