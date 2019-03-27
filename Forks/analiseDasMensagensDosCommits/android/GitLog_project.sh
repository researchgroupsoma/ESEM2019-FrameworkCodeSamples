#!/bin/bash

dir_aux="/home/gabriel/Documentos/ic/Forks/analiseDasMensagensDosCommits/android"
dir="/home/gabriel/Documentos/ic/Forks/analiseDasMensagensDosCommits/android/repositorios"

while read -r linha || [[ -n "$linha" ]] 
	do
		echo linha = $linha
		var1=$(echo $linha | awk -F ", " '{print $1,$2}')   
		set -- $var1

		caminhoDoProjeto=$1
		hashDoCommitMerge=$2

		var2=$(echo $caminhoDoProjeto | awk -F "/" '{print $1,$2}')   
		set -- $var1

		nomeDoFork=$1

		echo $dir/$caminhoDoProjeto
		
		cd $dir/$caminhoDoProjeto

		git checkout master
		
		git log --pretty=format:"%s" $hashDoCommitMerge...HEAD > $dir/$nomeDoFork.texto
		
	done < "$dir_aux/android.txt" 