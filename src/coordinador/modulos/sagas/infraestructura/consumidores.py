import pulsar
import _pulsar
from pulsar.schema import *
import uuid
import time
import logging
import traceback
import datetime
from pydispatch import dispatcher
from coordinador.modulos.sagas.dominio.eventos.auditoria import AuditoriaCreada
from coordinador.modulos.sagas.dominio.eventos.catastro import CreacionPropiedadFallida, PropiedadCreada
from coordinador.modulos.sagas.dominio.eventos.contrato import ContratoCreado, CreacionContratoFallido

from coordinador.seedwork.infraestructura import utils
from coordinador.modulos.sagas.infraestructura.schema.v1.eventos import EventoPropiedadCreada, EventoCreacionPropiedadFallida, EventoContratoCreado, EventoCreacionContratoFallido, EventoAuditoriaCreada, EventoCreacionAuditoriaFallida
from coordinador.modulos.sagas.infraestructura.schema.v1.comandos import ComandoCrearPropiedad, ComandoCrearPropiedadFallido, ComandoCrearContrato, ComandoCrearContratoFallido, ComandoCrearAuditoria, ComandoCrearAuditoriaFallida, ComandoRegistrarPropiedad

from coordinador.modulos.sagas.dominio.eventos.bff import SolicitudRegistrarRecibida, SolicitudRegistrarRecibidaFallida


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

            evento_propiedad_creada = PropiedadCreada(
                id_propiedad=mensaje.value().data.id_propiedad,
                numero_catastro=mensaje.value().data.numero_catastro)
            dispatcher.send(
                signal=f'{type(evento_propiedad_creada).__name__}Dominio', evento=evento_propiedad_creada)

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

            evento_contrato_creado = ContratoCreado(
                id_propiedad=mensaje.value().data.id_propiedad,
                numero_contrato=mensaje.value().data.numero_contrato)
            dispatcher.send(
                signal=f'{type(evento_contrato_creado).__name__}Dominio', evento=evento_contrato_creado)

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

            evento_contrato_compensacion = CreacionContratoFallido(
                mensaje.value().data.id_propiedad,)
            dispatcher.send(
                signal=f'{type(evento_contrato_compensacion).__name__}Dominio', evento=evento_contrato_compensacion)

            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        print('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()


#######################
# Eventos Auditoria #
#######################

def suscribirse_evento_auditoria_creada(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe(utils.EVENTO_AUDITORIA_CREADA, consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name=utils.SUB_EVENTO_AUDITORIA_CREADA, schema=AvroSchema(EventoAuditoriaCreada))

        while True:
            mensaje = consumidor.receive()
            datos = mensaje.value().data
            print(f'Evento auditoria creada: {datos}')

            evento_auditoria_creado = AuditoriaCreada(
                mensaje.value().data.id_propiedad,
                numero_contrato='CONT_444')
            dispatcher.send(
                signal=f'{type(evento_auditoria_creado).__name__}Dominio', evento=evento_auditoria_creado)

            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        print('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()


def suscribirse_evento_auditoria_fallida(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe(utils.EVENTO_AUDITORIA_FALLIDA, consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name=utils.SUB_EVENTO_AUDITORIA_FALLIDA, schema=AvroSchema(EventoCreacionAuditoriaFallida))

        while True:
            mensaje = consumidor.receive()
            datos = mensaje.value().data
            print(f'Evento auditoria creada fallida: {datos}')
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


def suscribirse_comando_crear_propiedad_fallida(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(utils.pulsar_service_url())
        consumidor = cliente.subscribe(utils.COMANDO_CREAR_PROPIEDAD_FALLIDA, consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name=utils.SUB_COMANDO_CREAR_PROPIEDAD_FALLIDA, schema=AvroSchema(ComandoCrearPropiedadFallido))

        while True:
            mensaje = consumidor.receive()
            datos = mensaje.value().data
            print(f'Comando crear propiedad fallida recibido: {datos}')

            evento_propiedad_compensacion = CreacionPropiedadFallida(
                id_propiedad=mensaje.value().data.id_propiedad)
            dispatcher.send(
                signal=f'{type(evento_propiedad_compensacion).__name__}Dominio', evento=evento_propiedad_compensacion)

            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        print('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()


########################
# Comandos Contractual #
########################

def suscribirse_comando_crear_contratro(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(utils.pulsar_service_url())
        consumidor = cliente.subscribe(utils.COMANDO_CREAR_CONTRATO, consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name=utils.SUB_COMANDO_CREAR_CONTRATO, schema=AvroSchema(ComandoCrearContrato))

        while True:
            mensaje = consumidor.receive()
            datos = mensaje.value().data
            print(f'Comando crear contrato recibido: {datos}')
            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        print('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()


def suscribirse_comando_crear_contratro_fallido(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(utils.pulsar_service_url())
        consumidor = cliente.subscribe(utils.COMANDO_CREAR_CONTRATO_FALLIDO, consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name=utils.SUB_COMANDO_CREAR_CONTRATO_FALLIDO, schema=AvroSchema(ComandoCrearContratoFallido))

        while True:
            mensaje = consumidor.receive()
            datos = mensaje.value().data
            print(f'Comando crear contrato fallido recibido: {datos}')

            evento_contrato_compensacion = CreacionContratoFallido(
                id_propiedad=mensaje.value().data.id_propiedad)
            dispatcher.send(
                signal=f'{type(evento_contrato_compensacion).__name__}Dominio', evento=evento_contrato_compensacion)

            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        print('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()


########################
# Comandos Auditoria   #
########################

def suscribirse_comando_crear_auditoria(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(utils.pulsar_service_url())
        consumidor = cliente.subscribe(utils.COMANDO_CREAR_AUDITORIA, consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name=utils.SUB_COMANDO_CREAR_AUDITORIA, schema=AvroSchema(ComandoCrearAuditoria))

        while True:
            mensaje = consumidor.receive()
            datos = mensaje.value().data
            print(f'Comando crear auditoria recibido: {datos}')
            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        print('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()


def suscribirse_comando_crear_auditoria_fallida(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(utils.pulsar_service_url())
        consumidor = cliente.subscribe(utils.COMANDO_CREAR_AUDITORIA_FALLIDA, consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name=utils.SUB_COMANDO_CREAR_AUDITORIA_FALLIDA, schema=AvroSchema(ComandoCrearAuditoriaFallida))

        while True:
            mensaje = consumidor.receive()
            datos = mensaje.value().data
            print(f'Comando crear auditoria fallido recibido: {datos}')
            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        print('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()


################
# Comandos BFF #
################

def suscribirse_comando_registrar_propiedad(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(utils.pulsar_service_url())
        consumidor = cliente.subscribe(utils.COMANDO_REGISTRAR_PROPIEDAD, consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name=utils.SUB_COMANDO_REGISTRAR_PROPIEDAD, schema=AvroSchema(ComandoRegistrarPropiedad))

        while True:
            mensaje = consumidor.receive()
            datos = mensaje.value().data
            print(f'Comando registrar propiedad BFF recibido: {datos}')

            evento_registrar = SolicitudRegistrarRecibida(
                id_propiedad=mensaje.value().data.id_propiedad)
            dispatcher.send(
                signal=f'{type(evento_registrar).__name__}Dominio', evento=evento_registrar)

            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        print('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()
