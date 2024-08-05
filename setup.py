import sys
from cx_Freeze import setup, Executable

base = None

setup(
    name='Gerenciador de tarefas Command Line',
    version='1.0',
    description='Criar tarefas e gerencia-lás',
    author='Alexsander Sautier',
    executables=[Executable('app.py', base=base, icon="tasks.ico")]
)