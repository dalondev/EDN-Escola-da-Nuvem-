'''
    Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

    Nota 1: 7.5
    Nota 2: 8.0
    Nota 3: 6.5

    O programa deve calcular a média e exibir todas as notas e o resultado final, 
    arredondando para duas casas decimais.
'''

notas_validadas = 0
qtd_notas = 0
adicionar_nota = True
repetir = 1
while repetir:
    validar_nota = input("Adicione uma nota: ")

    # Validar e adicionar notas
    try:
        validar_nota = float(validar_nota)
        notas_validadas = notas_validadas + validar_nota
        qtd_notas+=1
        print(f"Valor de qtd_notas: {qtd_notas}")
    except ValueError:
        print("Valor invalido! Ditite um numero valido")


    # Repetir Loop "1" ou Não Repetir "0"
    repetir = input("Para adicionar outra nota digite '1' ou 0 para apresentar o resumo: ")
    if repetir == "1" or repetir == 1:
        repetir=1
    else:
        print("A média das notas é: ", notas_validadas/qtd_notas)
        repetir=0
    