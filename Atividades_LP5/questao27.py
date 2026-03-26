# Questao 27: Crie um programa que solicite ao usuário três números e exiba o maior deles.

numero1 = int(input('Escolha o número 1: '))
numero2 = int(input('Escolha o número 2: '))
numero3 = int(input('Escolha o número 3: '))


if numero1 > numero2 and numero1 > numero3:
    print(f'{numero1} é o numero maior')
elif numero2 > numero1 and numero2 > numero3:
    print(f'{numero2} é o numero maior')
elif numero3 > numero1 and numero3 > numero2:
    print(f'{numero3} é o numero maior')
else:
    print('Inválido')





















































