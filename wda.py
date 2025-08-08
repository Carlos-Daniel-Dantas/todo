while True:
    print("""
_______________________________________
|      GERENCIADOR DE TAREFAS          |
|______________________________________|
|   1. Ler lista                       |
|   2. Adicionar item na lista         |
|   3. Remover item da lista           |
|   4. Marcar item como concluído      |
|   5. Reiniciar lista (remove tudo)   |
|______________________________________|
      """)

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        ab = open("lista.txt", "r")
        print(ab.read())

    elif opcao == 2:
        aa = (input("Adiciona algo na lista: "))
        print(f"{aa} Adicionado a lista!")
        f = open("lista.txt", "a")
        f.write(f"{aa} \n")
        f.close()

    elif opcao == 3:
        ler = open("lista.txt", "r")
        print(f"{ler.read()}")
        remov = input("Qual item você deseja remover: ")
        linha_remover = ler.readlines()
        ler.close()
        escrever_tarefas = open("lista.txt", "w")
        escrever_tarefas.writelines(remov)
        print(f"{remov} Removido")


    elif opcao == 4:
        concluir = input("Qual item você deseja concluir")

    elif opcao == 5:
        ler = open("lista.txt", "r")
        print(f"{ler.read()}")
        remov = input("Qual item você deseja remover: ")
        linha_remover = ler.readlines()
        ler.close()
        escrever_tarefas = open("lista.txt", "w")
        escrever_tarefas.writelines(remov)
        print(f"{remov} Removido")

    elif opcao == 6:
        break
    
    else:
        print("Opção Invalida! escolha apenas alguma das opções acima ")
