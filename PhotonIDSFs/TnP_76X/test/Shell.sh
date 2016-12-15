#!/bin/bash                                                                                                                                  

#cmsRun fitterWithManyTemplates_DataMVA_35pTCut.py outputFileName=35pTCut

python dumpPlotFromEffFile.py -i efficiency-data-passingLoose-BGSys.root -d PhotonToRECO -b True
python dumpPlotFromEffFile.py -i efficiency-data-passingMedium-BGSys.root -d PhotonToRECO -b True
python dumpPlotFromEffFile.py -i efficiency-data-passingTight-BGSys.root -d PhotonToRECO -b True
python dumpPlotFromEffFile.py -i efficiency-data-passingMVA-BGSys.root -d PhotonToRECO -b True