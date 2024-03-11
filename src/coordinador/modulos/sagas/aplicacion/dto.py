from dataclasses import dataclass, field
from coordinador.seedwork.aplicacion.dto import DTO

###################
# DTOs de eventos #
###################


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


@dataclass(frozen=True)
class AuditoriaCreadaDTO(DTO):
    id_propiedad: str = field(default_factory=str)
    numero_contrato: str = field(default_factory=str)

@dataclass(frozen=True)
class CreacionAuditoriaFallidaDTO(DTO):
    id_propiedad: str = field(default_factory=str)

####################
# DTOs de comandos #
####################


@dataclass(frozen=True)
class CrearPropiedadDTO(DTO):
    id_propiedad: str = field(default_factory=str)

@dataclass(frozen=True)
class CrearPropiedadFallidaDTO(DTO):
    id_propiedad: str = field(default_factory=str)


@dataclass(frozen=True)
class CrearContratroDTO(DTO):
    id_propiedad: str = field(default_factory=str)

@dataclass(frozen=True)
class CrearContratroFallidoDTO(DTO):
    id_propiedad: str = field(default_factory=str)


@dataclass(frozen=True)
class CrearAuditoriaDTO(DTO):
    id_propiedad: str = field(default_factory=str)

@dataclass(frozen=True)
class CrearAuditoriaFallidaDTO(DTO):
    id_propiedad: str = field(default_factory=str)

@dataclass(frozen=True)
class RegistrarPropiedadOutDTO(DTO):
    exitoso: bool = field(default_factory=bool)


###################
# DTOs de SAGA LOG #
###################
@dataclass(frozen=True)
class SagaLogDTO(DTO):
    id_correlacion: str = field(default_factory=str)
    index: str = field(default_factory=str)
    comando: str = field(default_factory=str)
    fecha_evento: str = field(default_factory=str)