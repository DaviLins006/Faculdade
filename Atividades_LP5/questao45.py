# Questao 45: Escreva um algoritmo que peça ao usuário para inserir 5 números e, ao final, exiba o maior número inserido.

n1 = int(input('Informe o primeiro numero:'))
n2 = int(input('Informe o segundo numero:'))
n3 = int(input('Informe o terceiro numero:'))
n4 = int(input('Informe o quarto numero:'))
n5 = int(input('Informe o quinto numero:'))

numeros = [n1,n2,n3,n4,n5]

maior = numeros [0]

for numero in numeros:
    if numero > maior:
        maior = numero

print('O número maio é o', maior)
       




















































