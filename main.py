#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import subprocess
import time
from datetime import datetime

#### CONFIGURAÇÕES ####
TEMPO_ESCANEAMENTO = 3 # Intervalo em segundos de cada scan no roteador.
NUM_FALHAS = 3         # Se o MAC não for detectado NUM_FALHAS vezes, é considerado como desconectado

# Lista de endereços MACS encontrados
macs = []

# Dicionário para guardar o número de falhas ao tentar encontrar o MAC do aluno
alertas = {}

# Dicionário de alunos e respectivos MACS
alunos = {}

# Gravação do arquivo de log da atividade durante a prova
log = open("log.txt","w")

print "Iniciando..."

# FASE 1
# Leitura do arquivo de alunos e inicialização da estrutura
with open("alunos.csv", "rb") as arquivo:

	conteudo = csv.reader(arquivo, delimiter=",", quotechar="|")

	# Montagem do dicionário
	for linha in conteudo:
		alunos[linha[0]] = linha[1]
		alertas[linha[0]] = 0

qtd_alunos = len(alunos)
print str(qtd_alunos) + " alunos registrados"

print "Iniciando monitoramento..."
while True:

	# FASE 2: Execução do programa de escaneamento.
	# OBS: O script SEMPRE deve ser executado como root
	output = subprocess.Popen(["arp-scan", "-l"], stdout=subprocess.PIPE).communicate()[0]

	# Formatação do output do programa anterior
	output_tmp = output.split("\n")

	for x in range(2, len(output_tmp) - 4):
		infos_aluno = output_tmp[x].split("\t")

		# Montagem da lista de endereços MAC encontrados
		macs.append(infos_aluno[1])

	qtd_detectados = 0;

	# FASE 3: Verificação se cada aluno registrado tem seu MAC encontrado no escaneamento
	for aluno, mac in alunos.iteritems():
		if(mac not in macs):
			alertas[aluno] += 1
		else:
			alertas[aluno] = 0
			qtd_detectados += 1

		# Output de um aluno caso ele tenha alcançado o número de falhas limite
		if(alertas[aluno] % NUM_FALHAS == 0 and alertas[aluno] != 0):
			msg = "[" + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "] Aluno: " + aluno + " não está conectado\n"
			alertas[aluno] = 0
			print msg
			log.write(msg)

	# Se todos os alunos forem encontrados, está tudo ok
	if(qtd_alunos == qtd_detectados):
		msg = "[" + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "] Todos alunos conectados\n"
		print msg
		log.write(msg)


	macs = []
	# Pausa no loop para o próximo escaneamento
	time.sleep(TEMPO_ESCANEAMENTO)

log.close()
