def validarNumero(texto, tentativas=3):
    """Valida se o valor digitado é um número (int ou float)."""
    for _ in range(tentativas):
        valor = input(texto)
        try:
            return float(valor)
        except ValueError:
            print("Valor inválido. Digite um número válido.")
    print("Número máximo de tentativas atingido.")
    return None

def validarOperador(tentativas=3):
    """Valida se o operador é um dos permitidos."""
    operadores_validos = {"+", "-", "*", "/", "**", "%"}
    for _ in range(tentativas):
        op = input("Digite o operador (+, -, *, /, **, %): ")
        if op in operadores_validos:
            return op
        print("Operador inválido! Tente novamente.")
    print("Número máximo de tentativas atingido.")
    return None

def validarCalculo():
    """Executa o cálculo com limite de tentativas."""
    n1 = validarNumero("Digite o primeiro número: ")
    if n1 is None: return

    op = validarOperador()
    if op is None: return

    n2 = validarNumero("Digite o segundo número: ")
    if n2 is None: return

    if op == "/" and n2 == 0:
        print(" Operação inválida! Você não pode dividir por zero.")
        return

    resultado = eval(f"{n1}{op}{n2}")
    print(f" Resultado de {n1} {op} {n2} = {resultado}")

# --- Executar ---
validarCalculo()
