# QUESTÃO 6: 6. Desenvolva um programa que pergunte ao usuário uma operação matemática (+, -, *, /) e dois números, e realize a operação escolhida.

print('soma')
print('subtração')
print('multiplicação')
print('divisão')



operacao = input(
    "Escolha uma operação e digite:")

numero1 = int(input("Digite o primeiro número:"))
numero2 = int(input("Digite o segundo número:"))


if operacao == "soma":
    resultado = numero1 + numero2
    print(f'O resultado é:' ,resultado)
elif operacao == "subtração":
    resultado = numero1 - numero2
    print(f'O resultado é:' ,resultado)
elif operacao == "multiplicação":
    resultado = numero1 * numero2
    print(f'O resultado é:' ,resultado)
elif operacao == "divisão":
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f'O resultado é:' ,resultado)
    else:
        print("Opção inválida")


















