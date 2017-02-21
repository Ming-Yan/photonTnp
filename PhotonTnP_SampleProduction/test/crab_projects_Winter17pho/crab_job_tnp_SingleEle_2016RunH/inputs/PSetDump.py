import FWCore.ParameterSet.Config as cms

process = cms.Process("tnp")

process.source = cms.Source("PoolSource",
    eventsToProcess = cms.untracked.VEventRange(),
    fileNames = cms.untracked.vstring('/store/data/Run2016B/SingleElectron/MINIAOD/23Sep2016-v2/80000/08A02DC3-608C-E611-ADA5-0025905B85B6.root', 
        '/store/data/Run2016B/SingleElectron/MINIAOD/23Sep2016-v2/80000/0C9C7188-708C-E611-A4D7-0025907DE266.root', 
        '/store/data/Run2016B/SingleElectron/MINIAOD/23Sep2016-v2/80000/14415255-6B8C-E611-87D3-002590E3A212.root')
)
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.mvaEleID_PHYS14_PU20bx25_nonTrig_V1_producer_config = cms.PSet(
    mvaName = cms.string('ElectronMVAEstimatorRun2Phys14NonTrig'),
    mvaTag = cms.string('25nsV1'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB1_5_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB2_5_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EE_5_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB1_10_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB2_10_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EE_10_oldscenario2phys14_BDT.weights.xml')
)

process.mvaEleID_PHYS14_PU20bx25_nonTrig_V1_wp80 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Phys14NonTrig25nsV1Categories"),
        mvaCuts = cms.vdouble(-0.253, 0.081, -0.081, 0.965, 0.917, 
            0.683),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Phys14NonTrig25nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-PHYS14-PU20bx25-nonTrig-V1-wp80'),
    isPOGApproved = cms.untracked.bool(False)
)

process.mvaEleID_PHYS14_PU20bx25_nonTrig_V1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Phys14NonTrig25nsV1Categories"),
        mvaCuts = cms.vdouble(-0.483, -0.267, -0.323, 0.933, 0.825, 
            0.337),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Phys14NonTrig25nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-PHYS14-PU20bx25-nonTrig-V1-wp90'),
    isPOGApproved = cms.untracked.bool(False)
)

process.mvaEleID_Spring15_25ns_Trig_V1_producer_config = cms.PSet(
    beamSpot = cms.InputTag("offlineBeamSpot"),
    conversionsAOD = cms.InputTag("allConversions"),
    conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
    mvaName = cms.string('ElectronMVAEstimatorRun2Spring15Trig'),
    mvaTag = cms.string('25nsV1'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml')
)

process.mvaEleID_Spring15_25ns_Trig_V1_wp80 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig25nsV1Categories"),
        mvaCuts = cms.vdouble(0.988153, 0.96791, 0.841729),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig25nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-Spring15-25ns-Trig-V1-wp80'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaEleID_Spring15_25ns_Trig_V1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig25nsV1Categories"),
        mvaCuts = cms.vdouble(0.972153, 0.922126, 0.610764),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig25nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-Spring15-25ns-Trig-V1-wp90'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaEleID_Spring15_25ns_nonTrig_V1_producer_config = cms.PSet(
    beamSpot = cms.InputTag("offlineBeamSpot"),
    conversionsAOD = cms.InputTag("allConversions"),
    conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
    mvaName = cms.string('ElectronMVAEstimatorRun2Spring15NonTrig'),
    mvaTag = cms.string('25nsV1'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml')
)

process.mvaEleID_Spring15_25ns_nonTrig_V1_wp80 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Categories"),
        mvaCuts = cms.vdouble(0.287435, 0.221846, -0.303263, 0.967083, 0.929117, 
            0.726311),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-Spring15-25ns-nonTrig-V1-wp80')
)

process.mvaEleID_Spring15_25ns_nonTrig_V1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Categories"),
        mvaCuts = cms.vdouble(-0.083313, -0.235222, -0.67099, 0.913286, 0.805013, 
            0.358969),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-Spring15-25ns-nonTrig-V1-wp90')
)

process.mvaEleID_Spring15_25ns_nonTrig_V1_wpLoose = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Categories"),
        mvaCuts = cms.vdouble(-0.265, -0.556, -0.551, -0.072, -0.286, 
            -0.267),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-Spring15-25ns-nonTrig-V1-wpLoose')
)

process.mvaEleID_Spring15_50ns_Trig_V1_producer_config = cms.PSet(
    beamSpot = cms.InputTag("offlineBeamSpot"),
    conversionsAOD = cms.InputTag("allConversions"),
    conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
    mvaName = cms.string('ElectronMVAEstimatorRun2Spring15Trig'),
    mvaTag = cms.string('50nsV1'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml')
)

process.mvaEleID_Spring15_50ns_Trig_V1_wp80 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig50nsV1Categories"),
        mvaCuts = cms.vdouble(0.981841, 0.946762, 0.79704),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig50nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-Spring15-50ns-Trig-V1-wp80'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaEleID_Spring15_50ns_Trig_V1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig50nsV1Categories"),
        mvaCuts = cms.vdouble(0.953843, 0.849994, 0.514118),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig50nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-Spring15-50ns-Trig-V1-wp90'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaEleID_Spring16_GeneralPurpose_V1_producer_config = cms.PSet(
    beamSpot = cms.InputTag("offlineBeamSpot"),
    conversionsAOD = cms.InputTag("allConversions"),
    conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
    mvaName = cms.string('ElectronMVAEstimatorRun2Spring16GeneralPurpose'),
    mvaTag = cms.string('V1'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB1_10.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB2_10.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EE_10.weights.xml')
)

process.mvaEleID_Spring16_GeneralPurpose_V1_wp80 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Categories"),
        mvaCuts = cms.vdouble(0.940962684155, 0.899208843708, 0.758484721184),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-Spring16-GeneralPurpose-V1-wp80')
)

process.mvaEleID_Spring16_GeneralPurpose_V1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Categories"),
        mvaCuts = cms.vdouble(0.836695742607, 0.715337944031, 0.356799721718),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-Spring16-GeneralPurpose-V1-wp90')
)

process.mvaEleID_Spring16_HZZ_V1_producer_config = cms.PSet(
    beamSpot = cms.InputTag("offlineBeamSpot"),
    conversionsAOD = cms.InputTag("allConversions"),
    conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
    mvaName = cms.string('ElectronMVAEstimatorRun2Spring16HZZ'),
    mvaTag = cms.string('V1'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_5.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_5.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_5.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_10.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_10.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_10.weights.xml')
)

process.mvaEleID_Spring16_HZZ_V1_wpLoose = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16HZZV1Categories"),
        mvaCuts = cms.vdouble(-0.211, -0.396, -0.215, -0.87, -0.838, 
            -0.763),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16HZZV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-Spring16-HZZ-V1-wpLoose'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaPhoID_Spring15_25ns_nonTrig_V2p1_producer_config = cms.PSet(
    esEffSigmaRRMap = cms.InputTag("photonIDValueMapProducer","phoESEffSigmaRR"),
    full5x5E1x3Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E1x3"),
    full5x5E2x2Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x2"),
    full5x5E2x5MaxMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x5Max"),
    full5x5E5x5Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E5x5"),
    full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
    full5x5SigmaIEtaIPhiMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIPhi"),
    mvaName = cms.string('PhotonMVAEstimatorRun2Spring15NonTrig'),
    mvaTag = cms.string('25nsV2p1'),
    phoChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
    phoPhotonIsolation = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
    phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolation"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    useValueMaps = cms.bool(False),
    weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_25ns_EB_V2.weights.xml', 
        'RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_25ns_EE_V2.weights.xml')
)

process.mvaPhoID_Spring15_25ns_nonTrig_V2p1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring15NonTrig25nsV2p1Categories"),
        mvaCuts = cms.vdouble(0.374, 0.336),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring15NonTrig25nsV2p1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-Spring15-25ns-nonTrig-V2p1-wp90')
)

process.mvaPhoID_Spring15_50ns_nonTrig_V2p1_producer_config = cms.PSet(
    esEffSigmaRRMap = cms.InputTag("photonIDValueMapProducer","phoESEffSigmaRR"),
    full5x5E1x3Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E1x3"),
    full5x5E2x2Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x2"),
    full5x5E2x5MaxMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x5Max"),
    full5x5E5x5Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E5x5"),
    full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
    full5x5SigmaIEtaIPhiMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIPhi"),
    mvaName = cms.string('PhotonMVAEstimatorRun2Spring15NonTrig'),
    mvaTag = cms.string('50nsV2p1'),
    phoChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
    phoPhotonIsolation = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
    phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolation"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    useValueMaps = cms.bool(False),
    weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_50ns_EB_V2.weights.xml', 
        'RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_50ns_EE_V2.weights.xml')
)

process.mvaPhoID_Spring15_50ns_nonTrig_V2p1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring15NonTrig50nsV2p1Categories"),
        mvaCuts = cms.vdouble(0.29538, 0.45837),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring15NonTrig50nsV2p1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-Spring15-50ns-nonTrig-V2p1-wp90'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaPhoID_Spring16_nonTrig_V1_producer_config = cms.PSet(
    effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfPhotons_90percentBased.txt'),
    mvaName = cms.string('PhotonMVAEstimatorRun2Spring16NonTrig'),
    mvaTag = cms.string('V1'),
    phoChargedIsolation = cms.InputTag("egmPhotonIsolation","h+-DR030-"),
    phoIsoCutoff = cms.double(2.5),
    phoIsoPtScalingCoeff = cms.vdouble(0.0053, 0.0034),
    phoPhotonIsolation = cms.InputTag("egmPhotonIsolation","gamma-DR030-"),
    phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolationWithConeVeto"),
    rho = cms.InputTag("fixedGridRhoAll"),
    weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/Spring16/photon_general_MVA_Spring16_EB_V3.weights.xml', 
        'RecoEgamma/PhotonIdentification/data/Spring16/photon_general_MVA_Spring16_EE_V3.weights.xml')
)

process.mvaPhoID_Spring16_nonTrig_V1_wp80 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Categories"),
        mvaCuts = cms.vdouble(0.68, 0.6),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-Spring16-nonTrig-V1-wp80')
)

process.mvaPhoID_Spring16_nonTrig_V1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Categories"),
        mvaCuts = cms.vdouble(0.2, 0.2),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-Spring16-nonTrig-V1-wp90')
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(False)
)

process.IsoConeDefinitions = cms.VPSet(cms.PSet(
    coneSize = cms.double(0.3),
    isolateAgainst = cms.string('h+'),
    isolationAlgo = cms.string('PhotonPFIsolationWithMapBasedVeto'),
    miniAODVertexCodes = cms.vuint32(2, 3),
    vertexIndex = cms.int32(0)
), 
    cms.PSet(
        coneSize = cms.double(0.3),
        isolateAgainst = cms.string('h0'),
        isolationAlgo = cms.string('PhotonPFIsolationWithMapBasedVeto'),
        miniAODVertexCodes = cms.vuint32(2, 3),
        vertexIndex = cms.int32(0)
    ), 
    cms.PSet(
        coneSize = cms.double(0.3),
        isolateAgainst = cms.string('gamma'),
        isolationAlgo = cms.string('PhotonPFIsolationWithMapBasedVeto'),
        miniAODVertexCodes = cms.vuint32(2, 3),
        vertexIndex = cms.int32(0)
    ))

