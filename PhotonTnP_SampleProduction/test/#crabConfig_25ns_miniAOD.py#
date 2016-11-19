if __name__ == '__main__':

# Usage : python crabConfig.py (to create jobs)
#         ./multicrab -c status -d <work area> (to check job status)

    from CRABAPI.RawCommand import crabCommand
    from httplib import HTTPException

    from CRABClient.UserUtilities import config
    config = config()
    
    from multiprocessing import Process

    # Common configuration

    config.General.workArea     = 'crab_projects_2016pho'
    config.General.transferLogs = False
    config.JobType.pluginName   = 'Analysis' # PrivateMC
    #config.JobType.psetName     = 'run_mc_76X_miniAOD.py'
    config.Data.inputDBS        = 'global'    
    #config.Data.lumiMask = 'Cert_190456-208686_8TeV_PromptReco_Collisions12_JSON.txt'
    config.Data.splitting       = 'LumiBased' # EventBased, FileBased, LumiBased (1 lumi ~= 300 events)
    config.Data.totalUnits      = -1
    config.Data.publication     = False
    #config.Site.whitelist       = ['T3_TW_NCU']
    config.Site.blacklist       = ['T3_TW_NCU']
    config.Site.storageSite     = 'T3_TW_NCU'

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException, hte:
            print hte.headers

    # dataset dependent configuration

    config.General.requestName = 'job_tnp_spring16_Madgraph'
    config.JobType.psetName    = 'makeTree.py'
    config.Data.unitsPerJob    = 150
    config.Data.inputDataset   = '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM'
    config.Data.outLFNDirBase  = '/store/user/pwang/08_16Test/MG'
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()

    config.General.requestName = 'job_tnp_spring16_aMCatNLO'
    config.JobType.psetName    = 'makeTree.py'
    config.Data.unitsPerJob    = 150
    config.Data.inputDataset   = '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM'
    config.Data.outLFNDirBase  = '/store/user/pwang/08_16Test/aMC'
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()



    config.Data.outLFNDirBase = '/store/user/pwang/08_16Test/2016_RunB'
    config.Data.splitting     = 'LumiBased'
    config.Data.lumiMask      = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/Cert_271036-275783_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt'
    config.Data.unitsPerJob   = 100
    config.JobType.pyCfgParams  = ['isMC=False',doEleTree,doPhoTree,doHLTTree]

    config.General.requestName  = '2016_RunB'
    config.Data.inputDataset    = '/SingleElectron/Run2016B-PromptReco-v2/MINIAOD'
    submit(config)


    #config.General.requestName = 'job_tnp_SingleEle_2016C'
    #config.JobType.psetName    = 'makeTreePhotons_Data.py'
    #config.Data.lumiMask       = 'Cert_13TeV_16Dec2015ReReco_Collisions15_25ns_JSON_Silver_v2.txt'
    #config.Data.unitsPerJob    = 150
    #config.Data.inputDataset   = '/SingleElectron/Run2015C_25ns-16Dec2015-v1/MINIAOD'
    #config.Data.outLFNDirBase  = '/store/user/pwang/2015C'
    #p = Process(target=submit, args=(config,))
    #p.start()
    #p.join()

    #config.General.requestName = 'job_tnp_SingleEle_2015D'
    #config.JobType.psetName    = 'makeTreePhotons_Data.py'
    #config.Data.lumiMask       = 'Cert_13TeV_16Dec2015ReReco_Collisions15_25ns_JSON_Silver_v2.txt'
    #config.Data.unitsPerJob    = 150
    #config.Data.inputDataset   = '/SingleElectron/Run2015D-16Dec2015-v1/MINIAOD'
    #config.Data.outLFNDirBase  = '/store/user/pwang/2015D'
    #p = Process(target=submit, args=(config,))
    #p.start()
    #p.join()

