# -*- coding: utf-8 -*-
"""
Este é o ponto de entrada do programa. Ele cria a lista que guarda as
tarefas, mantém o menu em repetição e encaminha cada opção escolhida para
a função correspondente no módulo tarefas.

Para executar o programa, a partir da pasta raiz do projeto:
    python src/main.py
"""

import menu
import tarefas as modulo_tarefas


def main():
    """
    Função principal do TaskTracker.

    Cria a lista vazia de tarefas, exibe a mensagem de boas-vindas e mantém
    o menu em repetição até que o usuário escolha a opção 5 (Sair).

    Regra 9 da Fase 1: a lista criada aqui é o repositório de dados do
    sistema durante a execução.
    Regra 8 da Fase 1: o programa só encerra na opção 5.
    """
    tarefas = []

    menu.exibir_boas_vindas()

    while True:
        menu.exibir_menu()
        opcao = menu.ler_opcao_menu()

        if opcao == "1":
            modulo_tarefas.cadastrar_tarefa(tarefas)
        elif opcao == "2":
            modulo_tarefas.listar_tarefas(tarefas)
        elif opcao == "3":
            modulo_tarefas.concluir_tarefa(tarefas)
        elif opcao == "4":
            modulo_tarefas.exibir_resumo(tarefas)
        elif opcao == "5":
            menu.exibir_despedida()
            break


# Esta verificação garante que a função main() só é executada quando o
# arquivo é rodado diretamente, e não quando ele é importado por outro código.
if __name__ == "__main__":
    main()