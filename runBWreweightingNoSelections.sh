#!/bin/bash

home=/afs/cern.ch/user/l/lenzip/work/ww2016/CMSSW_8_0_5/work/LineshapeTools
treesIn=eos/cms/store/user/lviliani/highMassNoSel/trees/
treesOu=eos/cms/store/user/lenzip/highMassNoSel/trees/

process=$1
mass=$2

cd $home
eval `scram runtime -sh`
cd -

/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select -b fuse mount eos

gardener.py BWEwkSingletReweighter $treesIn/latino_${process}HToWWTo2L2Nu_M${mass}_1.root . -u -t "Analyzer/myTree" -p "latino_(GluGlu|VBF)HToWWTo2L2Nu_M([0-9]+)_1.root" -w "" -k "" -i 0.05 -f 1.0 -s 0.05 -l 0 -n 1 -q 0.05 -p "latino_(GluGlu|VBF)HToWWTo2L2Nu_M([0-9]+)_1.root"

cp latino_${process}HToWWTo2L2Nu_M${mass}_1.root $treesOu/

/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select -b fuse umount eos
rmdir eos
