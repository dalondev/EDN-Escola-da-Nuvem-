'''
    Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 

    O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
'''

# Conversões Celsius
def celcius_to_fahrenheit(c):
    fahrenheit = (c * 9/5) + 32
    return print(round(fahrenheit,1))
def celcius_to_kelvin(c):
    kelvin = c - 273.15
    return print(kelvin)

# Converões Fahrenheit
def fahrenheit_to_celcius(f):
    celsius = (f - 32) * 5/9
    return print(round(celsius,4))
def fahrenheit_to_kelvin(f):
    kelvin = ((f-32) * (5/9)) + 273.15
    return print(kelvin)


# Converões Kelvin
def kelvin_to_celcius(k):
    celcius = k - 273.15
    return print(round(celcius,2))
def kelvin_to_fahrenheit(k):
    fahrenheit = ((k - 273.15) * 9/5) + 32
    return print(round(fahrenheit,2))

tempertura = float(input("Informe a temperatura: "))
unidade_origem = input("Informa a origem: Celsius(1), Fahrenhinte(2), Kelvin(3): ")
unidade_destino = input("Informa a destino: Celsius(1), Fahrenhinte(2), Kelvin(3): ")
valores_validos = ["1","2","3"]

if unidade_origem not in valores_validos or unidade_destino not in valores_validos:
    print("Unidade invalida. Use 1, 2 ou 3")

elif unidade_origem == unidade_destino:
    print("As unidades sao iguais. Nenhuma conversao necessaria")
        
    # Celsius
elif unidade_origem == "1":
    if unidade_destino == "2":
        celcius_to_fahrenheit(tempertura)
    elif unidade_destino == "3":
        celcius_to_kelvin(tempertura)
    # Fahrenhinte
    elif unidade_origem == "2":
        if unidade_destino == "1":
            fahrenheit_to_celcius(tempertura)
        elif unidade_destino == "3":
            fahrenheit_to_kelvin(tempertura)
    # Kelvin
    elif unidade_origem == "3":
        if unidade_destino == "1":
            kelvin_to_celcius(tempertura)
        elif unidade_destino == "2":
            kelvin_to_fahrenheit(tempertura)