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

def eliminarCaracteresEspeciais(linha):
	linha = linha.replace(".", " ")
	linha = linha.replace("'", "")
	linha = linha.replace('"', "")
	linha = linha.replace(',', "")
	linha = linha.replace('(', "")
	linha = linha.replace(')', "")
	linha = linha.replace('\n', "")
	return linha

contadorDePalavras = {}


caminhosDosLogs = find('*.txt', './repositorios')

for caminhoDoLog in caminhosDosLogs:
	
	arquivoDeLog = retornaArquivo(caminhoDoLog)
	
	for linha in arquivoDeLog:

		linha = eliminarCaracteresEspeciais(linha)

		linha = linha.lower()

		mensagemDividida = linha.split(" ")

		# for palavra in mensagemDividida:
		# 	print(palavra)

		for palavra in mensagemDividida:
			if palavra in contadorDePalavras:
				contadorDePalavras[palavra] = contadorDePalavras[palavra] + 1
			else:
				contadorDePalavras[palavra] = 1

for palavra in contadorDePalavras:
	print(palavra+",", contadorDePalavras[palavra])