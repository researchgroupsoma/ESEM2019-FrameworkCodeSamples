import datetime
import os
import Conexao
import Versionamento as v
import time


def retornaNomeDoOwner(line):
	linhaQuebrada = line.split('/')
	return linhaQuebrada[3]

def retornaNomeDoRepo(line):
	linhaQuebrada = line.split('/')
	nomeDoRepositorio = linhaQuebrada[4].replace('\n', '')
	return nomeDoRepositorio
	

def executar(nomeDoArquivoTxt):	
	conexao = Conexao.Conexao()
	
	file = open(nomeDoArquivoTxt+'.txt', 'r')
	print('repository', 'forks', 'diskUsage_KB', 'stargazers', 'watchers', 'issues', 'commits', 'pullRequests', 'updatedAt', 'projects', 'status', 'ahead_by', 'behind_by')

	for line in file:
		repositorio = conexao.retornaRepositorio(retornaNomeDoOwner(line), retornaNomeDoRepo(line))
		
		print (repositorio['nameWithOwner'],',',repositorio['forkCount'])

def main():

	# executar('googlesamples')
	executar('springsamples')
main()

# conexao = Conexao.Conexao()
# # print (conexao.retornaADiferencaEntreOsRepositorios('googlesamples/android-AutofillFramework', 'dlarsonks'))
# versionamento = v.Versionamento()

# arquivoXML = conexao.retornaPOMDeProjetoSpring("https://raw.githubusercontent.com/spring-guides/gs-reactive-rest-service/master/complete/pom.xml")

# dadosDoParent = versionamento.retornaDadosDoVersionamentoDoPOM(arquivoXML)

# print (dadosDoParent)