process.mvaConfigsForEleProducer = cms.VPSet(cms.PSet(
    mvaName = cms.string('ElectronMVAEstimatorRun2Phys14NonTrig'),
    mvaTag = cms.string('25nsV1'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB1_5_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB2_5_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EE_5_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB1_10_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB2_10_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EE_10_oldscenario2phys14_BDT.weights.xml')
), 
    cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        conversionsAOD = cms.InputTag("allConversions"),
        conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
        mvaName = cms.string('ElectronMVAEstimatorRun2Spring15NonTrig'),
        mvaTag = cms.string('25nsV1'),
        weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml')
    ), 
    cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        conversionsAOD = cms.InputTag("allConversions"),
        conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
        mvaName = cms.string('ElectronMVAEstimatorRun2Spring15Trig'),
        mvaTag = cms.string('50nsV1'),
        weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml')
    ), 
    cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        conversionsAOD = cms.InputTag("allConversions"),
        conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
        mvaName = cms.string('ElectronMVAEstimatorRun2Spring15Trig'),
        mvaTag = cms.string('25nsV1'),
        weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml')
    ), 
    cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        conversionsAOD = cms.InputTag("allConversions"),
        conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
        mvaName = cms.string('ElectronMVAEstimatorRun2Spring16HZZ'),
        mvaTag = cms.string('V1'),
        weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_5.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_5.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_5.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_10.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_10.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_10.weights.xml')
    ), 
    cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        conversionsAOD = cms.InputTag("allConversions"),
        conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
        mvaName = cms.string('ElectronMVAEstimatorRun2Spring16GeneralPurpose'),
        mvaTag = cms.string('V1'),
        weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB1_10.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB2_10.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EE_10.weights.xml')
    ))

process.mvaConfigsForPhoProducer = cms.VPSet(cms.PSet(
    esEffSigmaRRMap = cms.InputTag("photonIDValueMapProducer","phoESEffSigmaRR"),
    full5x5E1x3Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E1x3"),
    full5x5E2x2Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x2"),
    full5x5E2x5MaxMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x5Max"),
    full5x5E5x5Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E5x5"),
    full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
    full5x5SigmaIEtaIPhiMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIPhi"),
    mvaName = cms.string('PhotonMVAEstimatorRun2Spring15NonTrig'),
    mvaTag = cms.string('50nsV2p1'),
    phoChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
    phoPhotonIsolation = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
    phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolation"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    useValueMaps = cms.bool(False),
    weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_50ns_EB_V2.weights.xml', 
        'RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_50ns_EE_V2.weights.xml')
), 
    cms.PSet(
        esEffSigmaRRMap = cms.InputTag("photonIDValueMapProducer","phoESEffSigmaRR"),
        full5x5E1x3Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E1x3"),
        full5x5E2x2Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x2"),
        full5x5E2x5MaxMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x5Max"),
        full5x5E5x5Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E5x5"),
        full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
        full5x5SigmaIEtaIPhiMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIPhi"),
        mvaName = cms.string('PhotonMVAEstimatorRun2Spring15NonTrig'),
        mvaTag = cms.string('25nsV2p1'),
        phoChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
        phoPhotonIsolation = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
        phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolation"),
        rho = cms.InputTag("fixedGridRhoFastjetAll"),
        useValueMaps = cms.bool(False),
        weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_25ns_EB_V2.weights.xml', 
            'RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_25ns_EE_V2.weights.xml')
    ), 
    cms.PSet(
        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfPhotons_90percentBased.txt'),
        mvaName = cms.string('PhotonMVAEstimatorRun2Spring16NonTrig'),
        mvaTag = cms.string('V1'),
        phoChargedIsolation = cms.InputTag("egmPhotonIsolation","h+-DR030-"),
        phoIsoCutoff = cms.double(2.5),
        phoIsoPtScalingCoeff = cms.vdouble(0.0053, 0.0034),
        phoPhotonIsolation = cms.InputTag("egmPhotonIsolation","gamma-DR030-"),
        phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolationWithConeVeto"),
        rho = cms.InputTag("fixedGridRhoAll"),
        weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/Spring16/photon_general_MVA_Spring16_EB_V3.weights.xml', 
            'RecoEgamma/PhotonIdentification/data/Spring16/photon_general_MVA_Spring16_EE_V3.weights.xml')
    ))

process.GsfMatchedSuperClusterCands = cms.EDProducer("PatElectronMatchedCandidateProducer",
    ReferenceElectronCollection = cms.untracked.InputTag("goodElectrons"),
    cut = cms.string('abs(eta)<2.5 &&  et>5.0'),
    src = cms.InputTag("superClusterCands")
)


process.egmGsfElectronIDs = cms.EDProducer("VersionedGsfElectronIdProducer",
    physicsObjectIDs = cms.VPSet(cms.PSet(
        idDefinition = cms.PSet(
            cutFlow = cms.VPSet(cms.PSet(
                cutName = cms.string('MinPtCut'),
                isIgnored = cms.bool(False),
                minPt = cms.double(5.0),
                needsAdditionalProducts = cms.bool(False)
            ), 
                cms.PSet(
                    allowedEtaRanges = cms.VPSet(cms.PSet(
                        maxEta = cms.double(1.479),
                        minEta = cms.double(0.0)
                    ), 
                        cms.PSet(
                            maxEta = cms.double(2.5),
                            minEta = cms.double(1.479)
                        )),
                    cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(False),
                    useAbsEta = cms.bool(True)
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('GsfEleDEtaInCut'),
                    dEtaInCutValueEB = cms.double(0.0105),
                    dEtaInCutValueEE = cms.double(0.00814),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('GsfEleDPhiInCut'),
                    dPhiInCutValueEB = cms.double(0.115),
                    dPhiInCutValueEE = cms.double(0.182),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                    full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0103),
                    full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0301),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('GsfEleHadronicOverEMCut'),
                    hadronicOverEMCutValueEB = cms.double(0.104),
                    hadronicOverEMCutValueEE = cms.double(0.0897),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('GsfEleDxyCut'),
                    dxyCutValueEB = cms.double(0.0261),
                    dxyCutValueEE = cms.double(0.118),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(True),
                    vertexSrc = cms.InputTag("offlinePrimaryVertices"),
                    vertexSrcMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('GsfEleDzCut'),
                    dzCutValueEB = cms.double(0.41),
                    dzCutValueEE = cms.double(0.822),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(True),
                    vertexSrc = cms.InputTag("offlinePrimaryVertices"),
                    vertexSrcMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                    eInverseMinusPInverseCutValueEB = cms.double(0.102),
                    eInverseMinusPInverseCutValueEE = cms.double(0.126),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                    effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Spring15/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_25ns.txt'),
                    isIgnored = cms.bool(False),
                    isRelativeIso = cms.bool(True),
                    isoCutEBHighPt = cms.double(0.0893),
                    isoCutEBLowPt = cms.double(0.0893),
                    isoCutEEHighPt = cms.double(0.121),
                    isoCutEELowPt = cms.double(0.121),
                    needsAdditionalProducts = cms.bool(True),
                    ptCutOff = cms.double(20.0),
                    rho = cms.InputTag("fixedGridRhoFastjetAll")
                ), 
                cms.PSet(
                    beamspotSrc = cms.InputTag("offlineBeamSpot"),
                    conversionSrc = cms.InputTag("allConversions"),
                    conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                    cutName = cms.string('GsfEleConversionVetoCut'),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(True)
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('GsfEleMissingHitsCut'),
                    isIgnored = cms.bool(False),
                    maxMissingHitsEB = cms.uint32(2),
                    maxMissingHitsEE = cms.uint32(1),
                    needsAdditionalProducts = cms.bool(False)
                )),
            idName = cms.string('cutBasedElectronID-Spring15-25ns-V1-standalone-loose')
        ),
        idMD5 = cms.string('4fab9e4d09a2c1a36cbbd2279deb3627'),
        isPOGApproved = cms.untracked.bool(True)
    ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInCut'),
                        dEtaInCutValueEB = cms.double(0.0103),
                        dEtaInCutValueEE = cms.double(0.00733),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.0336),
                        dPhiInCutValueEE = cms.double(0.114),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0101),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0283),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.0876),
                        hadronicOverEMCutValueEE = cms.double(0.0678),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDxyCut'),
                        dxyCutValueEB = cms.double(0.0118),
                        dxyCutValueEE = cms.double(0.0739),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        vertexSrc = cms.InputTag("offlinePrimaryVertices"),
                        vertexSrcMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDzCut'),
                        dzCutValueEB = cms.double(0.373),
                        dzCutValueEE = cms.double(0.602),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        vertexSrc = cms.InputTag("offlinePrimaryVertices"),
                        vertexSrcMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.0174),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0898),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Spring15/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_25ns.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.0766),
                        isoCutEBLowPt = cms.double(0.0766),
                        isoCutEEHighPt = cms.double(0.0678),
                        isoCutEELowPt = cms.double(0.0678),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(2),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )),
                idName = cms.string('cutBasedElectronID-Spring15-25ns-V1-standalone-medium')
            ),
            idMD5 = cms.string('aa291aba714c148fcba156544907c440'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInCut'),
                        dEtaInCutValueEB = cms.double(0.00926),
                        dEtaInCutValueEE = cms.double(0.00724),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.0336),
                        dPhiInCutValueEE = cms.double(0.0918),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0101),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0279),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.0597),
                        hadronicOverEMCutValueEE = cms.double(0.0615),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDxyCut'),
                        dxyCutValueEB = cms.double(0.0111),
                        dxyCutValueEE = cms.double(0.0351),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        vertexSrc = cms.InputTag("offlinePrimaryVertices"),
                        vertexSrcMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDzCut'),
                        dzCutValueEB = cms.double(0.0466),
                        dzCutValueEE = cms.double(0.417),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        vertexSrc = cms.InputTag("offlinePrimaryVertices"),
                        vertexSrcMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.012),
                        eInverseMinusPInverseCutValueEE = cms.double(0.00999),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Spring15/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_25ns.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.0354),
                        isoCutEBLowPt = cms.double(0.0354),
                        isoCutEEHighPt = cms.double(0.0646),
                        isoCutEELowPt = cms.double(0.0646),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(2),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )),
                idName = cms.string('cutBasedElectronID-Spring15-25ns-V1-standalone-tight')
            ),
            idMD5 = cms.string('4e13b87c0573d3c8ebf91d446fa1d90f'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInCut'),
                        dEtaInCutValueEB = cms.double(0.0152),
                        dEtaInCutValueEE = cms.double(0.0113),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.216),
                        dPhiInCutValueEE = cms.double(0.237),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0114),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0352),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.181),
                        hadronicOverEMCutValueEE = cms.double(0.116),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDxyCut'),
                        dxyCutValueEB = cms.double(0.0564),
                        dxyCutValueEE = cms.double(0.222),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        vertexSrc = cms.InputTag("offlinePrimaryVertices"),
                        vertexSrcMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDzCut'),
                        dzCutValueEB = cms.double(0.472),
                        dzCutValueEE = cms.double(0.921),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        vertexSrc = cms.InputTag("offlinePrimaryVertices"),
                        vertexSrcMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.207),
                        eInverseMinusPInverseCutValueEE = cms.double(0.174),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Spring15/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_25ns.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.126),
                        isoCutEBLowPt = cms.double(0.126),
                        isoCutEEHighPt = cms.double(0.144),
                        isoCutEELowPt = cms.double(0.144),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(2),
                        maxMissingHitsEE = cms.uint32(3),
                        needsAdditionalProducts = cms.bool(False)
                    )),
                idName = cms.string('cutBasedElectronID-Spring15-25ns-V1-standalone-veto')
            ),
            idMD5 = cms.string('202030579ee3eec90fdc2d236ba3de7e'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00477),
                        dEtaInSeedCutValueEE = cms.double(0.00868),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.222),
                        dPhiInCutValueEE = cms.double(0.213),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.011),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0314),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.298),
                        hadronicOverEMCutValueEE = cms.double(0.101),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.241),
                        eInverseMinusPInverseCutValueEE = cms.double(0.14),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.0994),
                        isoCutEBLowPt = cms.double(0.0994),
                        isoCutEEHighPt = cms.double(0.107),
                        isoCutEELowPt = cms.double(0.107),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )),
                idName = cms.string('cutBasedElectronID-Summer16-80X-V1-loose')
            ),
            idMD5 = cms.string('c1c4c739f1ba0791d40168c123183475'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00311),
                        dEtaInSeedCutValueEE = cms.double(0.00609),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.103),
                        dPhiInCutValueEE = cms.double(0.045),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.00998),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0298),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.253),
                        hadronicOverEMCutValueEE = cms.double(0.0878),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.134),
                        eInverseMinusPInverseCutValueEE = cms.double(0.13),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.0695),
                        isoCutEBLowPt = cms.double(0.0695),
                        isoCutEEHighPt = cms.double(0.0821),
                        isoCutEELowPt = cms.double(0.0821),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )),
                idName = cms.string('cutBasedElectronID-Summer16-80X-V1-medium')
            ),
            idMD5 = cms.string('71b43f74a27d2fd3d27416afd22e8692'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00308),
                        dEtaInSeedCutValueEE = cms.double(0.00605),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.0816),
                        dPhiInCutValueEE = cms.double(0.0394),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.00998),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0292),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.0414),
                        hadronicOverEMCutValueEE = cms.double(0.0641),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.0129),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0129),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.0588),
                        isoCutEBLowPt = cms.double(0.0588),
                        isoCutEEHighPt = cms.double(0.0571),
                        isoCutEELowPt = cms.double(0.0571),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )),
                idName = cms.string('cutBasedElectronID-Summer16-80X-V1-tight')
            ),
            idMD5 = cms.string('ca2a9db2976d80ba2c13f9bfccdc32f2'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00749),
                        dEtaInSeedCutValueEE = cms.double(0.00895),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.228),
                        dPhiInCutValueEE = cms.double(0.213),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0115),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.037),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.356),
                        hadronicOverEMCutValueEE = cms.double(0.211),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.299),
                        eInverseMinusPInverseCutValueEE = cms.double(0.15),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.175),
                        isoCutEBLowPt = cms.double(0.175),
                        isoCutEEHighPt = cms.double(0.159),
                        isoCutEELowPt = cms.double(0.159),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(2),
                        maxMissingHitsEE = cms.uint32(3),
                        needsAdditionalProducts = cms.bool(False)
                    )),
                idName = cms.string('cutBasedElectronID-Summer16-80X-V1-veto')
            ),
            idMD5 = cms.string('0025c1841da1ab64a08d703ded72409b'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(35.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.4442),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.566)
                            )),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.004),
                        dEtaInSeedCutValueEE = cms.double(0.006),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.06),
                        dPhiInCutValueEE = cms.double(0.06),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(9999),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.03),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        cutName = cms.string('GsfEleFull5x5E2x5OverE5x5Cut'),
                        isIgnored = cms.bool(False),
                        minE1x5OverE5x5EB = cms.double(0.83),
                        minE1x5OverE5x5EE = cms.double(-1.0),
                        minE2x5OverE5x5EB = cms.double(0.94),
                        minE2x5OverE5x5EE = cms.double(-1.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(1.0),
                        constTermEE = cms.double(5),
                        cutName = cms.string('GsfEleHadronicOverEMLinearCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        slopeStartEB = cms.double(0.0),
                        slopeStartEE = cms.double(0.0),
                        slopeTermEB = cms.double(0.05),
                        slopeTermEE = cms.double(0.05)
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(5.0),
                        constTermEE = cms.double(5.0),
                        cutName = cms.string('GsfEleTrkPtIsoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        slopeStartEB = cms.double(0.0),
                        slopeStartEE = cms.double(0.0),
                        slopeTermEB = cms.double(0.0),
                        slopeTermEE = cms.double(0.0)
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(2.0),
                        constTermEE = cms.double(2.5),
                        cutName = cms.string('GsfEleEmHadD1IsoRhoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        rhoConstant = cms.double(0.28),
                        slopeStartEB = cms.double(0.0),
                        slopeStartEE = cms.double(50.0),
                        slopeTermEB = cms.double(0.03),
                        slopeTermEE = cms.double(0.03)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDxyCut'),
                        dxyCutValueEB = cms.double(0.02),
                        dxyCutValueEE = cms.double(0.05),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        vertexSrc = cms.InputTag("offlinePrimaryVertices"),
                        vertexSrcMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEcalDrivenCut'),
                        ecalDrivenEB = cms.int32(1),
                        ecalDrivenEE = cms.int32(1),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    )),
                idName = cms.string('heepElectronID-HEEPV60')
            ),
            idMD5 = cms.string('df10ac7e3a9c22f63fa7936573beaafb'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Categories"),
                    mvaCuts = cms.vdouble(0.287435, 0.221846, -0.303263, 0.967083, 0.929117, 
                        0.726311),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Spring15-25ns-nonTrig-V1-wp80')
            ),
            idMD5 = cms.string('113c47ceaea0fa687b8bd6d880eb4957'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Categories"),
                    mvaCuts = cms.vdouble(-0.083313, -0.235222, -0.67099, 0.913286, 0.805013, 
                        0.358969),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Spring15-25ns-nonTrig-V1-wp90')
            ),
            idMD5 = cms.string('ac4fdc160eefe9eae7338601c02ed4bb'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Categories"),
                    mvaCuts = cms.vdouble(-0.265, -0.556, -0.551, -0.072, -0.286, 
                        -0.267),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Spring15-25ns-nonTrig-V1-wpLoose')
            ),
            idMD5 = cms.string('99ff36834c4342110d84ea2350a1229c'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Categories"),
                    mvaCuts = cms.vdouble(0.940962684155, 0.899208843708, 0.758484721184),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Spring16-GeneralPurpose-V1-wp80')
            ),
            idMD5 = cms.string('b490bc0b0af2d5f3e9efea562370af2a'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Categories"),
                    mvaCuts = cms.vdouble(0.836695742607, 0.715337944031, 0.356799721718),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Spring16-GeneralPurpose-V1-wp90')
            ),
            idMD5 = cms.string('14c153aaf3c207deb3ad4932586647a7'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.011),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.031),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.004),
                        dEtaInSeedCutValueEE = cms.double(1e+30),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.02),
                        dPhiInCutValueEE = cms.double(1e+30),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.06),
                        hadronicOverEMCutValueEE = cms.double(0.065),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.013),
                        eInverseMinusPInverseCutValueEE = cms.double(0.013),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleCalPFClusterIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_HLT_ecalPFClusterIso.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.16),
                        isoCutEBLowPt = cms.double(0.16),
                        isoCutEEHighPt = cms.double(0.12),
                        isoCutEELowPt = cms.double(0.12),
                        isoType = cms.int32(0),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetCentralCalo")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleCalPFClusterIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_HLT_hcalPFClusterIso.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.12),
                        isoCutEBLowPt = cms.double(0.12),
                        isoCutEEHighPt = cms.double(0.12),
                        isoCutEELowPt = cms.double(0.12),
                        isoType = cms.int32(1),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetCentralCalo")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(0.0),
                        constTermEE = cms.double(0.0),
                        cutName = cms.string('GsfEleTrkPtIsoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        slopeStartEB = cms.double(0.0),
                        slopeStartEE = cms.double(0.0),
                        slopeTermEB = cms.double(0.08),
                        slopeTermEE = cms.double(0.08)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleNormalizedGsfChi2Cut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        normalizedGsfChi2CutValueEB = cms.double(1e+30),
                        normalizedGsfChi2CutValueEE = cms.double(3.0)
                    )),
                idName = cms.string('cutBasedElectronHLTPreselection-Summer16-V1')
            ),
            idMD5 = cms.string('aef5f00cc25a63b44192c6fc449f7dc0'),
            isPOGApproved = cms.untracked.bool(True)
        )),
    physicsObjectSrc = cms.InputTag("slimmedElectrons")
)


