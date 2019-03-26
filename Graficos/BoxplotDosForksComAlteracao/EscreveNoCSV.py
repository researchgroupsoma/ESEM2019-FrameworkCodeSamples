import csv
class EscreveNoCSV:

	def __init__(self):
		pass



	def escreveCabecalhoDaTabela(self, nomeDoArquivo):
		with open(nomeDoArquivo, 'a') as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
			spamwriter.writerow(['sample','repository','forks','diskUsage_KB','stargazers','watchers','issues','commits','pullRequests','updatedAt','projects','status','ahead_by','behind_by'])	

	def escreverOsMetadados(self, nomeDoArquivo, objeto):
		with open(nomeDoArquivo, 'a') as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
			spamwriter.writerow([objeto['sample'],objeto['repository'],objeto['forks'],objeto['diskUsage_KB'],objeto['stargazers'],objeto['watchers'],objeto['issues'],objeto['commits'],objeto['pullRequests'],objeto['updatedAt'],objeto['projects'],objeto['status'],objeto['ahead_by'],objeto['behind_by']])