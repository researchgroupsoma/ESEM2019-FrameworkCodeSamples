#! /bin/bash

cd 'repositorios/'
cat 'springsamples.txt' | while read LINE; do
    echo $LINE


 #    var1=$(echo $LINE | awk -F ", " '{print $1,$2}')   
	# set -- $var1
	# nomeCompletoDoRepositorio=$1

	# var1=$(echo $nomeCompletoDoRepositorio | awk -F "/" '{print $1,$2}')   
	# set -- $var1
	# nomeDoUser=$1
	# nomeDoRepositorio=$2

    # mkdir $nomeDoUser
    # cd $nomeDoUser
    git clone https://github.com/spring-guides/$LINE
    #cd ..
done