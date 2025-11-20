import csv

with open("pessoas.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)

    print("=== Dados do CSV ===")
    for linha in leitor:
        print(linha)
