import datetime
import os
import Conexao
import Versionamento as v
import EscreveNoCSV
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
	
	escreveNoCSV = EscreveNoCSV.EscreveNoCSV()
	
	file = open(nomeDoArquivoTxt+'.txt', 'r')
	
	escreveNoCSV.escreveCabecalhoDaTabela('metadados/' + nomeDoArquivoTxt +'.csv', False)

	for line in file:
		if line[0] == '#':
			continue

		print(line)		
		repositorio = conexao.retornaRepositorio(retornaNomeDoOwner(line), retornaNomeDoRepo(line))
		escreveNoCSV.escreverOsMetadados(repositorio, 'metadados/' + nomeDoArquivoTxt +'.csv', None)
		endCursor = None
		escreveNoCSV.escreveCabecalhoDaTabela('metadados/'+repositorio['name']+'.csv', True)
		nomeCompletoDoRepositorioBase = repositorio['nameWithOwner']
		while True:
			retornoDaRequisicao = conexao.retornaForks(retornaNomeDoOwner(line), retornaNomeDoRepo(line), endCursor)

			pageInfo = retornoDaRequisicao['pageInfo']

			forks = retornoDaRequisicao['edges']

			for item in forks:
				rateLimit = conexao.retornarRateLimit()['resources']['core']
				if rateLimit['remaining'] == 0:
					time.sleep(3600)
				print("Requisicoes restantes: " + str(rateLimit['remaining']) )
				nomeDoOwnerFork = item['node']['owner']['login']
				dadosDaComparacao = conexao.retornaStatusDeDiferenciacaoEntreRepositorios(nomeCompletoDoRepositorioBase, nomeDoOwnerFork)
				escreveNoCSV.escreverOsMetadados(item['node'], 'metadados/'+repositorio['name']+'.csv', dadosDaComparacao)
			if not pageInfo['hasNextPage']:
				break
			endCursor = pageInfo['endCursor']

def main():
	inicio = retornaTempo()
	
	criaPastaMetadados()

	# token = input('Digite o token:')
	# token = '8b401c6e46df398a9e73897c60ff4d54c323ec45'

	executar('googlesamples')
	executar('springsamples')


	fim = retornaTempo()
	
	print ('Tempo de inicio: ' + str(inicio))
	print ('Tempo de fim: ' + str(fim))

main()

# conexao = Conexao.Conexao()
# # print (conexao.retornaADiferencaEntreOsRepositorios('googlesamples/android-AutofillFramework', 'dlarsonks'))
# versionamento = v.Versionamento()

# arquivoXML = conexao.retornaPOMDeProjetoSpring("https://raw.githubusercontent.com/spring-guides/gs-reactive-rest-service/master/complete/pom.xml")

# dadosDoParent = versionamento.retornaDadosDoVersionamentoDoPOM(arquivoXML)

# print (dadosDoParent)