process.egmPhotonIDs = cms.EDProducer("VersionedPhotonIdProducer",
    physicsObjectIDs = cms.VPSet(cms.PSet(
        idDefinition = cms.PSet(
            cutFlow = cms.VPSet(cms.PSet(
                cutName = cms.string('MinPtCut'),
                isIgnored = cms.bool(False),
                minPt = cms.double(5.0),
                needsAdditionalProducts = cms.bool(False)
            ), 
                cms.PSet(
                    allowedEtaRanges = cms.VPSet(cms.PSet(
                        maxEta = cms.double(1.479),
                        minEta = cms.double(0.0)
                    ), 
                        cms.PSet(
                            maxEta = cms.double(2.5),
                            minEta = cms.double(1.479)
                        )),
                    cutName = cms.string('PhoSCEtaMultiRangeCut'),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(False),
                    useAbsEta = cms.bool(True)
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                    hadronicOverEMCutValueEB = cms.double(0.05),
                    hadronicOverEMCutValueEE = cms.double(0.05),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                    cutValueEB = cms.double(0.0102),
                    cutValueEE = cms.double(0.0274),
                    full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                cms.PSet(
                    C1_EB = cms.double(3.32),
                    C1_EE = cms.double(1.97),
                    C2_EB = cms.double(0),
                    C2_EE = cms.double(0.0),
                    anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('PhoAnyPFIsoWithEACut'),
                    effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring15/effAreaPhotons_cone03_pfChargedHadrons_25ns_NULLcorrection.txt'),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(True),
                    rho = cms.InputTag("fixedGridRhoFastjetAll"),
                    useRelativeIso = cms.bool(False)
                ), 
                cms.PSet(
                    C1_EB = cms.double(1.92),
                    C1_EE = cms.double(11.86),
                    C2_EB = cms.double(0.014),
                    C2_EE = cms.double(0.0139),
                    C3_EB = cms.double(1.9e-05),
                    C3_EE = cms.double(2.5e-05),
                    anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoNeutralHadronIsolation"),
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('PhoAnyPFIsoWithEAAndQuadScalingCut'),
                    effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring15/effAreaPhotons_cone03_pfNeutralHadrons_25ns_90percentBased.txt'),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(True),
                    rho = cms.InputTag("fixedGridRhoFastjetAll"),
                    useRelativeIso = cms.bool(False)
                ), 
                cms.PSet(
                    C1_EB = cms.double(0.81),
                    C1_EE = cms.double(0.83),
                    C2_EB = cms.double(0.0053),
                    C2_EE = cms.double(0.0034),
                    anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('PhoAnyPFIsoWithEACut'),
                    effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring15/effAreaPhotons_cone03_pfPhotons_25ns_90percentBased.txt'),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(True),
                    rho = cms.InputTag("fixedGridRhoFastjetAll"),
                    useRelativeIso = cms.bool(False)
                )),
            idName = cms.string('cutBasedPhotonID-Spring15-25ns-V1-standalone-loose')
        ),
        idMD5 = cms.string('3dbb7c6922f3e1b9eb9cf1c679ff70bb'),
        isPOGApproved = cms.untracked.bool(True)
    ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.05),
                        hadronicOverEMCutValueEE = cms.double(0.05),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.0102),
                        cutValueEE = cms.double(0.0268),
                        full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(1.37),
                        C1_EE = cms.double(1.1),
                        C2_EB = cms.double(0.0),
                        C2_EE = cms.double(0.0),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring15/effAreaPhotons_cone03_pfChargedHadrons_25ns_NULLcorrection.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(1.06),
                        C1_EE = cms.double(2.69),
                        C2_EB = cms.double(0.014),
                        C2_EE = cms.double(0.0139),
                        C3_EB = cms.double(1.9e-05),
                        C3_EE = cms.double(2.5e-05),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoNeutralHadronIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEAAndQuadScalingCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring15/effAreaPhotons_cone03_pfNeutralHadrons_25ns_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(0.28),
                        C1_EE = cms.double(0.39),
                        C2_EB = cms.double(0.0053),
                        C2_EE = cms.double(0.0034),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring15/effAreaPhotons_cone03_pfPhotons_25ns_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    )),
                idName = cms.string('cutBasedPhotonID-Spring15-25ns-V1-standalone-medium')
            ),
            idMD5 = cms.string('3c31de4198e6c34a0668e11fae83ac21'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.05),
                        hadronicOverEMCutValueEE = cms.double(0.05),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.01),
                        cutValueEE = cms.double(0.0268),
                        full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(0.76),
                        C1_EE = cms.double(0.56),
                        C2_EB = cms.double(0.0),
                        C2_EE = cms.double(0.0),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring15/effAreaPhotons_cone03_pfChargedHadrons_25ns_NULLcorrection.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(0.97),
                        C1_EE = cms.double(2.09),
                        C2_EB = cms.double(0.014),
                        C2_EE = cms.double(0.0139),
                        C3_EB = cms.double(1.9e-05),
                        C3_EE = cms.double(2.5e-05),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoNeutralHadronIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEAAndQuadScalingCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring15/effAreaPhotons_cone03_pfNeutralHadrons_25ns_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(0.08),
                        C1_EE = cms.double(0.16),
                        C2_EB = cms.double(0.0053),
                        C2_EE = cms.double(0.0034),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring15/effAreaPhotons_cone03_pfPhotons_25ns_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    )),
                idName = cms.string('cutBasedPhotonID-Spring15-25ns-V1-standalone-tight')
            ),
            idMD5 = cms.string('82ed54bcaf3c8d0ac4f2ae51aa8ff37d'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.0597),
                        hadronicOverEMCutValueEE = cms.double(0.0481),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.01031),
                        cutValueEE = cms.double(0.03013),
                        full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(1.295),
                        C1_EE = cms.double(1.011),
                        C2_EB = cms.double(0),
                        C2_EE = cms.double(0.0),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfChargedHadrons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(10.91),
                        C1_EE = cms.double(5.931),
                        C2_EB = cms.double(0.0148),
                        C2_EE = cms.double(0.0163),
                        C3_EB = cms.double(1.7e-05),
                        C3_EE = cms.double(1.4e-05),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoNeutralHadronIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEAAndQuadScalingCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(3.63),
                        C1_EE = cms.double(6.641),
                        C2_EB = cms.double(0.0047),
                        C2_EE = cms.double(0.0034),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfPhotons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    )),
                idName = cms.string('cutBasedPhotonID-Spring16-V2p2-loose')
            ),
            idMD5 = cms.string('d6ce6a4f3476294bf0a3261e00170daf'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.0396),
                        hadronicOverEMCutValueEE = cms.double(0.0219),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.01022),
                        cutValueEE = cms.double(0.03001),
                        full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(0.441),
                        C1_EE = cms.double(0.442),
                        C2_EB = cms.double(0.0),
                        C2_EE = cms.double(0.0),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfChargedHadrons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(2.725),
                        C1_EE = cms.double(1.715),
                        C2_EB = cms.double(0.0148),
                        C2_EE = cms.double(0.0163),
                        C3_EB = cms.double(1.7e-05),
                        C3_EE = cms.double(1.4e-05),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoNeutralHadronIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEAAndQuadScalingCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(2.571),
                        C1_EE = cms.double(3.863),
                        C2_EB = cms.double(0.0047),
                        C2_EE = cms.double(0.0034),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfPhotons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    )),
                idName = cms.string('cutBasedPhotonID-Spring16-V2p2-medium')
            ),
            idMD5 = cms.string('c739cfd0b6287b8586da187c06d4053f'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.0269),
                        hadronicOverEMCutValueEE = cms.double(0.0213),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.00994),
                        cutValueEE = cms.double(0.03),
                        full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(0.202),
                        C1_EE = cms.double(0.034),
                        C2_EB = cms.double(0.0),
                        C2_EE = cms.double(0.0),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfChargedHadrons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(0.264),
                        C1_EE = cms.double(0.586),
                        C2_EB = cms.double(0.0148),
                        C2_EE = cms.double(0.0163),
                        C3_EB = cms.double(1.7e-05),
                        C3_EE = cms.double(1.4e-05),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoNeutralHadronIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEAAndQuadScalingCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(2.362),
                        C1_EE = cms.double(2.617),
                        C2_EB = cms.double(0.0047),
                        C2_EE = cms.double(0.0034),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfPhotons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    )),
                idName = cms.string('cutBasedPhotonID-Spring16-V2p2-tight')
            ),
            idMD5 = cms.string('bdb623bdb1a15c13545020a919dd9530'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('PhoMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring15NonTrig25nsV2p1Categories"),
                    mvaCuts = cms.vdouble(0.374, 0.336),
                    mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring15NonTrig25nsV2p1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaPhoID-Spring15-25ns-nonTrig-V2p1-wp90')
            ),
            idMD5 = cms.string('62eb8da6a5e26164d52d36cb81f952fc'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('PhoMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Categories"),
                    mvaCuts = cms.vdouble(0.68, 0.6),
                    mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaPhoID-Spring16-nonTrig-V1-wp80')
            ),
            idMD5 = cms.string('471f10cc447e8f2d5294693821acc050'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('PhoMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Categories"),
                    mvaCuts = cms.vdouble(0.2, 0.2),
                    mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaPhoID-Spring16-nonTrig-V1-wp90')
            ),
            idMD5 = cms.string('1e6ba3d0c760d1d9a69be10e4aa012e2'),
            isPOGApproved = cms.untracked.bool(True)
        )),
    physicsObjectSrc = cms.InputTag("slimmedPhotons")
)


