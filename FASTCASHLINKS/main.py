# Bibliotecas
import csv
import chardet # Biblioteca que esta compativel com mac para nao dar erro em arquivos (uft8)
from readcashlink import montar_payload
from writecashlink import enviar_requisicao
from headerprod import obter_header # (Prod)
# from header import obter_header # (Dev)

# import json

header = obter_header()

# Detecta a codificação do arquivo de entrada
with open("cashlinks.csv", "rb") as f:
    encoding = chardet.detect(f.read())["encoding"]

# Abre o arquivo de entrada com a codificação correta
with open("cashlinks.csv", mode="r", newline="", encoding=encoding) as arquivo_entrada:
    with open("cashlinksaida.csv", mode="w", newline="", encoding='utf8') as arquivo_saida:
        # Criando leitor e escritor CSV
        leitor = csv.reader(arquivo_entrada, delimiter=";")
        escritor = csv.writer(arquivo_saida)

        # Adiciona o cabeçalho no arquivo cashlinksaida.csv
        escritor.writerow(
            ["TID", "Valor", "Nome", "Email", "Documento", "Celular", "Descrição", "PaymentMethod", "SubPaymentMethod",
             "Data de vencimento", "Link Cashlink"])

        # Pula a primeira linha que são os nomes dos campos do cashlink.csv
        next(leitor)

        # Para cada linha do arquivo de entrada
        for linha in leitor:
            # Monta o payload a partir da linha da planilha
            print(linha)
            campos = linha
            payload = montar_payload(campos)

            # Envia a requisição à API e obtém a resposta
            resp = enviar_requisicao(payload)

            # Concatena os elementos da lista com ';' como separador, e deixa com uma distancia de "; "
            resultado = "; ".join(str(x) for x in resp[0]) + "; " + resp[1]

            # Escreve o resultado no arquivo de saída
            escritor.writerow([resultado])
