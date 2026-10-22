Aluno: Eduardo Henrique Moraes Santos
RA: 22309110
Ciência de Dados e Machine Learning — Campus Asa Norte


##########################################################################################


TaskTracker

Sistema de gerenciamento de tarefas em linha de comando, desenvolvido em Python 3 e conteinerizado com Docker.

Projeto cumulativo da disciplina Bootcamp II

##########################################################################################

Sobre o projeto

No dia a dia, uma pessoa costuma acumular várias tarefas ao mesmo tempo: compromissos da faculdade, trabalhos com prazo, obrigações de casa e demandas do trabalho. Sem um sistema para organizar tudo isso, as tarefas ficam espalhadas em lugares diferentes e três problemas aparecem:

Esquecimento — a tarefa existe, mas se perde no meio das outras informações e só é lembrada depois que o prazo passou.
Falta de prioridade — sem uma ordem clara, a pessoa gasta tempo com o que é menos importante enquanto o urgente fica parado.
Falta de visão do progresso — a pessoa não consegue enxergar quanto já concluiu e quanto ainda falta.

O TaskTracker resolve isso reunindo as tarefas em um único lugar, classificadas por prioridade e com o progresso sempre visível.

##########################################################################################

Funcionalidades

1 - Cadastrar nova tarefa — solicita título, descrição, prioridade e data limite, valida cada entrada e registra a tarefa com a situação "Pendente".

2 - Visualizar tarefas cadastradas — exibe todas as tarefas numeradas e ordenadas por prioridade, mostrando título, descrição, prioridade, data limite e situação.

3 - Concluir uma tarefa — altera a situação da tarefa escolhida de "Pendente" para "Concluída".

4 - Ver resumo das tarefas — exibe o total de tarefas cadastradas, quantas estão pendentes e quantas já foram concluídas.

5 - Sair da aplicação — encerra o programa.

OBS.: O documento de orientação da Entrega Intermediária define como obrigatórias as opções de cadastrar, visualizar e sair, todas implementadas e presentes no menu. As opções de concluir uma tarefa e ver resumo foram mantidas por constarem no planejamento lógico elaborado na Fase 1, no qual o menu do TaskTracker foi desenhado com cinco funcionalidades. Preservá-las garante a fidelidade entre o algoritmo documentado na fase anterior e o código entregue nesta fase.

##########################################################################################

Regras de negócio aplicadas

As regras abaixo foram definidas na Fase 1 do projeto e estão implementadas no código:

O título é obrigatório. Entradas vazias ou compostas apenas por espaços em branco são recusadas.
A prioridade aceita exclusivamente Alta, Média (ou "Media") e Baixa, em qualquer combinação de maiúsculas e minúsculas.
Toda tarefa nasce automaticamente com a situação Pendente.
Só é possível concluir uma tarefa que exista na lista.
A data limite deve seguir o formato DD/MM/AAAA. Datas inexistentes, como 31/02/2026, são recusadas.
Uma tarefa já concluída não pode ser concluída novamente.
A listagem sempre exibe as tarefas na ordem Alta, Média e Baixa.
O programa só encerra quando o usuário escolhe a opção "Sair".
Os dados ficam armazenados em memória durante a execução, em uma lista de dicionários.

##########################################################################################

Tecnologias utilizadas
Python 3 — linguagem de desenvolvimento da aplicação. Versão utilizada: 3.13.16.
Biblioteca padrão do Python — o módulo datetime é usado na validação da data limite. O projeto não depende de nenhuma biblioteca externa.
Docker — conteinerização da aplicação, garantindo que o sistema rode de forma idêntica em qualquer máquina. Imagem base utilizada: python:3.11-slim.
Docker Compose — orquestração da execução, responsável por manter o container em modo interativo.
Git e GitHub — controle de versão e hospedagem do repositório.
Visual Studio Code — ambiente de desenvolvimento utilizado.

##########################################################################################

Estrutura do repositório

A organização de pastas e arquivos abaixo mantém o mapeamento arquitetural desenhado na Fase 1, documentado em docs/mapeamento_arquitetural.pdf, acrescida dos arquivos de conteinerização exigidos na Fase 3.

tasktracker-projeto/
├── README.md                        # Documentação principal da aplicação
├── Dockerfile                       # Receita de construção da imagem
├── docker-compose.yml               # Orquestração da execução interativa
├── .gitignore                       # Regras para ignorar arquivos temporários do Python
├── requirements.txt                 # Dependências do projeto
├── docs/
│   ├── planejamento_logico.pdf      # Planejamento lógico entregue na Fase 1
│   └── mapeamento_arquitetural.pdf  # Mapeamento da estrutura do repositório
└── src/
    ├── main.py                      # Ponto de entrada e laço do menu
    ├── menu.py                      # Exibe o menu e lê a opção digitada
    ├── tarefas.py                   # As quatro funcionalidades do sistema
    └── validacoes.py                # Regras de validação das entradas