process.egmPhotonIsolation = cms.EDProducer("CITKPFIsolationSumProducer",
    isolationConeDefinitions = cms.VPSet(cms.PSet(
        coneSize = cms.double(0.3),
        isolateAgainst = cms.string('h+'),
        isolationAlgo = cms.string('PhotonPFIsolationWithMapBasedVeto'),
        miniAODVertexCodes = cms.vuint32(2, 3),
        vertexIndex = cms.int32(0)
    ), 
        cms.PSet(
            coneSize = cms.double(0.3),
            isolateAgainst = cms.string('h0'),
            isolationAlgo = cms.string('PhotonPFIsolationWithMapBasedVeto'),
            miniAODVertexCodes = cms.vuint32(2, 3),
            vertexIndex = cms.int32(0)
        ), 
        cms.PSet(
            coneSize = cms.double(0.3),
            isolateAgainst = cms.string('gamma'),
            isolationAlgo = cms.string('PhotonPFIsolationWithMapBasedVeto'),
            miniAODVertexCodes = cms.vuint32(2, 3),
            vertexIndex = cms.int32(0)
        )),
    srcForIsolationCone = cms.InputTag("packedPFCandidates"),
    srcToIsolate = cms.InputTag("slimmedPhotons")
)


process.eleVarHelper = cms.EDProducer("PatElectronVariableHelper",
    l1EGColl = cms.InputTag("caloStage2Digis","EGamma"),
    probes = cms.InputTag("slimmedElectrons"),
    vertexCollection = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.electronMVAValueMapProducer = cms.EDProducer("ElectronMVAValueMapProducer",
    mvaConfigurations = cms.VPSet(cms.PSet(
        mvaName = cms.string('ElectronMVAEstimatorRun2Phys14NonTrig'),
        mvaTag = cms.string('25nsV1'),
        weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB1_5_oldscenario2phys14_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB2_5_oldscenario2phys14_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EE_5_oldscenario2phys14_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB1_10_oldscenario2phys14_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB2_10_oldscenario2phys14_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EE_10_oldscenario2phys14_BDT.weights.xml')
    ), 
        cms.PSet(
            beamSpot = cms.InputTag("offlineBeamSpot"),
            conversionsAOD = cms.InputTag("allConversions"),
            conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
            mvaName = cms.string('ElectronMVAEstimatorRun2Spring15NonTrig'),
            mvaTag = cms.string('25nsV1'),
            weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml')
        ), 
        cms.PSet(
            beamSpot = cms.InputTag("offlineBeamSpot"),
            conversionsAOD = cms.InputTag("allConversions"),
            conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
            mvaName = cms.string('ElectronMVAEstimatorRun2Spring15Trig'),
            mvaTag = cms.string('50nsV1'),
            weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml')
        ), 
        cms.PSet(
            beamSpot = cms.InputTag("offlineBeamSpot"),
            conversionsAOD = cms.InputTag("allConversions"),
            conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
            mvaName = cms.string('ElectronMVAEstimatorRun2Spring15Trig'),
            mvaTag = cms.string('25nsV1'),
            weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml')
        ), 
        cms.PSet(
            beamSpot = cms.InputTag("offlineBeamSpot"),
            conversionsAOD = cms.InputTag("allConversions"),
            conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
            mvaName = cms.string('ElectronMVAEstimatorRun2Spring16HZZ'),
            mvaTag = cms.string('V1'),
            weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_5.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_5.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_5.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_10.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_10.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_10.weights.xml')
        ), 
        cms.PSet(
            beamSpot = cms.InputTag("offlineBeamSpot"),
            conversionsAOD = cms.InputTag("allConversions"),
            conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
            mvaName = cms.string('ElectronMVAEstimatorRun2Spring16GeneralPurpose'),
            mvaTag = cms.string('V1'),
            weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB1_10.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB2_10.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EE_10.weights.xml')
        )),
    src = cms.InputTag("gedGsfElectrons"),
    srcMiniAOD = cms.InputTag("slimmedElectrons")
)


process.electronRegressionValueMapProducer = cms.EDProducer("ElectronRegressionValueMapProducer",
    ebReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    ebReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    eeReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    eeReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedEERecHits"),
    esReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsES"),
    esReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedESRecHits"),
    src = cms.InputTag("gedGsfElectrons"),
    srcMiniAOD = cms.InputTag("slimmedElectrons","","@skipCurrentProcess"),
    useFull5x5 = cms.bool(False)
)


process.goodElectronsMeasureHLT = cms.EDProducer("PatElectronTriggerCandProducer",
    bits = cms.InputTag("TriggerResults","","HLT"),
    dR = cms.double(0.3),
    filterNames = cms.vstring('hltEle27erWPTightGsfTrackIsoFilter'),
    inputs = cms.InputTag("goodElectronsProbeMeasureHLT"),
    isAND = cms.bool(False),
    objects = cms.InputTag("selectedPatTrigger")
)


process.goodElectronsPROBECutBasedLoose = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Spring15-25ns-V1-standalone-loose")
)


process.goodElectronsPROBECutBasedLoose80X = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-loose")
)


process.goodElectronsPROBECutBasedMedium = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Spring15-25ns-V1-standalone-medium")
)


process.goodElectronsPROBECutBasedMedium80X = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-medium")
)


process.goodElectronsPROBECutBasedTight = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Spring15-25ns-V1-standalone-tight")
)


process.goodElectronsPROBECutBasedTight80X = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-tight")
)


process.goodElectronsPROBECutBasedVeto = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Spring15-25ns-V1-standalone-veto")
)


process.goodElectronsPROBECutBasedVeto80X = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-veto")
)


process.goodElectronsPROBEHLTsafe = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronHLTPreselection-Summer16-V1")
)


process.goodElectronsPROBEMVA80Xwp80 = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","mvaEleID-Spring16-GeneralPurpose-V1-wp80")
)


process.goodElectronsPROBEMVA80Xwp90 = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","mvaEleID-Spring16-GeneralPurpose-V1-wp90")
)


process.goodElectronsProbeHLT = cms.EDProducer("PatElectronTriggerCandProducer",
    bits = cms.InputTag("TriggerResults","","HLT"),
    dR = cms.double(0.3),
    filterNames = cms.vstring(),
    inputs = cms.InputTag("goodElectrons"),
    isAND = cms.bool(True),
    objects = cms.InputTag("selectedPatTrigger")
)


process.goodElectronsProbeMeasureHLT = cms.EDProducer("PatElectronTriggerCandProducer",
    bits = cms.InputTag("TriggerResults","","HLT"),
    dR = cms.double(0.3),
    filterNames = cms.vstring(),
    inputs = cms.InputTag("goodElectrons"),
    isAND = cms.bool(True),
    objects = cms.InputTag("selectedPatTrigger")
)


