# -*- coding: utf-8 -*-
"""
Este módulo concentra as regras de validação das entradas digitadas pelo
usuário, conforme planejado na Fase 1 do projeto. Cada função pergunta ao
usuário e só devolve o valor quando ele for válido.
"""

from datetime import datetime


# ---------------------------------------------------------------------------
# CONSTANTES DE VALIDAÇÃO
# ---------------------------------------------------------------------------

# Regra 2 da Fase 1: a prioridade só pode ser Alta, Média ou Baixa.
# O dicionário abaixo aceita o texto digitado de várias formas (com acento,
# sem acento, maiúsculo ou minúsculo) e converte para a forma padronizada.
PRIORIDADES_VALIDAS = {
    "alta": "Alta",
    "media": "Média",
    "média": "Média",
    "baixa": "Baixa",
}


# ---------------------------------------------------------------------------
# REGRA 1 - TÍTULO OBRIGATÓRIO
# ---------------------------------------------------------------------------

def ler_titulo():
    """
    Pede o título da tarefa até que um título válido seja informado.

    Regra 1 da Fase 1: o sistema não aceita tarefas sem título. Entradas
    vazias ou compostas apenas por espaços em branco são recusadas.
    """
    while True:
        titulo = input("Título da tarefa: ").strip()
        if titulo == "":
            print("Erro: o título não pode ficar em branco. Tente novamente.")
            continue
        return titulo


def ler_descricao():
    """Pede a descrição da tarefa. Campo de preenchimento livre."""
    return input("Descrição da tarefa: ").strip()


# ---------------------------------------------------------------------------
# REGRA 2 - PRIORIDADE RESTRITA
# ---------------------------------------------------------------------------

def ler_prioridade():
    """
    Pede a prioridade da tarefa até que um valor válido seja informado.

    Regra 2 da Fase 1: são aceitas exclusivamente as opções Alta, Média
    (com ou sem acento) e Baixa, em qualquer combinação de maiúsculas
    e minúsculas.
    """
    while True:
        digitado = input("Prioridade (Alta / Média / Baixa): ").strip().lower()
        if digitado in PRIORIDADES_VALIDAS:
            return PRIORIDADES_VALIDAS[digitado]
        print("Erro: a prioridade deve ser Alta, Média ou Baixa. Tente novamente.")


# ---------------------------------------------------------------------------
# REGRA 5 - FORMATO DA DATA LIMITE
# ---------------------------------------------------------------------------

def ler_data_limite():
    """
    Pede a data limite da tarefa até que uma data válida seja informada.

    Regra 5 da Fase 1: a data deve seguir o formato DD/MM/AAAA. A função
    strptime verifica tanto o formato quanto a existência real da data,
    recusando entradas como 31/02/2026.
    """
    while True:
        data = input("Data limite (DD/MM/AAAA): ").strip()
        try:
            datetime.strptime(data, "%d/%m/%Y")
            return data
        except ValueError:
            print("Erro: use o formato DD/MM/AAAA. Tente novamente.")


# ---------------------------------------------------------------------------
# REGRA 4 - NÚMERO DE TAREFA EXISTENTE
# ---------------------------------------------------------------------------

def ler_numero_tarefa(total_de_tarefas):
    """
    Pede o número da tarefa até que um número válido seja informado.

    Regra 4 da Fase 1: só é possível concluir uma tarefa que exista na
    lista. O número digitado precisa ser um inteiro entre 1 e o total de
    tarefas exibidas.
    """
    while True:
        digitado = input("Número da tarefa que deseja concluir: ").strip()

        if not digitado.isdigit():
            print("Erro: número de tarefa inválido. Tente novamente.")
            continue

        numero = int(digitado)
        if numero < 1 or numero > total_de_tarefas:
            print("Erro: número de tarefa inválido. Tente novamente.")
            continue

        return numero