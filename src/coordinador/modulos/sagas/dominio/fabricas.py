from .entidades import Sagalog
from .excepciones import TipoObjetoNoExisteEnDominioAnalisisExcepcion
from coordinador.seedwork.dominio.repositorios import Mapeador
from coordinador.seedwork.dominio.fabricas import Fabrica
from coordinador.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class _FabricaSagalog(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            sagalog = mapeador.dto_a_entidad(obj)
            return sagalog

@dataclass
class FabricaSagalog(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Sagalog.__class__:
            fabrica_sagalog = _FabricaSagalog()
            return fabrica_sagalog.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioAnalisisExcepcion()