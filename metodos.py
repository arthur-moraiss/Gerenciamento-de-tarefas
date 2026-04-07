from operacoesbd import *
import os
def lerInteiro(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print('Digite uma opcao válida!')


def lerTexto(msg):
    while True:
        texto = input(msg).strip()
        if texto:
            return texto
        print("Campo não pode estar vazio.")


def finalizarFuncao():
    input('\nPressione ENTER para continuar...')
    os.system('cls' if os.name == 'nt' else 'clear')

def listarTarefas(conexao):
    consulta = 'select * from sistema'

    tarefas = listarBancoDados(conexao, consulta)

    if not tarefas:
        print('Nenhuma tarefa encontrada.')
    else:
        print('\n' + '-' * 90)
        print(f'{"ID":<3} | {"TITULO":<20} | {"DESCRICAO":<20} | {"STATUS":<12} | DATA')
        print('-' * 90)

        for i in tarefas:
            titulo = (i[1] or '')[:30]
            descricao = (i[2] or '')[:20]
            status = (i[4] or '')

            print(f'{i[0]:<3} | {titulo:<20} | {descricao:<20} | {status:<12} | {i[3]}')
    finalizarFuncao()

def inserirNovaTarefa(conexao):
    tituloNovo = input('Digite o titulo da tarefa: ')
    descricaoNova = input('Digite a descrição: ')

    consulta = 'insert into sistema (titulo,descricao) values (%s,%s)'
    dados = [tituloNovo, descricaoNova]

    Novatarefa = insertNoBancoDados(conexao, consulta, dados)

    print(f'O codigo da nova tarefa é {Novatarefa}')
    finalizarFuncao()
def atualizarStatus(conexao):
    codigTarafa = int(input("Digite o ID da tarefa que deseja ataulizar o status: "))
    while True:
        print('\n:::OPÇÕES DE STATUS:::')
        print('[ 1 ] concluido')
        print('[ 2 ] descartado')

        escolha = input('Digite a opção: ').strip()

        if escolha == '1':
            novoStatus = 'concluido'
            break
        elif escolha == '2':
            novoStatus = 'descartado'
            break
        else:
            print(' Opção inválida! Digite apenas 1 ou 2.')
    consulta = 'update sistema set status = %s where id = %s'
    dados = [novoStatus, codigTarafa]

    linhasAfetadas = atualizarBancoDados(conexao, consulta, dados)

    if linhasAfetadas == 0:
        print('Não existe Tarefa para o codigo informado.')
    else:
        print("Status atualizado com sucesso.")
    finalizarFuncao()
def removerTarefa(conexao):
    excluirTarefa = input("Digite o ID da tarefa a ser removida: ")
    consulta = 'delete from sistema where id = %s;'
    dados = [excluirTarefa]

    linhasAfetadas = excluirBancoDados(conexao, consulta, dados)
    if linhasAfetadas == 0:
        print('Não existe tarefa para o codigo informado.')
    else:
        print("Tarefa atualizada com sucesso.")
    finalizarFuncao()
def sair(conexao):
    print('Obrigado por usar nosso APP!')
    input('\nPressione ENTER para sair...')


funcoes = {
    1: inserirNovaTarefa,
    2: listarTarefas,
    3: atualizarStatus,
    4: removerTarefa,
    5: sair
    }