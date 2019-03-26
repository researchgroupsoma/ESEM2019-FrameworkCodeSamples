import csv
class EscreveNoCSV:

	def __init__(self):
		pass



	def escreveCabecalhoDaTabela(self, nomeDoArquivo):
		with open(nomeDoArquivo, 'a') as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
			spamwriter.writerow(['release', 'date'])	

	def escreverOsMetadados(self, nomeDoArquivo, release, data):
		with open(nomeDoArquivo, 'a') as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
			spamwriter.writerow([release, data])
