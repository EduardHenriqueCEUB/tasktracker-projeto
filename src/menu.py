# -*- coding: utf-8 -*-
"""
Este módulo cuida de tudo que aparece na tela e da leitura da opção
escolhida pelo usuário, conforme planejado na Fase 1 do projeto.
"""


def exibir_cabecalho(texto):
    """
    Imprime um título destacado para separar as seções na tela.

    As duas linhas em branco impressas antes do cabeçalho criam o respiro
    visual entre um bloco e outro. O espaçamento fica aqui, e não no texto
    recebido, porque o método center() contaria os caracteres de quebra de
    linha e desalinharia o título.
    """
    print()
    print()
    print("=" * 50)
    print(texto.center(50))
    print("=" * 50)


def exibir_boas_vindas():
    """Exibe a mensagem de abertura do programa."""
    exibir_cabecalho("BEM-VINDO AO TASKTRACKER")
    print("\nSistema de gerenciamento de tarefas")


def exibir_menu():
    """Exibe o menu principal com as cinco opções disponíveis no sistema."""
    exibir_cabecalho("TASKTRACKER - MENU PRINCIPAL")
    print("1 - Cadastrar nova tarefa")
    print("2 - Visualizar tarefas cadastradas")
    print("3 - Concluir uma tarefa")
    print("4 - Ver resumo das tarefas")
    print("5 - Sair da aplicação")
    print("-" * 50)


def ler_opcao_menu():
    """
    Pede a opção do menu e verifica se o valor digitado está entre 1 e 5.

    Enquanto a opção for inválida, o sistema avisa o usuário e pergunta
    novamente, sem encerrar o programa.
    """
    while True:
        opcao = input("Digite a opção desejada: ").strip()
        if opcao in ("1", "2", "3", "4", "5"):
            return opcao
        print("Opção inválida, tente novamente.")


def exibir_despedida():
    """Exibe a mensagem de encerramento do programa."""
    exibir_cabecalho("ENCERRANDO O TASKTRACKER")
    print("Até logo!")
    print()