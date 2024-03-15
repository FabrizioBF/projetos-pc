"""
18. Escreva um programa para ler três números inteiros. Depois some os três números e verifique se a soma é positiva,
negativa ou igual a zero.
"""

# Solicita três números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Calcula a soma dos três números
soma = num1 + num2 + num3

# Verifica se a soma é positiva, negativa ou igual a zero
if soma > 0:
    print("A soma dos números é positiva.")
elif soma < 0:
    print("A soma dos números é negativa.")
else:
    print("A soma dos números é igual a zero.")
