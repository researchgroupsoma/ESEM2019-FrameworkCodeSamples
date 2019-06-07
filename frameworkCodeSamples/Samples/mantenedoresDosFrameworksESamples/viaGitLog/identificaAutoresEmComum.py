import json

def retornaAutorEmJson(linha):
	autor = {}
	nome = linha.split(",")[0].replace("\n", "")
	email = linha.split(",")[1].replace("\n", "")
	autor = {
	'nome' : nome,
	'email' : email
	}
	return autor

def retornaArquivo(nomeDoArquivo):
	arquivo = ''
	try:
		arquivo = open(nomeDoArquivo, 'r')
	except Exception as e:
		output  = io.BytesIO()
		arquivo = io.TextIOWrapper(output, encoding='cp1252', line_buffering=True)
	return arquivo


#Ler o arquivo de log com o nome e email de cada author de commit
arquivoComLogDoFramework = retornaArquivo('spring/repositorios/framework/spring-boot.txt')

#Cria um conjunto que tem todos os autores dos commits do framework

autoresDoFramework = set()

#cria um conjunto de autores em comum

print('framework',',samples',',framework contributors', ',sample contributors', ',common contributors',',common/framework',',common/sample')

#Para cada linha do arquivo faca
for linha in arquivoComLogDoFramework:
	autor = retornaAutorEmJson(linha)
	if autor['email'] != '':
		# print('salvando o autor:', autor)
		autoresDoFramework.add(json.dumps(autor))

#Ler o arquivo com a lista de todos os samples
arquivoComNomeDosCodeSamples = retornaArquivo('springsamples.txt')
	#para cada linha na listaDeSamples
for nomeDoSample in arquivoComNomeDosCodeSamples:
	#Ler o log do samples
	nomeDoSample = nomeDoSample.replace('\n','')
	
	gitLogDoSample = retornaArquivo('spring/repositorios/samples/'+nomeDoSample+'.txt')
	
	numeroDeAutoresDoSample = 0
	autoresEmComum = set()
	
	for linha in gitLogDoSample:
		autorDoCodeSample = retornaAutorEmJson(linha)

		if autorDoCodeSample['email'] != '':
			numeroDeAutoresDoSample = numeroDeAutoresDoSample + 1

			for autorDoFramework in autoresDoFramework:
				autorDoFramework = json.loads(autorDoFramework)

				if autorDoFramework['nome'] == autorDoCodeSample['nome'] or autorDoFramework['email'] == autorDoCodeSample['email']:
					autoresEmComum.add(json.dumps(autorDoCodeSample))
	print('spring,', nomeDoSample,',',str(len(autoresDoFramework)),',', str(numeroDeAutoresDoSample), ',',str(len(autoresEmComum)))