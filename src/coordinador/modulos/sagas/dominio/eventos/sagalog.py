from __future__ import annotations
from dataclasses import dataclass
from coordinador.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime


@dataclass
class SagalogRegistrado(EventoDominio):
    id_correlacion: str = None
    index: str = None
    comando: str = None
    fecha_evento: str = None
 
@dataclass
class SagalogFallida(EventoDominio):
    id_correlacion: str = None
    index: str = None
    comando: str = None
    fecha_evento: str = None

@dataclass
class Sagalogancelada(EventoDominio):
    id_correlacion: str = None
    index: str = None
    comando: str = None
    fecha_evento: str = None