import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing
import PhysicsTools.TagAndProbe.baseline.commonFitMVA as common

options = VarParsing('analysis')
options.register(
    "isMC",
#    True,
    False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Compute efficiency for MC"
    )

options.register(
    "inputFileName",
    #"/afs/cern.ch/work/i/ishvetso/public/for_Matteo/TnPTree_mc-powheg.root",
    "/data2/pwang/TnP/76X_v2/TnP_Data.root",
    #"TnP_Data.root",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "Input filename"
    )

options.register(
    "outputFileName",
    "",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "Output filename"
    )

options.register(
    "idName",
    "passingMVA",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "ID variable name as in the fitter_tree"
    )

options.register(
    "dirName",
    "PhotonToRECO",
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "Folder name containing the fitter_tree"
    )

options.register(
    "doCutAndCount",
    False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Do not compute fitting, just cut and count"
    )
options.parseArguments()

process = cms.Process("TagProbe")
process.source = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.destinations = ['cout', 'cerr']
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

################################################

InputFileName = options.inputFileName
OutputFile = "efficiency-mc-"+options.idName
if (not options.isMC):
    OutputFile = "efficiency-data-"+options.idName

if (options.outputFileName != ""):
    OutputFile = OutputFile+"-"+options.outputFileName+".root"
else:
    OutputFile = OutputFile+".root"

################################################

#specifies the binning of parameters
EfficiencyBins = cms.PSet(
#    probe_Ele_et = cms.vdouble(20. ,40. ,60. ,100.),
#    probe_sc_eta = cms.vdouble(-2.5, -1.0, 0.0, 1.0, 2.5),
    probe_sc_eta = cms.vdouble(-2.5,-1.566,-1.4442,-1.0,0.0, 1.0, 1.4442, 1.566, 2.5),
    probe_sc_et = cms.vdouble(20. ,30, 40. ,50.,  200.),


    )

DataBinningSpecification = cms.PSet(
    UnbinnedVariables = cms.vstring("mass"),
    BinnedVariables = cms.PSet(EfficiencyBins),
    BinToPDFmap = cms.vstring(

        "mva_20p0To30p0_0p0To1p0", 
        #"mva_40p0To50p0_1p0To1p4442", 
        "*et_bin0*eta_bin0*","mva_20p0To30p0_m2p5Tom1p566",
        "*et_bin0*eta_bin1*","mva_20p0To30p0_m1p566Tom1p4442",
        "*et_bin0*eta_bin2*","mva_20p0To30p0_m1p4442Tom1p0",
        "*et_bin0*eta_bin3*","mva_20p0To30p0_m1p0To0p0",
        "*et_bin0*eta_bin4*","mva_20p0To30p0_0p0To1p0",
        "*et_bin0*eta_bin5*","mva_20p0To30p0_1p0To1p4442",
        "*et_bin0*eta_bin6*","mva_20p0To30p0_1p4442To1p566",
        "*et_bin0*eta_bin7*","mva_20p0To30p0_1p566To2p5",

        "*et_bin1*eta_bin0*","mva_30p0To40p0_m2p5Tom1p566",
        "*et_bin1*eta_bin1*","mva_30p0To40p0_m1p566Tom1p4442",
        "*et_bin1*eta_bin2*","mva_30p0To40p0_m1p4442Tom1p0",
        "*et_bin1*eta_bin3*","mva_30p0To40p0_m1p0To0p0",
        "*et_bin1*eta_bin4*","mva_30p0To40p0_0p0To1p0",
        "*et_bin1*eta_bin5*","mva_30p0To40p0_1p0To1p4442",
        "*et_bin1*eta_bin6*","mva_30p0To40p0_1p4442To1p566",
        "*et_bin1*eta_bin7*","mva_30p0To40p0_1p566To2p5",

        "*et_bin2*eta_bin0*","mva_40p0To50p0_m2p5Tom1p566",
        "*et_bin2*eta_bin1*","mva_40p0To50p0_m1p566Tom1p4442",
        "*et_bin2*eta_bin2*","mva_40p0To50p0_m1p4442Tom1p0",
        "*et_bin2*eta_bin3*","mva_40p0To50p0_m1p0To0p0",
        "*et_bin2*eta_bin4*","mva_40p0To50p0_0p0To1p0",
        "*et_bin2*eta_bin5*","mva_40p0To50p0_1p0To1p4442",
        "*et_bin2*eta_bin6*","mva_40p0To50p0_1p4442To1p566",
        "*et_bin2*eta_bin7*","mva_40p0To50p0_1p566To2p5",


        "*et_bin3*eta_bin0*","mva_50p0To200p0_m2p5Tom1p566",
        "*et_bin3*eta_bin1*","mva_50p0To200p0_m1p566Tom1p4442",
        "*et_bin3*eta_bin2*","mva_50p0To200p0_m1p4442Tom1p0",
        "*et_bin3*eta_bin3*","mva_50p0To200p0_m1p0To0p0",
        "*et_bin3*eta_bin4*","mva_50p0To200p0_0p0To1p0",
        "*et_bin3*eta_bin5*","mva_50p0To200p0_1p0To1p4442",
        "*et_bin3*eta_bin6*","mva_50p0To200p0_1p4442To1p566",
        "*et_bin3*eta_bin7*","mva_50p0To200p0_1p566To2p5",
        )
    )

