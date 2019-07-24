#! /bin/bash


cat 'samples.txt' | while read LINE; do
    echo $LINE


    var1=$(echo $LINE | awk -F ", " '{print $1,$2}')   
	set -- $var1
	nomeCompletoDoRepositorio=$1

	var1=$(echo $nomeCompletoDoRepositorio | awk -F "/" '{print $1,$2}')   
	set -- $var1
	nomeDoUser=$1
	nomeDoRepositorio=$2

    mkdir "/home/gabriel/Documentos/ic/frameworkCodeSamples/Samples/repositorios/"$nomeDoUser
    cd "/home/gabriel/Documentos/ic/frameworkCodeSamples/Samples/repositorios/"$nomeDoUser
    git clone https://github.com/$LINE
    
done
