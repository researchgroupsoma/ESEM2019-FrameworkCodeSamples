import os, fnmatch

def find(pattern, path):
	result = []
	for root, dirs, files in os.walk(path):
		for name in files:
			if fnmatch.fnmatch(name, pattern):
				result.append(os.path.join(root, name))
	return result

def retornaArquivo(nomeDoArquivo):
	arquivo = ''
	try:
		arquivo = open(nomeDoArquivo, 'r')
	except Exception as e:
		output  = io.BytesIO()
		arquivo = io.TextIOWrapper(output, encoding='cp1252', line_buffering=True)
	return arquivo


arquivoComNomeDosProjetos = retornaArquivo('googlesamples.txt')

# print('project', ',', 'java', ',', 'properties', ',', 'jar', ',', 'build.gradle',',','pom.xml',',','manifest.xml',',','xml',',','bat',',','md',',','adoc',',','README',',','yaml',',','txt',',','sh',',','travis.yml',',','yml',',','cmd',',','kt',',','json',',','others')

for caminho in arquivoComNomeDosProjetos:
	

	caminho = caminho.split('\n')[0]
	
	# # print(caminho)

	pasta = './android/repositorios/'+caminho
	
	# # print(pasta)

	# caminhoDosJava = find('*.java', pasta)

	# caminhoDosProperties = find('*.properties', pasta)

	# caminhoDosJar = find('*.jar', pasta)
	
	# caminhoDosBuildGradle = find('*build.gradle', pasta)
	
	# caminhoDosPom = find('*pom.xml', pasta)

	# caminhoDosManifest = find('AndroidManifest.xml', pasta)

	# caminhoDosXml = find('*.xml', pasta)

	# caminhoDosBat = find('*.bat', pasta)

	# caminhoDosMd = find('*.md', pasta)
	
	# caminhoDosAdoc = find('*.adoc', pasta)

	# caminhoDosRead = find('*README.md', pasta)

	# caminhoDosYaml = find('*.yaml', pasta)

	# caminhoDosTxt = find('*.txt', pasta)

	# caminhoDosSh = find('*.sh', pasta)

	# caminhoDosYml = find('*.yml', pasta)

	# caminhoDosCmd = find('*.cmd', pasta)

	# caminhoDosKt = find('*.kt', pasta)

	# caminhoDosJson = find('*.json', pasta)
	
	# caminhoDosTravis = find('*travis.yml', pasta)

	numeroDeTodos = find('*.*', pasta)

	count = 0

	for arquivo in numeroDeTodos:
		if not ".git" in arquivo:
			count += 1

	print(caminho, ',', count)

	# numeroDeTodos = len(numeroDeTodos) - (len(caminhoDosJava) + len(caminhoDosProperties) + len(caminhoDosJar) +	len(caminhoDosBuildGradle) + len(caminhoDosXml) + len(caminhoDosBat) + len(caminhoDosMd) + len(caminhoDosAdoc) +  len(caminhoDosYaml) + len(caminhoDosTxt) + len(caminhoDosSh) + len(caminhoDosYml) + len(caminhoDosCmd) + len(caminhoDosKt) + len(caminhoDosJson) )


	# print(caminho +', '+ str(len(caminhoDosJava)) +', '+ str(len(caminhoDosProperties)) +', '+ str( len(caminhoDosJar))  +', '+ str(len(caminhoDosBuildGradle))  +', '+ str(len(caminhoDosPom))   +', '+ str(len(caminhoDosManifest))   +', '+ str(len(caminhoDosXml))   +', '+ str(len(caminhoDosBat))   +', '+ str(len(caminhoDosMd))   +', '+ str(len(caminhoDosAdoc))   +', '+ str(len(caminhoDosRead))   +', '+ str(len(caminhoDosYaml))   +', '+ str(len(caminhoDosTxt))   +', '+ str(len(caminhoDosSh))   +', '+ str(len(caminhoDosTravis))   +', '+ str(len(caminhoDosYml))   +', '+ str(len(caminhoDosCmd))   +', '+ str(len(caminhoDosKt))   +', '+ str(len(caminhoDosJson)) +', '+ str(numeroDeTodos))