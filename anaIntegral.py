from ROOT import *
import sys
import numpy as np
import pickle

filein=TFile(sys.argv[1])
treeName="myTree"
tree=filein.Get(treeName)
cprimestart = float(sys.argv[2])
cprimestop  = float(sys.argv[3])
cprimestep  = float(sys.argv[4])
brnewstart = float(sys.argv[5])
brnewstop  = float(sys.argv[6])
brnewstep  = float(sys.argv[7])
mass = sys.argv[8]

cprimes = np.arange(cprimestart, cprimestop, cprimestep).tolist()
brnews  = np.arange(brnewstart, brnewstop, brnewstep).tolist()
if (cprimestop) not in cprimes:
  cprimes.append(cprimestop)
if (brnewstart) not in brnews:
  brnews.insert(0, brnewstart)

TH1.SetDefaultSumw2()
fileout=TFile(sys.argv[2], "recreate")
fileout.cd()
original=TH1F("original", "original", 200, 0, 5000)
error=Double(0.)
tree.Draw("higgsLHEMass>>original")
integralOrig=original.IntegralAndError(1, 200, error)
print "original", integralOrig, "+/-", error
original.Write()
filecontent=""
try:
  with open("globalShiftsReweighting.pkl", "rb") as picklefile:
    output = pickle.load(picklefile)
except:
  output = {}
output[mass]={}  
for cprime in cprimes:
  output[mass]["cprime"+str(cprime)]={}  
  for brnew in brnews:
    output[mass]["cprime"+str(cprime)]["brnew"+str(brnew)]={}
    name="cprime"+str(cprime)+"BRnew"+str(brnew)
    plot=TH1F(name, name, 200, 0, 5000)
    tree.Draw("higgsLHEMass>>"+name, name)
    error=Double(0.)
    integral=plot.IntegralAndError(1,200,error)
    filecontent += mass+" "+str(cprime)+" "+str(brnew)+" "+str(integral/integralOrig)+"\n" 
    output[mass]["cprime"+str(cprime)]["brnew"+str(brnew)]["weight"]=integral/integralOrig
    print name, integral, "+/-", error

    plot.Write()
with open("globalShiftsReweighting.pkl", "wb") as outpickle: 
  pickle.dump(output, outpickle)
with open("globalShiftsReweighting.txt", "a") as myfile:
  myfile.write(filecontent)
#fileout.Write()    


    
