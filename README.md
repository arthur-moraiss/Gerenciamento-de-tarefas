📋 Sistema de Gerenciamento de Tarefas

Este projeto é um sistema simples de gerenciamento de tarefas via terminal, desenvolvido em Python, com integração a banco de dados.

Ele permite:

Adicionar tarefas
Listar tarefas
Atualizar status
Remover tarefas
⚙️ Tecnologias utilizadas
Python 🐍
MySQL (ou outro banco relacional)
Módulo próprio: operacoesbd (responsável pela conexão e operações no banco)
📂 Estrutura do Código
🔹 Importações
from operacoesbd import *
import os
operacoesbd: contém funções para interagir com o banco (insert, select, update, delete)
os: usado para limpar o terminal
🧠 Funções do Sistema
📌 lerInteiro(msg)
def lerInteiro(msg):

Função para garantir que o usuário digite um número inteiro válido.

Variáveis:

msg: mensagem exibida ao usuário
ValueError: erro tratado caso o usuário digite algo inválido
📌 lerTexto(msg)
def lerTexto(msg):

Garante que o usuário digite um texto não vazio.

Variáveis:

msg: mensagem exibida
texto: armazena o valor digitado pelo usuário
📌 finalizarFuncao()
def finalizarFuncao():

Pausa o sistema e limpa o terminal.

Variáveis:

os.name: identifica o sistema operacional
'cls': limpa no Windows
'clear': limpa no Linux/Mac
📌 listarTarefas(conexao)
def listarTarefas(conexao):

Lista todas as tarefas cadastradas no banco.

Variáveis:

conexao: conexão com o banco de dados
consulta: query SQL (select * from sistema)
tarefas: lista de registros retornados do banco
i: representa cada tarefa individual

Campos da tarefa (índices):

i[0]: ID
i[1]: título
i[2]: descrição
i[3]: data
i[4]: status
📌 inserirNovaTarefa(conexao)
def inserirNovaTarefa(conexao):

Adiciona uma nova tarefa ao banco.

Variáveis:

tituloNovo: título da tarefa
descricaoNova: descrição da tarefa
consulta: comando SQL de inserção
dados: lista com os valores a serem inseridos
Novatarefa: ID da nova tarefa criada
📌 atualizarStatus(conexao)
def atualizarStatus(conexao):

Atualiza o status de uma tarefa.

Variáveis:

codigTarafa: ID da tarefa (obs: nome com pequeno erro de digitação)
escolha: opção escolhida pelo usuário
novoStatus: novo status da tarefa (concluido ou descartado)
consulta: query SQL de atualização
dados: valores usados na query
linhasAfetadas: quantidade de registros alterados
📌 removerTarefa(conexao)
def removerTarefa(conexao):

Remove uma tarefa do banco.

Variáveis:

excluirTarefa: ID da tarefa
consulta: comando SQL DELETE
dados: parâmetro para a query
linhasAfetadas: verifica se a tarefa existia
📌 sair(conexao)
def sair(conexao):

Finaliza o sistema.

🔁 Dicionário de Funções
funcoes = {
    1: inserirNovaTarefa,
    2: listarTarefas,
    3: atualizarStatus,
    4: removerTarefa,
    5: sair
}

Esse dicionário funciona como um menu dinâmico, onde:

A chave (1, 2, 3...) é a opção do usuário
O valor é a função que será executada
