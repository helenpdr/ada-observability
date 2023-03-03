import http.client
import random
import time

from flask import Flask, render_template
import prometheus_client as prom
from prometheus_flask_exporter import PrometheusMetrics
import logging


logging.basicConfig(level=logging.DEBUG,
                    format='%asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

app = Flask(__name__)
metrics = PrometheusMetrics(app)

quantidade_usuarios_online = prom.Gauge("quantidade_usuarios_online",
                                        "Número de usuários online no momento")

def parametros_endpoint():
    time.sleep(random.randint(1, 10))
    quantidade_usuarios_online.set(random.randint(1, 100))

@app.route('/renda-fixa')
def renda_fixa():
    app.logger.info("Acessando Renda Fixa!")
    parametros_endpoint()
    if random.randint(0, 1) == 0:
        return http.client.BAD_REQUEST
    return render_template('lista.html', titulo='Renda Fixa')

@app.route('/renda-variavel')
def renda_variavel():
    app.logger.info("Acessando Renda Variável!")
    parametros_endpoint()
    return render_template('lista.html', titulo='Renda Variável')

@app.route('/cripto')
def cripto():
    app.logger.info("Acessando Cripto!")
    parametros_endpoint()
    return render_template('lista.html', titulo='Cripto')

@app.route('/fii')
def fiis():
    app.logger.info("Acessando Fii!")
    parametros_endpoint()
    return render_template('lista.html', titulo='FIIs')

if __name__ == "__main__":
    app.run(host="0.0.0.0")