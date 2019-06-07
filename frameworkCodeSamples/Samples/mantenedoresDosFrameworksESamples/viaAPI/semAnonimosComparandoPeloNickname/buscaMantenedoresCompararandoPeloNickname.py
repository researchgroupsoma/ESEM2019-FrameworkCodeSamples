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
		'Authorization': 'Bearer ba444b6defd11047fe878d792b4d8905b3e16cca'
	}
	return cabecalho;

def retornaConjuntoDeContribuidores(dono, nomeDoRepositorio):
	conexao = http.client.HTTPSConnection('api.github.com', 443)
	contribuidores = dict()
	corpoDaRequisicaoEmJSON = ""
	endpoint = "https://api.github.com/repos/" + dono + "/" + nomeDoRepositorio + "/contributors?page=1"
	conexao.request('GET', endpoint, corpoDaRequisicaoEmJSON, criaCabecalho())
	response = conexao.getresponse()
	respostaEmJson = json.loads(response.read().decode());
	page = 2

	while (respostaEmJson != []):
		for contribuidor in respostaEmJson:
			contribuidores[contribuidor['login']] = contribuidor['contributions']
		endpoint = "https://api.github.com/repos/" + dono + "/" + nomeDoRepositorio + "/contributors?page="+str(page)
		conexao.request('GET', endpoint, corpoDaRequisicaoEmJSON, criaCabecalho())
		response = conexao.getresponse()
		respostaEmJson = json.loads(response.read().decode());
		page+=1
	return contribuidores


# Para cada framework
# 	Criar um conjunto de contribuidores e Inserir todos os contribuidores
retorno = retornaConjuntoDeContribuidores('spring-projects','spring-boot')

contribuidoresDoFramework = dictToSet(retorno.keys())

codeSamples = retornaArquivo('springsamples.txt')


for codeSample in codeSamples:
	codeSample = codeSample.replace('\n', '')
	
	retorno = retornaConjuntoDeContribuidores('spring-guides', codeSample)
	
	contribuidoresDoSample = dictToSet(retorno.keys())

	contribuidoresEmComum =contribuidoresDoFramework.intersection(contribuidoresDoSample)

	print(codeSample+', '+str(len(contribuidoresDoFramework))+', '+str(len(contribuidoresDoSample))+', '+str(len(contribuidoresEmComum)))
