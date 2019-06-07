from datetime import datetime

class Commit():

	def mapeaMesParaInteiro(self, mes):
		inteiro = 0
		if mes == 'Jan':
			inteiro = 1
		if mes == 'Feb':
			inteiro = 2
		if mes == 'Mar':
			inteiro = 3
		if mes == 'Apr':
			inteiro = 4
		if mes == 'May':
			inteiro = 5
		if mes == 'Jun':
			inteiro = 6
		if mes == 'Jul':
			inteiro = 7
		if mes == 'Aug':
			inteiro = 8
		if mes == 'Sep':
			inteiro = 9
		if mes == 'Oct':
			inteiro = 10
		if mes == 'Nov':
			inteiro = 11
		if mes == 'Dec':
			inteiro = 12
		return inteiro

	def retornaDataFormatada(self, data):
		vetor = data.split(" ")
		dataFormatada = vetor[4] + "-" + str(self.mapeaMesParaInteiro(vetor[1])) + "-" + vetor[2]
		dataFormatada = datetime.strptime(dataFormatada, "%Y-%m-%d")
		return dataFormatada

	def delay(self, dataDoFramework):
	    dataDoFramework = datetime.strptime(dataDoFramework, "%Y-%m-%d")
	    data = (self.data - dataDoFramework).days
	    if data < 0:
	    	data = 0
	    return data

	def toString(self):
		return ''+self.caminhoDoArquivo + ", "+ self.hashNumber + ", "+ self.data

	def __init__(self, caminhoDoArquivo, hashNumber, data):
		self.caminhoDoArquivo = caminhoDoArquivo
		self.hashNumber = hashNumber
		self.data = self.retornaDataFormatada(data)
