import requests

def gerar_usuario_aleatorio():
    url = "https://randomuser.me/api/"
    resposta = requests.get(url)

    if resposta.status_code != 200:
        print("Erro ao acessar API Random User.")
        return

    dados = resposta.json()
    usuario = dados["results"][0]

    nome = f"{usuario['name']['first']} {usuario['name']['last']}"
    email = usuario["email"]
    pais = usuario["location"]["country"]

    print("\n=== Usuário Aleatório ===")
    print("Nome :", nome)
    print("Email:", email)
    print("País :", pais)

# Executar
gerar_usuario_aleatorio()
