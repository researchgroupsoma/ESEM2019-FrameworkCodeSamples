import os, fnmatch

def find(pattern, path):
	result = []
	for root, dirs, files in os.walk(path):
		for name in files:
			if fnmatch.fnmatch(name, pattern):
				result.append(os.path.join(root, name))
	return result

def devolveArquivo(caminho):
	return open(caminho, 'r')

def devolveObjeto(linha):
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
		'behind_by': linhaDividida[12]
	}
	return metadados

def devolveLinhaDividida(linha):
	return linha.split(',')


def main():
	caminhos = find('*.csv', './spring')

	contadorDeProjetosSpringComCommitsAFrenteDaMaster = 0

	for caminho in caminhos:

		arquivo = devolveArquivo (caminho)

		for linha in arquivo:
			linhaDividida = devolveLinhaDividida(linha)
			# metadado = devolveObjeto(linha)

			if linhaDividida[0] != 'repository' and int(linhaDividida[11]) > 0:
				print(linha, end='')



				
main()
