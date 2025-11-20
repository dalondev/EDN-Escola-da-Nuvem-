import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)

    if resposta.status_code != 200:
        print("Erro ao consultar CEP.")
        return

    dados = resposta.json()

    if "erro" in dados:
        print("CEP inválido!")
        return

    print("\n=== Consulta de CEP ===")
    print("Logradouro:", dados.get("logradouro", "Não informado"))
    print("Bairro     :", dados.get("bairro", "Não informado"))
    print("Cidade     :", dados.get("localidade", "Não informado"))
    print("Estado     :", dados.get("uf", "Não informado"))

# Programa principal
cep = input("Digite o CEP (somente números): ")
consultar_cep(cep)
