def retornaArquivo(nomeDoArquivo):
	arquivo = ''
	try:
		arquivo = open(nomeDoArquivo, 'r')
	except Exception as e:
		output  = io.BytesIO()
		arquivo = io.TextIOWrapper(output, encoding='cp1252', line_buffering=True)
	return arquivo


arquivo = retornaArquivo("onlyCreationDates.csv")

for linha in arquivo:
	linha = linha.replace("\n", "")
	linha = linha.split(" ")[0]
	linha = linha.split("-")
	# linha = linha[0] + "-" + linha[1]
	print(linha[0])