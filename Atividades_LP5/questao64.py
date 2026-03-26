# questao 64: Crie uma lista com 10 números aleatórios e exiba apenas os números que são múltiplos de 3

import random

numeros = [random.randint(1, 100) for _ in range(10)]
print("Números gerados:", numeros)

multiplos_de_3 = [n for n in numeros if n % 3 == 0]
print("Múltiplos de 3:", multiplos_de_3)









































