# -*- coding: utf-8 -*-
"""
Este módulo reúne as quatro funcionalidades do TaskTracker: cadastrar,
listar, concluir e resumir tarefas. Cada tarefa é representada por um
dicionário e todas ficam guardadas em uma lista, conforme planejado na
Fase 1 do projeto.
"""

import menu
import validacoes


# ---------------------------------------------------------------------------
# CONSTANTES DAS TAREFAS
# ---------------------------------------------------------------------------

# Regra 7 da Fase 1: a listagem sempre exibe as tarefas na ordem
# Alta -> Média -> Baixa. Este dicionário define o peso de cada prioridade.
ORDEM_PRIORIDADE = {
    "Alta": 1,
    "Média": 2,
    "Baixa": 3,
}

# Regra 3 da Fase 1: toda tarefa nasce com a situação "Pendente".
SITUACAO_INICIAL = "Pendente"
SITUACAO_CONCLUIDA = "Concluída"


# ---------------------------------------------------------------------------
# FUNCIONALIDADE 1 - CADASTRAR TAREFA
# ---------------------------------------------------------------------------

def cadastrar_tarefa(tarefas):
    """
    Cadastra uma nova tarefa na lista.

    Segue o passo a passo do cadastro definido na Fase 1: pede o título,
    a descrição, a prioridade e a data limite, valida cada entrada, define
    a situação como "Pendente" e guarda tudo em um dicionário dentro da
    lista de tarefas.
    """
    menu.exibir_cabecalho("CADASTRO DE NOVA TAREFA")

    titulo = validacoes.ler_titulo()
    descricao = validacoes.ler_descricao()
    prioridade = validacoes.ler_prioridade()
    data_limite = validacoes.ler_data_limite()

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "situacao": SITUACAO_INICIAL,
    }

    tarefas.append(tarefa)
    print()
    print('Tarefa "{}" cadastrada com sucesso!'.format(titulo))


# ---------------------------------------------------------------------------
# FUNCIONALIDADE 2 - VISUALIZAR TAREFAS
# ---------------------------------------------------------------------------

def ordenar_por_prioridade(tarefas):
    """
    Devolve uma cópia da lista de tarefas ordenada por prioridade.

    Regra 7 da Fase 1: as tarefas de prioridade Alta aparecem primeiro,
    depois as Médias e por último as Baixas.
    """
    return sorted(tarefas, key=lambda t: ORDEM_PRIORIDADE[t["prioridade"]])


def listar_tarefas(tarefas):
    """
    Exibe na tela todas as tarefas cadastradas, uma por vez.

    Se a lista estiver vazia, exibe uma mensagem informando que não há
    registros no momento e volta ao menu principal.
    """
    menu.exibir_cabecalho("SUAS TAREFAS")

    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada até o momento.")
        return

    lista_ordenada = ordenar_por_prioridade(tarefas)

    for numero, tarefa in enumerate(lista_ordenada, start=1):
        print()
        print("[{}] {}".format(numero, tarefa["titulo"]))
        print("    Descrição...: {}".format(tarefa["descricao"]))
        print("    Prioridade..: {}".format(tarefa["prioridade"]))
        print("    Data limite.: {}".format(tarefa["data_limite"]))
        print("    Situação....: {}".format(tarefa["situacao"]))

    print()
    print("-" * 50)
    print("Total de tarefas exibidas: {}".format(len(lista_ordenada)))


# ---------------------------------------------------------------------------
# FUNCIONALIDADE 3 - CONCLUIR TAREFA
# ---------------------------------------------------------------------------

def concluir_tarefa(tarefas):
    """
    Marca uma tarefa como concluída.

    Regra 4 da Fase 1: só é possível concluir uma tarefa que exista na lista.
    Regra 6 da Fase 1: uma tarefa já concluída não pode ser concluída de novo.
    """
    if len(tarefas) == 0:
        menu.exibir_cabecalho("CONCLUIR TAREFA")
        print("Não há tarefas para concluir.")
        return

    listar_tarefas(tarefas)
    lista_ordenada = ordenar_por_prioridade(tarefas)

    print()
    numero = validacoes.ler_numero_tarefa(len(lista_ordenada))
    tarefa = lista_ordenada[numero - 1]

    if tarefa["situacao"] == SITUACAO_CONCLUIDA:
        print()
        print("Esta tarefa já foi concluída anteriormente.")
        return

    tarefa["situacao"] = SITUACAO_CONCLUIDA
    print()
    print('Tarefa "{}" foi concluída!'.format(tarefa["titulo"]))


# ---------------------------------------------------------------------------
# FUNCIONALIDADE 4 - RESUMO GERAL
# ---------------------------------------------------------------------------

def exibir_resumo(tarefas):
    """
    Exibe a contagem total de tarefas, quantas estão pendentes e quantas
    já foram concluídas.
    """
    menu.exibir_cabecalho("RESUMO GERAL")

    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada até o momento.")
        return

    total = len(tarefas)
    concluidas = 0
    for tarefa in tarefas:
        if tarefa["situacao"] == SITUACAO_CONCLUIDA:
            concluidas += 1
    pendentes = total - concluidas

    print("Total de tarefas...: {}".format(total))
    print("Pendentes..........: {}".format(pendentes))
    print("Concluídas.........: {}".format(concluidas))