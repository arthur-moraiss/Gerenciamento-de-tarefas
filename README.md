Sistema de Gerenciamento de Tarefas

Este projeto é um sistema simples de gerenciamento de tarefas via
terminal, desenvolvido em Python, com integração a banco de dados.

Funcionalidades: - Adicionar tarefas - Listar tarefas - Atualizar
status - Remover tarefas

========================================

FUNÇÕES E VARIÁVEIS

lerInteiro(msg): - msg: mensagem exibida ao usuário - Garante que o
valor digitado seja um número inteiro válido

lerTexto(msg): - msg: mensagem exibida ao usuário - texto: valor
digitado (não pode ser vazio)

finalizarFuncao(): - Pausa o sistema e limpa o terminal - os.name:
identifica o sistema operacional

listarTarefas(conexao): - conexao: conexão com o banco - consulta: SQL
(select * from sistema) - tarefas: lista de resultados - i: cada tarefa

Campos: i[0] = ID i[1] = título i[2] = descrição i[3] = data i[4] =
status

inserirNovaTarefa(conexao): - tituloNovo: título da tarefa -
descricaoNova: descrição - consulta: SQL insert - dados: valores
inseridos - Novatarefa: ID criado

atualizarStatus(conexao): - codigTarafa: ID da tarefa - escolha: opção
do usuário - novoStatus: status atualizado - consulta: SQL update -
dados: valores usados - linhasAfetadas: número de linhas alteradas

removerTarefa(conexao): - excluirTarefa: ID da tarefa - consulta: SQL
delete - dados: parâmetro - linhasAfetadas: verifica existência

sair(conexao): - Finaliza o sistema

========================================

DICIONÁRIO DE FUNÇÕES

funcoes = { 1: inserirNovaTarefa, 2: listarTarefas, 3: atualizarStatus,
4: removerTarefa, 5: sair }

========================================

Como usar: 1. Configure o banco 2. Execute o sistema 3. Escolha uma
opção no menu
