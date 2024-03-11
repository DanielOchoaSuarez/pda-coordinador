from pydispatch import dispatcher
from .coordinadores.saga_propiedad import HandlerEventoDominio

from coordinador.modulos.sagas.dominio.eventos.catastro import PropiedadCreada, CreacionPropiedadFallida
from coordinador.modulos.sagas.dominio.eventos.contrato import ContratoCreado, CreacionContratoFallido
from coordinador.modulos.sagas.dominio.eventos.auditoria import AuditoriaCreada, CreacionAuditoriaFallida
from coordinador.modulos.sagas.dominio.eventos.bff import SolicitudRegistrarRecibida, SolicitudRegistrarRecibidaFallida


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


###############################
# Eventos dominio auditoria   #
###############################

dispatcher.connect(HandlerEventoDominio.handle_auditoria_creada, signal=f'{AuditoriaCreada.__name__}Dominio')
dispatcher.connect(HandlerEventoDominio.handle_auditoria_creada_compensacion, signal=f'{CreacionAuditoriaFallida.__name__}Dominio')


#################
# Eventos BFF   #
#################

dispatcher.connect(HandlerEventoDominio.handle_registrar_propiedad_recibida, signal=f'{SolicitudRegistrarRecibida.__name__}Dominio')
