def idade_em_dias(ano_nascimento: int) -> int:

    ano_atual = 2025  # Pode ser alterado ou obtido automaticamente se preferir
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365
    return idade_dias