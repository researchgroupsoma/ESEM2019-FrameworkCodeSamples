import csv
class EscreveNoCSV:

	def __init__(self):
		pass



	def escreveCabecalhoDaTabela(self, nomeDoArquivo):
		with open(nomeDoArquivo, 'a') as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
			spamwriter.writerow(['path', 'build.compileSdk', 'build.targetSdk', 'build.minSdkVersion', 'AndroidManifest.maxSdkVersion' ,'AndroidManifest.targetSdkVersion', 'AndroidManifest.minSdkVersion'])	

	def escreverOsMetadadosDoBuild(self, caminhoCompleto, informacoesDeVersaoDoAndroid, nomeDoArquivo):
		with open(nomeDoArquivo, 'a') as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
			spamwriter.writerow([caminhoCompleto,
				informacoesDeVersaoDoAndroid['compileSdk'],
				informacoesDeVersaoDoAndroid['targetSdk'],
				informacoesDeVersaoDoAndroid['minSdkVersion'], '', '', ''])


	def escreverOsMetadadosDoAndroidManifest(self, caminhoCompleto, informacoesDeVersaoDoAndroidManifest, nomeDoArquivo):
		with open(nomeDoArquivo, 'a') as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
			spamwriter.writerow([caminhoCompleto,
				 '', '', '',
				informacoesDeVersaoDoAndroidManifest['maxSdkVersion'],
				informacoesDeVersaoDoAndroidManifest['targetSdkVersion'],
				informacoesDeVersaoDoAndroidManifest['minSdkVersion']])