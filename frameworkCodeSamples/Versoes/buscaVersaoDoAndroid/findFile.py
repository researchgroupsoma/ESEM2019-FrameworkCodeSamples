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



caminhosDoBuild = find('build.gradle', '.')
caminhosDoAndroidManifest = find('AndroidManifest.xml', '.')
	

v = Versionamento.Versionamento()
e = EscreveNoCSV.EscreveNoCSV()

print(len(caminhosDoAndroidManifest))

for caminho in caminhosDoAndroidManifest:
	# print(caminho)
	arquivo = devolveArquivo(caminho)
	androidManifest = v.retornaDadosDoVersionamentoDoAndroidManifest(str(arquivo.read()))
	# if not (androidManifest['minSdkVersion'] == '' and androidManifest['targetSdkVersion'] == '' and androidManifest['maxSdkVersion'] == ''):
	# 	print (androidManifest)
e.escreveCabecalhoDaTabela("googlesamples.csv")


for caminho in caminhosDoBuild:
	print(caminho)
	arquivo = devolveArquivo(caminho)
	informacoesDeVersaoDoAndroidNoBuild = v.retornaDadosDoVersionamentoDoBuild(str(arquivo.read()))
	e.escreverOsMetadadosDoBuild(caminho, informacoesDeVersaoDoAndroidNoBuild, "googlesamples.csv")

for caminho in caminhosDoAndroidManifest:
	print(caminho)
	arquivo = devolveArquivo(caminho)
	informacoesDeVersaoDoAndroidNoAndroidoManifest = v.retornaDadosDoVersionamentoDoAndroidManifest(str(arquivo.read()))
	e.escreverOsMetadadosDoAndroidManifest(caminho, informacoesDeVersaoDoAndroidNoAndroidoManifest, "googlesamples.csv")