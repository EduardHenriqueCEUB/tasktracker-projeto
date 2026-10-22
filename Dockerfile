# ---------------------------------------------------------------------------
# TaskTracker - Dockerfile
# ---------------------------------------------------------------------------
# Projeto cumulativo da disciplina Bootcamp II - Fase 3 (Entrega Final).
#
# Autor: Eduardo Henrique Moraes Santos
# RA: 22309110
# Curso: Ciencia de Dados e Machine Learning - Campus Asa Norte
#
# Este arquivo e a "receita" da imagem. Ele descreve, passo a passo, como
# construir um ambiente isolado que ja vem com o Python instalado e com o
# codigo-fonte do TaskTracker dentro, pronto para ser executado em qualquer
# maquina que tenha o Docker, sem precisar instalar nada alem do proprio
# Docker.
# ---------------------------------------------------------------------------

# Imagem base: Python 3.11 na versao "slim".
# A versao slim foi escolhida por ser uma imagem enxuta, que traz o
# interpretador Python e apenas o essencial do sistema operacional. Isso deixa
# a imagem final menor e o build mais rapido do que a imagem padrao.
FROM python:3.11-slim

# Diretorio de trabalho dentro do container.
# A partir daqui, todo comando executado parte da pasta /app, que funciona
# como a "pasta raiz do projeto" dentro do ambiente isolado.
WORKDIR /app

# Desliga o buffer de saida do Python.
# Sem isso, as mensagens do programa podem ficar presas na memoria e so
# aparecer no final. Como o TaskTracker e um sistema interativo de terminal,
# as perguntas e respostas precisam aparecer na tela no momento exato em que
# sao impressas.
ENV PYTHONUNBUFFERED=1

# Garante que o terminal do container interprete corretamente os acentos.
# O TaskTracker exibe palavras como "Media", "Situacao" e "Concluida" com
# acentuacao, entao a codificacao UTF-8 e definida explicitamente.
ENV PYTHONIOENCODING=UTF-8

# Copia o codigo-fonte da maquina local para dentro da imagem.
# Apenas a pasta src/ e copiada, porque e nela que esta todo o codigo
# necessario para a execucao. Documentacao e arquivos de apoio ficam de fora
# de proposito, para manter a imagem leve.
COPY src/ /app/src/

# Comando executado quando o container sobe.
# Ele chama o ponto de entrada do sistema, exatamente como seria feito no
# terminal da maquina local.
CMD ["python", "src/main.py"]