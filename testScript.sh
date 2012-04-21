#!/bin/sh

./python2perl "$1" > out.pl
chmod +x out.pl
$1 > py.out && ./out.pl > pl.out && diff py.out pl.out && rm py.out pl.out out.pl
