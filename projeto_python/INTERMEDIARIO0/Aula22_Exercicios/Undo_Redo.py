"""faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa
    listar tarefas
    opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    opção de refazer (a cada vez que chamarmos, refaz a última ação)"""


def show_op(todo_list):
    print()
    print('Tarefas: ')
    print(todo_list)
    print()


def do_undo(todo_list, redo_list):
    if not todo_list:
        print("nada a desfazer")
        return

    last_todo = todo_list.pop();
    redo_list.append(last_todo)


def do_redo(todo_list, redo_list):
    if not redo_list:
        print('nada a refazer')
        return

    last_redo = redo_list.pop();
    todo_list.append(last_redo)


def do_add(todo, todo_list):
    todo_list.append(todo)




if True:
    todo_list = []
    redo_list = []

    while True:
        todo = input("Digite uma tarefa ou undo, redo, ls, s-sair: ")

        if todo =='ls':
            show_op(todo_list)
            continue
        elif todo == 'undo':
            do_undo(todo_list, redo_list)
            continue
        elif todo =='redo':
            do_redo(todo_list, redo_list)
            continue
        elif todo == 's':
            break

        do_add(todo, todo_list)