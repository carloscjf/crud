def mostrar_menu():
    print("CRUD".center(20))
    print("1. Criar usuário")
    print("2. Listar Usuários")
    print("3. Atualizar Usuário")
    print("4. Deletar Usuário")
    print("5. Sair")

usuarios = []

def criar_usuario(nome, idade, senha):
    usuario = {"nome": nome, "idade": idade, "senha": senha}
    usuarios.append(usuario)
    print("\nUsuário criado com sucesso!")

def listar_usuarios():
    if not usuarios:
        print("\nNenhum usuário cadastrado.")
    else:
        print("Lista de usuários:")
        for i, usuario in enumerate(usuarios):
            print(f"Índice: {i} | Nome: {usuario['nome']} | Idade: {usuario['idade']}")

def atualizar_usuario(indice, nome_novo, idade_nova, senha_nova):
    if 0 <= indice < len(usuarios):
        usuarios[indice]["nome"] = nome_novo
        usuarios[indice]["idade"] = idade_nova
        usuarios[indice]["senha"] = senha_nova
        print("\nUsuário atualizado com sucesso!")
    else: 
        print("znÍndice inválido!")
      
def excluir_usuario(indice):
    if 0 <= indice < len(usuarios):
        usuarios.pop(indice)
        print("Usuário deletado com sucesso!")
    else:
        print("Índice inválido!")

# Mostra o menu uma vez no início
mostrar_menu()

while True:
    opcao = input("\nSelecione uma opção (1-5): ")

    if opcao == '1':
        nome = input("Digite seu nome: ")
        idade = input("Digite sua idade: ")
        senha = input("Digite sua senha: ")
        criar_usuario(nome, idade, senha)
        
    elif opcao == '2':
        listar_usuarios()
        
    elif opcao == '3':
        listar_usuarios()
        if usuarios:
            try:
                indice = int(input("znDigite o índice do usuário que deseja atualizar: "))
                nome_novo = input("Digite o novo nome: ")
                idade_nova = input("Digite a nova idade: ")
                senha_nova = input("Digite a nova senha: ")
                atualizar_usuario(indice, nome_novo, idade_nova, senha_nova)
            except ValueError:
                print("Digite um número válido.")
                
    elif opcao == '4':
        listar_usuarios()
        if usuarios:
            try:
                indice = int(input("Digite o índice do usuário que deseja excluir: "))
                excluir_usuario(indice)
            except ValueError:
                print("Digite um número válido.")
                
    elif opcao == '5':
        print("fim.")
        break
        
    else:
        print("Opção inválida! Digite um número de 1 a 5.")
