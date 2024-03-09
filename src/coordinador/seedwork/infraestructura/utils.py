import time
import os
import datetime

epoch = datetime.datetime.utcfromtimestamp(0)


EVENTO_PROPIEDADA_CREADA = 'eventos-propiedad-creada'
SUB_EVENTO_PROPIEDADA_CREADA = 'pda-sub-evento-propiedad-creada'

EVENTO_PROPIEDAD_FALLIDA = 'eventos-propiedad-fallida'
SUB_EVENTO_PROPIEDAD_FALLIDA = 'pda-sub-evento-propiedad-fallida'

EVENTO_CONTRATRO_CREADO = 'eventos-contratro-creado'
SUB_EVENTO_CONTRATRO_CREADO = 'pda-sub-evento-contratro-creado'

EVENTO_CONTRATRO_FALLIDO = 'eventos-contratro-fallido'
SUB_EVENTO_CONTRATRO_FALLIDO = 'pda-sub-evento-contratro-fallido'


def time_millis():
    return int(time.time() * 1000)


def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0


def millis_a_datetime(millis):
    return datetime.datetime.fromtimestamp(millis/1000.0)


def broker_host():
    return os.getenv('BROKER_HOST', default="localhost")
