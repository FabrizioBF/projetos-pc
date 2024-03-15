""""
15.Escreva um programa para receber duas notas, uma para a prova 1 e a outra para a prova 2.
Então verifique se o estudante foi aprovado ou reprovado em cada uma delas.
"""
# Lê as notas das duas provas
nota_prova1 = float(input("Digite a nota da primeira prova: "))
nota_prova2 = float(input("Digite a nota da segunda prova: "))

# Verifica se o aluno foi aprovado ou reprovado em cada prova
if nota_prova1 >= 6:
    print("O aluno foi aprovado na primeira prova.")
else:
    print("O aluno foi reprovado na primeira prova.")

if nota_prova2 >= 6:
    print("O aluno foi aprovado na segunda prova.")
else:
    print("O aluno foi reprovado na segunda prova.")
