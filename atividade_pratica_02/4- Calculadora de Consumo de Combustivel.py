'''
    Desenvolva um programa que calcula o consumo médio de combustível de um veículo. 
    Use os seguintes dados:

    Distância percorrida: 300 km

    Combustível gasto: 25 litros 
    O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, 
    incluindo o resultado final arredondado para duas casas decimais.
'''
km = int(input("Digite a quilometragem em números: "))
litros = int(input("Digite o combustível gasto: "))

print(f"O consumo médio da viagem foi {km/litros}")