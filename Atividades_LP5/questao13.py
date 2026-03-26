# Questão 13: Crie um algoritmo que solicite ao usuário um mês do ano (1 a 12) e exiba a estação do ano correspondente.

mes = int(input('Informe o mês em que estamos:'))

if mes == 1 or mes == 2 or mes == 12:
    print('Estamos no Verão. A estação mais quente!!')
elif mes == 3 or mes == 4 or mes == 5:
    print('Estamos no Outono. A estação de transição.')
elif mes == 6 or mes == 7 or mes == 8:
    print('Estamos no Inverno. A estação mais fria!!')  
elif mes == 9 or mes == 10 or mes == 11:
    print('Estamos na Primavera. A estação de florescência!!')
else:
    ('Por favor informe um numero de um a 12.')







































