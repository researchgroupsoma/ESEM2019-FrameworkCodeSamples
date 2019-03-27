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


arquivoComNomeDosProjetos = retornaArquivo('springsamples.txt')

print('project,', 'imports,', 'javaFiles,', 'imports/javaFiles')


for caminho in arquivoComNomeDosProjetos:
	
	caminho = caminho.split('\n')[0]
	
	pasta = './repositorios/'+caminho
	
	caminhoDosJava = find('*.java', pasta)

	numeroDeImportacoes = 0
	
	for caminhoJava in caminhoDosJava:
		
		arquivoJava = retornaArquivo(caminhoJava)

		for linhaJava in arquivoJava:
			if linhaJava.split(' ')[0] == 'import' :
				biblioteca = linhaJava.split(' ')[1]
				biblioteca = biblioteca.split('.')
				if biblioteca[0] == 'org' and biblioteca[1] == 'springframework' and biblioteca[2] == 'boot':
					numeroDeImportacoes = numeroDeImportacoes + 1

	print(str(caminho)+', '+str(numeroDeImportacoes)+', '+str(len(caminhoDosJava)) +', %0.2f' % ( numeroDeImportacoes / len(caminhoDosJava) ))