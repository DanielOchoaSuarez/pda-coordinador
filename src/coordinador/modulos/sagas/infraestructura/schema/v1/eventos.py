from pulsar.schema import *
from coordinador.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion


####################
# Eventos Catastro #
####################


class EventoPropiedadCreadaPayload(Record):
    id_propiedad = String()
    numero_catastro = String()


class EventoPropiedadCreada(EventoIntegracion):
    data = EventoPropiedadCreadaPayload()


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


#######################
# Eventos Auditoria   #
#######################


class AuditoriaCreadaPayload(Record):
    id_propiedad = String()
    numero_contrato = String()


class EventoAuditoriaCreada(EventoIntegracion):
    data = AuditoriaCreadaPayload()


class CreacionAuditoriaFallidaPayload(Record):
    id_propiedad = String()


class EventoCreacionAuditoriaFallida(EventoIntegracion):
    data = CreacionAuditoriaFallidaPayload()


#################
# Eventos BFF   #
#################


class EventoRegistrarRecibidoPayload(Record):
    id_propiedad = String()


class EventoRegistrarRecibido(EventoIntegracion):
    data = EventoRegistrarRecibidoPayload()


class EventoRegistrarPropiedadTerminadoPayload(Record):
    exitoso = Boolean()


class EventoRegistrarPropiedadTerminado(EventoIntegracion):
    data = EventoRegistrarPropiedadTerminadoPayload()
