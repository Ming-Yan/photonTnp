import FWCore.ParameterSet.Config as cms

all_pdfs = cms.PSet(
loose_20p0To30p0_m2p5Tom1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[1.0,-5.000,5.000],sigmaP[0.5,0.001,5.000])",
"RooGaussian::signalResFail(mass, meanF[1.0,-5.000,5.000],sigmaF[0.5,0.001,5.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"templatesLoose.root\", \"hMass_20.0To30.0_-2.5To-1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"templatesLoose.root\", \"hMass_20.0To30.0_-2.5To-1.566_Fail\")",
"Chebychev::backgroundFail(mass, {cFail1[0,-1,1], cFail2[0,-1,1], cFail3[0,-1,1]})",
"Chebychev::backgroundPass(mass, {cPass1[0,-1,1], cPass2[0,-1,1], cPass3[0,-1,1]})",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

loose_20p0To30p0_m1p566Tom1p4442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[1.0,-5.000,5.000],sigmaP[0.5,0.001,5.000])",
"RooGaussian::signalResFail(mass, meanF[1.0,-5.000,5.000],sigmaF[0.5,0.001,5.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"templatesLoose.root\", \"hMass_20.0To30.0_-1.566To-1.4442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"templatesLoose.root\", \"hMass_20.0To30.0_-1.566To-1.4442_Fail\")",
"Chebychev::backgroundFail(mass, {cFail1[0,-1,1], cFail2[0,-1,1], cFail3[0,-1,1]})",
"Chebychev::backgroundPass(mass, {cPass1[0,-1,1], cPass2[0,-1,1], cPass3[0,-1,1]})",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

loose_20p0To30p0_m1p4442Tom1p0 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[1.0,-5.000,5.000],sigmaP[0.5,0.001,5.000])",
"RooGaussian::signalResFail(mass, meanF[1.0,-5.000,5.000],sigmaF[0.5,0.001,5.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"templatesLoose.root\", \"hMass_20.0To30.0_-1.4442To-1.0_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"templatesLoose.root\", \"hMass_20.0To30.0_-1.4442To-1.0_Fail\")",
"Chebychev::backgroundFail(mass, {cFail1[0,-1,1], cFail2[0,-1,1], cFail3[0,-1,1]})",
"Chebychev::backgroundPass(mass, {cPass1[0,-1,1], cPass2[0,-1,1], cPass3[0,-1,1]})",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

loose_20p0To30p0_m1p0To0p0 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[1.0,-5.000,5.000],sigmaP[0.5,0.001,5.000])",
"RooGaussian::signalResFail(mass, meanF[1.0,-5.000,5.000],sigmaF[0.5,0.001,5.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"templatesLoose.root\", \"hMass_20.0To30.0_-1.0To0.0_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"templatesLoose.root\", \"hMass_20.0To30.0_-1.0To0.0_Fail\")",
"Chebychev::backgroundFail(mass, {cFail1[0,-1,1], cFail2[0,-1,1], cFail3[0,-1,1]})",
"Chebychev::backgroundPass(mass, {cPass1[0,-1,1], cPass2[0,-1,1], cPass3[0,-1,1]})",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

loose_20p0To30p0_0p0To1p0 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[1.0,-5.000,5.000],sigmaP[0.5,0.001,5.000])",
"RooGaussian::signalResFail(mass, meanF[1.0,-5.000,5.000],sigmaF[0.5,0.001,5.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"templatesLoose.root\", \"hMass_20.0To30.0_0.0To1.0_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"templatesLoose.root\", \"hMass_20.0To30.0_0.0To1.0_Fail\")",
"Chebychev::backgroundFail(mass, {cFail1[0,-1,1], cFail2[0,-1,1], cFail3[0,-1,1]})",
"Chebychev::backgroundPass(mass, {cPass1[0,-1,1], cPass2[0,-1,1], cPass3[0,-1,1]})",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

