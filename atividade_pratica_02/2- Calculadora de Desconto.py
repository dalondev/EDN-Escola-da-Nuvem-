'''
    Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

    Nome do produto: "Camiseta"

    Preço original: R$ 50.00

    Porcentagem de desconto: 20% 
    O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
'''

produto = input("Digite o produto: ")
preco = float(input("Preço original: "))

comDesconto = preco - (20 / 100) * 100 

print(f"Preco com desconto: {comDesconto}")