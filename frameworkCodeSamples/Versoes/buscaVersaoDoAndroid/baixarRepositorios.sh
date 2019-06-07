#! /bin/bash
cat 'googlesamples.txt' | while read LINE; do
    echo $LINE
    git clone $LINE
done