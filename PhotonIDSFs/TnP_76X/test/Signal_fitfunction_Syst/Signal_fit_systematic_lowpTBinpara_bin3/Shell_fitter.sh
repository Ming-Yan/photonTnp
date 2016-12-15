#!/bin/bash

#cmsRun fitterWithManyTemplates_DataLoose_MG.py outputFileName=MG

#cmsRun fitterWithManyTemplates_DataMedium_MG.py outputFileName=MG

#cmsRun fitterWithManyTemplates_DataTight_MG.py outputFileName=MG

#cmsRun fitterWithManyTemplates_DataMVA_MG.py outputFileName=MG



cmsRun fitter_Loose.py </dev/null >& testLoose_S.txt &

cmsRun fitter_Medium.py </dev/null >& testMedium_S.txt &

cmsRun fitter_Tight.py </dev/null >& testTight_S.txt &

cmsRun fitter_MVA.py </dev/null >& testMVA_S.txt &