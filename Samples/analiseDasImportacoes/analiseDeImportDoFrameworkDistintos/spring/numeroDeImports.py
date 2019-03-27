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

for caminho in arquivoComNomeDosProjetos:
	
	caminho = caminho.split('\n')[0]
	
	pasta = './repositorios/'+caminho
	
	caminhoDosJava = find('*.java', pasta)

	conjuntoDeImports = set()
	
	for caminhoJava in caminhoDosJava:
		
		arquivoJava = retornaArquivo(caminhoJava)

		for linhaJava in arquivoJava:
			if linhaJava.split(' ')[0] == 'import' :
				biblioteca = linhaJava.split(' ')[1]
				if biblioteca.split('.')[0] == 'org' and biblioteca.split('.')[1] == 'springframework' and biblioteca.split('.')[2] == 'boot':
					conjuntoDeImports.add(biblioteca.replace('\n', '').replace(';', ''))

	print(str(caminho)+', '+str(len(conjuntoDeImports)))