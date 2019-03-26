import csv
class EscreveNoCSV:

	def __init__(self):
		pass



	def escreveCabecalhoDaTabela(self, nomeDoArquivo, isFork):
		with open(nomeDoArquivo, 'a') as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
			if isFork == True:
				spamwriter.writerow(['repository', 'forks', 'diskUsage_KB', 'stargazers', 'watchers', 'issues', 'commits', 'pullRequests', 'updatedAt', 'projects', 'status', 'ahead_by', 'behind_by'])
			else:
				spamwriter.writerow(['repository', 'forks', 'diskUsage_KB', 'stargazers', 'watchers', 'issues', 'commits', 'pullRequests', 'updatedAt', 'projects'])	

	def escreverOsMetadados(self, repositorio, nomeDoArquivo, dadosDaComparacao):
		with open(nomeDoArquivo, 'a') as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
			stargazers = repositorio['stargazers']
			watchers = repositorio['watchers']
			issues = repositorio['issues']
			commits = repositorio['ref']['target']['history']
			pullRequests = repositorio['pullRequests']
			projects = repositorio['projects']
			if not dadosDaComparacao == None:
				try:
					status = dadosDaComparacao['status']
					ahead_by = dadosDaComparacao['ahead_by']
					behind_by = dadosDaComparacao['behind_by']
				except Exception as e:
					status = ''
					ahead_by = ''
					behind_by = ''

				spamwriter.writerow([repositorio['nameWithOwner'], repositorio['forkCount'], repositorio['diskUsage'], stargazers['totalCount'], watchers['totalCount'], 
				issues['totalCount'], commits['totalCount'], pullRequests['totalCount'], 
				repositorio['updatedAt'], projects['totalCount'], status, ahead_by, behind_by ])
			else:
				spamwriter.writerow([repositorio['name'], repositorio['forkCount'], repositorio['diskUsage'], stargazers['totalCount'], watchers['totalCount'], 
				issues['totalCount'], commits['totalCount'], pullRequests['totalCount'], 
				repositorio['updatedAt'], projects['totalCount']])


