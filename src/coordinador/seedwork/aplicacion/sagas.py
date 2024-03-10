from abc import ABC, abstractmethod
from coordinador.seedwork.aplicacion.comandos import Comando
from coordinador.seedwork.dominio.eventos import EventoDominio
from dataclasses import dataclass
from .comandos import ejecutar_commando
import uuid
import datetime


class CoordinadorSaga(ABC):
    id_correlacion: uuid.UUID

    @abstractmethod
    def persistir_en_saga_log(self, mensaje):
        ...

    @abstractmethod
    def construir_comando(self, evento: EventoDominio, tipo_comando: type) -> Comando:
        ...

    def publicar_comando(self, evento: EventoDominio, tipo_comando: type):
        comando = self.construir_comando(evento, tipo_comando)
        print("SAGA TEMPORAL - Seedwork_Saga publicar_comando(): " + str(comando.__class__))
        ejecutar_commando(comando)

    @abstractmethod
    def inicializar_pasos(self):
        ...

    @abstractmethod
    def procesar_evento(self, evento: EventoDominio):
        ...

    @abstractmethod
    def iniciar():
        ...

    @abstractmethod
    def terminar():
        ...


class Paso():
    id_correlacion: uuid.UUID
    fecha_evento: datetime.datetime
    index: int


@dataclass
class Inicio(Paso):
    index: int = 0


@dataclass
class Fin(Paso):
    index: int


@dataclass
class Transaccion(Paso):
    index: int
    comando: Comando
    evento: EventoDominio
    error: EventoDominio
    compensacion: Comando
    # exitosa: bool


class CoordinadorOrquestacion(CoordinadorSaga, ABC):
    pasos: list[Paso]
    index: int

    def obtener_paso_dado_un_evento(self, evento: EventoDominio):
        for i, paso in enumerate(self.pasos):
            if not isinstance(paso, Transaccion):
                continue

            if isinstance(evento, paso.evento) or isinstance(evento, paso.error):
                return paso, i
        raise Exception("Evento no hace parte de la transacción")

    def es_ultima_transaccion(self, index):
        return isinstance(self.pasos[index+1], Fin)

    def procesar_evento(self, evento: EventoDominio):
        paso, index = self.obtener_paso_dado_un_evento(evento)
        print(
            f"SAGA Orquestacion - procesando {index} de {len(self.pasos) - 2} pasos")

        if isinstance(evento, paso.evento):
            print("SAGA Orquestacion - Procesando siguiente paso")

            if self.es_ultima_transaccion(index):
                print("SAGA Orquestacion - Fin transacciones")
                self.terminar()
            else:
                self.publicar_comando(evento, self.pasos[index+1].comando)

        elif isinstance(evento, paso.error):
            print("SAGA Orquestacion - Procesando error")

            if isinstance(self.pasos[index-1], Inicio):
                print("SAGA Orquestacion - Fin compensaciones")
            else:
                self.publicar_comando(evento, self.pasos[index-1].compensacion)
