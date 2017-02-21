if __name__ == '__main__':

# Usage : python crabConfig.py (to create jobs)
#         ./multicrab -c status -d <work area> (to check job status)

    from CRABAPI.RawCommand import crabCommand
    from httplib import HTTPException

    from CRABClient.UserUtilities import config
    config = config()
    
    from multiprocessing import Process

    # Common configuration

    config.General.workArea     = 'crab_projects_Winter17pho_redoFeb19'
    config.General.transferLogs = False
    config.JobType.pluginName   = 'Analysis' # PrivateMC
    config.JobType.sendExternalFolder     = True
    #config.JobType.psetName     = 'run_mc_76X_miniAOD.py'
    config.Data.inputDBS        = 'global'    
    #config.Data.lumiMask = 'Cert_190456-208686_8TeV_PromptReco_Collisions12_JSON.txt'
    config.Data.splitting       = 'LumiBased' # EventBased, FileBased, LumiBased (1 lumi ~= 300 events)
    config.Data.totalUnits      = -1
    config.Data.publication     = False
    #config.Site.whitelist       = ['T3_TW_NCU']
    config.Site.blacklist       = ['T3_TW_NCU']
    config.Site.blacklist       = ['T2_US_Vanderbilt']
    config.Site.blacklist       = ['T2_US_MIT']
    config.Site.blacklist       = ['T2_BE_IIHE']
    config.Site.storageSite     = 'T3_TW_NCU'

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException, hte:
            print hte.headers

    # dataset dependent configuratio

    config.General.requestName = 'job_tnp_summer16_Madgraph_v3'
    config.JobType.psetName    = 'makeTree.py'
    config.Data.unitsPerJob    = 80
    #config.Data.inputDataset   = '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14_ext1-v1/MINIAODSIM'
    config.Data.inputDataset   = '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/MINIAODSIM'
    config.Data.outLFNDirBase  = '/store/user/pwang/Winter17_GJCut/MG_Summer16'
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'job_tnp_summer16_aMCatNLO_v3'
    config.JobType.psetName    = 'makeTree.py'
    #config.JobType.sendExternalFolder     = True
    config.Data.unitsPerJob    = 80
    #config.Data.inputDataset   = '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring16MiniAODv2-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM'
    config.Data.inputDataset   = '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_HCALDebug_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'
    config.Data.outLFNDirBase  = '/store/user/pwang/Winter17_GJCut/aMC_Summer16'
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()


    config.General.requestName = 'job_tnp_SingleEle_2016RunB'
    config.JobType.psetName    = 'makeTree.py'
    config.JobType.pyCfgParams = ['isMC=False']
    config.Data.unitsPerJob    = 25
    config.Data.lumiMask       = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
    config.Data.inputDataset   = '/SingleElectron/Run2016B-23Sep2016-v3/MINIAOD'
    config.Data.outLFNDirBase  = '/store/user/pwang/Winter17_GJCut/2016_RunB'
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'job_tnp_SingleEle_2016RunC'
    config.JobType.psetName    = 'makeTree.py'
    config.JobType.pyCfgParams = ['isMC=False']
    config.Data.unitsPerJob    = 25
    config.Data.lumiMask       = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
    config.Data.inputDataset   = '/SingleElectron/Run2016C-23Sep2016-v1/MINIAOD'
    config.Data.outLFNDirBase  = '/store/user/pwang/Winter17_GJCut/2016_RunC'
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'job_tnp_SingleEle_2016RunD'
    config.JobType.psetName    = 'makeTree.py'
    config.JobType.pyCfgParams = ['isMC=False']
    config.Data.unitsPerJob    = 25
    config.Data.lumiMask       = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
    config.Data.inputDataset   = '/SingleElectron/Run2016D-23Sep2016-v1/MINIAOD'
    config.Data.outLFNDirBase  = '/store/user/pwang/Winter17_GJCut/2016_RunD'
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'job_tnp_SingleEle_2016RunE'
    config.JobType.psetName    = 'makeTree.py'
    config.JobType.pyCfgParams = ['isMC=False']
    config.Data.unitsPerJob    = 25
    config.Data.lumiMask       = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
    config.Data.inputDataset   = '/SingleElectron/Run2016E-23Sep2016-v1/MINIAOD'
    config.Data.outLFNDirBase  = '/store/user/pwang/Winter17_GJCut/2016_RunE'
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'job_tnp_SingleEle_2016RunF'
    config.JobType.psetName    = 'makeTree.py'
    config.JobType.pyCfgParams = ['isMC=False']
    config.Data.unitsPerJob    = 25
    config.Data.lumiMask       = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
    config.Data.inputDataset   = '/SingleElectron/Run2016F-23Sep2016-v1/MINIAOD'
    config.Data.outLFNDirBase  = '/store/user/pwang/Winter17_GJCut/2016_RunF'
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'job_tnp_SingleEle_2016RunG'
    config.JobType.psetName    = 'makeTree.py'
    config.JobType.pyCfgParams = ['isMC=False']
    config.Data.unitsPerJob    = 25
    config.Data.lumiMask       = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
    config.Data.inputDataset   = '/SingleElectron/Run2016G-23Sep2016-v1/MINIAOD'
    config.Data.outLFNDirBase  = '/store/user/pwang/Winter17_GJCut/2016_RunG'
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'job_tnp_SingleEle_2016RunH'
    config.JobType.psetName    = 'makeTree.py'
    config.JobType.pyCfgParams = ['isMC=False']
    config.Data.unitsPerJob    = 25
    config.Data.lumiMask       = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/Final/Cert_271036-284044_13TeV_PromptReco_Collisions16_JSON.txt'
    config.Data.inputDataset   = '/SingleElectron/Run2016H-PromptReco-v3/MINIAOD'
    config.Data.outLFNDirBase  = '/store/user/pwang/Winter17_GJCut/2016_RunH'
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()


    config.General.requestName = 'job_tnp_SingleEle_2016RunB_v2'
    config.JobType.psetName    = 'makeTree.py'
    config.JobType.pyCfgParams = ['isMC=False']
    config.Data.unitsPerJob    = 25
    config.Data.lumiMask       = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
    config.Data.inputDataset   = '/SingleElectron/Run2016B-23Sep2016-v2/MINIAOD'
    config.Data.outLFNDirBase  = '/store/user/pwang/Winter17_GJCut/2016_RunB_v2'
    #p = Process(target=submit, args=(config,))
    #p.start()
    #p.join()


    config.General.requestName = 'job_tnp_SingleEle_2016RunH_v1'
    config.JobType.psetName    = 'makeTree.py'
    config.JobType.pyCfgParams = ['isMC=False']
    config.Data.unitsPerJob    = 25
    config.Data.lumiMask       = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/Final/Cert_271036-284044_13TeV_PromptReco_Collisions16_JSON.txt'
    config.Data.inputDataset   = '/SingleElectron/Run2016H-PromptReco-v1/MINIAOD'
    config.Data.outLFNDirBase  = '/store/user/pwang/Winter17_GJCut/2016_RunH_v1'
    #p = Process(target=submit, args=(config,))
    #p.start()
    #p.join()

    config.General.requestName = 'job_tnp_SingleEle_2016RunH_v2'
    config.JobType.psetName    = 'makeTree.py'
    config.JobType.pyCfgParams = ['isMC=False']
    config.Data.unitsPerJob    = 25
    config.Data.lumiMask       = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/Final/Cert_271036-284044_13TeV_PromptReco_Collisions16_JSON.txt'
    config.Data.inputDataset   = '/SingleElectron/Run2016H-PromptReco-v2/MINIAOD'
    config.Data.outLFNDirBase  = '/store/user/pwang/Winter17_GJCut/2016_RunH_v2'
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()
