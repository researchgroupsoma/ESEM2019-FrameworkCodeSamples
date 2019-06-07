from Commit import Commit
from git import Repo
import Versionamento as v

def retornaArquivoInvertido(arquivo):
	aux = []
	lista = []
	for linha in arquivo:
		aux.append(linha)

	while (len (aux) > 0):
		pop = aux.pop()
		lista.append (pop)
	return lista
def versoesDoSpring():
	versoesDoFramework = dict()
	arquivo = retornaArquivo("springReleases.csv")
	for release in arquivo:
		release = release.split(",")
		versoesDoFramework[release[0]] = release[1].split(" ")[0]
	return versoesDoFramework

def versoesDoAndroid():
	versoesDoFramework = dict()
	versoesDoFramework["19"] = "2013-10-13"
	versoesDoFramework["21"] = "2014-10-17"
	versoesDoFramework["22"] = "2015-03-09"
	versoesDoFramework["23"] = "2015-08-17"
	versoesDoFramework["24"] = "2016-06-15"
	versoesDoFramework["25"] = "2016-12-05"
	versoesDoFramework["26"] = "2017-08-21"
	versoesDoFramework["27"] = "2017-12-05"
	versoesDoFramework["28"] = "2018-06-08"
	return versoesDoFramework

def retornaArquivo(nomeDoArquivo):
	arquivo = ''
	try:
		arquivo = open(nomeDoArquivo, 'r')
	except Exception as e:
		output  = io.BytesIO()
		arquivo = io.TextIOWrapper(output, encoding='cp1252', line_buffering=True)
	return arquivo

def checkoutEmCommit(caminhoDoProjeto, hashNumber):
	repo = Repo(pathAndroid + caminhoDoProjeto)		
	repo.git.checkout(hashNumber)

def criaCommit(commit):
		commit = commit.split(",")
		caminhoDoArquivo = commit[0]
		hashNumber = commit[1]
		data = commit[3]
		return Commit(caminhoDoArquivo, hashNumber, data)

versionamento = v.Versionamento()

pathAndroid = "/home/gabriel/Documentos/ic/Versoes/buscaVersaoDoAndroid/repositorios/"

pathSpring = "/home/gabriel/Documentos/ic/Versoes/buscarOHistoricoDeVersoesDeSpringSamples/repositorios/" 
versoesDoFramework = versoesDoAndroid()

#ler o arquivo com o nome dos samples
arquivoComNomeDosSamples = retornaArquivo("googlesamples.txt")
#para cada linha
for sample in arquivoComNomeDosSamples:
	#tira o \n do nome do sample
	sample = sample.replace("\n", "")
	versaoAnterior = ""
	caminhoAnterior = -1
	#ler o arquivotxt correspondente a linha
	arquivoDeLog = retornaArquivoInvertido(retornaArquivo("androidLogs/"+sample+".txt"))
	for commit in arquivoDeLog:
		#criar um objeto que representando o hash, data e caminho do arquivo
		commit = criaCommit(commit)

		

		if caminhoAnterior != "" and caminhoAnterior != commit.caminhoDoArquivo:
			caminhoAnterior = ""
			versaoAnterior = ""
			print()
			print(commit.caminhoDoArquivo, end=", ")

		#dar checkout
		checkoutEmCommit(sample, commit.hashNumber)
		#retorna arquivo de configuracao
		try:
			arquivoDeConfiguracao = retornaArquivo(pathAndroid+commit.caminhoDoArquivo)
		except Exception as e:
			continue
		
		arquivoDeConfiguracao = str(arquivoDeConfiguracao.read())
		#busca a versao do sdk 
		dadosDaVersao = versionamento.retornaDadosDoVersionamentoDoBuild(arquivoDeConfiguracao)['compileSdk']
		if versaoAnterior == "":
			caminhoAnterior = commit.caminhoDoArquivo
			versaoAnterior = dadosDaVersao
		

		if dadosDaVersao != versaoAnterior:
			try:
				versaoAnterior = dadosDaVersao
				print(dadosDaVersao, ",", commit.data ,",", commit.delay(versoesDoFramework[dadosDaVersao]), end=", ")
				# print(dadosDaVersao, ",", commit.data ,",", commit.delay(versoesDoFramework[dadosDaVersao]))
			except Exception as e:
				continue				