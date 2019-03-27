
#!/bin/bash

dir_aux="/home/gabriel/Documentos/ic/Frameworks/analiseDoNumeroDeImportDoFramework/android"
dir="/home/gabriel/Documentos/ic/Frameworks/analiseDoNumeroDeImportDoFramework/android/repositorios"

while read -r linha || [[ -n "$linha" ]] 
	do
		echo linha = $linha
		var1=$(echo $linha | awk -F ", " '{print $1,$2}')   
		set -- $var1

		caminhoDoProjeto=$1
		hashDoCommitMerge=$2

		echo $dir/$caminhoDoProjeto
		
		cd $dir/$caminhoDoProjeto

		git checkout master
	
	done < "$dir_aux/googlesamples.txt" 