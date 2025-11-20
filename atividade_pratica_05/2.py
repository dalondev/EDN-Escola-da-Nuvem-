def eh_palindromo(texto: str) -> str:

    texto_limpo = ""

    # Mantém apenas letras e números
    for caractere in texto:
        if caractere.isalnum():
            texto_limpo += caractere.lower()

    # Verifica se é igual ao inverso
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"