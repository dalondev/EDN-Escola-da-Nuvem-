import statistics

# Lendo os tempos do arquivo de log
tempos = []

with open("logs.txt", "r") as arquivo:
    for linha in arquivo:
        if "Tempo execução:" in linha:
            # Pega só o número da linha
            valor = float(linha.split(":")[1].strip())
            tempos.append(valor)

# Calculando média e desvio padrão
media = statistics.mean(tempos)
desvio = statistics.stdev(tempos)

print(f"Média dos tempos: {media:.2f}")
print(f"Desvio padrão: {desvio:.2f}")
