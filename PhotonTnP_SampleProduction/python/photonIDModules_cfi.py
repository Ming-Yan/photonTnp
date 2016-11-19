import FWCore.ParameterSet.Config as cms

###################################################################
## ID MODULES
###################################################################

from PhysicsTools.SelectorUtils.tools.vid_id_tools import *

def setIDs(process, options):

    dataFormat = DataFormat.MiniAOD
    if (options['useAOD']):
        dataFormat = DataFormat.AOD
        
    switchOnVIDPhotonIdProducer(process, dataFormat)
        
    # define which IDs we want to produce
    my_id_modules = ['RecoEgamma.PhotonIdentification.Identification.cutBasedPhotonID_Spring15_25ns_V1_cff',
                     'RecoEgamma.PhotonIdentification.Identification.mvaPhotonID_Spring15_25ns_nonTrig_V2p1_cff']
                 
    for idmod in my_id_modules:
        setupAllVIDIdsInModule(process, idmod, setupVIDPhotonSelection)

    process.goodPhotonsPROBECutBasedLoose = cms.EDProducer("PatPhotonSelectorByValueMap",
                                                           input     = cms.InputTag("goodPhotons"),
                                                           cut       = cms.string(options['PHOTON_CUTS']),
                                                           selection = cms.InputTag("egmPhotonIDs:cutBasedPhotonID-Spring15-25ns-V1-standalone-loose"),
                                                           id_cut    = cms.bool(True)
                                                           )

    process.goodPhotonsPROBECutBasedMedium = process.goodPhotonsPROBECutBasedLoose.clone()
    process.goodPhotonsPROBECutBasedMedium.selection = cms.InputTag("egmPhotonIDs:cutBasedPhotonID-Spring15-25ns-V1-standalone-medium")
    process.goodPhotonsPROBECutBasedTight = process.goodPhotonsPROBECutBasedLoose.clone()
    process.goodPhotonsPROBECutBasedTight.selection = cms.InputTag("egmPhotonIDs:cutBasedPhotonID-Spring15-25ns-V1-standalone-tight")
    process.goodPhotonsPROBEMVA = process.goodPhotonsPROBECutBasedLoose.clone()
    process.goodPhotonsPROBEMVA.selection = cms.InputTag("egmPhotonIDs:mvaPhoID-Spring15-25ns-nonTrig-V2p1-wp90")    



    # additional preselected cut for ZG analysis, add by PH in 08_15
    process.goodPhotonsPhoIso = cms.EDProducer("PatPhotonSelectorByDoubleValueMap",
                                               input     = cms.InputTag("goodPhotons"),
                                               cut       = cms.string(options['PHOTON_CUTS']),
                                               selection = cms.InputTag("photonIDValueMapProducer:phoPhotonIsolation"),
                                               id_cut    = cms.double(15.0),
                                               isGreaterThan = cms.bool(False)
                                               )
    

    # additional preselected cut for ZG analysis, add by PH in 08_15
    process.goodPhotonsPROBEFullPreselection = cms.EDProducer("PatPhotonSelectorByDoubleValueMap",
                                                              input     = cms.InputTag("goodPhotonsPhoIso"),
                                                              cut       = cms.string(options['PHOTON_CUTS']),
                                                              selection = cms.InputTag("photonIDValueMapProducer:phoWorstChargedIsolation"),
                                                              id_cut    = cms.double(15.0),
                                                              isGreaterThan = cms.bool(False)
                                                              )
    # END OF additional preselected cut for ZG analysis, add by PH in 08_15



#    process.goodPhotonsTAGCutBasedLoose = cms.EDProducer("PatPhotonSelectorByValueMap",
#                                                         input     = cms.InputTag("goodPhotons"),
#                                                         cut       = cms.string(options['PHOTON_TAG_CUTS']),
#                                                         selection = cms.InputTag("egmPhotonIDs:cutBasedPhotonID-Spring15-25ns-V1-standalone-loose"),
#                                                         id_cut    = cms.bool(True)
#                                                         )
    
#    process.goodPhotonsTAGCutBasedMedium = process.goodPhotonsTAGCutBasedLoose.clone()
#    process.goodPhotonsTAGCutBasedMedium.selection = cms.InputTag("egmPhotonIDs:cutBasedPhotonID-Spring15-25ns-V1-standalone-medium")
#    process.goodPhotonsTAGCutBasedTight = process.goodPhotonsTAGCutBasedLoose.clone()
#    process.goodPhotonsTAGCutBasedTight.selection = cms.InputTag("egmPhotonIDs:cutBasedPhotonID-Spring15-25ns-V1-standalone-tight")