OBS.: os itens exigidos nos documentos de orientação das Fases 2 e 3 — README.md, .gitignore, docs/planejamento_logico.pdf, src/main.py, Dockerfile e docker-compose.yml — estão todos presentes nesta estrutura. Os demais arquivos são os que haviam sido planejados no mapeamento arquitetural da Fase 1 e foram mantidos, de modo que o repositório corresponda exatamente ao que foi documentado nas fases anteriores. Nenhum arquivo das entregas anteriores foi removido.

##########################################################################################

Divisão do código-fonte

Cada módulo dentro de src/ corresponde a uma parte da receita lógica descrita no planejamento da Fase 1:

1 - main.py — ponto de entrada do programa. Cria a lista vazia que guarda as tarefas, controla o laço de repetição do menu e encerra a aplicação na opção 5 (Regras 8 e 9).

2 - menu.py — interface com o usuário. Exibe a mensagem de boas-vindas e as cinco opções, lê a opção digitada, verifica se está entre 1 e 5 e avisa quando é inválida.

3 - tarefas.py — as quatro funcionalidades: cadastrar_tarefa(), listar_tarefas(), concluir_tarefa() e exibir_resumo(). Também ordena a listagem por prioridade e impede a conclusão repetida de uma mesma tarefa (Regras 3, 6 e 7).

4 - validacoes.py — regras de validação das entradas. Título não pode ficar em branco (Regra 1), prioridade só pode ser Alta, Média ou Baixa (Regra 2), data no formato DD/MM/AAAA e número de tarefa existente (Regras 4 e 5).

A ordem de importação entre os módulos não forma ciclos: o main.py importa menu e tarefas; o tarefas.py importa menu e validacoes; e os módulos menu.py e validacoes.py não importam nenhum outro.

##########################################################################################

Como instalar e executar com Python

Pré-requisito: ter o Python 3 instalado (desenvolvido e testado na versão 3.13.16). Para conferir, abra o terminal e digite python --version.

1 - Clone o repositório para o seu computador:

git clone https://github.com/EduardHenriqueCEUB/tasktracker-projeto.git

2 - Entre na pasta do projeto:

cd tasktracker-projeto

3 - Execute a aplicação:

python src/main.py

OBS.: Não é necessário instalar dependências nem criar ambiente virtual, pois o projeto utiliza apenas a biblioteca padrão do Python.

##########################################################################################

Como executar com Docker

Esta é a forma recomendada de executar o TaskTracker. Com o Docker, não é preciso ter o Python instalado na máquina: a própria imagem já traz o interpretador na versão correta e o código-fonte da aplicação.

Pré-requisito: ter o Docker instalado e em execução. Para conferir, abra o terminal e digite docker --version. No Windows, o Docker Desktop precisa estar aberto, com a mensagem "Engine running" visível.

Todos os comandos abaixo devem ser executados a partir da pasta raiz do projeto, a mesma onde estão o Dockerfile e o docker-compose.yml.

1 - Como construir a imagem

docker build -t tasktracker-app .

O parâmetro -t define o nome da imagem e o ponto final indica que o Dockerfile está no diretório atual. Na primeira execução, o Docker baixa a imagem base do Python, o que leva alguns minutos. Nas execuções seguintes ele reaproveita as camadas já construídas e o processo é quase instantâneo.

2 - Como rodar o container em modo isolado

docker run -it --rm tasktracker-app

O parâmetro -i mantém o canal de entrada aberto e o -t reserva um terminal, o que permite digitar as opções do menu dentro do container. O --rm apaga o container automaticamente ao sair da aplicação, evitando o acúmulo de containers parados na máquina.

3 - Como rodar via orquestração (Recomendado)

docker compose run --rm tasktracker-app

Esta é a forma mais simples de executar o sistema. O Docker Compose lê o arquivo docker-compose.yml, constrói a imagem caso ela ainda não exista e sobe o container já no modo interativo, sem que o usuário precise informar os parâmetros manualmente.

OBS.: Para encerrar a aplicação em qualquer um dos modos acima, basta escolher a opção 5 - Sair da aplicação no menu.

##########################################################################################

Divisão dos arquivos de conteinerização

Os dois arquivos criados na Fase 3 têm funções distintas e complementares:

1 - Dockerfile — é a receita da imagem. Define a imagem base python:3.11-slim, escolhida por ser enxuta e deixar a imagem final menor; define /app como diretório de trabalho; desliga o buffer de saída do Python, para que as perguntas e respostas apareçam na tela no momento exato em que são impressas; copia a pasta src/ para dentro da imagem; e define o comando que sobe a aplicação. É este arquivo que o comando docker build utiliza.

