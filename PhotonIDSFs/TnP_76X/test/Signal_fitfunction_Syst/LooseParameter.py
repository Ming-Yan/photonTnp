import FWCore.ParameterSet.Config as cms

all_pdfs = cms.PSet(
passingPresel_20p0To30p0_m2p5Tom1p566 = cms.vstring(
"RooCBExGaussShape::signalResPass(mass,meanP[-0.522,-5.000,5.000],sigmaP[2.866,0.000,15.000],alphaP[2.024,0.000,50.000],nP[0.600,0.000,50.000],sigmaP_2[1.685,0.500,15.000])",
"RooCBExGaussShape::signalResFail(mass,meanF[-2.894,-5.000,5.000],sigmaF[0.129,0.000,15.000],alphaF[0.112,0.000,50.000],nF[0.720,0.000,20.000],sigmaF_2[3.803,0.500,12.000])",
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
"RooCBExGaussShape::signalResPass(mass,meanP[-2.629,-5.000,5.000],sigmaP[2.716,0.000,15.000],alphaP[0.480,0.000,50.000],nP[4.936,0.000,50.000],sigmaP_2[3.225,0.500,15.000])",
"RooCBExGaussShape::signalResFail(mass,meanF[-5.000,-5.000,5.000],sigmaF[13.033,0.000,15.000],alphaF[49.682,0.000,50.000],nF[2.527,0.000,20.000],sigmaF_2[5.269,0.500,12.000])",
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
"RooCBExGaussShape::signalResPass(mass,meanP[-0.957,-5.000,5.000],sigmaP[3.202,0.000,15.000],alphaP[1.875,0.000,50.000],nP[0.558,0.000,50.000],sigmaP_2[1.750,0.500,15.000])",
"RooCBExGaussShape::signalResFail(mass,meanF[-3.724,-5.000,5.000],sigmaF[0.118,0.000,15.000],alphaF[0.042,0.000,50.000],nF[0.578,0.000,20.000],sigmaF_2[5.229,0.500,12.000])",
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
"RooCBExGaussShape::signalResPass(mass,meanP[-0.003,-5.000,5.000],sigmaP[2.640,0.000,15.000],alphaP[1.962,0.000,50.000],nP[0.530,0.000,50.000],sigmaP_2[1.165,0.500,15.000])",
"RooCBExGaussShape::signalResFail(mass,meanF[2.211,-5.000,5.000],sigmaF[15.000,0.000,15.000],alphaF[7.449,0.000,50.000],nF[12.784,0.000,20.000],sigmaF_2[1.755,0.500,12.000])",
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
"RooCBExGaussShape::signalResPass(mass,meanP[0.065,-5.000,5.000],sigmaP[2.693,0.000,15.000],alphaP[2.069,0.000,50.000],nP[0.444,0.000,50.000],sigmaP_2[1.137,0.500,15.000])",
"RooCBExGaussShape::signalResFail(mass,meanF[-2.361,-5.000,5.000],sigmaF[0.049,0.000,15.000],alphaF[0.178,0.000,50.000],nF[0.376,0.000,20.000],sigmaF_2[3.387,0.500,12.000])",
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
"RooCBExGaussShape::signalResPass(mass,meanP[-0.966,-5.000,5.000],sigmaP[3.275,0.000,15.000],alphaP[1.823,0.000,50.000],nP[0.580,0.000,50.000],sigmaP_2[1.744,0.500,15.000])",
"RooCBExGaussShape::signalResFail(mass,meanF[-3.716,-5.000,5.000],sigmaF[0.166,0.000,15.000],alphaF[0.057,0.000,50.000],nF[0.575,0.000,20.000],sigmaF_2[5.162,0.500,12.000])",
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
"RooCBExGaussShape::signalResPass(mass,meanP[-2.883,-5.000,5.000],sigmaP[1.272,0.000,15.000],alphaP[0.217,0.000,50.000],nP[6.247,0.000,50.000],sigmaP_2[3.255,0.500,15.000])",
"RooCBExGaussShape::signalResFail(mass,meanF[-5.000,-5.000,5.000],sigmaF[12.894,0.000,15.000],alphaF[14.505,0.000,50.000],nF[3.870,0.000,20.000],sigmaF_2[5.175,0.500,12.000])",
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
"RooCBExGaussShape::signalResPass(mass,meanP[1.195,-5.000,5.000],sigmaP[4.738,0.000,15.000],alphaP[11.380,0.000,50.000],nP[20.184,0.000,50.000],sigmaP_2[0.605,0.500,15.000])",
"RooCBExGaussShape::signalResFail(mass,meanF[-3.054,-5.000,5.000],sigmaF[0.132,0.000,15.000],alphaF[0.128,0.000,50.000],nF[0.639,0.000,20.000],sigmaF_2[3.997,0.500,12.000])",
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