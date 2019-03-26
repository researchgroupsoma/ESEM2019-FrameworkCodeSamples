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

	objeto = {
		'a_head' : linhaDividida[11]
	}
	return objeto

def devolveLinhaDividida(linha):
	return linha.split(',')



caminhos = find('*.csv', '.')

contador = 0

for caminho in caminhos:
	print(caminho)
	arquivo = devolveArquivo(caminho)
	for linha in arquivo:
		valorDoAhead = int (devolveObjeto(linha)['a_head'])
		if valorDoAhead > 0:
			contador = contador + 1

print(contador)