from dataclasses import dataclass, field
from coordinador.seedwork.aplicacion.dto import DTO


@dataclass(frozen=True)
class PropiedadCreadaDTO(DTO):
    id_propiedad: str = field(default_factory=str)
    numero_catastro: str = field(default_factory=str)


@dataclass(frozen=True)
class PropiedadFallidaDTO(DTO):
    id_propiedad: str = field(default_factory=str)


@dataclass(frozen=True)
class ContratoCreadoDTO(DTO):
    id_propiedad: str = field(default_factory=str)
    numero_contrato: str = field(default_factory=str)


@dataclass(frozen=True)
class CreacionContratoFallidoDTO(DTO):
    id_propiedad: str = field(default_factory=str)
