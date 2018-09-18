listTask = []

listUser = {
    "user": "teste",
    "pass": "123"
}

def main():
    print("---Bem vindo ao todo list---\n")


    print("Digite:\n")
    escolha = input("(1: Cadastrar) (2:Entrar) (3:Sair)")
    if escolha == "1":
        cadastrar()
    elif escolha == "2":
        login()
    else:
        pass

def login():
    print("LOGIN\n")

    print("Informe os dados:\n")

    user = input("Digite seu usuario: \n")
    senha = input("Digite sua senha: \n")

    if user == listUser["user"] and senha == listUser["pass"]:
        menu()
    else:
        print("Dados invalidos, tente novamente.")
        login()


def cadastrar():
    print("Cadastro no Todo\n")

    print("Informe os dados:\n")

    user = input("Digite seu usuario de login: \n")
    listUser["usuario"] = user
    senha = input("Digite sua senha de login: \n")
    listUser["senha"] = senha

    confir = input("Deseja confirmar seus dados? (1:SIM) (2:NÂO)\n")
    if confir == "1":
        main()
    else:
        cadastrar()

def menu():
    print("MENU:\n")
    play = True
    while play == True:
        op = input("Menu: (1:add) (2:remove) (3:show list) (4:sair)\n")
        if op == "1":
            addTasks()

        elif op == "2":
            rmvTasks()
        elif op == "3":
            showTask()
        else:
                # play = False
            print("Bye")
        break

def addTasks():
    task = input("Digite uma tarefa: ")
    listTask.append(task)

    ask = input("Deseja adicionar outra tarefa? (1:Y) (2:N)\n")
    if ask == "1":
        addTasks()
    else:
        menu()


def rmvTasks():
    task = input("Digite a tarefa que deseja remover: ")

    if (task in listTask):
        listTask.remove(task)
        menu()
    else:
        print("tarefa não existe, tente novamente")
        rmvTasks()


def showTask():
    print("Lista de Tarefas:\n")
    for showlist in listTask:
        print(showlist)
    menu()




main()