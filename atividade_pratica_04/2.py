def registrar_notas():
    notas = []  # lista para armazenar as notas

    while True:
        entrada = input("Digite a nota (ou 'fim' para encerrar): ")

        # Se o usuário quiser encerrar
        if entrada.lower() == "fim":
            break

        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida. Digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número ou 'fim' para encerrar.")

    if len(notas) > 0:
        media = sum(notas) / len(notas)
        print(f"\nMédia da turma: {media:.1f}")
    else:
        print("\nNenhuma nota válida foi registrada.")
