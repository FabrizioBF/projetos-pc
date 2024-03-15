""""
16.Escreva um programa que receba duas notas (uma nota para a prova1 e a outra para a prova2). Depois calcule
a média aritmética simples dessas notas e verifique se o estudante é aprovado ou reprovado.
"""
# Lê as notas das duas provas
nota_prova1 = float(input("Digite a nota da primeira prova: "))
nota_prova2 = float(input("Digite a nota da segunda prova: "))

# Calcula a média aritmética simples
media = (nota_prova1 + nota_prova2) / 2

# Verifica se o aluno foi aprovado ou reprovado
if media >= 6:
    print("O aluno foi aprovado. Média:", media)
else:
    print("O aluno foi reprovado. Média:", media)
