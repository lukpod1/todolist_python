import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


listTask = []


def addTasks():
    task = input("Digite uma tarefa: ")
    listTask.append(task)
    cls()


def rmvTasks():
    task = input("Digite a tarefa que deseja remover: ")
    listTask.remove(task)
    cls()


def showTask():
    print(listTask)


print("---Bem vindo ao todo list---\n")

play = True
while play == True:
    op = input("Menu: (1:add) (2:remove) (3:show list) (4:sair)\n")

    if op == "1":
        addTasks()
        ask = input("Deseja sair? (1:Y) (2:N)\n")
        cls()
        if ask == "1":
            play = False
        else:
            play = True
    elif op == "2":
        rmvTasks()
    elif op == "3":
        showTask()
    else:
        print("Bye")
        play = False
