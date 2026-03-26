# Questao 47: Crie um programa que peça ao usuário um número e exiba a tabuada desse número de 1 a 10.

numero = int(input('Digite um numero para ver a tabuada:'))
print(f'Tabuada do {numero}:')
for tabuada in range(1, 11):  
    resultado = numero * tabuada
    print(f'{numero} x {tabuada} = {resultado}')





























