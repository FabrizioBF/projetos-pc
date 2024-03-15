""""
17.Escreva um programa para ler três números inteiros. Depois some os três números e verifique se a soma é divisível por 5.
"""
# Lê os três números
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

# Calcula a soma dos três números
soma = num1 + num2 + num3

# Verifica se a soma é divisível por 5
if soma % 5 == 0:
    print("A soma dos números é divisível por 5.")
else:
    print("A soma dos números não é divisível por 5.")