process.goodElectronsTAGCutBasedTight = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.1) && !(1.4442<=abs(-log(tan(superClusterPosition.theta/2)))<=1.566) && pt >= 30.0'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-tight")
)


process.goodElectronsTagHLT = cms.EDProducer("PatElectronTriggerCandProducer",
    bits = cms.InputTag("TriggerResults","","HLT"),
    dR = cms.double(0.3),
    filterNames = cms.vstring('hltEle27erWPTightGsfTrackIsoFilter'),
    inputs = cms.InputTag("goodElectronsTAGCutBasedTight"),
    isAND = cms.bool(True),
    objects = cms.InputTag("selectedPatTrigger")
)


process.goodPhotonsChIso = cms.EDProducer("PatPhotonSelectorByDoubleValueMap",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10 && ((abs(eta)<1.4442 && hadronicOverEm<0.08 && full5x5_sigmaIetaIeta < 0.015) || (abs(eta)>1.56 && (abs(eta)<2.5 && hadronicOverEm<0.05 && full5x5_sigmaIetaIeta < 0.045)) )'),
    id_cut = cms.double(2.0),
    input = cms.InputTag("goodPhotons"),
    isGreaterThan = cms.bool(False),
    selection = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation")
)


process.goodPhotonsPROBECutBasedLoose = cms.EDProducer("PatPhotonSelectorByValueMap",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10 && ((abs(eta)<1.4442 && hadronicOverEm<0.08 && full5x5_sigmaIetaIeta < 0.015) || (abs(eta)>1.56 && (abs(eta)<2.5 && hadronicOverEm<0.05 && full5x5_sigmaIetaIeta < 0.045)) )'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring15-25ns-V1-standalone-loose")
)


process.goodPhotonsPROBECutBasedLoose80X = cms.EDProducer("PatPhotonSelectorByValueMap",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10 && ((abs(eta)<1.4442 && hadronicOverEm<0.08 && full5x5_sigmaIetaIeta < 0.015) || (abs(eta)>1.56 && (abs(eta)<2.5 && hadronicOverEm<0.05 && full5x5_sigmaIetaIeta < 0.045)) )'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-loose")
)


process.goodPhotonsPROBECutBasedMedium = cms.EDProducer("PatPhotonSelectorByValueMap",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10 && ((abs(eta)<1.4442 && hadronicOverEm<0.08 && full5x5_sigmaIetaIeta < 0.015) || (abs(eta)>1.56 && (abs(eta)<2.5 && hadronicOverEm<0.05 && full5x5_sigmaIetaIeta < 0.045)) )'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring15-25ns-V1-standalone-medium")
)


process.goodPhotonsPROBECutBasedMedium80X = cms.EDProducer("PatPhotonSelectorByValueMap",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10 && ((abs(eta)<1.4442 && hadronicOverEm<0.08 && full5x5_sigmaIetaIeta < 0.015) || (abs(eta)>1.56 && (abs(eta)<2.5 && hadronicOverEm<0.05 && full5x5_sigmaIetaIeta < 0.045)) )'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-medium")
)


process.goodPhotonsPROBECutBasedTight = cms.EDProducer("PatPhotonSelectorByValueMap",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10 && ((abs(eta)<1.4442 && hadronicOverEm<0.08 && full5x5_sigmaIetaIeta < 0.015) || (abs(eta)>1.56 && (abs(eta)<2.5 && hadronicOverEm<0.05 && full5x5_sigmaIetaIeta < 0.045)) )'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring15-25ns-V1-standalone-tight")
)


process.goodPhotonsPROBECutBasedTight80X = cms.EDProducer("PatPhotonSelectorByValueMap",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10 && ((abs(eta)<1.4442 && hadronicOverEm<0.08 && full5x5_sigmaIetaIeta < 0.015) || (abs(eta)>1.56 && (abs(eta)<2.5 && hadronicOverEm<0.05 && full5x5_sigmaIetaIeta < 0.045)) )'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-tight")
)


process.goodPhotonsPROBEFullPreselection = cms.EDProducer("PatPhotonSelectorByDoubleValueMap",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10 && ((abs(eta)<1.4442 && hadronicOverEm<0.08 && full5x5_sigmaIetaIeta < 0.015) || (abs(eta)>1.56 && (abs(eta)<2.5 && hadronicOverEm<0.05 && full5x5_sigmaIetaIeta < 0.045)) )'),
    id_cut = cms.double(15.0),
    input = cms.InputTag("goodPhotonsPhoIso"),
    isGreaterThan = cms.bool(False),
    selection = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolation")
)


process.goodPhotonsPROBEMVA = cms.EDProducer("PatPhotonSelectorByValueMap",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10 && ((abs(eta)<1.4442 && hadronicOverEm<0.08 && full5x5_sigmaIetaIeta < 0.015) || (abs(eta)>1.56 && (abs(eta)<2.5 && hadronicOverEm<0.05 && full5x5_sigmaIetaIeta < 0.045)) )'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","mvaPhoID-Spring15-25ns-nonTrig-V2p1-wp90")
)


process.goodPhotonsPROBEMVA80Xwp80 = cms.EDProducer("PatPhotonSelectorByValueMap",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10 && ((abs(eta)<1.4442 && hadronicOverEm<0.08 && full5x5_sigmaIetaIeta < 0.015) || (abs(eta)>1.56 && (abs(eta)<2.5 && hadronicOverEm<0.05 && full5x5_sigmaIetaIeta < 0.045)) )'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","mvaPhoID-Spring16-nonTrig-V1-wp80")
)


process.goodPhotonsPROBEMVA80Xwp90 = cms.EDProducer("PatPhotonSelectorByValueMap",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10 && ((abs(eta)<1.4442 && hadronicOverEm<0.08 && full5x5_sigmaIetaIeta < 0.015) || (abs(eta)>1.56 && (abs(eta)<2.5 && hadronicOverEm<0.05 && full5x5_sigmaIetaIeta < 0.045)) )'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","mvaPhoID-Spring16-nonTrig-V1-wp90")
)


process.goodPhotonsPhoIso = cms.EDProducer("PatPhotonSelectorByDoubleValueMap",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10 && ((abs(eta)<1.4442 && hadronicOverEm<0.08 && full5x5_sigmaIetaIeta < 0.015) || (abs(eta)>1.56 && (abs(eta)<2.5 && hadronicOverEm<0.05 && full5x5_sigmaIetaIeta < 0.045)) )'),
    id_cut = cms.double(15.0),
    input = cms.InputTag("goodPhotonsChIso"),
    isGreaterThan = cms.bool(False),
    selection = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation")
)


process.goodPhotonsProbeHLT = cms.EDProducer("PatPhotonTriggerCandProducer",
    bits = cms.InputTag("TriggerResults","","HLT"),
    dR = cms.double(0.3),
    filterNames = cms.vstring(),
    inputs = cms.InputTag("goodPhotons"),
    isAND = cms.bool(True),
    objects = cms.InputTag("selectedPatTrigger")
)


process.goodSuperClustersHLT = cms.EDProducer("RecoEcalCandidateTriggerCandProducer",
    bits = cms.InputTag("TriggerResults","","HLT"),
    dR = cms.double(0.3),
    filterNames = cms.vstring(),
    inputs = cms.InputTag("goodSuperClusters"),
    isAND = cms.bool(True),
    objects = cms.InputTag("selectedPatTrigger")
)


process.photonIDValueMapProducer = cms.EDProducer("PhotonIDValueMapProducer",
    ebReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    ebReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    eeReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    eeReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedEERecHits"),
    esReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsES"),
    esReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedESRecHits"),
    particleBasedIsolation = cms.InputTag("particleBasedIsolation","gedPhotons"),
    pfCandidates = cms.InputTag("particleFlow"),
    pfCandidatesMiniAOD = cms.InputTag("packedPFCandidates"),
    src = cms.InputTag("gedPhotons"),
    srcMiniAOD = cms.InputTag("slimmedPhotons"),
    vertices = cms.InputTag("offlinePrimaryVertices"),
    verticesMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.photonMVAValueMapProducer = cms.EDProducer("PhotonMVAValueMapProducer",
    mvaConfigurations = cms.VPSet(cms.PSet(
        esEffSigmaRRMap = cms.InputTag("photonIDValueMapProducer","phoESEffSigmaRR"),
        full5x5E1x3Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E1x3"),
        full5x5E2x2Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x2"),
        full5x5E2x5MaxMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x5Max"),
        full5x5E5x5Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E5x5"),
        full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
        full5x5SigmaIEtaIPhiMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIPhi"),
        mvaName = cms.string('PhotonMVAEstimatorRun2Spring15NonTrig'),
        mvaTag = cms.string('50nsV2p1'),
        phoChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
        phoPhotonIsolation = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
        phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolation"),
        rho = cms.InputTag("fixedGridRhoFastjetAll"),
        useValueMaps = cms.bool(False),
        weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_50ns_EB_V2.weights.xml', 
            'RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_50ns_EE_V2.weights.xml')
    ), 
        cms.PSet(
            esEffSigmaRRMap = cms.InputTag("photonIDValueMapProducer","phoESEffSigmaRR"),
            full5x5E1x3Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E1x3"),
            full5x5E2x2Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x2"),
            full5x5E2x5MaxMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x5Max"),
            full5x5E5x5Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E5x5"),
            full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
            full5x5SigmaIEtaIPhiMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIPhi"),
            mvaName = cms.string('PhotonMVAEstimatorRun2Spring15NonTrig'),
            mvaTag = cms.string('25nsV2p1'),
            phoChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
            phoPhotonIsolation = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
            phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolation"),
            rho = cms.InputTag("fixedGridRhoFastjetAll"),
            useValueMaps = cms.bool(False),
            weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_25ns_EB_V2.weights.xml', 
                'RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_25ns_EE_V2.weights.xml')
        ), 
        cms.PSet(
            effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfPhotons_90percentBased.txt'),
            mvaName = cms.string('PhotonMVAEstimatorRun2Spring16NonTrig'),
            mvaTag = cms.string('V1'),
            phoChargedIsolation = cms.InputTag("egmPhotonIsolation","h+-DR030-"),
            phoIsoCutoff = cms.double(2.5),
            phoIsoPtScalingCoeff = cms.vdouble(0.0053, 0.0034),
            phoPhotonIsolation = cms.InputTag("egmPhotonIsolation","gamma-DR030-"),
            phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolationWithConeVeto"),
            rho = cms.InputTag("fixedGridRhoAll"),
            weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/Spring16/photon_general_MVA_Spring16_EB_V3.weights.xml', 
                'RecoEgamma/PhotonIdentification/data/Spring16/photon_general_MVA_Spring16_EE_V3.weights.xml')
        )),
    src = cms.InputTag("slimmedPhotons"),
    srcMiniAOD = cms.InputTag("slimmedPhotons")
)


process.photonRegressionValueMapProducer = cms.EDProducer("PhotonRegressionValueMapProducer",
    ebReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    ebReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    eeReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    eeReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedEERecHits"),
    esReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsES"),
    esReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedESRecHits"),
    src = cms.InputTag("gedPhotons"),
    srcMiniAOD = cms.InputTag("slimmedPhotons","","@skipCurrentProcess"),
    useFull5x5 = cms.bool(False)
)


