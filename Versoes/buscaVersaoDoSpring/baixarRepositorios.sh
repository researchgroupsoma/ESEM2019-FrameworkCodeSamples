#! /bin/bash
cat 'springsamples.txt' | while read LINE; do
    echo $LINE
    cd repositorios
    git clone $LINE
    cd ..
done