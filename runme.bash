#!/bin/bash


## https://gitlab.bfabric.org/proteomics/prx/-/tree/master/src

function digestandquery(){
    echo $1 \
    | ~/bin/tryptic-digest \
    | egrep "^[A-Z]{8,30}$" \
    | python3 main.py

}


export -f digestandquery

curl -s https://fgcz-ms.uzh.ch/fasta/fgcz_10090_UP00589_cnl_20230405.fasta \
  | fcat \
  | head -n 10000 \
  | parallel -j $1 digestandquery 