loose_20p0To30p0_1p0To1p4442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[1.0,-5.000,5.000],sigmaP[0.5,0.001,5.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,0.0,0.0],sigmaF[1.9,1.9,1.9])",
"ZGeneratorLineShape::signalPhyPass(mass,\"templatesLoose.root\", \"hMass_20.0To30.0_1.0To1.4442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"templatesLoose.root\", \"hMass_20.0To30.0_1.0To1.4442_Fail\")",
#"Chebychev::backgroundFail(mass, {cFail1[0,-2,2], cFail2[0,-2,2], cFail3[0,-2,2]})",
#"Chebychev::backgroundPass(mass, {cPass1[0,-2,2], cPass2[0,-2,2], cPass3[0,-1,1]})",
"RooExponential::backgroundFail(mass, aFail[-0.1, -1., 1])",
"RooExponential::backgroundPass(mass, aPass[-0.1, -1., 1])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

loose_20p0To30p0_1p4442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[1.0,-5.000,5.000],sigmaP[0.5,0.001,5.000])",
"RooGaussian::signalResFail(mass, meanF[1.0,-5.000,5.000],sigmaF[0.5,0.001,5.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"templatesLoose.root\", \"hMass_20.0To30.0_1.4442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"templatesLoose.root\", \"hMass_20.0To30.0_1.4442To1.566_Fail\")",
"Chebychev::backgroundFail(mass, {cFail1[0,-1,1], cFail2[0,-1,1], cFail3[0,-1,1]})",
"Chebychev::backgroundPass(mass, {cPass1[0,-1,1], cPass2[0,-1,1], cPass3[0,-1,1]})",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

loose_20p0To30p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[1.0,-5.000,5.000],sigmaP[0.5,0.001,5.000])",
"RooGaussian::signalResFail(mass, meanF[1.0,-5.000,5.000],sigmaF[0.5,0.001,5.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"templatesLoose.root\", \"hMass_20.0To30.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"templatesLoose.root\", \"hMass_20.0To30.0_1.566To2.5_Fail\")",
"Chebychev::backgroundFail(mass, {cFail1[0,-1,1], cFail2[0,-1,1], cFail3[0,-1,1]})",
"Chebychev::backgroundPass(mass, {cPass1[0,-1,1], cPass2[0,-1,1], cPass3[0,-1,1]})",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

loose_30p0To40p0_m2p5Tom1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[1.0,-5.000,5.000],sigmaP[0.5,0.001,5.000])",
"RooGaussian::signalResFail(mass, meanF[1.0,-5.000,5.000],sigmaF[0.5,0.001,5.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"templatesLoose.root\", \"hMass_30.0To40.0_-2.5To-1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"templatesLoose.root\", \"hMass_30.0To40.0_-2.5To-1.566_Fail\")",
"Chebychev::backgroundFail(mass, {cFail1[0,-1,1], cFail2[0,-1,1], cFail3[0,-1,1]})",
"Chebychev::backgroundPass(mass, {cPass1[0,-1,1], cPass2[0,-1,1], cPass3[0,-1,1]})",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

loose_30p0To40p0_m1p566Tom1p4442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[1.0,-5.000,5.000],sigmaP[0.5,0.001,5.000])",
"RooGaussian::signalResFail(mass, meanF[1.0,-5.000,5.000],sigmaF[0.5,0.001,5.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"templatesLoose.root\", \"hMass_30.0To40.0_-1.566To-1.4442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"templatesLoose.root\", \"hMass_30.0To40.0_-1.566To-1.4442_Fail\")",
"Chebychev::backgroundFail(mass, {cFail1[0,-1,1], cFail2[0,-1,1], cFail3[0,-1,1]})",
"Chebychev::backgroundPass(mass, {cPass1[0,-1,1], cPass2[0,-1,1], cPass3[0,-1,1]})",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

