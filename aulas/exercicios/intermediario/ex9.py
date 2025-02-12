import os
import json

def limpa():
    os.system('cls')
    
def lin():
    print('--'*15)
    
def listar(lista_tarefas):
    lin()
    if not lista_tarefas:
        print('LISTA DE TAREFAS VAZIA')
        return
    for i in lista_tarefas:
        print(i.upper())
    lin()

def apagar(tarefas,recuperar):
    if not tarefas:
        print('NADA A APAGAR')
        return
    tarefa = tarefas.pop()
    recuperar.append(tarefa)
    print()
              
def recuperar(tarefas,recuperar):
    if not recuperar:
        print('NADA A RECUPERAR')
        return
    tarefa = recuperar.pop()
    tarefas.append(tarefa)
    print()

def adicionar(comando, tarefas):
    tarefa = comando.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    tarefas.append(tarefa)
 
def ler (tarefa, caminho_json): 
    dados = []
    try:
        with open(caminho_json, 'r', encoding='utf-8') as file:
            dados = json.load(file)
    except FileNotFoundError:
        salvar(tarefa, caminho_json)
        return tarefa

def salvar(tarefas, caminho_json):
    dados = tarefas
    with open(caminho_json, 'w', encoding='utf-8') as file:
        dados = json.dump(tarefas, file , indent=2, ensure_ascii=False)
        return dados

CAMINHO_ARQUIVO = 'ex9.json'
tarefas = ler([] , CAMINHO_ARQUIVO)
backup = []    
    
while True:
    print('[listar] [apagar] [recuperar]')
    cmd = input('COMANDO: ')
    
    comandos = {
        'listar': lambda: listar(tarefas),
        'apagar': lambda: apagar(tarefas,backup),
        'recuperar': lambda: recuperar(tarefas,backup),
        'adicionar': lambda: adicionar(cmd, tarefas)   
    } 
     
    comando = comandos.get(cmd) if comandos.get(cmd) is not None else comandos['adicionar']
    comando()
    salvar(tarefas, CAMINHO_ARQUIVO)
