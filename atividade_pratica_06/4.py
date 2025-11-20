import requests

def consultar_moeda(codigo):
    codigo = codigo.upper()
    url = f"https://economia.awesomeapi.com.br/json/last/{codigo}-BRL"
    resposta = requests.get(url)

    if resposta.status_code != 200:
        print("Erro ao consultar cotação.")
        return

    dados = resposta.json()

    if len(dados) == 0:
        print("Moeda não encontrada.")
        return

    chave = list(dados.keys())[0]   # Ex.: USDBRL
    info = dados[chave]

    print("\n=== Cotação Atual ===")
    print("Moeda:", codigo)
    print("Valor atual (bid):   R$", info["bid"])
    print("Valor mínimo (low):  R$", info["low"])
    print("Valor máximo (high): R$", info["high"])
    print("Data e hora:", info["create_date"])

# Programa principal
moeda = input("Digite o código da moeda (USD, EUR, GBP...): ")
consultar_moeda(moeda)
