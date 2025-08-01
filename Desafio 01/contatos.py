contatos = []

def adicionar_contato(contato, contatos):
    contato = {'nome': contato['nome'], 'telefone': contato['telefone'], 'email': contato['email'], 'favorito': False}
    contatos.append(contato)
    print(f"\nContato {contato['nome']} adicionado com sucesso!")

def listar_contatos(contatos):
    print("\nLista de contatos:")
    for i, contato in enumerate(contatos, start=1):
        favorito = '★' if contato['favorito'] else ' '
        print(f"{i}.{contato['nome']} {favorito} \n  {contato['telefone']} \n  {contato['email']}")

def editar_contato(i, contatos, contato_editado): 
    contato_editado = {'nome': contato_editado['novo_nome'], 'telefone': contato_editado['novo_telefone'], 'email': contato_editado['novo_email']}
    i_ajustado = i - 1
    if 0 <= i_ajustado < len(contatos):
        contatos[i_ajustado]['nome'] = contato_editado['nome'] 
        contatos[i_ajustado]['telefone'] = contato_editado['telefone']
        contatos[i_ajustado]['email'] = contato_editado['email']
        print(f"Contato {contatos[i_ajustado]['nome']} editado com sucesso!")
    else:
        print("O contato de número %s não foi encontrado." % i)

def favoritar_contato(i, contatos):
    i_ajustado = i - 1
    if 0 <= i_ajustado < len(contatos):
        contatos[i_ajustado]['favorito'] = True
        print(f"\nContato {contatos[i_ajustado]['nome']} favoritado com sucesso!\n")
    else:
        print("O contato de número %s não foi encontrado.\n" % i)
        
def listar_favoritos(contatos):
    print("\nLista de favoritos:")
    for contato in contatos:
        if contato['favorito']:
            print(f" {contato['nome']} \n {contato['telefone']} \n {contato['email']}\n")
        
def excluir_contato(i, contatos):
    i_ajustado = i - 1
    if 0 <= i_ajustado < len(contatos):
        contato_excluido = contatos.pop(i_ajustado)
        print(f"\nContato {contato_excluido['nome']} excluído com sucesso!\n")
    else:
        print("O contato de número %s não foi encontrado.\n" % i)

while True:
    print("\nAgenda de contatos:")
    print("1. Adicionar contato")
    print("2. Listar contatos")
    print("3. Editar contato")
    print("4. Favoritar contato")
    print("5. Contatos favoritos")
    print("6. Excluir contato")
    print("7. Sair\n")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("\nDigite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        adicionar_contato({'nome': nome, 'telefone': telefone, 'email': email}, contatos)
        pass

    elif opcao == '2':
        listar_contatos(contatos)
        pass
    elif opcao == '3': 
        listar_contatos(contatos)
        i = int(input("Digite o número do contato que deseja editar: "))
        i_ajustado = i - 1
        if 0 <= i_ajustado < len(contatos):
            print('Para manter os dados já existentes, deixe o campo em branco.')
            novo_nome = input("Digite o novo nome do contato: ")
            if novo_nome == '':
                novo_nome = contatos[i_ajustado]['nome']
            novo_telefone = input("Digite o novo telefone do contato: ")
            if novo_telefone == '':
                novo_telefone = contatos[i_ajustado]['telefone']
            novo_email = input("Digite o novo email do contato: ")
            if novo_email == '':
                novo_email = contatos[i_ajustado]['email']
            editar_contato(i, contatos, {'novo_nome': novo_nome, 'novo_telefone': novo_telefone, 'novo_email': novo_email})
        else:
            print("O contato de número %s não foi encontrado." % i)
    elif opcao == '4':
        listar_contatos(contatos)
        i = int(input("Digite o número do contato que deseja favoritar: "))
        favoritar_contato(i, contatos)
        pass
    elif opcao == '5':
        listar_favoritos(contatos)
        pass
    elif opcao == '6': 
        listar_contatos(contatos)
        i = int(input("Digite o número do contato que deseja excluir: "))
        excluir_contato(i, contatos)
    elif opcao == '7':
        print('Saindo do gerenciador de contatos...')
        break
    else:      
        print('Opção inválida. Tente novamente.')
        