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
	contribuidores = []
	corpoDaRequisicaoEmJSON = ""
	endpoint = "https://api.github.com/repos/" + dono + "/" + nomeDoRepositorio + "/contributors?anon=1&page=1"
	conexao.request('GET', endpoint, corpoDaRequisicaoEmJSON, criaCabecalho())
	response = conexao.getresponse()
	respostaEmJson = json.loads(response.read().decode());
	page = 2

	while (respostaEmJson != []):
		for contribuidor in respostaEmJson:
			if contribuidor['type'] == 'Anonymous':
				contribuidores.append({
						'name': contribuidor['name'],
						'email': contribuidor['email']
					})

		endpoint = "https://api.github.com/repos/" + dono + "/" + nomeDoRepositorio + "/contributors?anon=1&page="+str(page)
		conexao.request('GET', endpoint, corpoDaRequisicaoEmJSON, criaCabecalho())
		response = conexao.getresponse()
		respostaEmJson = json.loads(response.read().decode());
		page+=1
	return contribuidores


# Para cada framework
# 	Criar um conjunto de contribuidores e Inserir todos os contribuidores

contribuidoresDoFramework = retornaConjuntoDeContribuidores('spring-projects','spring-boot')

codeSamples = retornaArquivo('springsamples.txt')


for codeSample in codeSamples:
	codeSample = codeSample.replace('\n', '')
	contribuidoresEmComum = []
	
	contribuidoresDoSample = retornaConjuntoDeContribuidores('spring-guides', codeSample)
	
	for contribuidorDoSample in contribuidoresDoSample:
		for contribuidorDoFramework in contribuidoresDoFramework:

			if contribuidorDoFramework['name'] == contribuidorDoSample['name']:
				contribuidoresEmComum.append(contribuidorDoSample)
				break

			elif contribuidorDoFramework['email'] == contribuidorDoSample['email']:
				contribuidoresEmComum.append(contribuidorDoSample)
				break
	print(codeSample+', '+str(len(contribuidoresDoFramework))+', '+str(len(contribuidoresDoSample))+', '+str(len(contribuidoresEmComum)))
