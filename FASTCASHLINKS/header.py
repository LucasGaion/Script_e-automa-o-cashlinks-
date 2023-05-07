# Cabeçalhos da requisição HTTP
import requests

url = "https://dev.meu.cash/apiv10Sandbox/transaction/in/deposit"
headers = {
        "Accept": "application/json",
        "Authorization": "APIKEY ca5a4b92-70ab-44ae-8d97-21b3368303eb",
        "Content-Type": "application/json"
}

# Retorna o headers contendo authorization e content-type
def obter_header():
 return headers

# Retorna a URl com o Cabeçalhos e a requisição HTTP
def obter_url_api():
 return url

# Resposta da URl com o Cabeçalhos e a requisição HTTP e o handers
resposta = requests.post(url,headers=headers)

# Confere o codigo de status que esta a API
print("Código de status:", resposta.status_code)
