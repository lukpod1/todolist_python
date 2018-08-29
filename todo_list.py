
listTask = []

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

    if(task in listTask):
        listTask.remove(task)
    else:
        print("tarefa não existe, tente novamente")
        rmvTasks()


def showTask():
    for showlist in listTask:
        print(showlist)

def menu():

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
            print("Bye")
            play = False
            break

print("---Bem vindo ao todo list---\n")
menu()

