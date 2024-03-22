"""
33.Escreva um programa que leia uma frase digitada pelo usuário, depois troque a ocorrência da letra “a” pela letra “e”
e depois apresente a frase nova.
"""

# Solicita ao usuário que digite uma frase
frase = input("Digite uma frase: ")

# Substitui todas as ocorrências da letra "a" por "e" na frase
frase_substituida = frase.replace("a", "e")

# Exibe a frase com as substituições
print("Frase com as substituições:", frase_substituida)
