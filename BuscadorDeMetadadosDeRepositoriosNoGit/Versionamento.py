class Versionamento(object):

	def __init__(self):
		pass
		
	def find_between(self, s, first, last ):
	    try:
	        start = s.index( first ) + len( first )
	        end = s.index( last, start )
	        return s[start:end]
	    except ValueError:
	        return ""

	def find_between_r(self, s, first, last ):
	    try:
	        start = s.rindex( first ) + len( first )
	        end = s.rindex( last, start )
	        return s[start:end]
	    except ValueError:
	        return ""

	def retornaDadosDoVersionamentoDoPOM(self, arquivoXML):
		bruto = self.find_between(arquivoXML, "<parent>", "</parent>")
		
		groupId = self.find_between(bruto, '<groupId>', '</groupId>')
		artifactId = self.find_between(bruto, '<artifactId>', '</artifactId>')
		version = self.find_between(bruto, '<version>', '</version>')

		refinado = {
			'groupId' : groupId,
			'artifactId' : artifactId,
			'version' : version
		}
		return refinado