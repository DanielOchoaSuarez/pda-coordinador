
from coordinador.modulos.sagas.dominio.fabricas import FabricaSagalog
from .mapeadores import MapeadorSagalog

from coordinador.modulos.sagas.dominio.entidades import Sagalog
from coordinador.modulos.sagas.dominio.repositorios import RepositorioSagalog
from coordinador.config.db import db_session
from uuid import UUID
from .dto import SagaLog as SagaLogDTO


class RepositorioSagalogSQL(RepositorioSagalog):

    def __init__(self):
        self._fabrica_sagalog: FabricaSagalog = FabricaSagalog()

    @property
    def fabrica_sagalog(self):
        return self._fabrica_sagalog

    def obtener_por_id(self, id: UUID) -> Sagalog:
        # reserva_dto = db_session.query(CatastroDTO).filter_by(propiedad_id=str(id)).one()
        # return self._fabrica_catastro.crear_objeto(reserva_dto, MapeadorCatastro())
        ...

    def obtener_todos(self) -> list[Sagalog]:
        ...

    def agregar(self, log: Sagalog):
        sagalog_dto = self.fabrica_sagalog.crear_objeto(log, MapeadorSagalog())
        db_session.add(sagalog_dto)
        db_session.commit()

    def actualizar(self, propiedad: Sagalog):
        ...

    def eliminar(self, propiedad_id: UUID):
        ...