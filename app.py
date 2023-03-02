import random
import time

from flask import Flask, render_template
import prometheus_client as prom
from prometheus_flask_exporter import PrometheusMetrics



app = Flask(__name__)
metrics = PrometheusMetrics(app)

quantidade_usuarios_online = prom.Gauge("quantidade_usuarios_online",
                                        "Número de usuários online no momento")

def parametros_endpoint():
    time.sleep(random.randint(1, 10))
    quantidade_usuarios_online.set(random.randint(1, 100))

@app.route('/renda-fixa')
def renda_fixa():
    parametros_endpoint()
    return render_template('lista.html', titulo='Renda Fixa')

@app.route('/renda-variavel')
def renda_variavel():
    parametros_endpoint()
    return render_template('lista.html', titulo='Renda Variável')

@app.route('/cripto')
def cripto():
    parametros_endpoint()
    return render_template('lista.html', titulo='Cripto')

@app.route('/fii')
def fiis():
    parametros_endpoint()
    return render_template('lista.html', titulo='FIIs')

if __name__ == "__main__":
    app.run(host="0.0.0.0")