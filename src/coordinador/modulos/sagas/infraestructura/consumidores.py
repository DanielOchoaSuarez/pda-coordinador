import pulsar
import _pulsar
from pulsar.schema import *
import uuid
import time
import logging
import traceback
import datetime

from coordinador.seedwork.infraestructura import utils
from coordinador.modulos.sagas.infraestructura.schema.v1.eventos import EventoPropiedadCreada, EventoCreacionPropiedadFallida, EventoContratoCreado, EventoCreacionContratoFallido
from coordinador.modulos.sagas.infraestructura.schema.v1.comandos import ComandoCrearPropiedad


####################
# Eventos Catastro #
####################

def suscribirse_evento_propiedad_creada(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe(utils.EVENTO_PROPIEDADA_CREADA, consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name=utils.SUB_EVENTO_PROPIEDADA_CREADA, schema=AvroSchema(EventoPropiedadCreada))

        while True:
            mensaje = consumidor.receive()
            datos = mensaje.value().data
            print(f'Evento propiedad creada: {datos}')
            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        print('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()


def suscribirse_evento_propiedad_fallida(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe(utils.EVENTO_PROPIEDAD_FALLIDA, consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name=utils.SUB_EVENTO_PROPIEDAD_FALLIDA, schema=AvroSchema(EventoCreacionPropiedadFallida))

        while True:
            mensaje = consumidor.receive()
            datos = mensaje.value().data
            print(f'Evento propiedad creada fallida: {datos}')
            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        print('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()


#######################
# Eventos Contractual #
#######################

def suscribirse_evento_contratro_creado(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe(utils.EVENTO_CONTRATRO_CREADO, consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name=utils.SUB_EVENTO_CONTRATRO_CREADO, schema=AvroSchema(EventoContratoCreado))

        while True:
            mensaje = consumidor.receive()
            datos = mensaje.value().data
            print(f'Evento contratro creado: {datos}')
            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        print('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()


def suscribirse_evento_contratro_fallido(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe(utils.EVENTO_CONTRATRO_FALLIDO, consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name=utils.SUB_EVENTO_CONTRATRO_FALLIDO, schema=AvroSchema(EventoCreacionContratoFallido))

        while True:
            mensaje = consumidor.receive()
            datos = mensaje.value().data
            print(f'Evento contratro creado fallido: {datos}')
            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        print('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()


#####################
# Comandos Catastro #
#####################

def suscribirse_comando_crear_propiedad(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(utils.pulsar_service_url())
        consumidor = cliente.subscribe(utils.COMANDO_CREAR_PROPIEDAD, consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name=utils.SUB_COMANDO_CREAR_PROPIEDAD, schema=AvroSchema(ComandoCrearPropiedad))

        while True:
            mensaje = consumidor.receive()
            datos = mensaje.value().data
            print(f'Comando crear propiedad recibido: {datos}')
            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        print('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()
