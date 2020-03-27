from itertools import count

def adiciona(todo, todo_list):
    todo_list.append(todo)

def lista(todo_list):
    print()
    print('Tarefas :')
    if not todo_list:
        print('Lista vazia')
    else:
        i = 0
        for todo in todo_list:
            i += 1
            print(f'{i} : {todo}')
    print(f'Total: {len(todo_list)} tarefas \n')

def do_undo(todo_list, redo_list):
    if not todo_list:
        print('Nada a desfazer')
        return
    last_todo = todo_list.pop()
    print(f'{last_todo}, removido')
    redo_list.append(last_todo)

def do_redo(todo_list, redo_list):
    if not redo_list:
        print('Nada a refazer')
        return
    last_todo = redo_list.pop()
    print(f'{last_todo}, readicionado a lista')
    todo_list.append(last_todo)


if __name__ == "__main__":
    todo_list = []
    redo_list = []
    menu = ''
    while menu != 'x':
        escolha = input('Digite uma tarefa ou d:desfazer r: refazer l: listar ou x:sair : ')
        if escolha == 'x':
            menu = 'x'
            print('Programa finalizado')
        elif escolha == 'd':
            do_undo(todo_list, redo_list)
            continue
        elif escolha == 'r':
            do_redo(todo_list, redo_list)
            continue
        elif escolha == 'l':
            lista(todo_list)
            continue
        else :
            adiciona(escolha, todo_list)
          
        
            