#!/bin/bash

mass=$1

home=/afs/cern.ch/user/l/lenzip/work/ww2016/CMSSW_8_0_5/work/JHUGenerator
node=`pwd`
cd $home
eval `scram runtime -sh`
./JHUGen DecayMode1=10 DecayMode2=10 MReso=$mass PrintPMZZ=2,5000 PrintPMZZIntervals=2499 ReweightDecay WidthSchemeIn=2 PMZZEvals=200000 &> $node/log_${mass}.txt
cp $node/log_${mass}.txt .
