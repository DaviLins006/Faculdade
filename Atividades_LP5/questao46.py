#Questao 46: Desenvolva um programa que pergunte ao usuário para inserir 10 números e, ao final, exiba a média dos números inseridos.

n1 = int(input('Informe o primeiro numero:'))
n2 = int(input('Informe o segundo numero:'))
n3 = int(input('Informe o terceiro numero:'))
n4 = int(input('Informe o quarto numero:'))
n5 = int(input('Informe o quinto numero:'))
n6 = int(input('Informe o sexto numero:'))
n7 = int(input('Informe o setimo numero:'))
n8 = int(input('Informe o oitavo numero:'))
n9 = int(input('Informe o nono numero:'))
n10 = int(input('Informe o decimo numero: '))



numeros = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]

soma = 0
for numero in numeros:
    soma += numero

media = soma / 10

print("A média dos numeros é:", media)








