process.pileupReweightingProducer = cms.EDProducer("PileupWeightProducer",
    PileupData = cms.vdouble(5050.0, 241000.0, 783000.0, 1740000.0, 2370000.0, 
        3410000.0, 6120000.0, 24300000.0, 67800000.0, 145000000.0, 
        257000000.0, 406000000.0, 563000000.0, 706000000.0, 841000000.0, 
        954000000.0, 1030000000.0, 1060000000.0, 1060000000.0, 1020000000.0, 
        947000000.0, 851000000.0, 741000000.0, 619000000.0, 493000000.0, 
        372000000.0, 267000000.0, 182000000.0, 118000000.0, 71800000.0, 
        41300000.0, 22400000.0, 11500000.0, 5570000.0, 2560000.0, 
        1120000.0, 470000.0, 192000.0, 77800.0, 33000.0, 
        16100.0, 9870.0, 7670.0, 6920.0, 6660.0, 
        6560.0, 6490.0, 6400.0, 6280.0, 6120.0),
    PileupMC = cms.vdouble(0.000829312873542, 0.00124276120498, 0.00339329181587, 0.00408224735376, 0.00383036590008, 
        0.00659159288946, 0.00816022734493, 0.00943640833116, 0.0137777376066, 0.017059392038, 
        0.0213193035468, 0.0247343174676, 0.0280848773878, 0.0323308476564, 0.0370394341409, 
        0.0456917721191, 0.0558762890594, 0.0576956187107, 0.0625325287017, 0.0591603758776, 
        0.0656650815128, 0.0678329011676, 0.0625142146389, 0.0548068448797, 0.0503893295063, 
        0.040209818868, 0.0374446988111, 0.0299661572042, 0.0272024759921, 0.0219328403791, 
        0.0179586571619, 0.0142926728247, 0.00839941654725, 0.00522366397213, 0.00224457976761, 
        0.000779274977993, 0.000197066585944, 7.16031761328e-05, 0.0, 0.0, 
        0.0, 0.0, 0.0, 0.0, 0.0, 
        0.0, 0.0, 0.0, 0.0, 0.0),
    pileupInfoTag = cms.InputTag("slimmedAddPileupInfo")
)


process.randomEngineStateProducer = cms.EDProducer("RandomEngineStateProducer")


process.sampleInfo = cms.EDProducer("tnp::SampleInfoTree",
    genInfo = cms.InputTag("generator")
)


process.superClusterCands = cms.EDProducer("ConcreteEcalCandidateProducer",
    particleType = cms.int32(11),
    src = cms.InputTag("reducedEgamma","reducedSuperClusters")
)


process.tagTightEleID = cms.EDProducer("CandViewShallowCloneCombiner",
    checkCharge = cms.bool(False),
    cut = cms.string('60<mass<120'),
    decay = cms.string('goodElectronsTagHLT goodElectronsProbeHLT')
)


process.tagTightHLT = cms.EDProducer("CandViewShallowCloneCombiner",
    checkCharge = cms.bool(True),
    cut = cms.string('60<mass<120'),
    decay = cms.string('goodElectronsTagHLT@+ goodElectronsProbeMeasureHLT@-')
)


process.tagTightPhoID = cms.EDProducer("CandViewShallowCloneCombiner",
    checkCharge = cms.bool(False),
    cut = cms.string('60<mass<120'),
    decay = cms.string('goodElectronsTagHLT goodPhotonsProbeHLT')
)


process.tagTightSC = cms.EDProducer("CandViewShallowCloneCombiner",
    checkCharge = cms.bool(False),
    cut = cms.string('60<mass<120'),
    decay = cms.string('goodElectronsTagHLT goodSuperClustersHLT')
)


process.goodElectrons = cms.EDFilter("PATElectronRefSelector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    src = cms.InputTag("slimmedElectrons")
)


process.goodPhotons = cms.EDFilter("PATPhotonRefSelector",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10 && ((abs(eta)<1.4442 && hadronicOverEm<0.08 && full5x5_sigmaIetaIeta < 0.015) || (abs(eta)>1.56 && (abs(eta)<2.5 && hadronicOverEm<0.05 && full5x5_sigmaIetaIeta < 0.045)) )'),
    src = cms.InputTag("slimmedPhotons")
)


process.goodSuperClusters = cms.EDFilter("RecoEcalCandidateRefSelector",
    cut = cms.string('abs(eta)<2.5 &&  et>5.0'),
    filter = cms.bool(True),
    src = cms.InputTag("superClusterCands")
)


process.hltFilter = cms.EDFilter("HLTHighLevel",
    HLTPaths = cms.vstring('HLT_Ele27_eta2p1_WPTight_Gsf_v*'),
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    andOr = cms.bool(True),
    eventSetupPathsKey = cms.string(''),
    throw = cms.bool(True)
)


