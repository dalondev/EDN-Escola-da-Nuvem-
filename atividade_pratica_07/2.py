import csv

# Dados que vamos escrever no CSV
pessoas = [
    ["Nome", "Idade", "Cidade"],
    ["Ana", 25, "São Paulo"],
    ["Carlos", 30, "Rio de Janeiro"],
    ["Marina", 22, "Belo Horizonte"]
]

# Criando e escrevendo o arquivo CSV
with open("pessoas.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(pessoas)

print("Arquivo pessoas.csv criado com sucesso!")
