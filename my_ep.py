#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Import para usar os argumentos da linha de comando
import sys

#sys.argv[0] = nome do programa
#sys.argv[1] = flags '-u' ou '-a'
#sys.argv[2] = nome do arquivo de entrada

#-------------------------------------------------------
#Faz leitura da entrada e armazena em usr_list. Cada posicao da lista e uma linha da entrada.
usr_list = []
for line in open(sys.argv[2]):
	usr_list.append(line)
#-------------------------------------------------------
#Monta listas de UIDs, nomes e users
all_users = []
all_names = []
all_uids  = []
for i in usr_list:
	temp = []
	count = 0
	for j in i:
		if j == ':':
			if count == 0: #insere o user
				all_users.append("".join(temp))
			if count == 2: #insere o uid
				all_uids.append("".join(temp))
			if count == 4: #insere o name
				all_names.append("".join(temp))
			count = count + 1
			temp = []
			continue
		if count == 0: #pega o user
			temp.append(j)
			continue
		if count == 2: #pega o uid
			temp.append(j)
			continue
		if count == 4: #pega o name
			temp.append(j)
#------------------------------------------------------
#Busca por UIDs repetidas
repeated_uids = []
repeated_names = [] 
if sys.argv[1] == '-u':    
    for i in all_uids:
	    if all_uids.count(i) > 1 and repeated_uids.count(i) == 0:
		    repeated_uids.append(i)
#Buscar por nomes repetidos
elif sys.argv[1] == '-a': 
    for i in all_names:
        if all_names.count(i) > 1 and repeated_names.count(i) == 0:
            repeated_names.append(i)
#------------------------------------------------------
#Escreve <UID>:<usuarios>
if repeated_uids != []:
	f = open('u_output', 'w')
	for i in repeated_uids:
		v = 0
		f.write(i + ':')
		for idx, j in enumerate(all_users):
			if i == all_uids[idx]:
				if v == 0:
					f.write(j)
					v = 1
				else:
					f.write(',' + j)
		f.write('\n')
#------------------------------------------------------
#Escreve <Name>:<usuarios>
elif repeated_names != []:
	f = open('a_output', 'w')
	for i in repeated_names:
			v = 0
			f.write(i + ':')
			for idx, j in enumerate(all_users):
				if i == all_names[idx]:
					if v == 0:
						f.write(j)
						v = 1
					else:
						f.write(',' + j)
			f.write('\n')

#------------------------------------------------------

