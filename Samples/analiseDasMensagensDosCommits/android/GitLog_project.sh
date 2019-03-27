
#!/bin/bash

dir_aux="/home/gabriel/Documentos/ic/Frameworks/analiseDasMensagensDosCommits/android/repositorios"
dir="/home/gabriel/Documentos/ic/Frameworks/analiseDasMensagensDosCommits/android/repositorios"

while read -r linha || [[ -n "$linha" ]] 
	do
		echo linha = $linha
		# var1=$(echo $linha | awk -F ", " '{print $1,$2}')   
		# set -- $var1

		# caminhoDoProjeto=$1
		# hashDoCommitMerge=$2

		# echo $dir/$caminhoDoProjeto
		
		cd $dir/$linha

		git checkout master
		
		git log --pretty=format:"%s" > $dir/$linha.txt #number of changes M A D
		
	done < "$dir_aux/googlesamples.txt" 