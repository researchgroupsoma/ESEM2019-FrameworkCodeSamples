import datetime
import os
import Conexao
import time


def retornaNomeDoOwner(line):
	linhaQuebrada = line.split('/')
	return linhaQuebrada[3]

def retornaNomeDoRepo(line):
	linhaQuebrada = line.split('/')
	nomeDoRepositorio = linhaQuebrada[4].replace('\n', '')
	return nomeDoRepositorio

def retornaTempo():
	return (datetime.datetime.time(datetime.datetime.now()))

def criaPastaMetadados():
	if not os.path.exists('metadados'):
		os.makedirs('metadados')


def executar(nomeDoArquivoTxt):
	conexao = Conexao.Conexao()
	
	file = open(nomeDoArquivoTxt+'.txt', 'r')
	
	for line in file:
		if line[0] == '#':
			continue

		# print(line)		
		repositorio = conexao.retornaRepositorio(retornaNomeDoOwner(line), retornaNomeDoRepo(line))
		endCursor = None
		nomeCompletoDoRepositorioBase = repositorio['nameWithOwner']
		while True:
			retornoDaRequisicao = conexao.retornaForks(retornaNomeDoOwner(line), retornaNomeDoRepo(line), endCursor)

			pageInfo = retornoDaRequisicao['pageInfo']

			forks = retornoDaRequisicao['edges']

			for item in forks:
				rateLimit = conexao.retornarRateLimit()['resources']['core']
				if rateLimit['remaining'] == 0:
					time.sleep(3600)
				# print("Requisicoes restantes: " + str(rateLimit['remaining']) )
				nomeDoOwnerFork = item['node']['owner']['login']
				# print(item['node'])
				dadosDaComparacao = conexao.retornaStatusDeDiferenciacaoEntreRepositorios(nomeCompletoDoRepositorioBase, nomeDoOwnerFork)
				try:
					if (dadosDaComparacao['ahead_by'] > 0):
						print(item['node']['nameWithOwner'] + ', '+dadosDaComparacao['merge_base_commit']['sha'])
				except Exception as e:
					continue
			if not pageInfo['hasNextPage']:
				break
			endCursor = pageInfo['endCursor']

def main():
	inicio = retornaTempo()
	
	# criaPastaMetadados()

	# token = input('Digite o token:')
	# token = '8b401c6e46df398a9e73897c60ff4d54c323ec45'

	executar('googlesamples')
	# executar('springsamples')


	fim = retornaTempo()
	
	# print ('Tempo de inicio: ' + str(inicio))
	# print ('Tempo de fim: ' + str(fim))

main()