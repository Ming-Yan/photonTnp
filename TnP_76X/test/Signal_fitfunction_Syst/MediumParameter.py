import FWCore.ParameterSet.Config as cms

all_pdfs = cms.PSet(
passingPresel_20p0To30p0_m2p5Tom1p566 = cms.vstring(
"RooCBExGaussShape::signalResPass(mass,meanP[0.816,-5.000,5.000],sigmaP[4.263,0.000,15.000],alphaP[34.243,0.000,50.000],nP[8.514,0.000,50.000],sigmaP_2[0.859,0.500,15.000])",
"RooCBExGaussShape::signalResFail(mass,meanF[-2.131,-5.000,5.000],sigmaF[1.329,0.000,15.000],alphaF[0.870,0.000,50.000],nF[0.850,0.000,20.000],sigmaF_2[3.018,0.500,12.000])",
"ZGeneratorLineShape::signalPhyPass(mass)",
"ZGeneratorLineShape::signalPhyFail(mass)",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.1, 0, 1], peakPass[90.0])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.1, 0, 1], peakFail[90.0])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

passingPresel_20p0To30p0_m1p566Tom1p4442 = cms.vstring(
"RooCBExGaussShape::signalResPass(mass,meanP[-2.750,-5.000,5.000],sigmaP[2.278,0.000,15.000],alphaP[0.500,0.000,50.000],nP[3.435,0.000,50.000],sigmaP_2[3.269,0.500,15.000])",
"RooCBExGaussShape::signalResFail(mass,meanF[-4.996,-5.000,5.000],sigmaF[11.611,0.000,15.000],alphaF[5.719,0.000,50.000],nF[18.372,0.000,20.000],sigmaF_2[5.254,0.500,12.000])",
"ZGeneratorLineShape::signalPhyPass(mass)",
"ZGeneratorLineShape::signalPhyFail(mass)",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.1, 0, 1], peakPass[90.0])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.1, 0, 1], peakFail[90.0])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

passingPresel_20p0To30p0_m1p4442Tom1p0 = cms.vstring(
"RooCBExGaussShape::signalResPass(mass,meanP[-0.939,-5.000,5.000],sigmaP[3.205,0.000,15.000],alphaP[1.944,0.000,50.000],nP[0.490,0.000,50.000],sigmaP_2[1.740,0.500,15.000])",
"RooCBExGaussShape::signalResFail(mass,meanF[-2.878,-5.000,5.000],sigmaF[0.136,0.000,15.000],alphaF[0.094,0.000,50.000],nF[0.758,0.000,20.000],sigmaF_2[3.428,0.500,12.000])",
"ZGeneratorLineShape::signalPhyPass(mass)",
"ZGeneratorLineShape::signalPhyFail(mass)",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.1, 0, 1], peakPass[90.0])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.1, 0, 1], peakFail[90.0])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

passingPresel_20p0To30p0_m1p0To0p0 = cms.vstring(
"RooCBExGaussShape::signalResPass(mass,meanP[0.016,-5.000,5.000],sigmaP[2.646,0.000,15.000],alphaP[2.005,0.000,50.000],nP[0.491,0.000,50.000],sigmaP_2[1.151,0.500,15.000])",
"RooCBExGaussShape::signalResFail(mass,meanF[-2.130,-5.000,5.000],sigmaF[0.103,0.000,15.000],alphaF[0.317,0.000,50.000],nF[0.525,0.000,20.000],sigmaF_2[2.725,0.500,12.000])",
"ZGeneratorLineShape::signalPhyPass(mass)",
"ZGeneratorLineShape::signalPhyFail(mass)",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.1, 0, 1], peakPass[90.0])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.1, 0, 1], peakFail[90.0])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

passingPresel_20p0To30p0_0p0To1p0 = cms.vstring(
"RooCBExGaussShape::signalResPass(mass,meanP[0.060,-5.000,5.000],sigmaP[2.675,0.000,15.000],alphaP[2.106,0.000,50.000],nP[0.411,0.000,50.000],sigmaP_2[1.134,0.500,15.000])",
"RooCBExGaussShape::signalResFail(mass,meanF[-2.139,-5.000,5.000],sigmaF[0.079,0.000,15.000],alphaF[0.272,0.000,50.000],nF[0.530,0.000,20.000],sigmaF_2[2.722,0.500,12.000])",
"ZGeneratorLineShape::signalPhyPass(mass)",
"ZGeneratorLineShape::signalPhyFail(mass)",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.1, 0, 1], peakPass[90.0])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.1, 0, 1], peakFail[90.0])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

passingPresel_20p0To30p0_1p0To1p4442 = cms.vstring(
"RooCBExGaussShape::signalResPass(mass,meanP[-0.965,-5.000,5.000],sigmaP[3.249,0.000,15.000],alphaP[1.872,0.000,50.000],nP[0.526,0.000,50.000],sigmaP_2[1.737,0.500,15.000])",
"RooCBExGaussShape::signalResFail(mass,meanF[-2.900,-5.000,5.000],sigmaF[0.146,0.000,15.000],alphaF[0.094,0.000,50.000],nF[0.761,0.000,20.000],sigmaF_2[3.444,0.500,12.000])",
"ZGeneratorLineShape::signalPhyPass(mass)",
"ZGeneratorLineShape::signalPhyFail(mass)",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.1, 0, 1], peakPass[90.0])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.1, 0, 1], peakFail[90.0])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

passingPresel_20p0To30p0_1p4442To1p566 = cms.vstring(
"RooCBExGaussShape::signalResPass(mass,meanP[-2.980,-5.000,5.000],sigmaP[1.356,0.000,15.000],alphaP[0.299,0.000,50.000],nP[3.755,0.000,50.000],sigmaP_2[3.280,0.500,15.000])",
"RooCBExGaussShape::signalResFail(mass,meanF[-4.857,-5.000,5.000],sigmaF[11.645,0.000,15.000],alphaF[4.193,0.000,50.000],nF[5.435,0.000,20.000],sigmaF_2[5.081,0.500,12.000])",
"ZGeneratorLineShape::signalPhyPass(mass)",
"ZGeneratorLineShape::signalPhyFail(mass)",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.1, 0, 1], peakPass[90.0])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.1, 0, 1], peakFail[90.0])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

passingPresel_20p0To30p0_1p566To2p5 = cms.vstring(
"RooCBExGaussShape::signalResPass(mass,meanP[-0.266,-5.000,5.000],sigmaP[3.067,0.000,15.000],alphaP[2.047,0.000,50.000],nP[0.565,0.000,50.000],sigmaP_2[1.518,0.500,15.000])",
"RooCBExGaussShape::signalResFail(mass,meanF[-2.122,-5.000,5.000],sigmaF[1.388,0.000,15.000],alphaF[0.894,0.000,50.000],nF[0.783,0.000,20.000],sigmaF_2[3.064,0.500,12.000])",
"ZGeneratorLineShape::signalPhyPass(mass)",
"ZGeneratorLineShape::signalPhyFail(mass)",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.1, 0, 1], peakPass[90.0])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.1, 0, 1], peakFail[90.0])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

)