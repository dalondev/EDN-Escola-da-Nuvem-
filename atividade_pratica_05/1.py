def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    """
    Calcula o valor da gorjeta com base no valor total da conta e na porcentagem desejada.
    """
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta
