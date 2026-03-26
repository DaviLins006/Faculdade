# Questao 42: Escreva um algoritmo que solicite ao usuário 5 números inteiros e calcule a soma desses números.

numero1 = int(input('Informe o primeiro numero:'))
numero2 = int(input('Informe o segundo numero:'))
numero3 = int(input('Informe o terceiro numero:'))
numero4 = int(input('Informe o quarto numero:'))
numero5 = int(input('Informe o quinto numero:'))


numeros = [numero1,numero2,numero3,numero4,numero5]

soma = 0
for n in numeros:
    soma += n

print("Soma:", soma)









































