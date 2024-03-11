from __future__ import annotations
from dataclasses import dataclass, field
from coordinador.seedwork.dominio.entidades import AgregacionRaiz
from coordinador.modulos.sagas.dominio.eventos.sagalog import SagalogRegistrado

@dataclass
class Sagalog(AgregacionRaiz):
    id_correlacion: str = field(default=str)
    index: str = field(default=str)
    comando: str = field(default=str)
    fecha_evento: str = field(default=str)
    
    def registrar_catastro(self, sagalog: Sagalog):

        self.agregar_evento(SagalogRegistrado(
            id_correlacion=sagalog.id_correlacion,
            index=sagalog.index,
            comando=sagalog.comando,
            fecha_evento=sagalog.fecha_evento))
