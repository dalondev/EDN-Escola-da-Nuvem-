import json

# Dados que vamos salvar
dados = {
    "nome": "João",
    "idade": 28,
    "cidade": "Curitiba"
}

# Escrevendo no arquivo JSON
with open("pessoa.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, indent=4)

print("Arquivo JSON criado!")

# Lendo o arquivo JSON
with open("pessoa.json", "r", encoding="utf-8") as arquivo:
    dados_lidos = json.load(arquivo)

print("=== Dados Lidos do JSON ===")
print(dados_lidos)
