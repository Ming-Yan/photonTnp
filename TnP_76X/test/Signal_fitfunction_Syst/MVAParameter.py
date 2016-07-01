import FWCore.ParameterSet.Config as cms

all_pdfs = cms.PSet(
passingPresel_20p0To30p0_m2p5Tom1p566 = cms.vstring(
"RooCBExGaussShape::signalResPass(mass,meanP[1.083,-5.000,5.000],sigmaP[4.673,0.000,15.000],alphaP[42.912,0.000,50.000],nP[20.002,0.000,50.000],sigmaP_2[0.669,0.500,15.000])",
"RooCBExGaussShape::signalResFail(mass,meanF[-3.839,-5.000,5.000],sigmaF[0.104,0.000,15.000],alphaF[0.146,0.000,50.000],nF[0.486,0.000,20.000],sigmaF_2[5.283,0.500,12.000])",
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
"RooCBExGaussShape::signalResPass(mass,meanP[-2.632,-5.000,5.000],sigmaP[1.439,0.000,15.000],alphaP[0.203,0.000,50.000],nP[7.831,0.000,50.000],sigmaP_2[3.167,0.500,15.000])",
"RooCBExGaussShape::signalResFail(mass,meanF[-5.000,-5.000,5.000],sigmaF[12.287,0.000,15.000],alphaF[5.960,0.000,50.000],nF[13.535,0.000,20.000],sigmaF_2[5.991,0.500,12.000])",
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
"RooCBExGaussShape::signalResPass(mass,meanP[-0.965,-5.000,5.000],sigmaP[3.172,0.000,15.000],alphaP[1.782,0.000,50.000],nP[0.612,0.000,50.000],sigmaP_2[1.727,0.500,15.000])",
"RooCBExGaussShape::signalResFail(mass,meanF[-4.107,-5.000,5.000],sigmaF[0.003,0.000,15.000],alphaF[0.002,0.000,50.000],nF[0.487,0.000,20.000],sigmaF_2[5.758,0.500,12.000])",
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
"RooCBExGaussShape::signalResPass(mass,meanP[-0.041,-5.000,5.000],sigmaP[2.593,0.000,15.000],alphaP[1.877,0.000,50.000],nP[0.567,0.000,50.000],sigmaP_2[1.179,0.500,15.000])",
"RooCBExGaussShape::signalResFail(mass,meanF[-3.297,-5.000,5.000],sigmaF[0.003,0.000,15.000],alphaF[0.038,0.000,50.000],nF[0.229,0.000,20.000],sigmaF_2[4.879,0.500,12.000])",
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
"RooCBExGaussShape::signalResPass(mass,meanP[-0.003,-5.000,5.000],sigmaP[2.614,0.000,15.000],alphaP[1.955,0.000,50.000],nP[0.517,0.000,50.000],sigmaP_2[1.163,0.500,15.000])",
"RooCBExGaussShape::signalResFail(mass,meanF[-0.483,-5.000,5.000],sigmaF[15.000,0.000,15.000],alphaF[6.468,0.000,50.000],nF[17.530,0.000,20.000],sigmaF_2[5.248,0.500,12.000])",
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
"RooCBExGaussShape::signalResPass(mass,meanP[-0.981,-5.000,5.000],sigmaP[3.236,0.000,15.000],alphaP[1.738,0.000,50.000],nP[0.631,0.000,50.000],sigmaP_2[1.725,0.500,15.000])",
"RooCBExGaussShape::signalResFail(mass,meanF[-4.084,-5.000,5.000],sigmaF[0.041,0.000,15.000],alphaF[0.024,0.000,50.000],nF[0.488,0.000,20.000],sigmaF_2[5.638,0.500,12.000])",
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
"RooCBExGaussShape::signalResPass(mass,meanP[-2.734,-5.000,5.000],sigmaP[0.315,0.000,15.000],alphaP[0.043,0.000,50.000],nP[9.937,0.000,50.000],sigmaP_2[3.145,0.500,15.000])",
"RooCBExGaussShape::signalResFail(mass,meanF[-5.000,-5.000,5.000],sigmaF[12.051,0.000,15.000],alphaF[7.242,0.000,50.000],nF[19.974,0.000,20.000],sigmaF_2[5.803,0.500,12.000])",
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
"RooCBExGaussShape::signalResPass(mass,meanP[-0.349,-5.000,5.000],sigmaP[3.028,0.000,15.000],alphaP[1.879,0.000,50.000],nP[0.699,0.000,50.000],sigmaP_2[1.549,0.500,15.000])",
"RooCBExGaussShape::signalResFail(mass,meanF[-3.949,-5.000,5.000],sigmaF[0.048,0.000,15.000],alphaF[0.086,0.000,50.000],nF[0.434,0.000,20.000],sigmaF_2[5.347,0.500,12.000])",
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