#3- Calculadora de Volume

# Crie um programa que calcule o volume de uma caixa retangular. Use as seguintes dimensões:
# Comprimento: 12 cm
# Largura: 14 cm
# Altura: 20 cm 
# O programa deve calcular o volume e exibir o resultado em cm³.

import math

comprimento = float(input("Digite o comprimento em cm: "))
largura = float(input("Digite a largura em cm: "))
altura =  float(input("Digite o altura em cm: "))

volume = comprimento * largura * altura
print(f"O volume da caixa retangular é: {volume} cm³")