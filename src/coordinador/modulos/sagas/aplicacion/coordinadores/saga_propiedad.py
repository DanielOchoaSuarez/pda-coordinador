from datetime import datetime

from coordinador.seedwork.aplicacion.sagas import CoordinadorOrquestacion, Transaccion, Inicio, Fin
from coordinador.seedwork.aplicacion.comandos import Comando
from coordinador.seedwork.dominio.eventos import EventoDominio

from coordinador.seedwork.aplicacion.handlers import Handler

# Comandos y eventos Crear propiedad (Catastro)
from coordinador.modulos.sagas.aplicacion.comandos.crear_propiedad import CrearPropiedad
from coordinador.modulos.sagas.aplicacion.comandos.crear_propiedad_compensacion import CrearPropiedadCompensacion
from coordinador.modulos.sagas.dominio.eventos.catastro import PropiedadCreada, CreacionPropiedadFallida

# Comandos y eventos Contratos (Contractual)
from coordinador.modulos.sagas.aplicacion.comandos.crear_contrato import CrearContrato
from coordinador.modulos.sagas.aplicacion.comandos.crear_contrato_compensacion import CrearContratoCompensacion
from coordinador.modulos.sagas.dominio.eventos.contrato import ContratoCreado, CreacionContratoFallido


class CoordinadorPropiedades(CoordinadorOrquestacion):

    def inicializar_pasos(self):
        print("SAGA Orquestacion - Inicializando pasos")
        self.pasos = [
            Inicio(index=0),
            Transaccion(index=1,
                        comando=CrearPropiedad,
                        evento=PropiedadCreada,
                        error=CreacionPropiedadFallida,
                        compensacion=CrearPropiedadCompensacion),
            Transaccion(index=2,
                        comando=CrearContrato,
                        evento=ContratoCreado,
                        error=CreacionContratoFallido,
                        compensacion=CrearContratoCompensacion),
            Fin(index=3)
        ]

    def iniciar(self):
        print("Iniciando saga propiedades")
        self.persistir_en_saga_log(self.pasos[0])

    def terminar(self):
        print("Terminando saga propiedades")
        self.persistir_en_saga_log(self.pasos[-1])

    def persistir_en_saga_log(self, mensaje):
        # TODO Persistir estado en DB
        # Probablemente usted podría usar un repositorio para ello
        ...

    def construir_comando(self, evento: EventoDominio, tipo_comando: type):
        print(
            f"SAGA Orquestacion - Transformando evento {evento} en comando {tipo_comando.__name__}")

        if isinstance(evento, PropiedadCreada):
            return tipo_comando(
                id_propiedad=evento.id_propiedad,
                fecha_creacion=datetime.now().strftime("%d/%m/%Y"))

        elif isinstance(evento, CrearPropiedadCompensacion):
            return tipo_comando(
                id_propiedad=evento.id_propiedad,
                fecha_creacion=datetime.now().strftime("%d/%m/%Y"))

        elif isinstance(evento, CreacionContratoFallido):
            return tipo_comando(
                id_propiedad=evento.id_propiedad,
                fecha_creacion=datetime.now().strftime("%d/%m/%Y"))


def oir_mensaje(mensaje):
    if isinstance(mensaje, EventoDominio):
        print("SAGA Orquestacion - Coordinando: ", mensaje)
        coordinador = CoordinadorPropiedades()
        coordinador.inicializar_pasos()
        coordinador.procesar_evento(mensaje)
    else:
        raise NotImplementedError("El mensaje no es evento de Dominio")


class HandlerEventoDominio(Handler):

    @staticmethod
    def handle_propiedad_creada(evento):
        print("SAGA Orquestacion - Evento propiedad creada")
        propiedad_creada = PropiedadCreada(
            id_propiedad=evento.id_propiedad, numero_catastro=evento.numero_catastro)
        oir_mensaje(propiedad_creada)

    @staticmethod
    def handle_propiedad_creada_compensacion(evento):
        print("SAGA Orquestacion - Evento propiedad creada compensacion")
        propiedad_creada_compensacion = CreacionPropiedadFallida(
            id_propiedad=evento.id_propiedad)
        oir_mensaje(propiedad_creada_compensacion)

    @staticmethod
    def handle_contrato_creado(evento):
        print("SAGA Orquestacion - Evento contrato creado")
        contrato_creado = ContratoCreado(
            id_propiedad=evento.id_propiedad, numero_contrato=evento.numero_contrato)
        oir_mensaje(contrato_creado)

    @staticmethod
    def handle_contrato_creado_compensacion(evento):
        print("SAGA Orquestacion - Evento contrato creado compensacion")
        contrato_creado_compensacion = CreacionContratoFallido(
            id_propiedad=evento.id_propiedad)
        oir_mensaje(contrato_creado_compensacion)
