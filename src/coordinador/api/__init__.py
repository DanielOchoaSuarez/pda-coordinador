from flask import Flask, jsonify
from coordinador.config.db import init_db
from coordinador.config.errors import ApiError
from .orquestador import ab

app = Flask(__name__)
app.secret_key = '1D7FC7F9-3B7E-4C40-AF4D-141ED3F6013A'
init_db()
app.register_blueprint(ab)


@app.errorhandler(ApiError)
def handle_exception(err):
    response = {
        "msg": err.description
    }
    return jsonify(response), err.code


def comenzar_consumidor():
    import threading
    import coordinador.modulos.sagas.infraestructura.consumidores as contratos

    # Suscripción a eventos
    threading.Thread(target=contratos.suscribirse_evento_propiedad_creada, args=[app]).start()
    threading.Thread(target=contratos.suscribirse_evento_propiedad_fallida, args=[app]).start()
    threading.Thread(target=contratos.suscribirse_evento_contratro_creado, args=[app]).start()
    threading.Thread(target=contratos.suscribirse_evento_contratro_fallido, args=[app]).start()
    threading.Thread(target=contratos.suscribirse_evento_auditoria_creada, args=[app]).start()
    threading.Thread(target=contratos.suscribirse_evento_auditoria_fallida, args=[app]).start()

    # Suscripción a comandos (Solo lectura)
    threading.Thread(target=contratos.suscribirse_comando_crear_propiedad, args=[app]).start()
    threading.Thread(target=contratos.suscribirse_comando_crear_propiedad_fallida, args=[app]).start()
    threading.Thread(target=contratos.suscribirse_comando_crear_contratro, args=[app]).start()
    threading.Thread(target=contratos.suscribirse_comando_crear_contratro_fallido, args=[app]).start()
    threading.Thread(target=contratos.suscribirse_comando_crear_auditoria, args=[app]).start()
    threading.Thread(target=contratos.suscribirse_comando_crear_auditoria_fallida, args=[app]).start()

    # Suscripción comandos BFF
    threading.Thread(target=contratos.suscribirse_comando_registrar_propiedad, args=[app]).start()


comenzar_consumidor()
