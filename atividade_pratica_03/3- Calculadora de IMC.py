'''
    Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
    O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
    calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.


    < 18.5: classificacao = "Abaixo do peso" 

    < 25: classificacao = "Peso normal"

    < 30: classificacao = "Sobrepeso"

    Para os demais cenários: classificacao = "Obeso"
'''

# Entrada com peso e altura
peso=float(input("Digite o peso: "))
altura=float(input("Digite a altura: "))

# Calcular IMC
imc = peso/(altura**2)

# < 18.5 ABAIXO DO PESO
if imc <= 18.5:
    print(f"{imc}kg - Abaixo do peso")

# < 25 NORMAL
elif imc > 18.5 and imc <= 25:
    print(f"{imc}kg - Normal")

# < 30 PESO
elif imc >= 25 and imc < 30:
    print(f"{imc}kg - Acima do peso")

# > 30 OBESO
elif imc > 30:
    print(f"{imc}kg - Obeso")