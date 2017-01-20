#############################################################
########## General settings
#############################################################
# flag to be Tested
flags = {
    'passingLoose'      : '(passingLoose  == 1)',
    'passingMedium'     : '(passingMedium == 1)',
    'passingTight'      : '(passingTight  == 1)',
    'passingLoose80X'   : '(passingLoose80X  == 1)',
    'passingMedium80X'  : '(passingMedium80X == 1)',
    'passingTight80X'   : '(passingTight80X  == 1)',
    'passingMVA80Xwp80' : '(passingMVA80Xwp80 == 1)',
    'passingMVA80Xwp90' : '(passingMVA80Xwp90 == 1)',
    }

baseOutDir = 'results/Moriond17/tnpPhoID_Winter17_v3/runFull2016'

#############################################################
########## samples definition  - preparing the samples
#############################################################
### samples are defined in etc/inputs/tnpSampleDef.py
### not: you can setup another sampleDef File in inputs
import etc.inputs.tnpSampleDef as tnpSamples
tnpTreeDir = 'GsfElectronToPhoID'

samplesDef = {
    'data'   : tnpSamples.Moriond17_80X['data_Run2016H'].clone(),
    'mcNom'  : tnpSamples.Moriond17_80X['DY_madgraph_Winter17'].clone(),
    'mcAlt'  : tnpSamples.Moriond17_80X['DY_amcatnlo_Winter17'].clone(),
    'tagSel' : tnpSamples.Moriond17_80X['DY_madgraph_Winter17'].clone(),
}
## can add data sample easily
samplesDef['data'].add_sample( tnpSamples.Moriond17_80X['data_Run2016G'] )
samplesDef['data'].add_sample( tnpSamples.Moriond17_80X['data_Run2016F'] )
samplesDef['data'].add_sample( tnpSamples.Moriond17_80X['data_Run2016E'] )
samplesDef['data'].add_sample( tnpSamples.Moriond17_80X['data_Run2016D'] )
samplesDef['data'].add_sample( tnpSamples.Moriond17_80X['data_Run2016C'] )
samplesDef['data'].add_sample( tnpSamples.Moriond17_80X['data_Run2016B'] )

## some sample-based cuts... general cuts defined here after
## require mcTruth on MC DY samples and additional cuts
## all the samples MUST have different names (i.e. sample.name must be different for all)
## if you need to use 2 times the same sample, then rename the second one
#samplesDef['data'  ].set_cut('run >= 273726')
samplesDef['data' ].set_tnpTree(tnpTreeDir)
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_tnpTree(tnpTreeDir)
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_tnpTree(tnpTreeDir)
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_tnpTree(tnpTreeDir)

if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_mcTruth()
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_mcTruth()
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_mcTruth()
if not samplesDef['tagSel'] is None:
    samplesDef['tagSel'].rename('mcAltSel_DY_madgraph')
    samplesDef['tagSel'].set_cut('tag_Ele_pt > 35  && tag_Ele_nonTrigMVA > 0.95')

## set MC weight, simple way (use tree weight) 
#weightName = 'totWeight'
#if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
#if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
#if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_weight(weightName)

## set MC weight, can use several pileup rw for different data taking periods
weightName = 'weights_2016_runAll.totWeight'
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_weight(weightName)
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_puTree('eos/cms/store/group/phys_egamma/tnp/80X/pu/Winter17/DY_madgraph_Winter17_pho.pu.puTree.root')
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_puTree('eos/cms/store/group/phys_egamma/tnp/80X/pu/Winter17/DY_amcatnlo_Winter17_pho.pu.puTree.root')
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_puTree('eos/cms/store/group/phys_egamma/tnp/80X/pu/Winter17/DY_madgraph_Winter17_pho.pu.puTree.root')


#############################################################
########## bining definition  [can be nD bining]
#############################################################
biningDef = [
   { 'var' : 'probe_sc_eta' , 'type': 'float', 'bins': [-2.5,-2.0,-1.566,-1.4442, -0.8, 0.0, 0.8, 1.4442, 1.566, 2.0, 2.5] },
   { 'var' : 'probe_Pho_et' , 'type': 'float', 'bins': [15,20,35,50,90,150,500] },
]

#############################################################
########## Cuts definition for all samples
#############################################################
### cut
cutBase   = 'tag_Ele_pt > 30 && abs(tag_sc_eta) < 2.17'

# can add addtionnal cuts for some bins (first check bin number using tnpEGM --checkBins)
additionalCuts = { 
   0 : 'tag_Ele_nonTrigMVA > 0.97 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
   1 : 'tag_Ele_nonTrigMVA > 0.97 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
   2 : 'tag_Ele_nonTrigMVA > 0.97 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
   3 : 'tag_Ele_nonTrigMVA > 0.97 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
   4 : 'tag_Ele_nonTrigMVA > 0.97 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
   5 : 'tag_Ele_nonTrigMVA > 0.97 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
   6 : 'tag_Ele_nonTrigMVA > 0.97 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
   7 : 'tag_Ele_nonTrigMVA > 0.97 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
   8 : 'tag_Ele_nonTrigMVA > 0.97 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
   9 : 'tag_Ele_nonTrigMVA > 0.97 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
   10 : 'tag_Ele_nonTrigMVA > 0.97 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
   11 : 'tag_Ele_nonTrigMVA > 0.97 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
   12 : 'tag_Ele_nonTrigMVA > 0.97 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
   13 : 'tag_Ele_nonTrigMVA > 0.97 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
   14 : 'tag_Ele_nonTrigMVA > 0.97 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
   15 : 'tag_Ele_nonTrigMVA > 0.97 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
   16 : 'tag_Ele_nonTrigMVA > 0.97 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
   17 : 'tag_Ele_nonTrigMVA > 0.97 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
   18 : 'tag_Ele_nonTrigMVA > 0.97 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
   19 : 'tag_Ele_nonTrigMVA > 0.97 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
}

#### or remove any additional cut (default)
#additionalCuts = None

#############################################################
########## fitting params to tune fit by hand if necessary
#############################################################
tnpParNomFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",
    ]

tnpParAltSigFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    "acmsP[60.,50.,90.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.001, 1]","peakP[90.0]",
    "acmsF[60.,50.,90.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.001, 1]","peakF[90.0]",
    ]
     
tnpParAltBkgFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.7,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.7,0.5,5.0]",
    "alphaP[0.,-5.,5.]",
    "alphaF[0.,-5.,5.]",
    ]
        
