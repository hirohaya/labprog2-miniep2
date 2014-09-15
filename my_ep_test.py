#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Import para usar os argumentos da linha de comando
import sys

#sys.argv[0] = nome do programa
#sys.argv[1] = nome do arquivo de entrada

#-------------------------------------------------------
#Faz leitura da entrada e armazena em usr_list. Cada posicao da lista e uma linha da entrada.
program_output = []
for line in open(sys.argv[1]):
	program_output.append(line)
#-------------------------------------------------------
#Testa para a saida conhecida se o output do programa para o parametro da linha de comando -u esta certo
u_test = ["121:flashbang,blackarrow,gravehound,rainbowecstasy\n", 
		 "532:ghostshell,bloodbane,yggdrassil\n"]
a_test = ["Barack Obama:flashbang,gravehound\n", 
          "Gyan Tsu-wong:ghostshell,shadowstalker\n", 
          "Tina Peitcholas:chimera,rainbowecstasy,astralmoon\n"]
if sys.argv[1] == "a_output":
	fail = 0
	for idx, i in enumerate(a_test):
		if program_output[idx] != i:
			fail = 1
		elif len(program_output) != len(a_test):
			fail = 1
	if fail == 1:
		print("Teste a_output falhou. :(")
	else:
		print("Teste a_output passou. :)")
elif sys.argv[1] == "u_output":
	fail = 0
	for idx, i in enumerate(u_test):
		if program_output[idx] != i:
			fail = 1
		elif len(program_output) != len(u_test):
			fail = 1
	if fail == 1:
		print("Teste u_output falhou. :(")
	else:
		print("Teste u_output passou. :)")
else:
	print("Entrada de teste desconhecida")