loose_30p0To40p0_m1p4442Tom1p0 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[1.0,-5.000,5.000],sigmaP[0.5,0.001,5.000])",
"RooGaussian::signalResFail(mass, meanF[1.0,-5.000,5.000],sigmaF[0.5,0.001,5.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"templatesLoose.root\", \"hMass_30.0To40.0_-1.4442To-1.0_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"templatesLoose.root\", \"hMass_30.0To40.0_-1.4442To-1.0_Fail\")",
"Chebychev::backgroundFail(mass, {cFail1[0,-1,1], cFail2[0,-1,1], cFail3[0,-1,1]})",
"Chebychev::backgroundPass(mass, {cPass1[0,-1,1], cPass2[0,-1,1], cPass3[0,-1,1]})",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

loose_30p0To40p0_m1p0To0p0 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[1.0,-5.000,5.000],sigmaP[0.5,0.001,5.000])",
"RooGaussian::signalResFail(mass, meanF[1.0,-5.000,5.000],sigmaF[0.5,0.001,5.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"templatesLoose.root\", \"hMass_30.0To40.0_-1.0To0.0_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"templatesLoose.root\", \"hMass_30.0To40.0_-1.0To0.0_Fail\")",
"Chebychev::backgroundFail(mass, {cFail1[0,-1,1], cFail2[0,-1,1], cFail3[0,-1,1]})",
"Chebychev::backgroundPass(mass, {cPass1[0,-1,1], cPass2[0,-1,1], cPass3[0,-1,1]})",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

loose_30p0To40p0_0p0To1p0 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[1.0,-10.000,10.000],sigmaP[0.5,0.001,5.000])",
"RooGaussian::signalResFail(mass, meanF[1.0,-10.000,10.000],sigmaF[0.5,0.001,5.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"templatesLoose.root\", \"hMass_30.0To40.0_0.0To1.0_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"templatesLoose.root\", \"hMass_30.0To40.0_0.0To1.0_Fail\")",
"Chebychev::backgroundFail(mass, {cFail1[0,-1,1], cFail2[0,-1,1], cFail3[0,-1,1]})",
"Chebychev::backgroundPass(mass, {cPass1[0,-1,1], cPass2[0,-1,1], cPass3[0,-1,1]})",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

loose_30p0To40p0_1p0To1p4442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[1.0,-10.000,10.000],sigmaP[0.5,0.001,5.000])",
"RooGaussian::signalResFail(mass, meanF[1.0,-10.000,10.000],sigmaF[0.5,0.001,5.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"templatesLoose.root\", \"hMass_30.0To40.0_1.0To1.4442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"templatesLoose.root\", \"hMass_30.0To40.0_1.0To1.4442_Fail\")",
"Chebychev::backgroundFail(mass, {cFail1[0,-1,1], cFail2[0,-1,1], cFail3[0,-1,1]})",
"Chebychev::backgroundPass(mass, {cPass1[0,-1,1], cPass2[0,-1,1], cPass3[0,-1,1]})",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

loose_30p0To40p0_1p4442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[1.0,-5.000,5.000],sigmaP[0.5,0.001,5.000])",
"RooGaussian::signalResFail(mass, meanF[1.0,-5.000,5.000],sigmaF[0.5,0.001,5.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"templatesLoose.root\", \"hMass_30.0To40.0_1.4442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"templatesLoose.root\", \"hMass_30.0To40.0_1.4442To1.566_Fail\")",
"Chebychev::backgroundFail(mass, {cFail1[0,-1,1], cFail2[0,-1,1], cFail3[0,-1,1]})",
"Chebychev::backgroundPass(mass, {cPass1[0,-1,1], cPass2[0,-1,1], cPass3[0,-1,1]})",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

loose_30p0To40p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[1.0,-5.000,5.000],sigmaP[0.5,0.001,5.000])",
"RooGaussian::signalResFail(mass, meanF[1.0,-5.000,5.000],sigmaF[0.5,0.001,5.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"templatesLoose.root\", \"hMass_30.0To40.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"templatesLoose.root\", \"hMass_30.0To40.0_1.566To2.5_Fail\")",
"Chebychev::backgroundFail(mass, {cFail1[0,-1,1], cFail2[0,-1,1], cFail3[0,-1,1]})",
"Chebychev::backgroundPass(mass, {cPass1[0,-1,1], cPass2[0,-1,1], cPass3[0,-1,1]})",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