2 - docker-compose.yml — é o maestro da execução. Declara o serviço tasktracker-app, aponta que a imagem deve ser construída a partir do Dockerfile desta mesma pasta e mantém as opções stdin_open e tty ativadas. Essas duas opções são indispensáveis neste projeto: o TaskTracker conversa com o usuário pela função input(), e sem elas o container subiria isolado, sem conseguir receber o que é digitado no teclado. É este arquivo que o comando docker compose run utiliza.

OBS.: Não há instalação de dependências no Dockerfile porque o TaskTracker utiliza exclusivamente a biblioteca padrão do Python 3, conforme documentado no requirements.txt.

##########################################################################################

Exemplo de uso

Ao executar o programa, o menu principal é exibido no terminal:

==================================================
           TASKTRACKER - MENU PRINCIPAL
==================================================
1 - Cadastrar nova tarefa
2 - Visualizar tarefas cadastradas
3 - Concluir uma tarefa
4 - Ver resumo das tarefas
5 - Sair da aplicação
--------------------------------------------------
Digite a opção desejada:

Escolhendo a opção 1, o sistema solicita os dados da tarefa. Durante o cadastro, as seguintes regras são verificadas a cada campo digitado:

1 - O título não pode ficar em branco. Enquanto o campo estiver vazio ou contiver apenas espaços, o sistema exibe a mensagem de erro e solicita o título novamente.

2 - A prioridade deve ser Alta, Média ou Baixa. Qualquer outro valor é recusado e o campo é solicitado novamente.

3 - A data limite deve seguir o formato DD/MM/AAAA e corresponder a uma data existente. Entradas como 31/02/2026 são recusadas.

4 - A descrição é de preenchimento livre e não possui restrição.

5 - A situação é definida automaticamente como "Pendente", sem solicitação ao usuário.

Com todos os campos preenchidos corretamente, o cadastro é concluído:

Título da tarefa: Entregar trabalho de Bootcamp II
Descrição da tarefa: Gravar o vídeo e enviar o PDF no AVA
Prioridade (Alta / Média / Baixa): Alta
Data limite (DD/MM/AAAA): 15/12/2026

Tarefa "Entregar trabalho de Bootcamp II" cadastrada com sucesso!

O comportamento é exatamente o mesmo quando a aplicação é executada dentro do container, o que comprova que a conteinerização preservou a lógica construída nas fases anteriores.

##########################################################################################

Sobre o armazenamento das tarefas

OBS.: Ao executar o src/main.py no terminal, as tarefas cadastradas existem apenas enquanto o programa está aberto. Elas ficam guardadas na memória do computador, em uma lista criada no início da execução. Ao escolher a opção "Sair" ou fechar o terminal, essa lista deixa de existir e as tarefas são perdidas. Ao abrir o programa novamente, ele começa vazio.

Esse comportamento é intencional e corresponde à Regra 9 definida no planejamento lógico da Fase 1, que estabelece o armazenamento em memória durante a execução. O escopo das entregas é a implementação da lógica, das validações e da conteinerização, e não a persistência dos dados.

Dentro do container a situação é a mesma, e fica ainda mais evidente: o container é um ambiente isolado e descartável, criado no momento da execução e removido ao final dela pelo parâmetro --rm. Tudo o que foi cadastrado durante aquela sessão desaparece junto com ele.

Para que as tarefas fossem mantidas entre uma execução e outra, seria necessário gravá-las fora do programa, em um dos seguintes destinos:

1 - Um arquivo no próprio computador, como uma planilha em formato CSV ou um arquivo de texto estruturado. É a solução mais simples: ao cadastrar uma tarefa, o programa escreveria uma nova linha no arquivo; ao iniciar, leria o arquivo e carregaria as tarefas de volta para a lista. Funciona bem para um único usuário e permite abrir os dados diretamente no Excel.

2 - Um banco de dados, como SQLite ou PostgreSQL. É a solução adequada quando várias pessoas usam o sistema ao mesmo tempo, quando o volume de tarefas cresce ou quando é preciso buscar e filtrar informações com rapidez. O banco também garante que dois cadastros simultâneos não se sobrescrevam e que os dados não sejam corrompidos.

No caso do container, o Docker resolveria isso com um recurso chamado volume, que é uma pasta da máquina ligada ao ambiente isolado, permitindo que o arquivo ou o banco continuem existindo mesmo depois que o container é removido.

Em ambos os casos, cada tarefa deixaria de ser apenas um registro temporário e passaria a ser um dado histórico. Esse é o ponto que liga o projeto a minha área de Ciência de Dados.

##########################################################################################