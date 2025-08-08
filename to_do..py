
lista_tarefas = []
tarefas_concluidas = []


while True:
    print("""

======================================
         GERENCIADOR DE TAREFAS 
======================================
          
1.  Adicionar uma nova tarefa   
2.  Listar todas as tarefas pendentes    
3.  Remover uma tarefa   
4.  Marcar uma tarefa como concluída
5.  Listar tarefas concluídas     
6.  Sair do programa
          
======================================
""")

    escolha = input(("Qual opção você deseja escolher: "))

    if escolha == '1':
        tarefa = input(("Qual tarefa você deseja realizar: "))
        lista_tarefas.append(tarefa)

        
    elif escolha == '2':
        for indice, escolha in enumerate(lista_tarefas):
            print(f"{indice + 1}. {escolha}")


    elif escolha == '3':
        print(lista_tarefas)
        remov = input(("Qual item você deseja remover: "))
        print(f"{remov} Removido de sua lista de tarefas! ")
        lista_tarefas.remove(remov)
    
    elif escolha == '4':
        print(lista_tarefas)
        concluir = input(("Qual tarefa você deseja concluir: "))
        lista_tarefas.remove(concluir)
        tarefas_concluidas.append(concluir)
        
    elif escolha == '5':
        print(tarefas_concluidas)

    elif escolha == '6':
        break

    else:
        print("Essa opção é invalida")




