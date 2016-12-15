import FWCore.ParameterSet.Config as cms

all_pdfs = cms.PSet(
passingPresel_20p0To30p0_m2p5Tom1p566 = cms.vstring(
"RooCBExGaussShape::signalResPass(mass,meanP[0.819,-5.000,5.000],sigmaP[4.237,0.000,15.000],alphaP[33.892,0.000,50.000],nP[8.973,0.000,50.000],sigmaP_2[0.856,0.500,15.000])",
"RooCBExGaussShape::signalResFail(mass,meanF[-2.320,-5.000,5.000],sigmaF[0.282,0.000,15.000],alphaF[0.267,0.000,50.000],nF[1.002,0.000,20.000],sigmaF_2[2.916,0.500,12.000])",
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
"RooCBExGaussShape::signalResPass(mass,meanP[-2.227,-5.000,5.000],sigmaP[3.784,0.000,15.000],alphaP[0.861,0.000,50.000],nP[2.764,0.000,50.000],sigmaP_2[3.003,0.500,15.000])",
"RooCBExGaussShape::signalResFail(mass,meanF[-3.025,-5.000,5.000],sigmaF[12.192,0.000,15.000],alphaF[7.123,0.000,50.000],nF[0.039,0.000,20.000],sigmaF_2[4.098,0.500,12.000])",
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
"RooCBExGaussShape::signalResPass(mass,meanP[-0.942,-5.000,5.000],sigmaP[3.186,0.000,15.000],alphaP[1.971,0.000,50.000],nP[0.460,0.000,50.000],sigmaP_2[1.744,0.500,15.000])",
"RooCBExGaussShape::signalResFail(mass,meanF[-2.784,-5.000,5.000],sigmaF[0.226,0.000,15.000],alphaF[0.176,0.000,50.000],nF[0.846,0.000,20.000],sigmaF_2[3.133,0.500,12.000])",
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
"RooCBExGaussShape::signalResPass(mass,meanP[0.020,-5.000,5.000],sigmaP[2.644,0.000,15.000],alphaP[2.026,0.000,50.000],nP[0.473,0.000,50.000],sigmaP_2[1.150,0.500,15.000])",
"RooCBExGaussShape::signalResFail(mass,meanF[-1.031,-5.000,5.000],sigmaF[1.650,0.000,15.000],alphaF[1.307,0.000,50.000],nF[0.535,0.000,20.000],sigmaF_2[2.066,0.500,12.000])",
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
"RooCBExGaussShape::signalResPass(mass,meanP[0.085,-5.000,5.000],sigmaP[2.683,0.000,15.000],alphaP[2.117,0.000,50.000],nP[0.401,0.000,50.000],sigmaP_2[1.117,0.500,15.000])",
"RooCBExGaussShape::signalResFail(mass,meanF[-1.015,-5.000,5.000],sigmaF[1.663,0.000,15.000],alphaF[1.356,0.000,50.000],nF[0.524,0.000,20.000],sigmaF_2[2.060,0.500,12.000])",
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
"RooCBExGaussShape::signalResPass(mass,meanP[-0.946,-5.000,5.000],sigmaP[3.256,0.000,15.000],alphaP[1.891,0.000,50.000],nP[0.507,0.000,50.000],sigmaP_2[1.717,0.500,15.000])",
"RooCBExGaussShape::signalResFail(mass,meanF[-2.830,-5.000,5.000],sigmaF[0.231,0.000,15.000],alphaF[0.176,0.000,50.000],nF[0.830,0.000,20.000],sigmaF_2[3.171,0.500,12.000])",
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
"RooCBExGaussShape::signalResPass(mass,meanP[-2.645,-5.000,5.000],sigmaP[3.096,0.000,15.000],alphaP[0.726,0.000,50.000],nP[2.926,0.000,50.000],sigmaP_2[3.169,0.500,15.000])",
"RooCBExGaussShape::signalResFail(mass,meanF[-3.093,-5.000,5.000],sigmaF[12.101,0.000,15.000],alphaF[3.277,0.000,50.000],nF[1.012,0.000,20.000],sigmaF_2[4.007,0.500,12.000])",
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
"RooCBExGaussShape::signalResPass(mass,meanP[-0.250,-5.000,5.000],sigmaP[3.048,0.000,15.000],alphaP[2.058,0.000,50.000],nP[0.553,0.000,50.000],sigmaP_2[1.500,0.500,15.000])",
"RooCBExGaussShape::signalResFail(mass,meanF[-1.415,-5.000,5.000],sigmaF[2.358,0.000,15.000],alphaF[1.276,0.000,50.000],nF[0.740,0.000,20.000],sigmaF_2[2.560,0.500,12.000])",
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