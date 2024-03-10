from __future__ import annotations
from dataclasses import dataclass
from coordinador.seedwork.dominio.eventos import (EventoDominio)


class EventoAuditoria(EventoDominio):
    ...


@dataclass
class AuditoriaCreada(EventoAuditoria):
    id_propiedad: str = None
    numero_contrato: str = None


@dataclass
class CreacionAuditoriaFallida(EventoAuditoria):
    id_propiedad: str = None
