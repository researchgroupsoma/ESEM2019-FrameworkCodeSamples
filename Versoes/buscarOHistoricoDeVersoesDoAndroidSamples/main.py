import subprocess
from git import Repo
import Versionamento as v
import EscreveNoCSV as e
import os, fnmatch
import io


def main():
	versionamento = v.Versionamento()
	escreveNoCsv = e.EscreveNoCSV()

	listaDeReleases = retornaListaDeReleasesDoSpring()

	mapa = criarMapeador()

	cabecalho = criaCabecalho(listaDeReleases)

	escreveNoCsv.escreveCabecalhoDaTabela("versoes.csv", cabecalho)

	result = find('*.txt', '.')

	for arquivo in result:

		print (arquivo)

		arquivoDeLog = retornaArquivoInvertido (retornaArquivo(arquivo))

		versaoDoCommitAnterior = ""

		dadosParaInserirNaTabela = retornaVetorVazio()

		for linhaDeLog in arquivoDeLog:
			# print(linhaDeLog)
			
			objetoLog = retornaObjetoLogPelaLinha(linhaDeLog)

			# print("dataDoCommit", retornaDataFormatada(objetoLog["dataDoCommit"]))
			
			if (dadosParaInserirNaTabela[0] != objetoLog['caminho'] and (dadosParaInserirNaTabela[0] != '')):
				# print ('entrou no if')
				# escreveNoCsv.escreverOsMetadados("versoes.csv", dadosParaInserirNaTabela)
				dadosParaInserirNaTabela = retornaVetorVazio()
			# else:
				# print('nao entrou no if')

			caminhoDoProjeto = retornaApenasCaminhoDoProjeto(objetoLog['caminho'])
			
			checkoutEmCommit(caminhoDoProjeto, objetoLog['hash'])
			
			build = retornaArquivo("/home/gabriel/Documentos/ic/repositorios/repositoriosAndroid/repositorios/" + objetoLog['caminho'])

			# print(build.read())

			dadosDaVersaoDoAndroid = versionamento.retornaDadosDoVersionamentoDoBuild(str(build.read()))['compileSdk']
			if dadosDaVersaoDoAndroid == "'android-20'":
				dadosDaVersaoDoAndroid = "20"
			elif dadosDaVersaoDoAndroid == "'android-26'":
				dadosDaVersaoDoAndroid = "26"
			elif dadosDaVersaoDoAndroid == "'android-23'":
				dadosDaVersaoDoAndroid = "23"
			print(dadosDaVersaoDoAndroid)

			if((versaoDoCommitAnterior != dadosDaVersaoDoAndroid) and dadosDaVersaoDoAndroid != "'android-L'" and dadosDaVersaoDoAndroid != "'android-P'" and dadosDaVersaoDoAndroid != "'android-MNC'"and dadosDaVersaoDoAndroid != 'parent.ext.compileSdkVersion' and dadosDaVersaoDoAndroid != '"android-P"' and dadosDaVersaoDoAndroid != 'Integer.valueOf(project.TARGET_SDK_VERSION)' and dadosDaVersaoDoAndroid != 'androidCompileSdkVersion as Integer' and dadosDaVersaoDoAndroid != 'compileSdk' and dadosDaVersaoDoAndroid != '' and dadosDaVersaoDoAndroid != 'information not found' and dadosDaVersaoDoAndroid != 'rootProject.compileSdk' and dadosDaVersaoDoAndroid != '"android-MNC"' and dadosDaVersaoDoAndroid != '"android-L"' and dadosDaVersaoDoAndroid != 'rootProject.ext.compileSdkVersion' and dadosDaVersaoDoAndroid != "'android-O'" and dadosDaVersaoDoAndroid != '"android-N"' and dadosDaVersaoDoAndroid != '"android-O"' and dadosDaVersaoDoAndroid != "'android-N'"):
				dadosParaInserirNaTabela[0] = objetoLog['caminho']
				index = mapear(mapa, dadosDaVersaoDoAndroid)
				dadosParaInserirNaTabela[index] = dadosDaVersaoDoAndroid
				d1 = retornaDataFormatada(objetoLog['dataDoCommit'])
				d2 = mapa[mapear(mapa, dadosDaVersaoDoAndroid)]
				dadosParaInserirNaTabela[index + 1] = days_between(d1, d2)
				dadosParaInserirNaTabela[index + 2] = d1
				versaoDoCommitAnterior = dadosDaVersaoDoAndroid
				escreveNoCsv.escreverOsMetadados("versoes.csv", dadosParaInserirNaTabela)


