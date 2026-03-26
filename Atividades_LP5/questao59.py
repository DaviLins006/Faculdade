# Questao 59: Escreva um programa que solicite ao usuário para digitar dois números e verifique se o primeiro é maior que o segundo. Continue pedindo números até que o primeiro número seja maior que o segundo.


while True:
    numero1 = int(input('Digite o primeiro número: '))
    numero2 = int(input('Digite o segundo número: '))

    if numero1 > numero2:
        print(f'{numero1} é maior que {numero2}.')
        break
    else:
        print(f'{numero1} não é maior que {numero2}. Seu Zé ruela.')























































