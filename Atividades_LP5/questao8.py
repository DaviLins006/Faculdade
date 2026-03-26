# Questão 8: Desenvolva um algoritmo que pergunte ao usuário o estado civil (solteiro, casado, divorciado, viúvo) e exiba uma mensagem correspondente.


estado = str(input('Qual o seu estado Civil? (Solteiro, Casado, Viúvo):'))


match estado:
    case "Solteiro":
        print('Seu estado Civil é Solteiro(a)')
    case "Casado":
        print('Seu estado Civil é Casado(a)')
    case "Viúvo":
        print('Seu estado Civil é Viúvo(a)')
    case _:
        print('Preencha algo válido')


































