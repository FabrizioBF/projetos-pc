"""
19.Escreva um programa para receber a data de nascimento do usuário. Calcule a idade atual e verifique se o
usuário está apto a votar.
"""
# Solicita o ano de nascimento ao usuário
ano_nascimento = int(input("Digite o ano de nascimento: "))

# Calcula a idade atual
ano_atual = 2023
idade = ano_atual - ano_nascimento

# Verifica se a pessoa está apta a votar
if idade >= 16:
    print("Você está apto(a) a votar!")
else:
    print("Você não está apto(a) a votar.")
