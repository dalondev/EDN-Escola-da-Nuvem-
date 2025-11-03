def verificar_senha():
    while True:
        senha = input("Digite uma senha (ou 'sair' para encerrar): ")

        if senha.lower() == "sair":
            print("Encerrando o programa.")
            break

        # Verifica tamanho e presença de número
        if len(senha) >= 8 and any(ch.isdigit() for ch in senha):
            print("Senha forte!")
            break
        else:
            print("Senha fraca. Tente novamente.\n")

verificar_senha()
