#!/bin/bash

curl -s https://fgcz-ms.uzh.ch/fasta/fgcz_10090_UP00589_cnl_20230405.fasta \
  | fcat \
  | head -n 1000 \
  | while read i;
  do
    echo 
    echo $i \
    | tryptic-digest \
    | egrep "^[A-Z]{8,30}$" \
    | python3 main.py
  done