loose_40p0To50p0_m2p5Tom1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[1.0,-5.000,5.000],sigmaP[0.5,0.001,5.000])",
"RooGaussian::signalResFail(mass, meanF[1.0,-5.000,5.000],sigmaF[0.5,0.001,5.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"templatesLoose.root\", \"hMass_40.0To50.0_-2.5To-1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"templatesLoose.root\", \"hMass_40.0To50.0_-2.5To-1.566_Fail\")",
"Chebychev::backgroundFail(mass, {cFail1[0,-1,1], cFail2[0,-1,1], cFail3[0,-1,1]})",
"Chebychev::backgroundPass(mass, {cPass1[0,-1,1], cPass2[0,-1,1], cPass3[0,-1,1]})",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

loose_40p0To50p0_m1p566Tom1p4442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[1.0,-5.000,5.000],sigmaP[0.5,0.001,5.000])",
"RooGaussian::signalResFail(mass, meanF[1.0,-5.000,5.000],sigmaF[0.5,0.001,5.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"templatesLoose.root\", \"hMass_40.0To50.0_-1.566To-1.4442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"templatesLoose.root\", \"hMass_40.0To50.0_-1.566To-1.4442_Fail\")",
"Chebychev::backgroundFail(mass, {cFail1[0,-1,1], cFail2[0,-1,1], cFail3[0,-1,1]})",
"Chebychev::backgroundPass(mass, {cPass1[0,-1,1], cPass2[0,-1,1], cPass3[0,-1,1]})",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

loose_40p0To50p0_m1p4442Tom1p0 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[1.0,-10.000,10.000],sigmaP[0.5,0.001,5.000])",
"RooGaussian::signalResFail(mass, meanF[1.0,-10.000,10.000],sigmaF[0.5,0.001,5.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"templatesLoose.root\", \"hMass_40.0To50.0_-1.4442To-1.0_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"templatesLoose.root\", \"hMass_40.0To50.0_-1.4442To-1.0_Fail\")",
"Chebychev::backgroundFail(mass, {cFail1[0,-1,1], cFail2[0,-1,1], cFail3[0,-1,1]})",
"Chebychev::backgroundPass(mass, {cPass1[0,-1,1], cPass2[0,-1,1], cPass3[0,-1,1]})",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

loose_40p0To50p0_m1p0To0p0 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[1.0,-5.000,5.000],sigmaP[0.5,0.001,5.000])",
"RooGaussian::signalResFail(mass, meanF[1.0,-5.000,5.000],sigmaF[0.5,0.001,5.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"templatesLoose.root\", \"hMass_40.0To50.0_-1.0To0.0_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"templatesLoose.root\", \"hMass_40.0To50.0_-1.0To0.0_Fail\")",
"Chebychev::backgroundFail(mass, {cFail1[0,-1,1], cFail2[0,-1,1], cFail3[0,-1,1]})",
"Chebychev::backgroundPass(mass, {cPass1[0,-1,1], cPass2[0,-1,1], cPass3[0,-1,1]})",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

loose_40p0To50p0_0p0To1p0 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[1.0,-5.000,5.000],sigmaP[0.5,0.001,5.000])",
"RooGaussian::signalResFail(mass, meanF[1.0,-5.000,5.000],sigmaF[0.5,0.001,5.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"templatesLoose.root\", \"hMass_40.0To50.0_0.0To1.0_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"templatesLoose.root\", \"hMass_40.0To50.0_0.0To1.0_Fail\")",
"Chebychev::backgroundFail(mass, {cFail1[0,-1,1], cFail2[0,-1,1], cFail3[0,-1,1]})",
"Chebychev::backgroundPass(mass, {cPass1[0,-1,1], cPass2[0,-1,1], cPass3[0,-1,1]})",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

