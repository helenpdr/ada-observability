import random
import time
import prometheus_client as prom

from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics



app = Flask(__name__)
metrics = PrometheusMetrics(app)

quantidade_usuarios_online = prom.Gauge("quantidade_usuarios_online",
                                        "Número de usuários online no momento")
@app.route('/renda-fixa')
@metrics.counter('efetivacao_renda_variavel',
                 'Número de papeis de renda fixa efetivados',
                 labels={'tipo':'ACOES'})

def renda_fixa():
    time.sleep(random.randint(1,10))
    quantidade_usuarios_online.set(random.randint(1,100))
    return render_template('lista.html', titulo='Renda Fixa')

if __name__ == "__main__":
    app.run(host="0.0.0.0")