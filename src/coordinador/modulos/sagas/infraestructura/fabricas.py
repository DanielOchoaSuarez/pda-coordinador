from dataclasses import dataclass
from coordinador.seedwork.dominio.fabricas import Fabrica
from coordinador.seedwork.dominio.repositorios import Repositorio
from coordinador.modulos.sagas.dominio.repositorios import RepositorioSagalog
from .excepciones import ExcepcionFabrica
from .repositorios import RepositorioSagalogSQL

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioSagalog.__class__:
            return RepositorioSagalogSQL()
        else:
            raise ExcepcionFabrica()