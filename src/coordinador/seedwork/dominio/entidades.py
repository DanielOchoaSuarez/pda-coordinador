from dataclasses import dataclass, field

from coordinador.seedwork.dominio.mixins import ValidarReglasMixin
from .eventos import EventoDominio
from .reglas import IdEntidadEsInmutable
from .excepciones import IdDebeSerInmutableExcepcion
from datetime import datetime
import uuid

@dataclass
class Entidad:
    id: uuid.UUID = field(hash=True)
    fecha_creacion: datetime =  field(default=datetime.now())
    fecha_actualizacion: datetime = field(default=datetime.now())

    @classmethod
    def siguiente_id(self) -> uuid.UUID:
        return uuid.uuid4()

    @property
    def id(self):
        return str(self._id)

    @id.setter
    def id(self, id: uuid.UUID) -> None:
        if not IdEntidadEsInmutable(self).es_valido():
            raise IdDebeSerInmutableExcepcion()
        self._id = self.siguiente_id()
        

@dataclass
class AgregacionRaiz(Entidad, ValidarReglasMixin):
    eventos: list[EventoDominio] = field(default_factory=list)

    def agregar_evento(self, evento: EventoDominio):
        self.eventos.append(evento)
    
    def limpiar_eventos(self):
        self.eventos = list()


@dataclass
class Locacion(Entidad):
    def __str__(self) -> str:
        ...