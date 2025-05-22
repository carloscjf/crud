def usuario():
    nome = input("Digite o nome de Usuário: ")
    idade = input("Digite a sua idade: ")

def criarTabela():
    print("CRUD".center(10))
    print("1. Usuário")
    print("2. Listar Usuário")
    print("3. Atualizar Usuário")
    print("4. Deletar Usuário")
    print("5. Sair")
    
    while True:
        opcao = int(input("Selecione uma opção! "))
        if opcao == 1:
            usuario()

criarTabela()
