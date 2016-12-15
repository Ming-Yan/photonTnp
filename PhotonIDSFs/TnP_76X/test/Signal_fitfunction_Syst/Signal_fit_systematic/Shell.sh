#!/bin/bash                                                                                                                                  

#cmsRun fitterWithManyTemplates_DataMVA_35pTCut.py outputFileName=35pTCut

#python dumpPlotFromEffFile.py -i efficiency-data-passingLoose-Signal.root -d PhotonToRECO -b True
python dumpPlotFromEffFile.py -i efficiency-data-passingMedium-Signal.root -d PhotonToRECO -b True
python dumpPlotFromEffFile.py -i efficiency-data-passingTight-Signal.root -d PhotonToRECO -b True
python dumpPlotFromEffFile.py -i efficiency-data-passingMVA-Signal.root -d PhotonToRECO -b True