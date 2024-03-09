from flask import Blueprint, jsonify

from coordinador.modulos.sagas.aplicacion.dto import *
from coordinador.seedwork.infraestructura import utils
from coordinador.modulos.sagas.infraestructura.despachadores import Despachador

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

    return jsonify({'result': 'eventos publicados'})
