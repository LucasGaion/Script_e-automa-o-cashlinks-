# Cabeçalhos da requisição HTTP
import requests

url = "https://www.fastcash.com.br/apiv10Sandbox/transaction/in/deposit"
headers = {
        "Accept": "application/json",
        "Authorization": "APIKEY 9dfc799a-9603-4d40-94b2-b7a31ef38086",
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

# Confere o codigo de status que esta a API disponivel
print("Código de status:", resposta.status_code)