loose_40p0To50p0_1p0To1p4442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[1.0,-5.000,5.000],sigmaP[0.5,0.001,5.000])",
"RooGaussian::signalResFail(mass, meanF[1.0,-5.000,5.000],sigmaF[0.5,0.001,5.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"templatesLoose.root\", \"hMass_40.0To50.0_1.0To1.4442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"templatesLoose.root\", \"hMass_40.0To50.0_1.0To1.4442_Fail\")",
"Chebychev::backgroundFail(mass, {cFail1[0,-1,1], cFail2[0,-1,1], cFail3[0,-1,1]})",
"Chebychev::backgroundPass(mass, {cPass1[0,-1,1], cPass2[0,-1,1], cPass3[0,-1,1]})",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

loose_40p0To50p0_1p4442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[1.0,-5.000,5.000],sigmaP[0.5,0.001,5.000])",
"RooGaussian::signalResFail(mass, meanF[1.0,-5.000,5.000],sigmaF[0.5,0.001,5.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"templatesLoose.root\", \"hMass_40.0To50.0_1.4442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"templatesLoose.root\", \"hMass_40.0To50.0_1.4442To1.566_Fail\")",
"Chebychev::backgroundFail(mass, {cFail1[0,-1,1], cFail2[0,-1,1], cFail3[0,-1,1]})",
"Chebychev::backgroundPass(mass, {cPass1[0,-1,1], cPass2[0,-1,1], cPass3[0,-1,1]})",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

loose_40p0To50p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[1.0,-5.000,5.000],sigmaP[0.5,0.001,5.000])",
"RooGaussian::signalResFail(mass, meanF[1.0,-5.000,5.000],sigmaF[0.5,0.001,5.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"templatesLoose.root\", \"hMass_40.0To50.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"templatesLoose.root\", \"hMass_40.0To50.0_1.566To2.5_Fail\")",
"Chebychev::backgroundFail(mass, {cFail1[0,-1,1], cFail2[0,-1,1], cFail3[0,-1,1]})",
"Chebychev::backgroundPass(mass, {cPass1[0,-1,1], cPass2[0,-1,1], cPass3[0,-1,1]})",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

loose_50p0To200p0_m2p5Tom1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[1.0,-5.000,5.000],sigmaP[0.5,0.001,5.000])",
"RooGaussian::signalResFail(mass, meanF[1.0,-5.000,5.000],sigmaF[0.5,0.001,5.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"templatesLoose.root\", \"hMass_50.0To200.0_-2.5To-1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"templatesLoose.root\", \"hMass_50.0To200.0_-2.5To-1.566_Fail\")",
"Chebychev::backgroundFail(mass, {cFail1[0,-1,1], cFail2[0,-1,1], cFail3[0,-1,1]})",
"Chebychev::backgroundPass(mass, {cPass1[0,-1,1], cPass2[0,-1,1], cPass3[0,-1,1]})",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

loose_50p0To200p0_m1p566Tom1p4442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[1.0,-5.000,5.000],sigmaP[0.5,0.001,5.000])",
"RooGaussian::signalResFail(mass, meanF[1.0,-5.000,5.000],sigmaF[0.5,0.001,5.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"templatesLoose.root\", \"hMass_50.0To200.0_-1.566To-1.4442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"templatesLoose.root\", \"hMass_50.0To200.0_-1.566To-1.4442_Fail\")",
"Chebychev::backgroundFail(mass, {cFail1[0,-1,1], cFail2[0,-1,1], cFail3[0,-1,1]})",
"Chebychev::backgroundPass(mass, {cPass1[0,-1,1], cPass2[0,-1,1], cPass3[0,-1,1]})",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

loose_50p0To200p0_m1p4442Tom1p0 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[1.0,-5.000,5.000],sigmaP[0.5,0.001,5.000])",
"RooGaussian::signalResFail(mass, meanF[1.0,-5.000,5.000],sigmaF[0.5,0.001,5.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"templatesLoose.root\", \"hMass_50.0To200.0_-1.4442To-1.0_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"templatesLoose.root\", \"hMass_50.0To200.0_-1.4442To-1.0_Fail\")",
"Chebychev::backgroundFail(mass, {cFail1[0,-1,1], cFail2[0,-1,1], cFail3[0,-1,1]})",
"Chebychev::backgroundPass(mass, {cPass1[0,-1,1], cPass2[0,-1,1], cPass3[0,-1,1]})",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

