# Questão 3: Desenvolva um programa que pergunte ao usuário o dia da semana (número de 1 a 7) e exiba o nome do dia correspondente.

dia = int(input('Escolha um dia da semana:'))


match dia:
    case 1:
        print('Hoje é Domingo!')
    case 2:
        print('Hoje é Segunda!')
    case 3:
        print('Hoje é Terça!')
    case 4:
        print('Hoje é Quarta!')
    case 5:
        print('Hoje é Quinta!')
    case 6:
        print('Hoje é Sexta!')
    case 7:
        print('Hoje é Sábado!')
    case _:
        print('Inválido')










