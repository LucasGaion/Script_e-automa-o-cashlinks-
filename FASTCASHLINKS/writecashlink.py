# Arquvo whitecashlink recebendo o retorno do payload a linha do arquivo cashlinksaida.csv escrevendo as resposta

# bibliotecas
# import readcashlink
from headerprod import obter_url_api, obter_header # (PROD)
# from header import obter_url_api, obter_header # (DEV)
import requests
import json

def enviar_requisicao(payload):

    # Envia a requisição à API e obtém a resposta
    url_api = obter_url_api()
    header = obter_header()
    resposta = requests.post(url_api, json=payload, headers=header)

    # Processa a resposta da API e retorna uma linha da planilha
    json_resposta = None
    if resposta.status_code == 200:
        json_resposta = json.loads(resposta.content)
        print(json_resposta)

        # O Json_resposta esta puxando da API, e payload puxando no arquivo cashlink.csv
        try:
            linha = (json_resposta['Result']['Transaction']['Tid'],
                     (json_resposta['Result']['Transaction']['Price']),
                     payload["Name"],
                     payload["Email"],
                     payload["Document"],
                     payload["MobilePhone"],
                     json_resposta['Result']['Transaction']['ItemDescription'],
                     json_resposta['Result']['Transaction']['PaymentMethod'],
                     json_resposta['Result']['Transaction']['SubPaymentMethod'],
                     payload["DueDate"])

            # Processa a resposta retorna uma linha da planilha de saida
            objeto = json_resposta['Result']['Parameters'][1]['Value']

        except TypeError:
            # Erros vao aparecer em cada linha o erro
            linha = "erro", "erro", "erro", "erro"
            objeto = "erro"

        return linha, objeto