process.GsfElectronToEleID = cms.EDAnalyzer("TagProbeFitTreeProducer",
    addEventVariablesInfo = cms.bool(True),
    addRunLumiInfo = cms.bool(True),
    allProbes = cms.InputTag("goodElectronsProbeHLT"),
    arbitration = cms.string('HighestPt'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    flags = cms.PSet(
        passingHLTsafe = cms.InputTag("goodElectronsPROBEHLTsafe"),
        passingLoose = cms.InputTag("goodElectronsPROBECutBasedLoose"),
        passingLoose80X = cms.InputTag("goodElectronsPROBECutBasedLoose80X"),
        passingMVA80Xwp80 = cms.InputTag("goodElectronsPROBEMVA80Xwp80"),
        passingMVA80Xwp90 = cms.InputTag("goodElectronsPROBEMVA80Xwp90"),
        passingMedium = cms.InputTag("goodElectronsPROBECutBasedMedium"),
        passingMedium80X = cms.InputTag("goodElectronsPROBECutBasedMedium80X"),
        passingTight = cms.InputTag("goodElectronsPROBECutBasedTight"),
        passingTight80X = cms.InputTag("goodElectronsPROBECutBasedTight80X"),
        passingVeto = cms.InputTag("goodElectronsPROBECutBasedVeto"),
        passingVeto80X = cms.InputTag("goodElectronsPROBECutBasedVeto80X")
    ),
    ignoreExceptions = cms.bool(True),
    isMC = cms.bool(False),
    pairFlags = cms.PSet(
        mass60to120 = cms.string('60 < mass < 120')
    ),
    pairVariables = cms.PSet(
        abseta = cms.string('abs(eta)'),
        eta = cms.string('eta'),
        mass = cms.string('mass'),
        pt = cms.string('pt')
    ),
    pfMet = cms.InputTag("slimmedMETsPuppi"),
    pileupInfoTag = cms.InputTag("slimmedAddPileupInfo"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    tagFlags = cms.PSet(

    ),
    tagProbePairs = cms.InputTag("tagTightEleID"),
    tagVariables = cms.PSet(
        Ele_abseta = cms.string('abs(eta)'),
        Ele_dxy = cms.InputTag("eleVarHelper","dxy"),
        Ele_dz = cms.InputTag("eleVarHelper","dz"),
        Ele_e = cms.string('energy'),
        Ele_et = cms.string('et'),
        Ele_eta = cms.string('eta'),
        Ele_mHits = cms.InputTag("eleVarHelper","missinghits"),
        Ele_nonTrigMVA = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values"),
        Ele_phi = cms.string('phi'),
        Ele_pt = cms.string('pt'),
        Ele_q = cms.string('charge'),
        Ele_trigMVA = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig25nsV1Values"),
        sc_abseta = cms.string('abs(-log(tan(superCluster.position.theta/2)))'),
        sc_energy = cms.string('superCluster.energy'),
        sc_et = cms.string('superCluster.energy*sin(superClusterPosition.theta)'),
        sc_eta = cms.string('-log(tan(superClusterPosition.theta/2))')
    ),
    variables = cms.PSet(
        probe_Ele_3charge = cms.string('chargeInfo().isGsfCtfScPixConsistent'),
        probe_Ele_abseta = cms.string('abs(eta)'),
        probe_Ele_chIso = cms.string('pfIsolationVariables().sumChargedHadronPt'),
        probe_Ele_chisq = cms.InputTag("eleVarHelper","chisq"),
        probe_Ele_dEtaIn = cms.string('deltaEtaSuperClusterTrackAtVtx'),
        probe_Ele_dEtaSeed = cms.string('deltaEtaSuperClusterTrackAtVtx+log(tan(superCluster.position.theta/2))-log(tan(superCluster.seed.position.theta/2))'),
        probe_Ele_dPhiIn = cms.string('deltaPhiSuperClusterTrackAtVtx'),
        probe_Ele_dr03TkSumPt = cms.string('dr03TkSumPt'),
        probe_Ele_dxy = cms.InputTag("eleVarHelper","dxy"),
        probe_Ele_dz = cms.InputTag("eleVarHelper","dz"),
        probe_Ele_e = cms.string('energy'),
        probe_Ele_e1x5 = cms.string('e1x5'),
        probe_Ele_e2x5 = cms.string('e2x5Max'),
        probe_Ele_e5x5 = cms.string('e5x5'),
        probe_Ele_ecalIso = cms.string('ecalPFClusterIso'),
        probe_Ele_et = cms.string('et'),
        probe_Ele_eta = cms.string('eta'),
        probe_Ele_hcalIso = cms.string('hcalPFClusterIso'),
        probe_Ele_hoe = cms.string('hadronicOverEm'),
        probe_Ele_hzzMVA80X = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16HZZV1Values"),
        probe_Ele_mHits = cms.InputTag("eleVarHelper","missinghits"),
        probe_Ele_neuIso = cms.string('pfIsolationVariables().sumNeutralHadronEt'),
        probe_Ele_nonTrigMVA = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values"),
        probe_Ele_nonTrigMVA80X = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values"),
        probe_Ele_ooemoop = cms.string('(1.0/ecalEnergy - eSuperClusterOverP/ecalEnergy)'),
        probe_Ele_phoIso = cms.string('pfIsolationVariables().sumPhotonEt'),
        probe_Ele_pt = cms.string('pt'),
        probe_Ele_q = cms.string('charge'),
        probe_Ele_r9 = cms.string('r9'),
        probe_Ele_r9_5x5 = cms.string('full5x5_r9'),
        probe_Ele_sieie = cms.string('sigmaIetaIeta'),
        probe_Ele_sieie_5x5 = cms.string('full5x5_sigmaIetaIeta'),
        probe_Ele_trigMVA = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig25nsV1Values"),
        probe_Ele_trkIso = cms.string('trackIso'),
        probe_Ele_trkPt = cms.string('gsfTrack().ptMode'),
        probe_sc_abseta = cms.string('abs(-log(tan(superCluster.position.theta/2)))'),
        probe_sc_energy = cms.string('superCluster.energy'),
        probe_sc_et = cms.string('superCluster.energy*sin(superClusterPosition.theta)'),
        probe_sc_eta = cms.string('-log(tan(superCluster.position.theta/2))'),
        probe_sc_etaW = cms.string('superCluster.etaWidth'),
        probe_sc_phi = cms.string('superCluster.phi'),
        probe_sc_phiW = cms.string('superCluster.phiWidth'),
        probe_sc_preshowerE = cms.string('superCluster.preshowerEnergy'),
        probe_sc_rawE = cms.string('superCluster.rawEnergy')
    ),
    vertexCollection = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.GsfElectronToPhoID = cms.EDAnalyzer("TagProbeFitTreeProducer",
    addEventVariablesInfo = cms.bool(True),
    addRunLumiInfo = cms.bool(True),
    allProbes = cms.InputTag("goodPhotonsProbeHLT"),
    arbitration = cms.string('HighestPt'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    flags = cms.PSet(
        passingGJPrePho = cms.InputTag("goodPhotonsPROBEFullPreselection"),
        passingLoose = cms.InputTag("goodPhotonsPROBECutBasedLoose"),
        passingLoose80X = cms.InputTag("goodPhotonsPROBECutBasedLoose80X"),
        passingMVA = cms.InputTag("goodPhotonsPROBEMVA"),
        passingMVA80Xwp80 = cms.InputTag("goodPhotonsPROBEMVA80Xwp80"),
        passingMVA80Xwp90 = cms.InputTag("goodPhotonsPROBEMVA80Xwp90"),
        passingMedium = cms.InputTag("goodPhotonsPROBECutBasedMedium"),
        passingMedium80X = cms.InputTag("goodPhotonsPROBECutBasedMedium80X"),
        passingTight = cms.InputTag("goodPhotonsPROBECutBasedTight"),
        passingTight80X = cms.InputTag("goodPhotonsPROBECutBasedTight80X")
    ),
    ignoreExceptions = cms.bool(True),
    isMC = cms.bool(False),
    pairFlags = cms.PSet(
        mass60to120 = cms.string('60 < mass < 120')
    ),
    pairVariables = cms.PSet(
        abseta = cms.string('abs(eta)'),
        eta = cms.string('eta'),
        mass = cms.string('mass'),
        pt = cms.string('pt')
    ),
    pfMet = cms.InputTag("slimmedMETsPuppi"),
    pileupInfoTag = cms.InputTag("slimmedAddPileupInfo"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    tagFlags = cms.PSet(

    ),
    tagProbePairs = cms.InputTag("tagTightPhoID"),
    tagVariables = cms.PSet(
        Ele_abseta = cms.string('abs(eta)'),
        Ele_dxy = cms.InputTag("eleVarHelper","dxy"),
        Ele_dz = cms.InputTag("eleVarHelper","dz"),
        Ele_e = cms.string('energy'),
        Ele_et = cms.string('et'),
        Ele_eta = cms.string('eta'),
        Ele_mHits = cms.InputTag("eleVarHelper","missinghits"),
        Ele_nonTrigMVA = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values"),
        Ele_phi = cms.string('phi'),
        Ele_pt = cms.string('pt'),
        Ele_q = cms.string('charge'),
        Ele_trigMVA = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig25nsV1Values"),
        sc_abseta = cms.string('abs(-log(tan(superCluster.position.theta/2)))'),
        sc_energy = cms.string('superCluster.energy'),
        sc_et = cms.string('superCluster.energy*sin(superClusterPosition.theta)'),
        sc_eta = cms.string('-log(tan(superClusterPosition.theta/2))')
    ),
    variables = cms.PSet(
        probe_Pho_ESsigma = cms.InputTag("photonIDValueMapProducer","phoESEffSigmaRR"),
        probe_Pho_abseta = cms.string('abs(eta)'),
        probe_Pho_chIso = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
        probe_Pho_chWorIso = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolation"),
        probe_Pho_e = cms.string('energy'),
        probe_Pho_et = cms.string('et'),
        probe_Pho_eta = cms.string('eta'),
        probe_Pho_full5x5x_r9 = cms.string('full5x5_r9'),
        probe_Pho_hoe = cms.string('hadronicOverEm'),
        probe_Pho_neuIso = cms.InputTag("photonIDValueMapProducer","phoNeutralHadronIsolation"),
        probe_Pho_phoIso = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
        probe_Pho_r9 = cms.string('r9'),
        probe_Pho_sieie = cms.string('full5x5_sigmaIetaIeta'),
        probe_Pho_sieip = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIPhi"),
        probe_mva = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring15NonTrig25nsV2p1Values"),
        probe_mva80X = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Values"),
        probe_sc_abseta = cms.string('abs(-log(tan(superCluster.position.theta/2)))'),
        probe_sc_energy = cms.string('superCluster.energy'),
        probe_sc_et = cms.string('superCluster.energy*sin(superCluster.position.theta)'),
        probe_sc_eta = cms.string('-log(tan(superCluster.position.theta/2))')
    ),
    vertexCollection = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.GsfElectronToSC = cms.EDAnalyzer("TagProbeFitTreeProducer",
    addEventVariablesInfo = cms.bool(True),
    addRunLumiInfo = cms.bool(True),
    allProbes = cms.InputTag("goodSuperClustersHLT"),
    arbitration = cms.string('HighestPt'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    flags = cms.PSet(
        passingRECO = cms.InputTag("GsfMatchedSuperClusterCands","superclusters")
    ),
    ignoreExceptions = cms.bool(True),
    isMC = cms.bool(False),
    pairFlags = cms.PSet(
        mass60to120 = cms.string('60 < mass < 120')
    ),
    pairVariables = cms.PSet(
        abseta = cms.string('abs(eta)'),
        eta = cms.string('eta'),
        mass = cms.string('mass'),
        pt = cms.string('pt')
    ),
    pfMet = cms.InputTag("slimmedMETsPuppi"),
    pileupInfoTag = cms.InputTag("slimmedAddPileupInfo"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    tagFlags = cms.PSet(

    ),
    tagProbePairs = cms.InputTag("tagTightSC"),
    tagVariables = cms.PSet(
        Ele_abseta = cms.string('abs(eta)'),
        Ele_dxy = cms.InputTag("eleVarHelper","dxy"),
        Ele_dz = cms.InputTag("eleVarHelper","dz"),
        Ele_e = cms.string('energy'),
        Ele_et = cms.string('et'),
        Ele_eta = cms.string('eta'),
        Ele_mHits = cms.InputTag("eleVarHelper","missinghits"),
        Ele_nonTrigMVA = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values"),
        Ele_phi = cms.string('phi'),
        Ele_pt = cms.string('pt'),
        Ele_q = cms.string('charge'),
        Ele_trigMVA = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig25nsV1Values"),
        sc_abseta = cms.string('abs(-log(tan(superCluster.position.theta/2)))'),
        sc_energy = cms.string('superCluster.energy'),
        sc_et = cms.string('superCluster.energy*sin(superClusterPosition.theta)'),
        sc_eta = cms.string('-log(tan(superClusterPosition.theta/2))')
    ),
    variables = cms.PSet(
        probe_sc_abseta = cms.string('abs(eta)'),
        probe_sc_e = cms.string('energy'),
        probe_sc_et = cms.string('et'),
        probe_sc_eta = cms.string('eta'),
        probe_sc_pt = cms.string('pt'),
        probe_sc_tkIso = cms.InputTag("recoEcalCandidateHelper","scTkIso")
    ),
    vertexCollection = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.GsfElectronToTrigger = cms.EDAnalyzer("TagProbeFitTreeProducer",
    addEventVariablesInfo = cms.bool(True),
    addRunLumiInfo = cms.bool(True),
    allProbes = cms.InputTag("goodElectronsProbeMeasureHLT"),
    arbitration = cms.string('HighestPt'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    flags = cms.PSet(
        passingHLT = cms.InputTag("goodElectronsMeasureHLT"),
        passingHLTsafe = cms.InputTag("goodElectronsPROBEHLTsafe"),
        passingLoose = cms.InputTag("goodElectronsPROBECutBasedLoose"),
        passingMedium = cms.InputTag("goodElectronsPROBECutBasedMedium"),
        passingTight = cms.InputTag("goodElectronsPROBECutBasedTight")
    ),
    ignoreExceptions = cms.bool(True),
    isMC = cms.bool(False),
    pairFlags = cms.PSet(
        mass60to120 = cms.string('60 < mass < 120')
    ),
    pairVariables = cms.PSet(
        abseta = cms.string('abs(eta)'),
        eta = cms.string('eta'),
        mass = cms.string('mass'),
        pt = cms.string('pt')
    ),
    pfMet = cms.InputTag("slimmedMETsPuppi"),
    pileupInfoTag = cms.InputTag("slimmedAddPileupInfo"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    tagFlags = cms.PSet(

    ),
    tagProbePairs = cms.InputTag("tagTightHLT"),
    tagVariables = cms.PSet(
        Ele_abseta = cms.string('abs(eta)'),
        Ele_dxy = cms.InputTag("eleVarHelper","dxy"),
        Ele_dz = cms.InputTag("eleVarHelper","dz"),
        Ele_e = cms.string('energy'),
        Ele_et = cms.string('et'),
        Ele_eta = cms.string('eta'),
        Ele_mHits = cms.InputTag("eleVarHelper","missinghits"),
        Ele_nonTrigMVA = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values"),
        Ele_phi = cms.string('phi'),
        Ele_pt = cms.string('pt'),
        Ele_q = cms.string('charge'),
        Ele_trigMVA = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig25nsV1Values"),
        sc_abseta = cms.string('abs(-log(tan(superCluster.position.theta/2)))'),
        sc_energy = cms.string('superCluster.energy'),
        sc_et = cms.string('superCluster.energy*sin(superClusterPosition.theta)'),
        sc_eta = cms.string('-log(tan(superClusterPosition.theta/2))')
    ),
    variables = cms.PSet(
        probe_Ele_3charge = cms.string('chargeInfo().isGsfCtfScPixConsistent'),
        probe_Ele_abseta = cms.string('abs(eta)'),
        probe_Ele_chIso = cms.string('pfIsolationVariables().sumChargedHadronPt'),
        probe_Ele_chisq = cms.InputTag("eleVarHelper","chisq"),
        probe_Ele_dEtaIn = cms.string('deltaEtaSuperClusterTrackAtVtx'),
        probe_Ele_dEtaSeed = cms.string('deltaEtaSuperClusterTrackAtVtx+log(tan(superCluster.position.theta/2))-log(tan(superCluster.seed.position.theta/2))'),
        probe_Ele_dPhiIn = cms.string('deltaPhiSuperClusterTrackAtVtx'),
        probe_Ele_dr03TkSumPt = cms.string('dr03TkSumPt'),
        probe_Ele_dxy = cms.InputTag("eleVarHelper","dxy"),
        probe_Ele_dz = cms.InputTag("eleVarHelper","dz"),
        probe_Ele_e = cms.string('energy'),
        probe_Ele_e1x5 = cms.string('e1x5'),
        probe_Ele_e2x5 = cms.string('e2x5Max'),
        probe_Ele_e5x5 = cms.string('e5x5'),
        probe_Ele_ecalIso = cms.string('ecalPFClusterIso'),
        probe_Ele_et = cms.string('et'),
        probe_Ele_eta = cms.string('eta'),
        probe_Ele_hcalIso = cms.string('hcalPFClusterIso'),
        probe_Ele_hoe = cms.string('hadronicOverEm'),
        probe_Ele_hzzMVA80X = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16HZZV1Values"),
        probe_Ele_mHits = cms.InputTag("eleVarHelper","missinghits"),
        probe_Ele_neuIso = cms.string('pfIsolationVariables().sumNeutralHadronEt'),
        probe_Ele_nonTrigMVA = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values"),
        probe_Ele_nonTrigMVA80X = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values"),
        probe_Ele_ooemoop = cms.string('(1.0/ecalEnergy - eSuperClusterOverP/ecalEnergy)'),
        probe_Ele_phoIso = cms.string('pfIsolationVariables().sumPhotonEt'),
        probe_Ele_pt = cms.string('pt'),
        probe_Ele_q = cms.string('charge'),
        probe_Ele_r9 = cms.string('r9'),
        probe_Ele_r9_5x5 = cms.string('full5x5_r9'),
        probe_Ele_sieie = cms.string('sigmaIetaIeta'),
        probe_Ele_sieie_5x5 = cms.string('full5x5_sigmaIetaIeta'),
        probe_Ele_trigMVA = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig25nsV1Values"),
        probe_Ele_trkIso = cms.string('trackIso'),
        probe_Ele_trkPt = cms.string('gsfTrack().ptMode'),
        probe_sc_abseta = cms.string('abs(-log(tan(superCluster.position.theta/2)))'),
        probe_sc_energy = cms.string('superCluster.energy'),
        probe_sc_et = cms.string('superCluster.energy*sin(superClusterPosition.theta)'),
        probe_sc_eta = cms.string('-log(tan(superCluster.position.theta/2))'),
        probe_sc_etaW = cms.string('superCluster.etaWidth'),
        probe_sc_phi = cms.string('superCluster.phi'),
        probe_sc_phiW = cms.string('superCluster.phiWidth'),
        probe_sc_preshowerE = cms.string('superCluster.preshowerEnergy'),
        probe_sc_rawE = cms.string('superCluster.rawEnergy')
    ),
    vertexCollection = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.out = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('p')
    ),
    fileName = cms.untracked.string('edmFile.root')
)


process.egmPhotonIsolationMiniAODSequence = cms.Sequence(process.egmPhotonIsolation)


process.mc_sequence = cms.Sequence()


process.ele_sequence = cms.Sequence(process.goodElectronsPROBEHLTsafe+process.goodElectronsPROBECutBasedVeto+process.goodElectronsPROBECutBasedLoose+process.goodElectronsPROBECutBasedMedium+process.goodElectronsPROBECutBasedTight+process.goodElectronsPROBECutBasedVeto80X+process.goodElectronsPROBECutBasedLoose80X+process.goodElectronsPROBECutBasedMedium80X+process.goodElectronsPROBECutBasedTight80X+process.goodElectronsPROBEMVA80Xwp90+process.goodElectronsPROBEMVA80Xwp80+process.goodElectronsProbeHLT)


process.init_sequence = cms.Sequence()


process.sc_sequence = cms.Sequence(process.superClusterCands+process.goodSuperClusters+process.goodSuperClustersHLT+process.GsfMatchedSuperClusterCands)


process.hlt_sequence = cms.Sequence(process.goodElectronsProbeMeasureHLT+process.goodElectronsMeasureHLT)


process.tree_sequence = cms.Sequence(process.GsfElectronToPhoID)


process.allTagsAndProbes = cms.Sequence(process.tagTightPhoID)


process.egmPhotonIDSequence = cms.Sequence(process.egmPhotonIsolationMiniAODSequence+process.photonIDValueMapProducer+process.photonMVAValueMapProducer+process.egmPhotonIDs+process.photonRegressionValueMapProducer)


process.egmGsfElectronIDSequence = cms.Sequence(process.electronMVAValueMapProducer+process.egmGsfElectronIDs+process.electronRegressionValueMapProducer)


process.pho_sequence = cms.Sequence(process.goodPhotons+process.egmPhotonIDSequence+process.goodPhotonsPROBECutBasedLoose+process.goodPhotonsPROBECutBasedMedium+process.goodPhotonsPROBECutBasedTight+process.goodPhotonsPROBEMVA+process.goodPhotonsPROBECutBasedLoose80X+process.goodPhotonsPROBECutBasedMedium80X+process.goodPhotonsPROBECutBasedTight80X+process.goodPhotonsPROBEMVA80Xwp90+process.goodPhotonsPROBEMVA80Xwp80+process.goodPhotonsProbeHLT+process.goodPhotonsChIso+process.goodPhotonsPhoIso+process.goodPhotonsPROBEFullPreselection)


process.tag_sequence = cms.Sequence(process.goodElectrons+process.egmGsfElectronIDSequence+process.goodElectronsTAGCutBasedTight+process.goodElectronsTagHLT)


process.cand_sequence = cms.Sequence(process.init_sequence+process.tag_sequence+process.pho_sequence)


process.p = cms.Path(process.sampleInfo+process.hltFilter+process.cand_sequence+process.allTagsAndProbes+process.mc_sequence+process.eleVarHelper+process.tree_sequence)


process.outpath = cms.EndPath()


process.DQMStore = cms.Service("DQMStore",
    LSbasedMode = cms.untracked.bool(False),
    collateHistograms = cms.untracked.bool(False),
    enableMultiThread = cms.untracked.bool(False),
    forceResetOnBeginLumi = cms.untracked.bool(False),
    referenceFileName = cms.untracked.string(''),
    verbose = cms.untracked.int32(0),
    verboseQT = cms.untracked.int32(0)
)


process.MessageLogger = cms.Service("MessageLogger",
    FrameworkJobReport = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        optionalPSet = cms.untracked.bool(True)
    ),
    categories = cms.untracked.vstring('FwkJob', 
        'FwkReport', 
        'FwkSummary', 
        'Root_NoDictionary'),
    cerr = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1000)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        noTimeStamps = cms.untracked.bool(False),
        optionalPSet = cms.untracked.bool(True),
        threshold = cms.untracked.string('')
    ),
    cerr_stats = cms.untracked.PSet(
        optionalPSet = cms.untracked.bool(True),
        output = cms.untracked.string('cerr'),
        threshold = cms.untracked.string('WARNING')
    ),
    cout = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    debugModules = cms.untracked.vstring(),
    debugs = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    default = cms.untracked.PSet(

    ),
    destinations = cms.untracked.vstring('warnings', 
        'errors', 
        'infos', 
        'debugs', 
        'cout', 
        'cerr'),
    errors = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    fwkJobReports = cms.untracked.vstring('FrameworkJobReport'),
    infos = cms.untracked.PSet(
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        optionalPSet = cms.untracked.bool(True),
        placeholder = cms.untracked.bool(True)
    ),
    statistics = cms.untracked.vstring('cerr_stats'),
    suppressDebug = cms.untracked.vstring(),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring(),
    warnings = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    )
)


process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
    LHCTransport = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(87654321)
    ),
    MuonSimHits = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(987346)
    ),
    VtxSmeared = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(98765432)
    ),
    ecalPreshowerRecHit = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(6541321)
    ),
    ecalRecHit = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(654321)
    ),
    externalLHEProducer = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(234567)
    ),
    famosPileUp = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    famosSimHits = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(13579)
    ),
    g4SimHits = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(11)
    ),
    generator = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(123456789)
    ),
    hbhereco = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    hfreco = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    hiSignal = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(123456789)
    ),
    hiSignalG4SimHits = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(11)
    ),
    hiSignalLHCTransport = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(88776655)
    ),
    horeco = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    l1ParamMuons = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(6453209)
    ),
    mix = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(12345)
    ),
    mixData = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(12345)
    ),
    mixGenPU = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    mixRecoTracks = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    mixSimCaloHits = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    paramMuons = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(54525)
    ),
    saveFileName = cms.untracked.string(''),
    siTrackerGaussianSmearingRecHits = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(24680)
    ),
    simBeamSpotFilter = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(87654321)
    ),
    simMuonCSCDigis = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(11223344)
    ),
    simMuonDTDigis = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(1234567)
    ),
    simMuonRPCDigis = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(1234567)
    ),
    simSiStripDigiSimLink = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(1234567)
    )
)


