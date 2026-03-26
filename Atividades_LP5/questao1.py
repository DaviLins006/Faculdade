# Questão 1: Crie um programa que pergunte ao usuário um número de 1 a 3 e exiba o nome correspondente ao número (1: "um", 2: "dois", 3: "três").
 
import os

print('Número 1')
print('Número 2')
print('Número 3')

opcao = int(input('Escolha um número:'))

os.system('cls')

match opcao:
    case 1:
        print('Você escolheu número Um ;)')
    case 2:
        print('você escolheu número Dois =>')
    case 3:
        print('Você escolheu número Três =)')
    case _:
        print('Opção Inválida')    





