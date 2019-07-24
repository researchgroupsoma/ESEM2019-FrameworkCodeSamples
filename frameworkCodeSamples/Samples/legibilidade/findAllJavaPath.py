import os, fnmatch

def find(pattern, path):
	result = []
	for root, dirs, files in os.walk(path):
		if('.git' in root):
			continue
		for name in files:
			if fnmatch.fnmatch(name, pattern):
				result.append(os.path.join(root, name))
	return result


with open ("/home/gabriel/Documentos/ic/frameworkCodeSamples/Samples/legibilidade/samples.txt") as arquivo_de_projetos:
    for linha in arquivo_de_projetos:
        linha = linha.replace("\n", "")
        arquivos_java = find("*.java", "/home/gabriel/Documentos/ic/frameworkCodeSamples/Samples/repositorios/"+linha)
        print(linha, end=",")
        for arquivo in arquivos_java:
            print(arquivo, end=",")
        print()
