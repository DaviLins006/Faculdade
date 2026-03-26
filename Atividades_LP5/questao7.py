# Questão 7: Escreva um programa que peça ao usuário uma nota de 0 a 10 e classifique a nota como "Baixa", "Média" ou "Alta" usando estrutura condicional if.

nota = float(input('Escreva a sua nota:'))

if nota < 5:
    print('Sua nota foi Baixa')
elif nota >= 5 and nota <= 7:
    print('Sua nota foi Media')
elif nota >= 5 and nota <= 10:
    print('Sua nota foi Alta')
else:
    print('Nota inválida. Por favor Digite sua nota de 0 a 10')



























