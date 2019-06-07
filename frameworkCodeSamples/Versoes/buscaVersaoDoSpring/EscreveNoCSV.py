import csv
class EscreveNoCSV:

	def __init__(self):
		pass



	def escreveCabecalhoDaTabela(self, nomeDoArquivo):
		with open(nomeDoArquivo, 'a') as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
			spamwriter.writerow(['path', 'groupId', 'artifactId', 'version'])	

	def escreverOsMetadados(self, caminhoCompleto, informacoesDeVersaoDoSpring, nomeDoArquivo):
		with open(nomeDoArquivo, 'a') as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
			spamwriter.writerow([caminhoCompleto,
				informacoesDeVersaoDoSpring['groupId'],
				informacoesDeVersaoDoSpring['artifactId'],
				informacoesDeVersaoDoSpring['version']])
