#!/usr/bin/python
# -*- coding: utf-8 -*-
'''Fazendo importações das bibliotecas'''
import requests
import json
import sys

'''Abrindo o arquivo de base de dados sobre a doença'''
fin = open('/home/newton/Documentos/EpideMapa/enderecos/TuberculoseCuiaba2015.csv', 'r')
'''lendo as linhas'''
linhas = fin.readlines()
'''Abrindo o arquivo destino onde será inserido as latitudes/longitudes dos endereços de ocorrência de doença'''
fout = open('/home/newton/Documentos/EpideMapa/enderecos/TuberculoseCuiaba2015Fatality2.csv', 'w')
i = 0
'''Percorrendo o Arquivo'''
for linha in linhas:	
	i = i+1
	j = 0
	'''Limitando á quinhentos dados'''
	if i == 500:
		break
	
	if(i != 1):
		endereco = ""
		'''Separando as colunas de dados de acordo com um delimitador'''
		dados = linha.split(',')
		if len(dados) >= 5:
			bairro = dados[2]
			rua = dados[3]
			numero = dados[4]
			'''Juntando os dados num formato padrão para ser inserido na request'''
			endereco = bairro+", "+rua+", "+numero+", Cuiabá"
			'''Setando a URL da Request e o formato de resultado + API Key'''
			maps_url = "https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyA3jww4q18FRggVIAmS0bA5Eu8X9nCWQK8&address="
			'''Fazendo a Requisição'''
			res = requests.get(maps_url + endereco)

		'''Se o status do resultado for "ok"'''	
		if(res.status_code == requests.codes.ok):
			'''Cria uma list com os JSON'''	
			dadosGeo = json.loads(res.text)
			'''Verificando se existe ao menos um elemento''' 
			if len(dadosGeo) > 0:
				try:
					'''Acessando as coordenadas de latitude e longitude no JSON gerado'''		
					latitude = "{:2.6f}".format(dadosGeo["results"][0]["geometry"]["location"]["lat"])
					longitude = "{:2.6f}".format(dadosGeo["results"][0]["geometry"]["location"]["lng"])
					'''Escrevendo apenas as coordenadas no novo arquivo'''
					fout.write("%f,%f\n" % (float(latitude), float(longitude)))
					
				except IndexError:
					j = j + 1
					print("Erros: %d" % j)
'''Fechando os Arquivos'''			
fout.close()
fin.close()
		
	




