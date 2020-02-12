#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import string
import collections
from subprocess import call

contadors='IPC,DSCR,IPCanterior,IPCanterior1,IPCanterior2,IPCanterior3,PM_L1_ICACHE_MISS,PERF_COUNT_HW_CACHE_L1D:READ:MISS,PERF_COUNT_HW_CACHE_L1D:WRITE:MISS,PERF_COUNT_HW_CACHE_LL:WRITE:MISS,PM_DATA_FROM_L3,PM_MEM_PREF,PERF_COUNT_HW_CACHE_L1I:PREFETCH:ACCESS,PERF_COUNT_HW_CACHE_L1D:PREFETCH:ACCESS,PM_MEM_READ,PM_L1_ICACHE_RELOADED_PREF,PM_DATA_FROM_MEMORY,PM_BR_MPRED_CMPL,LLC-LOAD-MISSES,PM_DISP_HELD_IQ_FULL,PM_CMPLU_STALL_DMISS_L3MISS,PERF_COUNT_HW_BRANCH_INSTRUCTIONS\n'
benchmarks = [2, 3, 7, 9, 11, 12, 14, 15, 17, 18, 21, 23, 24];

configs = [0,1,71,455];

results = open("dataset.csv", 'w');
results.write(contadors);

IPCproximo = 0;
eventos = [];

########################################################
## RESULTADOS EJECUCION ESTATICA DE OBTENCION DE DATOS #
########################################################
for h in benchmarks:
	for j in configs:
		primer = 0;
		fitx = open("datos/trabajo["+str(h)+"]conf["+str(j)+"].txt");
		for linea in fitx.read().split("\n"):
			if 'ACTUALIPC' in linea:##Llixc el anterior IPC
				if primer == 0:
					##aquí evito coger el primer ipc porque quiero el proximo, futuro ipc
					primer = 1;
				elif primer == 1:	
					IPCproximo = linea[18:len(linea)];#este es el proximo ipc
					dscr = eventos[0];##0 es dscr y 1 es ipc actual
					eventos = eventos[1:];#son los eventos del intervalo posterior
					for k in eventos:
						string = string +','+ str(k);

					results.write(IPCproximo+","+dscr+string+"\n");
					string = '';
			#elif primer == 0:
			#	print("Estoy aun calculando los IPCs anteriores");
			elif 'DATOS PREDICCION :' in linea:##Agafe totes les dades de 1.
				string = linea[19:len(linea)-1];##Agafe soles les dades sense el text.
				eventos = string.split(',');
				string ='';
		fitx.close();
		print("Procesado el fichero: trabajo["+str(h)+"]conf["+str(j)+"].txt");

########################################################
## RESULTADOS EJECUCION DINAMICA DE OBTENCION DE DATOS #
########################################################
for h in benchmarks:
	primer = 0;
	fitx = open("4.0/trabajo["+str(h)+"]conf[auto].txt");
	for linea in fitx.read().split("\n"):
		if 'ACTUALIPC' in linea:##Llixc el anterior IPC
			if primer == 0:
				##aquí evito coger el primer ipc porque quiero el proximo, futuro ipc
				primer = 1;
			elif primer == 1:	
				IPCproximo = linea[18:len(linea)];#este es el proximo ipc
				dscr = eventos[0];##0 es dscr y 1 es ipc actual
				eventos = eventos[1:];#son los eventos del intervalo posterior
				for k in eventos:
					string = string +','+ str(k);

				results.write(IPCproximo+","+dscr+string+"\n");
				string = '';
		#elif primer == 0:
		#	print("Estoy aun calculando los IPCs anteriores");
		elif 'DATOS PREDICCION :' in linea:##Agafe totes les dades de 1.
			string = linea[19:len(linea)-1];##Agafe soles les dades sense el text.
			eventos = string.split(',');
			string ='';
	fitx.close();
	print("Procesado el fichero: trabajo["+str(h)+"]conf[auto].txt");

########################################################
## RESULTADOS EJECUCION DINAMICA DE OBTENCION DE DATOS #
########################################################
for h in benchmarks:
	primer = 0;
	fitx = open("4.1/trabajo["+str(h)+"]conf[auto].txt");
	for linea in fitx.read().split("\n"):
		if 'ACTUALIPC' in linea:##Llixc el anterior IPC
			if primer == 0:
				##aquí evito coger el primer ipc porque quiero el proximo, futuro ipc
				primer = 1;
			elif primer == 1:	
				IPCproximo = linea[18:len(linea)];#este es el proximo ipc
				dscr = eventos[0];##0 es dscr y 1 es ipc actual
				eventos = eventos[1:];#son los eventos del intervalo posterior
				for k in eventos:
					string = string +','+ str(k);

				results.write(IPCproximo+","+dscr+string+"\n");
				string = '';
		#elif primer == 0:
		#	print("Estoy aun calculando los IPCs anteriores");
		elif 'DATOS PREDICCION :' in linea:##Agafe totes les dades de 1.
			string = linea[19:len(linea)-1];##Agafe soles les dades sense el text.
			eventos = string.split(',');
			string ='';
	fitx.close();
	print("Procesado el fichero: trabajo["+str(h)+"]conf[auto].txt");

########################################################
## RESULTADOS EJECUCION DINAMICA DE OBTENCION DE DATOS #
########################################################
for h in benchmarks:
	primer = 0;
	fitx = open("4.2/trabajo["+str(h)+"]conf[auto].txt");
	for linea in fitx.read().split("\n"):
		if 'ACTUALIPC' in linea:##Llixc el anterior IPC
			if primer == 0:
				##aquí evito coger el primer ipc porque quiero el proximo, futuro ipc
				primer = 1;
			elif primer == 1:	
				IPCproximo = linea[18:len(linea)];#este es el proximo ipc
				dscr = eventos[0];##0 es dscr y 1 es ipc actual
				eventos = eventos[1:];#son los eventos del intervalo posterior
				for k in eventos:
					string = string +','+ str(k);

				results.write(IPCproximo+","+dscr+string+"\n");
				string = '';
		#elif primer == 0:
		#	print("Estoy aun calculando los IPCs anteriores");
		elif 'DATOS PREDICCION :' in linea:##Agafe totes les dades de 1.
			string = linea[19:len(linea)-1];##Agafe soles les dades sense el text.
			eventos = string.split(',');
			string ='';
	fitx.close();
	print("Procesado el fichero: trabajo["+str(h)+"]conf[auto].txt");