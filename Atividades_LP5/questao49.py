# Questao 49: Desenvolva um programa que peça ao usuário para inserir 7 números e, ao final, exiba quantos desses números são maiores que 10.

n1 = int(input('Informe o primeiro numero:'))
n2 = int(input('Informe o segundo numero:'))
n3 = int(input('Informe o terceiro numero:'))
n4 = int(input('Informe o quarto numero:'))        
n5 = int(input('Informe o quinto numero:'))
n6 = int(input('Informe o sexto numero:'))
n7 = int(input('Informe o setimo numero:'))

numeros = [n1, n2, n3, n4, n5, n6, n7]

contador_maiores_que_10 = 0
for numero in numeros:     
    if numero > 10:
        contador_maiores_que_10 += 1

print("Quantidade de numeros maiores que 10:", contador_maiores_que_10) 





















