from flask import Blueprint, jsonify
from pydispatch import dispatcher

from coordinador.modulos.sagas.aplicacion.dto import *
from coordinador.seedwork.infraestructura import utils
from coordinador.modulos.sagas.infraestructura.despachadores import Despachador

from coordinador.modulos.sagas.dominio.eventos.catastro import PropiedadCreada, CreacionPropiedadFallida
from coordinador.modulos.sagas.dominio.eventos.contrato import ContratoCreado, CreacionContratoFallido


ab = Blueprint('orquestador', __name__)


@ab.route('/ping', methods=['GET'])
def health():
    return jsonify({'result': 'pong'})


@ab.route('/test-eventos', methods=['GET'])
def test_eventos():
    propiedad_creada_dto = PropiedadCreadaDTO(
        id_propiedad='1', numero_catastro='123')
    Despachador().publicar_evento(propiedad_creada_dto, utils.EVENTO_PROPIEDADA_CREADA)

    propiedad_fallida_dto = PropiedadFallidaDTO(id_propiedad='1')
    Despachador().publicar_evento(propiedad_fallida_dto,  utils.EVENTO_PROPIEDAD_FALLIDA)

    contrato_creado_dto = ContratoCreadoDTO(
        id_propiedad='1', numero_contrato='123')
    Despachador().publicar_evento(contrato_creado_dto, utils.EVENTO_CONTRATRO_CREADO)

    contrato_fallido_dto = CreacionContratoFallidoDTO(id_propiedad='1')
    Despachador().publicar_evento(contrato_fallido_dto, utils.EVENTO_CONTRATRO_FALLIDO)


    auditoria_creada_dto = AuditoriaCreadaDTO(
    id_propiedad='1', numero_contrato='123')
    Despachador().publicar_evento(auditoria_creada_dto, utils.EVENTO_AUDITORIA_CREADA)

    auditoria_fallida_dto = CreacionAuditoriaFallidaDTO(id_propiedad='1')
    Despachador().publicar_evento(auditoria_fallida_dto, utils.EVENTO_AUDITORIA_FALLIDA)

    return jsonify({'result': 'eventos publicados'})


@ab.route('/test-comandos', methods=['GET'])
def test_comandos():
    crear_propiedad = CrearPropiedadDTO(id_propiedad='A')
    Despachador().publicar_comando(crear_propiedad, utils.COMANDO_CREAR_PROPIEDAD)

    crear_propiedad_fallida = CrearPropiedadFallidaDTO(id_propiedad='B')
    Despachador().publicar_comando(crear_propiedad_fallida, utils.COMANDO_CREAR_PROPIEDAD_FALLIDA)

    crear_contrato = CrearContratroDTO(id_propiedad='C')
    Despachador().publicar_comando(crear_contrato, utils.COMANDO_CREAR_CONTRATO)

    crear_contrato_fallido = CrearContratroFallidoDTO(id_propiedad='D')
    Despachador().publicar_comando(crear_contrato_fallido, utils.COMANDO_CREAR_CONTRATO_FALLIDO)

    crear_auditoria = CrearAuditoriaDTO(id_propiedad='E')
    Despachador().publicar_comando(crear_auditoria, utils.COMANDO_CREAR_AUDITORIA)

    crear_auditoria_fallida = CrearAuditoriaFallidaDTO(id_propiedad='F')
    Despachador().publicar_comando(crear_auditoria_fallida, utils.COMANDO_CREAR_AUDITORIA_FALLIDA)

    return jsonify({'result': 'comandos publicados'})


@ab.route('/test-saga-propiedad', methods=['GET'])
def test_saga_propiedad():
    evento_propiedad_creada = PropiedadCreada(id_propiedad='111', numero_catastro='AAA111')
    dispatcher.send(signal=f'{type(evento_propiedad_creada).__name__}Dominio', evento=evento_propiedad_creada)
    return jsonify({'result': 'test saga propiedad creada iniciada'})


@ab.route('/test-saga-propiedad-compensacion', methods=['GET'])
def test_saga_propiedad_compensacion():
    evento_propiedad_compensacion = CreacionPropiedadFallida(id_propiedad='222')
    dispatcher.send(signal=f'{type(evento_propiedad_compensacion).__name__}Dominio', evento=evento_propiedad_compensacion)
    return jsonify({'result': 'test saga propiedad compensacion iniciada'})


@ab.route('/test-saga-contrato', methods=['GET'])
def test_saga_contrato():
    evento_contrato_creado = ContratoCreado(id_propiedad='333', numero_contrato='CONT_333')
    dispatcher.send(signal=f'{type(evento_contrato_creado).__name__}Dominio', evento=evento_contrato_creado)
    return jsonify({'result': 'test saga contrato creado iniciada'})


@ab.route('/test-saga-contrato-compensacion', methods=['GET'])
def test_saga_contrato_compensacion():
    evento_contrato_compensacion = CreacionContratoFallido(id_propiedad='444')
    dispatcher.send(signal=f'{type(evento_contrato_compensacion).__name__}Dominio', evento=evento_contrato_compensacion)
    return jsonify({'result': 'test saga contrato compensacion iniciada'})

