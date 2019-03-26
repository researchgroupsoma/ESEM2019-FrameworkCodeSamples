import os, fnmatch, EscreveNoCSV

def find(pattern, path):
	result = []
	for root, dirs, files in os.walk(path):
		for name in files:
			if fnmatch.fnmatch(name, pattern):
				result.append(os.path.join(root, name))
	return result

def devolveArquivo(caminho):
	return open(caminho, 'r')

def devolveObjeto(linha, sample):
	linhaDividida = devolveLinhaDividida(linha)

	if linhaDividida[0] == 'repository':
		linhaDividida[11] = 0

	metadados = {
		'repository' : linhaDividida[0],
		'forks': linhaDividida[1],
		'diskUsage_KB': linhaDividida[2],
		'stargazers': linhaDividida[3],
		'watchers': linhaDividida[4],
		'issues': linhaDividida[5],
		'commits': linhaDividida[6],
		'pullRequests': linhaDividida[7],
		'updatedAt': linhaDividida[8],
		'projects': linhaDividida[9],
		'status': linhaDividida[10],
		'ahead_by': linhaDividida[11],
		'behind_by': linhaDividida[12],
		'sample': sample
	}
	return metadados

def devolveLinhaDividida(linha):
	return linha.split(',')


def main(sample):
	escreveNoCSV = EscreveNoCSV.EscreveNoCSV()


	escreveNoCSV.escreveCabecalhoDaTabela('tabela.csv')

	caminhos = find('*.csv', './'+sample)

	for caminho in caminhos:
		print(caminho)
		arquivo = devolveArquivo (caminho)

		for linha in arquivo:
			metadado = devolveObjeto(linha, sample)
			if ( int(metadado['ahead_by']) > 0):
				escreveNoCSV.escreverOsMetadados('tabela.csv', metadado)






main('spring')
main('android')