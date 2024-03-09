from __future__ import annotations
from dataclasses import dataclass
from coordinador.seedwork.dominio.eventos import (EventoDominio)


class EventoContrato(EventoDominio):
    ...


@dataclass
class ContratoCreado(EventoContrato):
    id_propiedad: str = None
    numero_contrato: str = None


@dataclass
class CreacionContratoFallido(EventoContrato):
    id_propiedad: str = None
