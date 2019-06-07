
#!/bin/bash

dir_aux="/home/gabriel/Documentos/ic/Frameworks/analiseDoUltimoCommit/spring/repositorios"
dir="/home/gabriel/Documentos/ic/Frameworks/analiseDoUltimoCommit/spring/repositorios"

while read -r linha || [[ -n "$linha" ]] 
	do
		echo linha = $linha
		
		cd $dir/$linha

		git checkout master
		
		#git log --full-diff -p --raw --minimal > /home/facom/Documents/Teste/GIT/Tools/gitDiff/$pasta.txt #historico
		#git log --stat --pretty=format:"%h; %an; %ad; %ar; %cd; %s" > $dir/Samples/gitLog/$pasta.txt # ++ --
		git log --name-status --stat --pretty=format:"$linha;%h;%s" HEAD^..HEAD > $dir/$linha.txt
		#git log --shortstat --pretty=format:"%h; %an; %ad; %ar; %cd; %s" > $dir/Samples/gitLog/$pasta.txt #number of changes
		# git log --name-status --stat --pretty=format:"$pasta;%h;%s" > $dir/$linha.txt #number of changes M A D
		# git log --name-status --stat --pretty=format:"$caminhoDoProjeto;%h;%s" $hashDoCommitMerge...HEAD > $dir/$caminhoDoProjeto.txt
		# echo "\n" > $dir/$pasta.txt
		#git log --pretty=format:"$eco;$pasta;%h;%an;%ad;%s" > $dir/Samples/gitLog/$pasta.txt # descrição simplificada

	done < "$dir_aux/springsamples.txt" 