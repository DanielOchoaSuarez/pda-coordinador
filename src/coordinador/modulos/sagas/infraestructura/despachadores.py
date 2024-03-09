import pulsar

from pulsar.schema import *
from coordinador.seedwork.infraestructura import utils

from coordinador.modulos.sagas.aplicacion.dto import *
from coordinador.modulos.sagas.infraestructura.schema.v1.eventos import EventoPropiedadCreada, PropiedadCreadaPayload, EventoCreacionPropiedadFallida, CreacionPropiedadFallidaPayload
from coordinador.modulos.sagas.infraestructura.schema.v1.eventos import EventoContratoCreado, ContratoCreadoPayload, EventoCreacionContratoFallido, CreacionContratoFallidoPayload
# from coordinador.modulos.sagas.infraestructura.schema.v1.comandos import ComandoCrearReserva, ComandoCrearReservaPayload
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
            print('Creando PropiedadCreadaPayload')
            payload = PropiedadCreadaPayload(
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

    # def publicar_comando(self, comando, topico):
    #     # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
    #     payload = ComandoCrearReservaPayload(
    #         id_usuario=str(comando.id_usuario)
    #         # agregar itinerarios
    #     )
    #     comando_integracion = ComandoCrearReserva(data=payload)
    #     self._publicar_mensaje(comando_integracion, topico,
    #                            AvroSchema(ComandoCrearReserva))
