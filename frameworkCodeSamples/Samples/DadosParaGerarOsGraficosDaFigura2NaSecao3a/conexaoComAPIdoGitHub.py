import os
import Conexao

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
	
	for line in file:
		line = line.replace('\n','')
		repositorio = conexao.retornaRepositorio('spring-guides', line)
		stargazers = repositorio['repository']['stargazers']['totalCount']
		commits = repositorio['repository']['defaultBranchRef']['target']['history']['totalCount']
		print(line, ',', stargazers, ',', commits)

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