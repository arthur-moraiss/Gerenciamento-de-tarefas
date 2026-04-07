opcao = 0
from metodos import *

conexao = criarConexao('localhost','root', '9013nhY$9013nhY$', 'tarefas')

while opcao !=5:
    print(f'''
    {" Sistema de tarefas ":=^30}
    1 - Adicionar tarefa
    2 - Listar tarefas
    3 - Concluir tarefa
    4 - Remover tarefa
    5 - Sair ''')
    opcao = lerInteiro('\nDigite uma opcao: ')
    os.system('cls' if os.name == 'nt' else 'clear')

    if opcao in funcoes:
        funcoes[opcao](conexao)

    else:
        print("Opção Inválida!")



encerrarConexao(conexao)