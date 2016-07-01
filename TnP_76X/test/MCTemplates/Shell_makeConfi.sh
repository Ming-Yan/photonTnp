#!/bin/bash 

python makeConfigForTemplates.py -i loose -o ../../python/baseline/commonFitLoose_PU65550.py -t templatesLoose_PU65550.root --var1Bins=20,30,40,50,200 --var2Bins=-2.5,-1.566,-1.4442,-1,0,1,1.4442,1.566,2.5

python makeConfigForTemplates.py -i medium -o ../../python/baseline/commonFitMedium_PU65550.py -t templatesMedium_PU65550.root --var1Bins=20,30,40,50,200 --var2Bins=-2.5,-1.566,-1.4442,-1,0,1,1.4442,1.566,2.5

python makeConfigForTemplates.py -i tight -o ../../python/baseline/commonFitTight_PU65550.py -t templatesTight_PU65550.root --var1Bins=20,30,40,50,200 --var2Bins=-2.5,-1.566,-1.4442,-1,0,1,1.4442,1.566,2.5

python makeConfigForTemplates.py -i mva -o ../../python/baseline/commonFitMVA_PU65550.py -t templatesMVA_PU65550.root --var1Bins=20,30,40,50,200 --var2Bins=-2.5,-1.566,-1.4442,-1,0,1,1.4442,1.566,2.5



#python makeConfigForTemplates.py -i loose -o ../../python/baseline/commonFitLoose_35pTCut.py -t templatesLoose_35pTCut.root --var1Bins=20,30,40,50,200 --var2Bins=-2.5,-1.566,-1.4442,-1,0,1,1.4442,1.566,2.5

#python makeConfigForTemplates.py -i medium -o ../../python/baseline/commonFitMedium_35pTCut.py -t templatesMedium_35pTCut.root --var1Bins=20,30,40,50,200 --var2Bins=-2.5,-1.566,-1.4442,-1,0,1,1.4442,1.566,2.5

#python makeConfigForTemplates.py -i tight -o ../../python/baseline/commonFitTight_35pTCut.py -t templatesTight_35pTCut.root --var1Bins=20,30,40,50,200 --var2Bins=-2.5,-1.566,-1.4442,-1,0,1,1.4442,1.566,2.5

#python makeConfigForTemplates.py -i mva -o ../../python/baseline/commonFitMVA_35pTCut.py -t templatesMVA_35pTCut.root --var1Bins=20,30,40,50,200 --var2Bins=-2.5,-1.566,-1.4442,-1,0,1,1.4442,1.566,2.5