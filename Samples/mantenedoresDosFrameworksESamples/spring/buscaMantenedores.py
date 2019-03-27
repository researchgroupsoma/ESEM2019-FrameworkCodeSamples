import http.client
import json

def dictToSet(chaves):
	conjunto = set()
	for chave in chaves:
		conjunto.add(chave)
	return conjunto


def retornaArquivo(nomeDoArquivo):
	arquivo = ''
	try:
		arquivo = open(nomeDoArquivo, 'r')
	except Exception as e:
		output  = io.BytesIO()
		arquivo = io.TextIOWrapper(output, encoding='cp1252', line_buffering=True)
	return arquivo

def criaCabecalho():
	cabecalho = {
		'Content-type': 'application/json',
		'User-Agent': 'gabrielsmenezes',
		'Authorization': 'Bearer 8b401c6e46df398a9e73897c60ff4d54c323ec45'
	}
	return cabecalho;

def retornaConjuntoDeContribuidores(dono, nomeDoRepositorio):
	conexao = http.client.HTTPSConnection('api.github.com', 443)
	contribuidores = dict()
	corpoDaRequisicaoEmJSON = ""
	endpoint = "https://api.github.com/repos/" + dono + "/" + nomeDoRepositorio + "/contributors"
	conexao.request('GET', endpoint, corpoDaRequisicaoEmJSON, criaCabecalho())
	response = conexao.getresponse()
	respostaEmJson = json.loads(response.read().decode());

	for contribuidor in respostaEmJson:
		contribuidores[contribuidor['login']] = contribuidor['contributions']

	return contribuidores


#Para cada framework
	#Criar um conjunto de contribuidores e Inserir todos os contribuidores
retorno = retornaConjuntoDeContribuidores('spring-projects','spring-boot')

contribuidoresDoFramework = dictToSet(retorno.keys())

codeSamples = retornaArquivo('springsamples.txt')


for codeSample in codeSamples:
	codeSample = codeSample.replace('\n', '')
	
	retorno = retornaConjuntoDeContribuidores('spring-guides', codeSample)
	
	contribuidoresDoSample = dictToSet(retorno.keys())

	contribuidoresEmComum =contribuidoresDoFramework.intersection(contribuidoresDoSample)

	print( codeSample, end='')
	# for contribuidor in contribuidoresEmComum:
	# 	print(', ' + contribuidor + ', ' + str(retorno[contribuidor]), end='')
	

	# porcentagemDosDevsDoFrameworkQueEstaoNoCodeSamples = len(contribuidoresEmComum) / len(contribuidoresDoFramework)
	# porcentagemDosDevsDosCodeSamplesQueEstaoNoFramework = len(contribuidoresEmComum) / len(contribuidoresDoSample)

	# print(str(porcentagemDosDevsDoFrameworkQueEstaoNoCodeSamples) + ', ' + str(porcentagemDosDevsDosCodeSamplesQueEstaoNoFramework), end='')

	print(', '+str(len(contribuidoresDoFramework))+', '+str(len(contribuidoresDoSample))+', '+str(len(contribuidoresEmComum)), end='')
	print()

#Quantos porcento dos desenvolvedores do framework estão nos code samples

# len(desenvolvedoresEmComum) / len(contribuidoresDoFramework)

#Quantos porcento dos desenvolvedores dos code samples estão no framework

# len(desenvolvedoresEmComum) / len(contribuidoresDoSample) 