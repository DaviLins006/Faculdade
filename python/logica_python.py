# criando variaveis

nome = 'Davi'
sobrenome = "Araujo"
idade = 20
altura = 1.70
adulto = True

# escrevendo no console
print(nome)
print(sobrenome)
print(idade)
print(altura)
print(adulto)


# concatenando informações 
print('Meu nome é',nome)
print('Meu sobrenome é ' +  sobrenome)
print('Meu nome completo',nome,sobrenome)
print('Minha idade é {} e minha altura é {}'.format(idade,altura))

# maneira moderna (baiana) de concatenar
print(f'Meu nome é {nome} e tenho {idade} anos')


# Verificando tipos de Variavel
print(type(nome))
print(type(sobrenome))
print(type(idade))
print(type(altura))
print(type(adulto))

# Expressão Numerica

numero1 = 10
numero2 = 5

soma = numero1 + numero2 
sub = numero1 + numero2 
mult = numero1 * numero2
div = numero1 / numero2

print(f'A soma é {soma}')
print(f'A sub é {sub}')
print(f'A mult é {mult}')
print(f'A div é {div}')


expressao = numero1 + (numero2* numero2) - numero1
print(expressao)

expressao = numero1 / (numero2* numero2) + numero1
print(expressao)

expressao = numero1 / ((numero2* numero2) + numero1)
print(expressao)


# outras operações 

potencia = numero1**3
print(potencia)

div_exata = numero1//3
print(div_exata)












