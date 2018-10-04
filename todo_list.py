#módulo pra limpar console e modulo para fechar o programa
import sys
import os
clear = lambda: os.system('cls')



#Iniciando lista de tarefas vazia
listTask = []

#Dicionário de usuario
listUser = {

}

#Função de inicializacao
def main():
    print("-"*25+"!Trello"+"-"*26+"\n")


    print("Digite:\n")
    escolha = input("(1: Cadastrar) (2:Entrar) (3:Sair)\n")
    if escolha == "1":
        clear()
        cadastrar()
    elif escolha == "2":
        clear()
        login()
    elif escolha == "3":
        sys.exit()


#Função de login
def login():
    print("LOGIN\n")

    print("Digite:\n")

    escolha = input("(1: Logar) (2: Voltar) (3:Sair)\n")
    if escolha == "1":
        print("Informe os dados:\n")

        user = input("Digite seu usuario: \n")
        senha = input("Digite sua senha: \n")

        if user == "" and senha == "":
            print("Dados invalidos, tente novamente.\n")
            login()
        elif user == listUser["user"] and senha == listUser["pass"]:
            clear()
            showTask()
        else:
            clear()
            print("Dados invalidos, tente novamente.\n")
            login()
    elif escolha == "2":
        clear()
        main()
    elif escolha == "3":
        sys.exit()


#Função de cadastro
def cadastrar():
    print("Cadastro no Todo\n")

    print("Informe os dados:\n")

    user = input("Digite seu usuario de login: \n")
    listUser["user"] = user
    senha = input("Digite sua senha de login: \n")
    listUser["pass"] = senha

    confir = input("Deseja confirmar seus dados? (1:SIM) (2:NÂO)\n")
    if confir == "1" or confir == "sim":
        main()
    else:
        cadastrar()

#Funcao Menu principal
def menu():
    print("MENU:\n")
    play = True
    while play == True:
        op = input("(1:Adicionar) (2:Remover) (3:Editar) (4:sair)\n")
        if op == "1":
            clear()
            addTasks()
        elif op == "2":
            clear()
            rmvTasks()
        elif op == "3":
            clear()
            editTask()        
        elif op == "4":                
            print("Bye")
            clear()
            login()
        else:
            print("Opção inválida")
            menu()
        

#Funcao para menu de edição das tarefas
def menuEdicao():
    op = input("(1:Cancelar) (2:Editar outro)\n")
    if(op=="1"):
        clear()
        showTask()
    elif(op=="2"):
        editTask()
    else:
        print("Opção inválida")

#Funcao para adicionar tarefa
def addTasks():
    print("Adicionando Tarefas...\n")
    task = input("Digite uma tarefa: ")
    listTask.append(task)

    ask = input("Deseja adicionar outra tarefa? (1:Y) (2:N)\n")
    if ask == "1" or ask =="y":       
        addTasks()
        
    elif ask == "2" or ask=="n":
        clear()
        showTask()
    else:
        print("Opção inválida")
        addTasks()

#Funcao para remover tarefa
def rmvTasks():
    print("Removendo Tarefa...\n")
    task = input("Digite a tarefa que deseja remover: ")
    if (task in listTask):
        listTask.remove(task)       
        clear()
        showTask()
    else:
        print("tarefa não existe, tente novamente")
        rmvTasks()

#Funcao para editar tarefa
def editTask():
    print("Editando Tarefa...\n")
    task = input("Digite a tarefa que deseja editar: ")    
    if(task in listTask):
        taskEdit = input("Tarefa: " + task +"\nDigite a nova versão: ")
        indexItem = listTask.index(task)
        listTask.remove(task)
        listTask.insert(indexItem, taskEdit)
        menuEdicao()
    else:
        print("Tarefa não existe, tente novamente")
        editTask()


#Funcao para listar as tarefas
def showTask():
    print("="*25 + "Bem Vindo ao !Trello" + "="*26)
    print("\nLista de Tarefas:\n")
    for showlist in listTask:
        print(showlist)
    print()
    print("=" * 71)
    menu()



# inicializacao do programa chamando a funcao main()
main()
