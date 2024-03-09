from coordinador.seedwork.aplicacion.sagas import CoordinadorOrquestacion, Transaccion, Inicio, Fin
from coordinador.seedwork.aplicacion.comandos import Comando
from coordinador.seedwork.dominio.eventos import EventoDominio

# Comandos y eventos Crear propiedad (Catastro)
from coordinador.modulos.sagas.aplicacion.comandos.crear_propiedad import CrearPropiedad
from coordinador.modulos.sagas.aplicacion.comandos.crear_propiedad_compensacion import CrearPropiedadCompensacion
from coordinador.modulos.sagas.dominio.eventos.catastro import PropiedadCreada, CreacionPropiedadFallida

# Comandos y eventos Contratos (Contractual)
from coordinador.modulos.sagas.aplicacion.comandos.crear_contrato import CrearContrato
from coordinador.modulos.sagas.aplicacion.comandos.crear_contrato_compensacion import CrearContratoCompensacion
from coordinador.modulos.sagas.dominio.eventos.contrato import ContratoCreado, CreacionContratoFallido


class CoordinadorReservas(CoordinadorOrquestacion):

    def inicializar_pasos(self):
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
        self.persistir_en_saga_log(self.pasos[0])

    def terminar(self):
        self.persistir_en_saga_log(self.pasos[-1])

    def persistir_en_saga_log(self, mensaje):
        # TODO Persistir estado en DB
        # Probablemente usted podría usar un repositorio para ello
        ...

    def construir_comando(self, evento: EventoDominio, tipo_comando: type):
        # TODO Transforma un evento en la entrada de un comando
        # Por ejemplo si el evento que llega es ReservaCreada y el tipo_comando es PagarReserva
        # Debemos usar los atributos de ReservaCreada para crear el comando PagarReserva
        ...


# TODO Agregue un Listener/Handler para que se puedan redireccionar eventos de dominio
def oir_mensaje(mensaje):
    if isinstance(mensaje, EventoDominio):
        coordinador = CoordinadorReservas()
        coordinador.procesar_evento(mensaje)
    else:
        raise NotImplementedError("El mensaje no es evento de Dominio")