loose_50p0To200p0_m1p0To0p0 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[1.0,-5.000,5.000],sigmaP[0.5,0.001,5.000])",
"RooGaussian::signalResFail(mass, meanF[1.0,-5.000,5.000],sigmaF[0.5,0.001,5.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"templatesLoose.root\", \"hMass_50.0To200.0_-1.0To0.0_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"templatesLoose.root\", \"hMass_50.0To200.0_-1.0To0.0_Fail\")",
"Chebychev::backgroundFail(mass, {cFail1[0,-1,1], cFail2[0,-1,1], cFail3[0,-1,1]})",
"Chebychev::backgroundPass(mass, {cPass1[0,-1,1], cPass2[0,-1,1], cPass3[0,-1,1]})",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

loose_50p0To200p0_0p0To1p0 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[1.0,-5.000,5.000],sigmaP[0.5,0.001,5.000])",
"RooGaussian::signalResFail(mass, meanF[1.0,-5.000,5.000],sigmaF[0.5,0.001,5.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"templatesLoose.root\", \"hMass_50.0To200.0_0.0To1.0_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"templatesLoose.root\", \"hMass_50.0To200.0_0.0To1.0_Fail\")",
"Chebychev::backgroundFail(mass, {cFail1[0,-1,1], cFail2[0,-1,1], cFail3[0,-1,1]})",
"Chebychev::backgroundPass(mass, {cPass1[0,-1,1], cPass2[0,-1,1], cPass3[0,-1,1]})",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

loose_50p0To200p0_1p0To1p4442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[1.0,-5.000,5.000],sigmaP[0.5,0.001,5.000])",
"RooGaussian::signalResFail(mass, meanF[1.0,-5.000,5.000],sigmaF[0.5,0.001,5.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"templatesLoose.root\", \"hMass_50.0To200.0_1.0To1.4442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"templatesLoose.root\", \"hMass_50.0To200.0_1.0To1.4442_Fail\")",
"Chebychev::backgroundFail(mass, {cFail1[0,-1,1], cFail2[0,-1,1], cFail3[0,-1,1]})",
"Chebychev::backgroundPass(mass, {cPass1[0,-1,1], cPass2[0,-1,1], cPass3[0,-1,1]})",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

loose_50p0To200p0_1p4442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[1.0,-5.000,5.000],sigmaP[0.5,0.001,5.000])",
"RooGaussian::signalResFail(mass, meanF[1.0,-5.000,5.000],sigmaF[0.5,0.001,5.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"templatesLoose.root\", \"hMass_50.0To200.0_1.4442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"templatesLoose.root\", \"hMass_50.0To200.0_1.4442To1.566_Fail\")",
"Chebychev::backgroundFail(mass, {cFail1[0,-1,1], cFail2[0,-1,1], cFail3[0,-1,1]})",
"Chebychev::backgroundPass(mass, {cPass1[0,-1,1], cPass2[0,-1,1], cPass3[0,-1,1]})",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

loose_50p0To200p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[1.0,-10.000,10.000],sigmaP[0.5,0.001,5.000])",
"RooGaussian::signalResFail(mass, meanF[1.0,-10.000,10.000],sigmaF[0.5,0.001,5.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"templatesLoose.root\", \"hMass_50.0To200.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"templatesLoose.root\", \"hMass_50.0To200.0_1.566To2.5_Fail\")",
"Chebychev::backgroundFail(mass, {cFail1[0,-1,1], cFail2[0,-1,1], cFail3[0,-1,1]})",
"Chebychev::backgroundPass(mass, {cPass1[0,-1,1], cPass2[0,-1,1], cPass3[0,-1,1]})",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

)
