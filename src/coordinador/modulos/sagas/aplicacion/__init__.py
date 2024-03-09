from pydispatch import dispatcher
from .coordinadores.saga_propiedad import HandlerEventoDominio

from coordinador.modulos.sagas.dominio.eventos.catastro import PropiedadCreada, CreacionPropiedadFallida


dispatcher.connect(HandlerEventoDominio.handle_propiedad_creada, signal=f'{PropiedadCreada.__name__}Dominio')
