from __future__ import annotations
from dataclasses import dataclass
from coordinador.seedwork.dominio.eventos import (EventoDominio)


class EventoCatastro(EventoDominio):
    ...


@dataclass
class PropiedadCreada(EventoCatastro):
    id_propiedad: str = None
    numero_catastro: str = None


@dataclass
class CreacionPropiedadFallida(EventoCatastro):
    id_propiedad: str = None
