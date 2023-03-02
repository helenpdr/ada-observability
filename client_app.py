import random

import requests

duracao = True
endpoints = ["renda-variavel", "renda-fixa", "cripto", "fii"]

while duracao == True:
    requisicao = requests.get("http://app:5000/" + endpoints[random.randint(0, 3)])
    print(requisicao.status_code)


