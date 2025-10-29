"""
    4- Calculadora de Preço Total

    Desenvolva um programa que calcule o preço total de uma compra. Use as seguintes informações:

    Nome do produto: "Cadeira Infantil"
    Preço unitário: R$ 12.40
    Quantidade: 3 
    O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.
"""

produto = input("Digite o nome do produto: ")
valor_unidade = float(input("Valor por unidade: "))
qtd = float(input("Quantidade: "))
total = valor_unidade*qtd
print("")
print("")
print(qtd," ", produto," por ",total)

