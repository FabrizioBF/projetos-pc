""""
26.Escreva um programa que leia dois números inteiros e verifica se o primeiro número é divisível pelo segundo.
"""

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 % num2 == 0:
    print("O primeiro número é divisível pelo segundo.")
else:
    print("O primeiro número não é divisível pelo segundo.")
