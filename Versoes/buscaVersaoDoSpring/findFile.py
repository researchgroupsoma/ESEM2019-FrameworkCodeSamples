import os, fnmatch, Versionamento, EscreveNoCSV

def find(pattern, path):
	result = []
	for root, dirs, files in os.walk(path):
		for name in files:
			if fnmatch.fnmatch(name, pattern):
				result.append(os.path.join(root, name))
	return result

def devolveArquivo(caminho):
	return open(caminho, 'r')



caminhos = find('pom.xml', '.')
v = Versionamento.Versionamento()
e = EscreveNoCSV.EscreveNoCSV()

e.escreveCabecalhoDaTabela("springsamples.csv")

for caminho in caminhos:
	print(caminho)
	arquivo = devolveArquivo(caminho)
	informacoesDeVersaoDoAndroid = v.retornaDadosDoVersionamentoDoPOM(str(arquivo.read()))
	e.escreverOsMetadados(caminho, informacoesDeVersaoDoAndroid, "springsamples.csv")