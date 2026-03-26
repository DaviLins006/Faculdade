# Questao 50: Crie um programa que peça ao usuário para inserir um número e, em seguida, exiba os números de 1 até esse número, mas de forma decrescente.


numero = int(input('Digite um numero:'))
print(f'Numeros de 1 até {numero} em ordem decrescente:')

for i in range(numero, 0, -1):
    print(i, end=' ')


































