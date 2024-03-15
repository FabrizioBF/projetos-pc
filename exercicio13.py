""""
13.Escreva um programa para verificar se um número é par ou ímpar.
"""

# Lê um número digitado pelo usuário
numero = int(input("Digite um número: "))

# Verifica se o número é par ou ímpar
if numero % 2 == 0:
    print("O número", numero, "é par.")
else:
    print("O número", numero, "é ímpar.")
