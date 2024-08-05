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
    
    option = input('1 - Nova \n2 - Atualizar \n3 - Concluir \n4 - Deletar \n5 - Sair \nDigite sua opção: ')
    option = int(option)
    match option:
        case 1:
            task = input('Descreva a tarefa: ')
            con.create(task)
            clear()
        case 2:
            list_all()
            id = input('Digite o número da tarefa para ser atualizada: ')
            task = con.select_by_id(id)    
            print(f'\n{task[1]}\n')
            if task[2]:
                print('\nNão é possível atualizar tarefas finalizadas\n')        
            elif task:
                update = input('Descreva a tarefa: ')
                con.update(id, update)
            clear()    
        case 3:
            list_all()
            id = input('Digite o número da tarefa para ser concluida: ')
            con.update(id, '', True)
            clear()
        case 4:
            list_all()
            id = input('Digite o número da tarefa para ser deletada: ')
            task = con.select_by_id(id)
            if task[2]:
                print('\nNão é possível deletar tarefas finalizadas\n')    
                sleep(2)
            else:
                con.delete(id)
            clear()    
        case 5:
            print('\nObrigado por utilizar meu software')
            print('Desenvolvido por Alexsander Sautier')
            sleep(3)
            clear()
            executing=False