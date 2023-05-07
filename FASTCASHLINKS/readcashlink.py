def montar_payload(coluna):
    # Monta o objeto JSON (payload) a partir da linha da planilha
    payload = {
        "Tid": coluna[0],
        "Pid": 1006,
        "ProdId": 5492,
        "Custom": "CREDITO FRUBANA",
        "Amount": coluna[1].replace(',', '.'),  # erro corrigido de pegar numero com casas decimais
        "Description": coluna[6],
        "PaymentMethod": 5,
        "SubPaymentMethod": 24,
        "Name": coluna[2],
        "Email": coluna[3],
        "MobilePhone": coluna[5],
        "Document": coluna[4],
        "DueDate": coluna[7],
        "CashlinkType": 1,
        "Metadata": {
            "Key": "cashlinkType",
            "Value": "loan"
        }
    }



    return payload
