from coordinador.config.db import Base
from sqlalchemy import Column, String, DateTime, Integer

class SagaLog(Base):
    __tablename__ = "sagalog"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_correlacion = Column(String)
    index = Column(String)
    comando = Column(String)
    fecha_evento = Column(String)

    def __init__(self, id_correlacion, index, comando, fecha_evento):
        self.id_correlacion = id_correlacion
        self.index = index
        self.comando = comando
        self.fecha_evento = fecha_evento