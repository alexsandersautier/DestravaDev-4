from database import Connection
import os
from time import sleep
import sys

con = Connection()
def list_all():
    tasks = con.select_all()
    if len(tasks) > 0:
        print('\n')
        for task in tasks:
            concluded = 'Sim' if task[2] else 'Não'
            print(f'Tarefa Nº {task[0]}: {task[1]} - Concluída? {concluded}')
def clear():
    try:
        os.system('cls') or None
    except:
        ...            
executing = True
while executing:
    clear()
    list_all()  
    print('\nBem-vindo ao Gerenciador de Tarefas Command Line!\n')
    print('\nDigite um número para selecionar uma opção\n')
    print('1 - Nova \n2 - Atualizar \n3 - Concluir \n4 - Deletar \n5 - Sair \nDigite sua opção: ')
    option = sys.stdin.readline()
    option = int(option.replace('\n', ''))
    match option:
        case 1:
            print('Descreva a tarefa: ')
            task = sys.stdin.readline()
            con.create(task.replace('\n', ''))
            clear()
        case 2:
            list_all()
            print('Digite o número da tarefa para ser atualizada: ')
            id = sys.stdin.readline()
            task = con.select_by_id(id.replace('\n', ''))    
            print(f'\n{task[1]}\n')
            if task[2]:
                print('\nNão é possível atualizar tarefas finalizadas\n')        
            elif task:
                print('Descreva a tarefa: ')
                update = sys.stdin.readline()
                con.update(id.replace('\n', ''), update.replace('\n', ''))
            clear()    
        case 3:
            list_all()
            print('Digite o número da tarefa para ser concluida: ')
            id = sys.stdin.readline()
            con.update(id.replace('\n', ''), '', True)
            clear()
        case 4:
            list_all()
            print('Digite o número da tarefa para ser deletada: ')
            id = sys.stdin.readline()
            task = con.select_by_id(id.replace('\n', ''))
            if task[2]:
                print('\nNão é possível deletar tarefas finalizadas\n')    
                sleep(2)
            else:
                con.delete(id.replace('\n', ''))
            clear()    
        case 5:
            print('\nObrigado por utilizar meu software')
            print('Desenvolvido por Alexsander Sautier')
            sleep(3)
            clear()
            executing=False