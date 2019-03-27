
#!/bin/bash

dir_aux="/home/gabriel/Documentos/ic/Frameworks/analiseDasMensagensDosCommits/spring/repositorios"
dir="/home/gabriel/Documentos/ic/Frameworks/analiseDasMensagensDosCommits/spring/repositorios"

while read -r linha || [[ -n "$linha" ]] 
	do
		echo linha = $linha
		
		cd $dir/$linha

		git checkout master
		
		git log --pretty=format:"%s" > $dir/$linha.txt #number of changes M A D
		
	done < "$dir_aux/springsamples.txt" 