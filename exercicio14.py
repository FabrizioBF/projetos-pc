""""
14.Escreva um programa para verificar se um número é positivo, negativo ou zero.
"""

# Lê um número digitado pelo usuário
numero = float(input("Digite um número: "))

# Verifica se o número é positivo, negativo ou zero
if numero > 0:
    print("O número", numero, "é positivo.")
elif numero < 0:
    print("O número", numero, "é negativo.")
else:
    print("O número é zero.")
