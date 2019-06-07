import http.client
import json

class Conexao:

	def __init__(self):
		pass

	def criaConexaoComServidor(self):
		return http.client.HTTPSConnection('api.github.com', 443)


	def criaCabecalho(self):
		cabecalho = {
			'Content-type': 'application/json',
			'User-Agent': 'gabrielsmenezes',
			'Authorization': 'Bearer 8b28dd386d92b833e1a6dce7b22fc7fbafa88195'
		}
		return cabecalho;


	def criaCorpoDaRequisicao(self, owner, repositorio):
		return {"query":"query($nomeDoRepositorio:String!, $dono: String!){\n  repository (name: $nomeDoRepositorio, owner: $dono) {\n    name\n    stargazers{\n      totalCount\n    }\n    watchers{\n      totalCount\n    }\n    issues{\n      totalCount\n    }\n    forkCount\n    diskUsage\n    ref(qualifiedName: \"master\"){\n      target{\n        ... on Commit{\n          history{\n            totalCount\n          }\n        }\n      }\n    }\n    pullRequests () {\n      totalCount\n    }\n    updatedAt\n    projects{\n      totalCount\n    }\n    nameWithOwner\n  }\n}","variables":{"dono": owner,"nomeDoRepositorio": repositorio}}


	def criaCorpoDaRequisicaoParaForks(self, owner, repositorio, endCursor):
		return {"query":"query ($nomeDoRepositorio: String!, $dono: String!, $endCursor: String) {\n  repository(name: $nomeDoRepositorio, owner: $dono) {\n    forks(first: 100, after: $endCursor) {\n      edges {\n        node {\n          owner {\n            login\n          }\n          nameWithOwner\n          stargazers {\n            totalCount\n          }\n          watchers {\n            totalCount\n          }\n          issues {\n            totalCount\n          }\n          forkCount\n          diskUsage\n          ref(qualifiedName: \"master\") {\n            target {\n              ... on Commit {\n                history {\n                  totalCount\n                }\n              }\n            }\n          }\n          pullRequests {\n            totalCount\n          }\n          updatedAt\n          projects {\n            totalCount\n          }\n        }\n      }\n      pageInfo {\n        hasNextPage\n        endCursor\n      }\n    }\n  }\n}","variables":{"dono": owner,"nomeDoRepositorio": repositorio,"endCursor": endCursor}}

	def retornaStatusDeDiferenciacaoEntreRepositorios(self, nomeRepositorioBase, nomeOwnerFork):
		conexao = self.criaConexaoComServidor()
		cabecalho = self.criaCabecalho()
		corpoDaRequisicaoEmJSON = ""
		conexao.request('GET', "https://api.github.com/repos/" + nomeRepositorioBase + "/compare/master..." + nomeOwnerFork + ":master", 
			corpoDaRequisicaoEmJSON, cabecalho)

		response = conexao.getresponse()
		respostaEmJson = json.loads(response.read().decode());

		return respostaEmJson

	def retornaADiferencaEntreOsRepositorios(self, nomeRepositorioBase, nomeOwnerFork):
		resposta = self.retornaStatusDeDiferenciacaoEntreRepositorios(nomeRepositorioBase, nomeOwnerFork)
		conexao = http.client.HTTPSConnection('github.com', 443)
		cabecalho = {
			'Content-type': 'text/plain',
			'User-Agent': 'gabrielsmenezes',
		}
		diff_url = resposta['diff_url']
		corpoDaRequisicaoEmJSON = ""
		conexao.request('GET', diff_url, 
			corpoDaRequisicaoEmJSON, cabecalho)
		# print(response)
		response = conexao.getresponse().read().decode()
		return response


	def retornaForks(self, owner, repositorio, endCursor):
		connection = self.criaConexaoComServidor()

		cabecalho = self.criaCabecalho()
		corpoDaRequisicao = self.criaCorpoDaRequisicaoParaForks(owner, repositorio, endCursor)
		corpoDaRequisicaoEmJSON = json.dumps(corpoDaRequisicao)

		connection.request('POST', "/graphql", 
			corpoDaRequisicaoEmJSON, cabecalho)

		response = connection.getresponse()

		respostaEmJson = json.loads(response.read().decode());

		objetoRetornado = respostaEmJson['data']

		repositorio = objetoRetornado['repository']

		return repositorio['forks'];

	def retornaRepositorio(self, owner, repositorio):
		connection = self.criaConexaoComServidor()

		cabecalho = self.criaCabecalho()
		corpoDaRequisicao = self.criaCorpoDaRequisicao(owner, repositorio)
		corpoDaRequisicaoEmJSON = json.dumps(corpoDaRequisicao)

		connection.request('POST', "/graphql", 
			corpoDaRequisicaoEmJSON, cabecalho)

		response = connection.getresponse()

		respostaEmJson = json.loads(response.read().decode());

		objetoRetornado = respostaEmJson['data']

		repositorio = objetoRetornado['repository']

		return repositorio;

	def retornarRateLimit(self):
		conexao = self.criaConexaoComServidor()
		cabecalho = self.criaCabecalho()
		corpoDaRequisicaoEmJSON = ""
		conexao.request('GET', "https://api.github.com/rate_limit", corpoDaRequisicaoEmJSON, cabecalho)

		response = conexao.getresponse()
		respostaEmJson = json.loads(response.read().decode());

		return respostaEmJson		

	def retornaPOMDeProjetoSpring(self, link):
		conexao = http.client.HTTPSConnection('raw.githubusercontent.com', 443)

		cabecalho = {
			'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
			'If-None-Match': "31d0a36669543e362bfeb39c1a555f9048c7835a"

		}
		corpoDaRequisicaoEmJSON = ""
		conexao.request('GET', link , corpoDaRequisicaoEmJSON, cabecalho)

		response = conexao.getresponse()

		respostaEmJson = response.read();

		return str(respostaEmJson)