def criaCabecalho(listaDeReleases):
	cabecalho = ['path']
	for objetoRelease in listaDeReleases:		
		cabecalho.append(objetoRelease['release'])
		cabecalho.append(objetoRelease['data'].split('\n')[0])
		cabecalho.append('dateOfChange')
	return cabecalho

def checkoutEmCommit(caminhoDoProjeto, hash):
	repo = Repo("/home/gabriel/Documentos/ic/repositorios/repositoriosAndroid/repositorios/" + caminhoDoProjeto)		
	repo.git.checkout(hash)

def retornaObjetoLogPelaLinha(linhaDeLog):
	linhaDividida = retornaVetorComAsInformacoesDoLog(linhaDeLog)	
	objetoLog = retornaObjetoLog(linhaDividida)
	return objetoLog

def mapear(mapa, versao):
	return mapa.index(versao) + 1

def retornaVetorVazio():
	vetor = []
	for x in range(1,(112 * 3)):
		vetor.append('')
	return vetor

def criarMapeador():
	arquivo = retornaArquivo('androidReleases.csv')
	objetosRelease = retornaObjetosReleases (arquivo)
	mapa = []
	for release in objetosRelease:
		mapa.append(release['release'])
		mapa.append(release['dataDoCommit'].replace('\n', ''))
		mapa.append('')
	return mapa

def retornaObjetosReleases(arquivo):
	releases = []
	for line in arquivo:
		linhaDividida = retornaVetorComAsInformacoesDoLog(line)
		release = {
			'release' : linhaDividida[0],
			'dataDoCommit': linhaDividida[1]
		}
		releases.append(release)
	return releases

def ehInitial(caminho):
	caminhoDividido = caminho.split('/')
	return caminhoDividido[1] == 'initial'

def retornaListaDeReleasesDoSpring():
	arquivoComVersoesDoSpring = retornaArquivo('androidReleases.csv')
	releases = []
	for linha in arquivoComVersoesDoSpring:
		linhaDividida = retornaVetorComAsInformacoesDoLog(linha)
		objetoRelease = {
			'release':linhaDividida[0],
			'data':linhaDividida[1]
		}
		releases.append(objetoRelease)
	return releases

def retornaArquivoInvertido(arquivo):
	aux = []
	lista = []
	for linha in arquivo:
		aux.append(linha)

	while (len (aux) > 0):
		pop = aux.pop()
		lista.append (pop)
	return lista

def retornaApenasCaminhoDoProjeto(caminho):
	caminhoDoProjeto = caminho.split('/')[0]
	return caminhoDoProjeto

def retornaArquivo(nomeDoArquivo):
	arquivo = ''
	try:
		arquivo = open(nomeDoArquivo, 'r')
	except Exception as e:
		output  = io.BytesIO()
		arquivo = io.TextIOWrapper(output, encoding='cp1252', line_buffering=True)
	return arquivo


def retornaVetorComAsInformacoesDoLog(linha):
	return linha.split(',')

def retornaObjetoLog(linhaDividida):
	log = {
		'caminho' : linhaDividida[0],
		'hash' : linhaDividida[1], 
		'dataDoCommit': linhaDividida[3].replace('\n', '')
	}
	return log

def mapeaMesParaInteiro(mes):
	inteiro = 0
	if mes == 'Jan':
		inteiro = 1
	if mes == 'Feb':
		inteiro = 2
	if mes == 'Mar':
		inteiro = 3
	if mes == 'Apr':
		inteiro = 4
	if mes == 'May':
		inteiro = 5
	if mes == 'Jun':
		inteiro = 6
	if mes == 'Jul':
		inteiro = 7
	if mes == 'Aug':
		inteiro = 8
	if mes == 'Sep':
		inteiro = 9
	if mes == 'Oct':
		inteiro = 10
	if mes == 'Nov':
		inteiro = 11
	if mes == 'Dec':
		inteiro = 12
	return inteiro

from datetime import datetime

def retornaDataFormatada(data):
	vetor = data.split(" ")
	dataFormatada = vetor[4] + "-" + str(mapeaMesParaInteiro(vetor[1])) + "-" + vetor[2]
	return dataFormatada

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

def find(pattern, path):
	result = []
	for root, dirs, files in os.walk(path):
		for name in files:
			if fnmatch.fnmatch(name, pattern):
				result.append(os.path.join(root, name))
	return result

main()