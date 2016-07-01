#!/bin/bash

cmsRun fitterWithManyTemplates_DataLoose_BGSys.py outputFileName=BGSys

cmsRun fitterWithManyTemplates_DataMedium_BGSys.py outputFileName=BGSys

cmsRun fitterWithManyTemplates_DataTight_BGSys.py outputFileName=BGSys

cmsRun fitterWithManyTemplates_DataMVA_BGSys.py outputFileName=BGSys



#cmsRun fitter_Loose.py </dev/null >& testLoose_S.txt &

#cmsRun fitter_Medium.py </dev/null >& testMedium_S.txt &

#cmsRun fitter_Tight.py

#cmsRun fitter_MVA.py
