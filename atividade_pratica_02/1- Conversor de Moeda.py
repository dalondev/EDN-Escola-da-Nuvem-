'''
    Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

    Valor em reais: R$ 100.00

    Taxa do dólar: R$ 5.60

    Taxa do euro: R$ 6.60 
    O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
'''

valor = float(input("Digite um valor em REAIS: "))

print(f"Valor em Reais {round(valor,2)}")
print(f"Valor em dolar {round(valor*5.60,2)}")
print(f"Valor em euro {round(valor*6.60,2)}")