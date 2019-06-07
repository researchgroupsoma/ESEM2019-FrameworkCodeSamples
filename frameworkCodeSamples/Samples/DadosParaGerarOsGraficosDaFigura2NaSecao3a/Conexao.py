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
		# return {"query":"query($nomeDoRepositorio:String!, $dono: String!){\n  repository (name: $nomeDoRepositorio, owner: $dono) {\n    name\n    stargazers{\n      totalCount\n    }\n    watchers{\n      totalCount\n    }\n    issues{\n      totalCount\n    }\n    forkCount\n    diskUsage\n    ref(qualifiedName: \"master\"){\n      target{\n        ... on Commit{\n          history{\n            totalCount\n          }\n        }\n      }\n    }\n    pullRequests () {\n      totalCount\n    }\n    updatedAt\n    projects{\n      totalCount\n    }\n    nameWithOwner\n  }\n}","variables":{"dono": owner,"nomeDoRepositorio": repositorio}}
		return {"query" : "query($nomeDoRepositorio:String!,$dono:String!){repository(name:$nomeDoRepositorio,owner:$dono) { stargazers { totalCount } defaultBranchRef{target{... on Commit{ history{ totalCount }}}}}}","variables":{"dono": owner,"nomeDoRepositorio": repositorio}}

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

		repositorio = objetoRetornado

		return repositorio;