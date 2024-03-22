"""
30.Escreva um programa simples para calcular a quantidade de vogais em uma frase digitada pelo usuário.
"""

# Solicita uma frase ao usuário
frase = input("Digite uma frase: ")

# Inicializa a variável para contar as vogais
contador_vogais = 0

# Percorre cada caractere da frase
for caractere in frase:
    # Verifica se o caractere é uma vogal
    # (considerando letras maiúsculas e minúsculas)
    if caractere.lower() in "aeiou":
        contador_vogais += 1

        
# Exibe a quantidade de vogais na frase
print("Quantidade de vogais:", contador_vogais)        