process.TFileService = cms.Service("TFileService",
    closeFileFast = cms.untracked.bool(True),
    fileName = cms.string('TnPTree_data.root')
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring('HCAL', 
        'ZDC', 
        'CASTOR', 
        'EcalBarrel', 
        'EcalEndcap', 
        'EcalPreshower', 
        'TOWER')
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerGeometryFromDBEP = cms.ESProducer("CaloTowerGeometryFromDBEP",
    applyAlignment = cms.bool(False),
    hcalTopologyConstants = cms.PSet(
        maxDepthHB = cms.int32(2),
        maxDepthHE = cms.int32(3),
        mode = cms.string('HcalTopologyMode::LHC')
    )
)


process.CaloTowerTopologyEP = cms.ESProducer("CaloTowerTopologyEP")


process.CastorDbProducer = cms.ESProducer("CastorDbProducer")


process.CastorGeometryFromDBEP = cms.ESProducer("CastorGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.EcalBarrelGeometryFromDBEP = cms.ESProducer("EcalBarrelGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryFromDBEP = cms.ESProducer("EcalEndcapGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService")


process.EcalPreshowerGeometryFromDBEP = cms.ESProducer("EcalPreshowerGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.GlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.HcalAlignmentEP = cms.ESProducer("HcalAlignmentEP")


process.HcalGeometryFromDBEP = cms.ESProducer("HcalGeometryFromDBEP",
    applyAlignment = cms.bool(True),
    hcalTopologyConstants = cms.PSet(
        maxDepthHB = cms.int32(2),
        maxDepthHE = cms.int32(3),
        mode = cms.string('HcalTopologyMode::LHC')
    )
)


process.MuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.ParabolicParametrizedMagneticFieldProducer = cms.ESProducer("AutoParametrizedMagneticFieldProducer",
    label = cms.untracked.string('ParabolicMf'),
    valueOverride = cms.int32(-1),
    version = cms.string('Parabolic')
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    compatibiltyWith11 = cms.untracked.bool(True),
    useDDD = cms.untracked.bool(False)
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0),
    PreFilter = cms.bool(False)
)


process.StripCPEfromTrackAngleESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('StripCPEfromTrackAngle'),
    ComponentType = cms.string('StripCPEfromTrackAngle'),
    parameters = cms.PSet(
        mLC_P0 = cms.double(-0.326),
        mLC_P1 = cms.double(0.618),
        mLC_P2 = cms.double(0.3),
        mTEC_P0 = cms.double(-1.885),
        mTEC_P1 = cms.double(0.471),
        mTIB_P0 = cms.double(-0.742),
        mTIB_P1 = cms.double(0.202),
        mTID_P0 = cms.double(-1.427),
        mTID_P1 = cms.double(0.433),
        mTOB_P0 = cms.double(-1.026),
        mTOB_P1 = cms.double(0.253),
        maxChgOneMIP = cms.double(6000.0),
        useLegacyError = cms.bool(False)
    )
)


process.TrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer")


process.VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducerFromDB",
    debugBuilder = cms.untracked.bool(False),
    label = cms.untracked.string(''),
    valueOverride = cms.int32(-1)
)


process.ZdcGeometryFromDBEP = cms.ESProducer("ZdcGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.fakeForIdealAlignment = cms.ESProducer("FakeAlignmentProducer",
    appendToDataLabel = cms.string('fakeForIdeal')
)


process.hcalDDDRecConstants = cms.ESProducer("HcalDDDRecConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalDDDSimConstants = cms.ESProducer("HcalDDDSimConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalTopologyIdeal = cms.ESProducer("HcalTopologyIdealEP",
    Exclude = cms.untracked.string(''),
    appendToDataLabel = cms.string('')
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer",
    dump = cms.untracked.vstring(''),
    file = cms.untracked.string('')
)


process.idealForDigiCSCGeometry = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.idealForDigiDTGeometry = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.idealForDigiTrackerGeometry = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiPixelQualityFromDbRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        ))
)


process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer("SiStripBackPlaneCorrectionDepESProducer",
    BackPlaneCorrectionDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    )
)


process.siStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    APVGain = cms.VPSet(cms.PSet(
        Label = cms.untracked.string(''),
        NormalizationFactor = cms.untracked.double(1.0),
        Record = cms.string('SiStripApvGainRcd')
    ), 
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGain2Rcd')
        )),
    AutomaticNormalization = cms.bool(False),
    appendToDataLabel = cms.string(''),
    printDebug = cms.untracked.bool(False)
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripLorentzAngleRcd')
    ),
    LorentzAnglePeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripLorentzAngleRcd')
    )
)


process.siStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiStripDetVOffRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('RunInfoRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadStripRcd'),
            tag = cms.string('')
        )),
    PrintDebugOutput = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.stripCPEESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('stripCPE'),
    ComponentType = cms.string('SimpleStripCPE'),
    parameters = cms.PSet(

    )
)


process.trackerGeometryDB = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.trackerNumberingGeometryDB = cms.ESProducer("TrackerGeometricDetESModule",
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(False)
)


process.trackerTopology = cms.ESProducer("TrackerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    DumpStat = cms.untracked.bool(False),
    ReconnectEachRun = cms.untracked.bool(False),
    RefreshAlways = cms.untracked.bool(False),
    RefreshEachRun = cms.untracked.bool(False),
    RefreshOpenIOVs = cms.untracked.bool(False),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string('80X_dataRun2_Candidate_2016_09_02_10_26_48'),
    pfnPostfix = cms.untracked.string(''),
    pfnPrefix = cms.untracked.string(''),
    snapshotTime = cms.string(''),
    toGet = cms.VPSet()
)


process.HepPDTESSource = cms.ESSource("HepPDTESSource",
    pdtFileName = cms.FileInPath('SimGeneral/HepPDTESSource/data/pythiaparticle.tbl')
)


process.eegeom = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd')
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    GainWidthsForTrigPrims = cms.bool(False),
    HERecalibration = cms.bool(False),
    HEreCalibCutoff = cms.double(20.0),
    HFRecalibration = cms.bool(False),
    iLumi = cms.double(-1.0),
    testHFQIE10 = cms.bool(False),
    toGet = cms.untracked.vstring('GainWidths')
)


process.prefer("es_hardcode")

