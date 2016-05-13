#!/usr/bin/env python

import sys
import numpy as np
from scipy.interpolate import interp1d
import pickle
import marshal

mass=sys.argv[1]
filename=sys.argv[2]

outfilename="decayWeights.pkl"
try:
  with open(outfilename, "rb") as picklefile:
   output = pickle.load(picklefile)
except:
 output = {}

output[mass]={}

masspoint = []
weight = []

filein = open(filename)
startReading = False
stopReading = False
for line in filein:
  if "Done" in line:
    stopReading = True
  if startReading and not stopReading:
    split = line.split()
    masspoint.append(float(split[0]))
    weight.append(float(split[1]))
  if "finding P_decay(m4l) distribution" in line:
    startReading=True
#f = interp1d(np.asarray(masspoint), np.asarray(weight))#, kind='cubic')
#print f

output[mass]["decayWeight"] = {'x': masspoint, 'y': weight, 'kind': 'linear'} 

with open(outfilename, "wb") as outpickle:
  pickle.dump(output, outpickle)


    
  