McBinningSpecification = cms.PSet(
    UnbinnedVariables = cms.vstring("mass", "totWeight"),
    BinnedVariables = cms.PSet(EfficiencyBins, mcTrue = cms.vstring("true")),
    BinToPDFmap = cms.vstring(
        "mva_20p0To40p0_0p0To1p5", 
        "*et_bin0*eta_bin0*","mva_20p0To40p0_0p0To1p5",
        "*et_bin1*eta_bin0*","mva_40p0To60p0_0p0To1p5",
        "*et_bin2*eta_bin0*","mva_60p0To100p0_0p0To1p5",
        "*et_bin0*eta_bin1*","mva_20p0To40p0_1p5To2p5",
        "*et_bin1*eta_bin1*","mva_40p0To60p0_1p5To2p5",
        "*et_bin2*eta_bin1*","mva_60p0To100p0_1p5To2p5",
        )
)

########################

process.TnPMeasurement = cms.EDAnalyzer("TagProbeFitTreeAnalyzer",
                                        InputFileNames = cms.vstring(InputFileName),
                                        InputDirectoryName = cms.string(options.dirName),
                                        InputTreeName = cms.string("fitter_tree"), 
                                        OutputFileName = cms.string(OutputFile),
                                        NumCPU = cms.uint32(2),
                                        SaveWorkspace = cms.bool(False), #VERY TIME CONSUMING FOR MC
                                        doCutAndCount = cms.bool(options.doCutAndCount),
                                        floatShapeParameters = cms.bool(True),
                                        binnedFit = cms.bool(True),
                                        binsForFit = cms.uint32(60),
                                        WeightVariable = cms.string("totWeight"),
                                        # defines all the real variables of the probes available in the input tree and intended for use in the efficiencies
                                        Variables = cms.PSet(
        mass = cms.vstring("Tag-Probe Mass", "60.0", "120.0", "GeV/c^{2}"),
        probe_sc_et = cms.vstring("Probe E_{T}", "0", "100", "GeV/c"),
        probe_sc_eta = cms.vstring("Probe #eta", "-2.5", "2.5", ""), 
        totWeight = cms.vstring("totWeight", "-1000000", "100000000", ""),
        #event_met_pfmet = cms.vstring("event_met_pfmet", "-1000000", "100000000", "GeV")
        #event_met_pfphi = cms.vstring("event_met_pfphi", "-6", "6", "") 
        ),
                                        
                                        # defines all the discrete variables of the probes available in the input tree and intended for use in the efficiency calculation
                                        Expressions = cms.PSet(),
                                        Categories = cms.PSet(),
                                        PDFs = common.all_pdfs,
                                        Efficiencies = cms.PSet(),
                                        #Expressions = cms.PSet(myMT = cms.vstring("myMT", "sqrt(2*event_met_pfmet*tag_Pho_et*(1-cos(tag_Pho_phi-event_met_phi)))", "event_met_pfmet", "tag_Pho_et","tag_Pho_phi","event_met_phi")), 
                                        
                                        ###SJ
                                        Cuts = cms.PSet(
        #MTcut = cms.vstring("myMT", "50.", "below"),
        #mvacut = cms.vstring("tag_Pho_mva","0.95","above")
        tagEt = cms.vstring("tag_Pho_et","30","above") ###new
        ),    
                                        ###SJ
                                        )

