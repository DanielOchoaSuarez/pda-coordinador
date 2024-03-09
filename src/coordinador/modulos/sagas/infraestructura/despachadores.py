import pulsar

from pulsar.schema import *
from coordinador.seedwork.infraestructura import utils

from coordinador.modulos.sagas.aplicacion.dto import *
from coordinador.modulos.sagas.infraestructura.schema.v1.eventos import EventoPropiedadCreada, EventoPropiedadCreadaPayload, EventoCreacionPropiedadFallida, CreacionPropiedadFallidaPayload
from coordinador.modulos.sagas.infraestructura.schema.v1.eventos import EventoContratoCreado, ContratoCreadoPayload, EventoCreacionContratoFallido, CreacionContratoFallidoPayload
from coordinador.modulos.sagas.infraestructura.schema.v1.comandos import ComandoCrearPropiedad, ComandoCrearPropiedadPayload, ComandoCrearPropiedadFallido, ComandoCrearPropiedadFallidoPayload
from coordinador.modulos.sagas.infraestructura.schema.v1.comandos import ComandoCrearContrato, ComandoCrearContratoPayload, ComandoCrearContratoFallido, ComandoCrearContratoFallidoPayload
# from aeroalpes.modulos.vuelos.infraestructura.mapeadores import MapadeadorEventosReserva


class Despachador:
    def __init__(self):
        print('Creando despachador')
        # self.mapper = MapadeadorEventosReserva()

    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=schema)
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, dto, topico):

        payload = None
        evento_integracion = None

        if isinstance(dto, PropiedadCreadaDTO):
            print('Creando EventoPropiedadCreadaPayload')
            payload = EventoPropiedadCreadaPayload(
                id_propiedad=str(dto.id_propiedad),
                numero_catastro=str(dto.numero_catastro)
            )
            evento_integracion = EventoPropiedadCreada(data=payload)

        elif isinstance(dto, PropiedadFallidaDTO):
            print('Creando EventoCreacionPropiedadFallidaPayload')
            payload = CreacionPropiedadFallidaPayload(
                id_propiedad=str(dto.id_propiedad)
            )
            evento_integracion = EventoCreacionPropiedadFallida(data=payload)

        elif isinstance(dto, ContratoCreadoDTO):
            print('Creando EventoContratoCreadoPayload')
            payload = ContratoCreadoPayload(
                id_propiedad=str(dto.id_propiedad),
                numero_contrato=str(dto.numero_contrato)
            )
            evento_integracion = EventoContratoCreado(data=payload)

        elif isinstance(dto, CreacionContratoFallidoDTO):
            print('Creando EventoCreacionContratoFallidoPayload')
            payload = CreacionContratoFallidoPayload(
                id_propiedad=str(dto.id_propiedad)
            )
            evento_integracion = EventoCreacionContratoFallido(data=payload)

        self._publicar_mensaje(evento_integracion, topico,
                               AvroSchema(evento_integracion.__class__))

    def publicar_comando(self, dto, topico):

        if isinstance(dto, CrearPropiedadDTO):
            print('Creando ComandoCrearPropiedadPayload')
            payload = ComandoCrearPropiedadPayload(
                id_propiedad=str(dto.id_propiedad),
            )
            comando_integracion = ComandoCrearPropiedad(data=payload)

        elif isinstance(dto, CrearPropiedadFallidaDTO):
            print('Creando ComandoCrearPropiedadFallidoPayload')
            payload = ComandoCrearPropiedadFallidoPayload(
                id_propiedad=str(dto.id_propiedad),
            )
            comando_integracion = ComandoCrearPropiedadFallido(data=payload)

        elif isinstance(dto, CrearContratroDTO):
            print('Creando ComandoCrearContratoPayload')
            payload = ComandoCrearContratoPayload(
                id_propiedad=str(dto.id_propiedad),
            )
            comando_integracion = ComandoCrearContrato(data=payload)

        elif isinstance(dto, CrearContratroFallidoDTO):
            print('Creando ComandoCrearContratoFallidoPayload')
            payload = ComandoCrearContratoFallidoPayload(
                id_propiedad=str(dto.id_propiedad),
            )
            comando_integracion = ComandoCrearContratoFallido(data=payload)

        self._publicar_mensaje(comando_integracion, topico,
                               AvroSchema(comando_integracion.__class__))
