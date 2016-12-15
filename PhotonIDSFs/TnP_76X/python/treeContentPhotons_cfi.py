import FWCore.ParameterSet.Config as cms

##########################################################################
## TREE CONTENT
#########################################################################
    

ZVariablesToStore = cms.PSet(
    eta    = cms.string("eta"),
    abseta = cms.string("abs(eta)"),
    pt     = cms.string("pt"),
    mass   = cms.string("mass")
    )   

ProbeVariablesToStore = cms.PSet(
    probe_Pho_eta    = cms.string("eta"),
    probe_Pho_abseta = cms.string("abs(eta)"),
    probe_Pho_et     = cms.string("et"),
    probe_Pho_e      = cms.string("energy"),
    probe_Pho_sieie  = cms.string("full5x5_sigmaIetaIeta"),
## super cluster quantities
    probe_sc_energy = cms.string("superCluster.energy"),
    probe_sc_et     = cms.string("superCluster.energy*sin(superCluster.position.theta)"),    
    probe_sc_eta    = cms.string("superCluster.eta"),
    probe_sc_abseta = cms.string("abs(superCluster.eta)"),

#id based
    probe_Pho_full5x5x_r9   = cms.string("full5x5_r9"),
    probe_Pho_r9            = cms.string("r9"),
    probe_Pho_sigmaIEtaIEta = cms.string("full5x5_sigmaIetaIeta"),
    probe_Pho_ESsigma       = cms.InputTag("photonIDValueMapProducer:phoESEffSigmaRR"),
    probe_Pho_sigmaIEtaIPhi = cms.InputTag("photonIDValueMapProducer:phoFull5x5SigmaIEtaIPhi"),
    probe_Pho_hoe           = cms.string("hadronicOverEm"),

#iso
    probe_Pho_chIso    = cms.InputTag("photonIDValueMapProducer:phoChargedIsolation"),
    probe_Pho_neuIso   = cms.InputTag("photonIDValueMapProducer:phoNeutralHadronIsolation"),
    probe_Pho_phoIso   = cms.InputTag("photonIDValueMapProducer:phoPhotonIsolation"),
    probe_Pho_chWorIso = cms.InputTag("photonIDValueMapProducer:phoWorstChargedIsolation"), 
    probe_mva          = cms.InputTag("photonMVAValueMapProducer:PhotonMVAEstimatorRun2Spring15NonTrig50nsV2Values"),
)

TagVariablesToStore = cms.PSet(
    Pho_eta    = cms.string("eta"),
    Pho_abseta = cms.string("abs(eta)"),
    Pho_pt     = cms.string("pt"),
    Pho_et     = cms.string("et"),
    Pho_e      = cms.string("energy"),
    
    ## super cluster quantities
    sc_energy = cms.string("superCluster.energy"),
    sc_et     = cms.string("superCluster.energy*sin(superCluster.position.theta)"),    
    sc_eta    = cms.string("superCluster.eta"),
    sc_abseta = cms.string("abs(superCluster.eta)"),
    Pho_full5x5x_r9   = cms.string("full5x5_r9"),
    Pho_r9            = cms.string("r9"),
    Pho_mva           = cms.InputTag("photonMVAValueMapProducer:PhotonMVAEstimatorRun2Spring15NonTrig50nsV2Values"),
)

CommonStuffForPhotonProbe = cms.PSet(
    variables = cms.PSet(ProbeVariablesToStore),
    ignoreExceptions =  cms.bool (True),
    addRunLumiInfo   =  cms.bool (True),
    pileupInfoTag = cms.InputTag("slimmedAddPileupInfo"),
    addEventVariablesInfo   =  cms.bool(True),
    vertexCollection = cms.InputTag("offlineSlimmedPrimaryVertices"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    pfMet = cms.InputTag("slimmedMETs"),
    pairVariables =  cms.PSet(ZVariablesToStore),
    pairFlags     =  cms.PSet(
        mass60to120 = cms.string("60 < mass < 120")
        ),
    tagVariables   =  cms.PSet(TagVariablesToStore),
    tagFlags       =  cms.PSet(),    
    )

mcTruthCommonStuff = cms.PSet(
    isMC        = cms.bool(True),
    #tagMatches  = cms.InputTag("McMatchTag"),
    motherPdgId = cms.vint32(),
    #motherPdgId = cms.vint32(22,23), # g, Z
    #motherPdgId = cms.vint32(443), # JPsi
    #motherPdgId = cms.vint32(553), # Yupsilon
    #makeMCUnbiasTree       = cms.bool(False),
    #checkMotherInUnbiasEff = cms.bool(False),
    genParticles = cms.InputTag("prunedGenParticles"),
    useTauDecays = cms.bool(False),
    checkCharge = cms.bool(False),
    pdgId = cms.int32(11),
    mcVariables = cms.PSet(
        probe_eta    = cms.string("eta"),
        probe_abseta = cms.string("abs(eta)"),
        probe_et     = cms.string("et"),
        probe_e      = cms.string("energy"),
        ),
    mcFlags     =  cms.PSet(
        probe_flag = cms.string("pt>0")
        ),      
    )