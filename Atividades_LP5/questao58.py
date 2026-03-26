# Questao 58: Desenvolva um algoritmo que solicite ao usuário uma palavra e continue pedindo outra palavra até que ele digite "sair".

while True:
    palavra = input("Digite uma palavra (Digite 'sair' para encerrar): ")
    if palavra.lower() == "sair":
        print("Você saiu.")
        break
    else:
        print(f'Você digitou: {palavra}')





















































