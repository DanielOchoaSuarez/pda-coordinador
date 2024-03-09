from pydispatch import dispatcher
from .coordinadores.saga_propiedad import HandlerEventoDominio

from coordinador.modulos.sagas.dominio.eventos.catastro import PropiedadCreada, CreacionPropiedadFallida
from coordinador.modulos.sagas.dominio.eventos.contrato import ContratoCreado, CreacionContratoFallido

############################
# Eventos dominio catastro #
############################

dispatcher.connect(HandlerEventoDominio.handle_propiedad_creada, signal=f'{PropiedadCreada.__name__}Dominio')
dispatcher.connect(HandlerEventoDominio.handle_propiedad_creada_compensacion, signal=f'{CreacionPropiedadFallida.__name__}Dominio')


###############################
# Eventos dominio contractual #
###############################

dispatcher.connect(HandlerEventoDominio.handle_contrato_creado, signal=f'{ContratoCreado.__name__}Dominio')
dispatcher.connect(HandlerEventoDominio.handle_contrato_creado_compensacion, signal=f'{CreacionContratoFallido.__name__}Dominio')
