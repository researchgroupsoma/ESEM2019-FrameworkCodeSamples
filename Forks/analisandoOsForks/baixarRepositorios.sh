#! /bin/bash

cat 'spring.txt' | while read LINE; do
    echo $LINE
    cd 'repositorios/spring'

    var1=$(echo $LINE | awk -F ", " '{print $1,$2}')   
	set -- $var1
	nomeCompletoDoRepositorio=$1

	var1=$(echo $nomeCompletoDoRepositorio | awk -F "/" '{print $1,$2}')   
	set -- $var1
	nomeDoUser=$1
	nomeDoRepositorio=$2

    mkdir $nomeDoUser
    cd $nomeDoUser
    git clone https://github.com/$nomeDoUser/$nomeDoRepositorio
    cd ..
    cd ..
    cd ..
done