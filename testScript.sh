#!/bin/sh

for f in $@
do
    ./python2perl "$f" > out.pl
    chmod +x out.pl
    if $1 > py.out && ./out.pl > pl.out && diff py.out pl.out && rm py.out pl.out out.pl
    then
       echo "$f passed"
    else
       echo "$f failed"
    fi
done
