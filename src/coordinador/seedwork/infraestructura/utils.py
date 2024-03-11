import time
import os
import datetime

##############################################
# Eventos, comandos y subscriptores catastro #
##############################################

EVENTO_PROPIEDADA_CREADA = 'eventos-propiedad-creada'
SUB_EVENTO_PROPIEDADA_CREADA = 'pda-sub-evento-propiedad-creada'

EVENTO_PROPIEDAD_FALLIDA = 'eventos-propiedad-fallida'
SUB_EVENTO_PROPIEDAD_FALLIDA = 'pda-sub-evento-propiedad-fallida'

COMANDO_CREAR_PROPIEDAD = 'comandos-crear-propiedad'
SUB_COMANDO_CREAR_PROPIEDAD = 'pda-sub-comando-crear-propiedad'

COMANDO_CREAR_PROPIEDAD_FALLIDA = 'comandos-crear-propiedad-fallida'
SUB_COMANDO_CREAR_PROPIEDAD_FALLIDA = 'pda-sub-comando-crear-propiedad-fallida'


################################################
# Eventos, comandos  y subscriptores contratos #
################################################

EVENTO_CONTRATRO_CREADO = 'eventos-contratro-creado'
SUB_EVENTO_CONTRATRO_CREADO = 'pda-sub-evento-contratro-creado'

EVENTO_CONTRATRO_FALLIDO = 'eventos-contratro-fallido'
SUB_EVENTO_CONTRATRO_FALLIDO = 'pda-sub-evento-contratro-fallido'

COMANDO_CREAR_CONTRATO = 'comandos-crear-contrato'
SUB_COMANDO_CREAR_CONTRATO = 'pda-sub-comando-crear-contrato'

COMANDO_CREAR_CONTRATO_FALLIDO = 'comandos-crear-contrato-fallido'
SUB_COMANDO_CREAR_CONTRATO_FALLIDO = 'pda-sub-comando-crear-contrato-fallido'


################################################
# Eventos, comandos  y subscriptores Auditoria #
################################################

EVENTO_AUDITORIA_CREADA = 'eventos-auditoria-creada'
SUB_EVENTO_AUDITORIA_CREADA = 'pda-sub-evento-auditoria-creada'

EVENTO_AUDITORIA_FALLIDA = 'eventos-auditoria-fallida'
SUB_EVENTO_AUDITORIA_FALLIDA = 'pda-sub-evento-auditoria-fallida'

COMANDO_CREAR_AUDITORIA = 'comandos-crear-auditoria'
SUB_COMANDO_CREAR_AUDITORIA = 'pda-sub-comando-crear-auditoria'

COMANDO_CREAR_AUDITORIA_FALLIDA = 'comandos-crear-auditoria-fallida'
SUB_COMANDO_CREAR_AUDITORIA_FALLIDA = 'pda-sub-comando-crear-auditoria-fallida'



#########################################
# Eventos, comandos y subscriptores BFF #
#########################################
COMANDO_REGISTRAR_PROPIEDAD = 'comandos-registrar-propiedad'
SUB_COMANDO_REGISTRAR_PROPIEDAD = 'pda-sub-comando-registrar-propiedad'


epoch = datetime.datetime.utcfromtimestamp(0)


def time_millis():
    return int(time.time() * 1000)


def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0


def millis_a_datetime(millis):
    return datetime.datetime.fromtimestamp(millis/1000.0)


def broker_host():
    return os.getenv('BROKER_HOST', default="localhost")


def pulsar_service_url():
    return f'pulsar://{broker_host()}:6650'