setattr(process.TnPMeasurement.Categories, options.idName, cms.vstring(options.idName, "dummy[pass=1,fail=0]"))
setattr(process.TnPMeasurement.Categories, "mcTrue", cms.vstring("MC true", "dummy[true=1,false=0]"))

if (not options.isMC):
    delattr(process.TnPMeasurement, "WeightVariable")
    process.TnPMeasurement.Variables = cms.PSet(
        mass = cms.vstring("Tag-Probe Mass", "60.0", "120.0", "GeV/c^{2}"),
        probe_sc_et = cms.vstring("Probe E_{T}", "20", "1000", "GeV/c"),
        probe_sc_eta = cms.vstring("Probe #eta", "-2.5", "2.5", ""), 
        event_met_pfmet = cms.vstring("event_met_pfmet", "0", "100000000", "GeV"),
        #event_met_phi = cms.vstring("event_met_phi", "-10", "10", ""),
        #tag_Pho_phi = cms.vstring("tag_Pho_phi", "-10", "10", ""),
        
        ###SJ
        tag_Pho_et = cms.vstring("Tag  E_{T}", "20", "1000", "GeV/c"),
        tag_Pho_mva = cms.vstring("Tag  MVA", "-1.5", "1.5", "GeV/c")
        ###SJ
        #event_met_pfsumet = cms.vstring("event_met_pfsumet", "0", "1000", ""), 
        )
    for pdf in process.TnPMeasurement.PDFs.__dict__:
        param =  process.TnPMeasurement.PDFs.getParameter(pdf)
        if (type(param) is not cms.vstring):
            continue
        for i, l in enumerate(getattr(process.TnPMeasurement.PDFs, pdf)):
            if l.find("signalFractionInPassing") != -1:
                getattr(process.TnPMeasurement.PDFs, pdf)[i] = l.replace("[1.0]","[0.5,0.,1.]")

    setattr(process.TnPMeasurement.Efficiencies, options.idName, DataBinningSpecification)    
    setattr(getattr(process.TnPMeasurement.Efficiencies, options.idName) , "EfficiencyCategoryAndState", cms.vstring(options.idName, "pass"))
else:   
    setattr(process.TnPMeasurement.Efficiencies, "MCtruth_" + options.idName, McBinningSpecification)    
    setattr(getattr(process.TnPMeasurement.Efficiencies, "MCtruth_" + options.idName), "EfficiencyCategoryAndState", cms.vstring(options.idName, "pass"))

    for pdf in process.TnPMeasurement.PDFs.__dict__:
        param =  process.TnPMeasurement.PDFs.getParameter(pdf)
        if (type(param) is not cms.vstring):
            continue
        for i, l in enumerate(getattr(process.TnPMeasurement.PDFs, pdf)):
            if l.find("backgroundPass") != -1:
                getattr(process.TnPMeasurement.PDFs, pdf)[i] = "RooPolynomial::backgroundPass(mass, a[0.0])"
            if l.find("backgroundFail") != -1:
                getattr(process.TnPMeasurement.PDFs, pdf)[i] = "RooPolynomial::backgroundFail(mass, a[0.0])"

process.fit = cms.Path(
    process.TnPMeasurement  
    )


