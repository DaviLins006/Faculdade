# questao 65: Escreva um programa que solicite ao usuário uma lista de 5 números e exiba o maior e o menor número dessa lista.

numeros = []
for i in range(5):
    num = float(input("Digite um número: "))
    numeros.append(num)

print("Maior número:", max(numeros))
print("Menor número:", min(numeros))




































