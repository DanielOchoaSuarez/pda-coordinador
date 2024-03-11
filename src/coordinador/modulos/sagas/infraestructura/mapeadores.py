from coordinador.seedwork.dominio.repositorios import Mapeador
from coordinador.modulos.sagas.dominio.entidades import Sagalog
from .dto import SagaLog as SagalogDTO

class MapeadorSagalog(Mapeador):

    def obtener_tipo(self) -> type:
        return Sagalog.__class__

    def entidad_a_dto(self, entidad: Sagalog) -> SagalogDTO:
        sagalog_dto = SagalogDTO(
            entidad.id_correlacion,
            entidad.index,
            entidad.comando,
            entidad.fecha_evento
        )
        return sagalog_dto

    def dto_a_entidad(self, dto: SagalogDTO) -> Sagalog:
        sagalog = Sagalog(
            id_correlacion=dto.id_correlacion,
            index=dto.index,
            comando=dto.comando,
            fecha_evento=dto.fecha_evento,
        )       
        return sagalog