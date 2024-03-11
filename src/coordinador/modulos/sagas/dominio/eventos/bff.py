from __future__ import annotations
from dataclasses import dataclass
from coordinador.seedwork.dominio.eventos import (EventoDominio)


class EventoRegistro(EventoDominio):
    ...


@dataclass
class SolicitudRegistrarRecibida(EventoRegistro):
    id_propiedad: str = None


@dataclass
class SolicitudRegistrarRecibidaFallida(EventoRegistro):
    id_propiedad: str = None
