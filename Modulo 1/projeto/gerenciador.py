tarefas = []

def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {'tarefa': nome_tarefa, 'completada': False}
    tarefas.append(tarefa)
    print(f"Tarefa '{nome_tarefa}' adicionada com sucesso!\n")

def ver_tarefas(tarefas):
    print("\nLista de tarefas:")
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✔️ " if tarefa['completada'] else " "
        nome_tarefa = tarefa['tarefa']
        print(f"{indice}. [{status}] {nome_tarefa}")

def atualizar_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
   indice_tarefa_ajustado = indice_tarefa - 1
   if 0 <= indice_tarefa_ajustado < len(tarefas): 
    tarefas[indice_tarefa_ajustado]['tarefa'] = novo_nome_tarefa
    print(f"Tarefa {indice_tarefa} atualizada para '{novo_nome_tarefa}' com sucesso!\n")
   else :
    print("A tarefa de número %s não foi encontrada. Tente novamente.\n" % indice_tarefa) 

def completar_tarefa(tarefas, indice_tarefa):
    indice_tarefa_ajustado = indice_tarefa - 1
    if 0 <= indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]['completada'] = True
        print(f"\nTarefa {indice_tarefa} foi completada com sucesso!\n")
    else:
        print("A tarefa de número %s não foi encontrada. Tente novamente.\n" % indice_tarefa)
        return
    
def deletar_tarefas_completadas(tarefas):
    for tarefa in tarefas:
        if tarefa['completada']:    # é o mesmo que if tarefa['completada'] == True: e if True:, pois está puxando as tarefas completadas que já foram setadas como True
            tarefas.remove(tarefa)
    print("\nTarefas completadas foram deletadas com sucesso!")
        

while True:
    print("\nGerenciador de tarefas:")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair\n")

    escolha = input("Escolha uma opção:")

    if escolha == '1':
        nome_tarefa = input("\nDigite o nome da tarefa que deseja adicionar: ")
        adicionar_tarefa(tarefas, nome_tarefa) 
        pass

    elif escolha == '2':
        ver_tarefas(tarefas)
        pass

    elif escolha == '3':
        ver_tarefas(tarefas)
        indice_tarefa = int(input("\nDigite o número da tarefa que deseja atualizar: "))
        novo_nome_tarefa = input("Digite o novo nome da tarefa: ")
        atualizar_tarefa(tarefas, indice_tarefa, novo_nome_tarefa)
        pass

    elif escolha == '4':
        ver_tarefas(tarefas)
        indice_tarefa = int(input("\nDigite o número da tarefa que deseja completar: "))
        completar_tarefa(tarefas, indice_tarefa)
        pass

    elif escolha == '5':
        deletar_tarefas_completadas(tarefas)
        ver_tarefas(tarefas)
        pass

    elif escolha == '6':
        print("\nSaindo do gerenciador...")
        break
    else:
        print("Opção inválida, tente novamente.")
