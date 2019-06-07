import subprocess
from git import Repo
import EscreveNoCSV
from datetime import datetime

def main():
	e = EscreveNoCSV.EscreveNoCSV()
	e.escreveCabecalhoDaTabela("springRealeases.csv")

	repo = Repo("./spring-boot/")

	for tag in repo.tags:
		dataDoCommit = tag.commit.committed_date
		utc_offset = datetime.fromtimestamp(dataDoCommit) - datetime.utcfromtimestamp(dataDoCommit)

		print( utc_offset  )
		dataDoCommitEmDatetime = datetime.utcfromtimestamp(dataDoCommit).strftime('%Y-%m-%d %H:%M:%S.%f%z')
		e.escreverOsMetadados("springRealeases.csv", tag, dataDoCommitEmDatetime)

main()
