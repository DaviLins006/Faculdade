# Questao 52: Desenvolva um algoritmo que solicite ao usuário uma senha e continue pedindo até que a senha correta "1234" seja digitada.


senha_correta = "1234"

while True:
    senha_usuario = input("Digite a senha: ")
    if senha_usuario == senha_correta:
        print("Senha correta! Acesso concedido.")
        break
    else:
        print("Senha incorreta. Tente novamente.")













































