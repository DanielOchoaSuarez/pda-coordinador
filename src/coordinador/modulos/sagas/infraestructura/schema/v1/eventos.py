from pulsar.schema import *
from coordinador.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
from coordinador.seedwork.infraestructura.utils import time_millis
import uuid

####################
# Eventos Catastro #
####################


class PropiedadCreadaPayload(Record):
    id_propiedad = String()
    numero_catastro = String()


class EventoPropiedadCreada(EventoIntegracion):
    data = PropiedadCreadaPayload()


class CreacionPropiedadFallidaPayload(Record):
    id_propiedad = String()


class EventoCreacionPropiedadFallida(EventoIntegracion):
    data = CreacionPropiedadFallidaPayload()


#######################
# Eventos Contractual #
#######################


class ContratoCreadoPayload(Record):
    id_propiedad = String()
    numero_contrato = String()


class EventoContratoCreado(EventoIntegracion):
    data = ContratoCreadoPayload()


class CreacionContratoFallidoPayload(Record):
    id_propiedad = String()


class EventoCreacionContratoFallido(EventoIntegracion):
    data = CreacionContratoFallidoPayload()
