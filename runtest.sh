#!/bin/bash
#by anthony
#2016-09-27

LMDIR=/home/anthony/Git/pocketsphinx/model/en-us/en-us.lm.bin
DICTDIR=/home/anthony/Git/pocketsphinx/model/en-us/cmudict-en-us.dict
HMMDIR=/home/anthony/Git/pocketsphinx/model/en-us/en-us

testFile1="/home/anthony/Git/pocketsphinx/test/data/goforward.raw"
echo $testFile1
resultFile1="$testFile1.txt"	
echo $resultFile1
pocketsphinx_continuous -lm $LMDIR -dict $DICTDIR -hmm $HMMDIR -infile $testFile1 > $resultFile1

testFile2="/home/anthony/Git/pocketsphinx/test/data/cards/001.wav"
echo $testFile2
resultFile2="$testFile2.txt"	
echo $resultFile2
pocketsphinx_continuous -lm $LMDIR -dict $DICTDIR -hmm $HMMDIR -infile $testFile2 > $resultFile2

echo "result of test 1: $(tail $resultFile1)"
echo "result of test 2: $(tail $resultFile2)"
