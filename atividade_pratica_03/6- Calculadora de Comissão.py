'''
    Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas
    efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão
    sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais. 

    Entrada: O arquivo de entrada contém um texto (primeiro nome do vendedor) e 2 valores de
    dupla precisão (double) com duas casas decimais, representando o salário fixo do vendedor e
    montante total das vendas efetuadas por este vendedor, respectivamente. 

    Saída: Imprima o total que o funcionário deverá receber, conforme exemplo fornecido.
'''

# 1470.00

nome_funcionario= input("Nome do funcionário: ")
salario_fixo= round(float(input("Salario fixo: ")),2)
total_vendas= round(float(input("Total em vendas: ")),2)
percentual = (total_vendas * 15) / 100

print(f"salario_fixo: + Percencentual (R$ {percentual}): R$ {salario_fixo + percentual} ")