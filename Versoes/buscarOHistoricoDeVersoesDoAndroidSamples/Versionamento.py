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

	def retornaDadosDoVersionamentoDoBuild(self, arquivoGradle):
		bruto = self.find_between(arquivoGradle, "android {", "}")
		if bruto == "":
			bruto = self.find_between(arquivoGradle, "ext {", "}")
			refinado = {
				'compileSdk' : self.find_between(bruto, "compileSdkVersion = ", "\n"),
			    'targetSdk' : self.find_between(bruto, "targetSdkVersion = ", "\n"),
				'minSdkVersion' : self.find_between(bruto, "minSdkVersion = ", "\n")
			}
		else :
			refinado = {
				'compileSdk' : self.find_between(bruto, "compileSdkVersion ", "\n"),
			    'targetSdk' : self.find_between(bruto, "targetSdkVersion ", "\n"),
				'minSdkVersion' : self.find_between(bruto, "minSdkVersion ", "\n")
			}

		if (bruto == "" or refinado['compileSdk'] == '' and refinado['targetSdk'] == '' and refinado['minSdkVersion'] == ''):
			refinado = {
				'compileSdk' : 'information not found',
			    'targetSdk' : 'information not found',
				'minSdkVersion' : 'information not found'
			}

		return refinado			