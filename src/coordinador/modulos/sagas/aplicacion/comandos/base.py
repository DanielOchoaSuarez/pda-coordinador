from coordinador.seedwork.aplicacion.comandos import ComandoHandler


class CrearComandoBaseHandler(ComandoHandler):
    def __init__(self):
        print('Creando instancia de CrearComandoBaseHandler')

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_vuelos(self):
        return self._fabrica_vuelos
