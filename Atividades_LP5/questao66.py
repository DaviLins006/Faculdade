# questao 66: escreva um algoritmo que forneça um menu para o usuário: 1-Cadastrar nome, 2- atualizar o nome, 3, excluir, 4-listar todos os cadastrados, ao final da operação deve dar uma mensagem indicando o resultado da operação e perguntando se deseja realizar
# outra operação, o seu aplicativo apenas deve encerrar quando a opção não for inserida


cadastros = []
while True:
    print("Menu:")
    print("1- cadastrar nome")
    print("2- atualizar nome")
    print("3- excluir nome")
    print("4- listar todos os cadastrados")
    print("5- sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        nome = input("Digite o nome para cadastrar: ")
        cadastros.append(nome)
        print(f"Nome '{nome}' cadastrado com sucesso!")
    elif opcao == "2":
        nome_atual = input("Digite o nome que deseja atualizar: ")
        if nome_atual in cadastros:
            nome_novo = input("Digite o novo nome: ")
            index = cadastros.index(nome_atual)
            cadastros[index] = nome_novo
            print(f"Nome '{nome_atual}' atualizado para '{nome_novo}' com sucesso!")
        else:
            print(f"Nome '{nome_atual}' não encontrado.")
    elif opcao == "3":
        nome_excluir = input("Digite o nome que deseja excluir: ")
        if nome_excluir in cadastros:
            cadastros.remove(nome_excluir)
            print(f"Nome '{nome_excluir}' excluído com sucesso!")
        else:
            print(f"Nome '{nome_excluir}' não encontrado.")
    elif opcao == "4":
        print("Nomes cadastrados:")
        for nome in cadastros:
            print(nome)
    elif opcao == "5":
        print("Encerrando o programa. Até mais!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")






























































