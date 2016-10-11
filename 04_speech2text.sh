#!/bin/bash
#by anthony
#2016-10-11
LMDIR=/home/anthony/Git/pocketsphinx/model/en-us/en-us.lm.bin
DICTDIR=/home/anthony/Git/pocketsphinx/model/en-us/cmudict-en-us.dict
HMMDIR=/home/anthony/Git/pocketsphinx/model/en-us/en-us

WAV=$1.wav
TXT=$WAV.txt
ffmpeg -i $1 -ar 16000 $WAV

pocketsphinx_continuous -lm $LMDIR -dict $DICTDIR -hmm $HMMDIR -infile $WAV > $TXT

