#Questao 16: Desenvolva um programa que peça ao usuário um tipo de combustível (gasolina, etanol, diesel) e exiba o preço correspondente por litro


print('Gasolina')
print('Etanol')
print('Diesel')

combustivel = str(input('Escolha um tipo combustivel:'))

match combustivel:
    case 'Gasolina':
        print('O litro da Gasolina está R$ 6,46. Faz u L')
    case 'Etanol':
        print('O liro de etanol está R$ 3,27. Ta barato demais')
    case 'Diesel':
        print('O Litro de Diesel está R$ 7,35. Faz u LLLLLLLL ')
    case _:
        print('Diabo é isso doido??')



















































