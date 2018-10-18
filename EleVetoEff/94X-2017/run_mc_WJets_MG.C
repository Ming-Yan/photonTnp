{
    gSystem->AddIncludePath("-Iexternal");
    gSystem->SetBuildDir("tmpdir", kTRUE);
    gROOT->ProcessLine(".L xAna.C++");

    gStyle->SetOptStat(0);

    string inpath[16] =
    {
        "/eos/cms/store/group/phys_smp/ggNtuples/13TeV/mc/V09_04_09_00/job_fall17_WJetsToLNu_MG/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/crab_job_fall17_WJetsToLNu_MG/181012_135828/0000/ggtree_mc_*.root",
        "/eos/cms/store/group/phys_smp/ggNtuples/13TeV/mc/V09_04_09_00/job_fall17_WJetsToLNu_MG_ext1/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/crab_job_fall17_WJetsToLNu_MG_ext1/181012_135845/0000/ggtree_mc_*.root",
        // HT samples
        "/eos/cms/store/group/phys_smp/ggNtuples/13TeV/mc/V09_04_09_00/job_fall17_WJetsToLNu_MG_HT400to600/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/crab_job_fall17_WJetsToLNu_MG_HT400to600/181015_094615/0000/ggtree_mc_*.root",
        "/eos/cms/store/group/phys_smp/ggNtuples/13TeV/mc/V09_04_09_00/job_fall17_WJetsToLNu_MG_HT400to600/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/crab_job_fall17_WJetsToLNu_MG_HT400to600/181015_094615/0001/ggtree_mc_*.root",
        "/eos/cms/store/group/phys_smp/ggNtuples/13TeV/mc/V09_04_09_00/job_fall17_WJetsToLNu_MG_HT800to1200/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/crab_job_fall17_WJetsToLNu_MG_HT800to1200/181015_094650/0000/ggtree_mc_*.root",
        "/eos/cms/store/group/phys_smp/ggNtuples/13TeV/mc/V09_04_09_00/job_fall17_WJetsToLNu_MG_HT800to1200/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/crab_job_fall17_WJetsToLNu_MG_HT800to1200/181015_094650/0001/ggtree_mc_*.root",
        "/eos/cms/store/group/phys_smp/ggNtuples/13TeV/mc/V09_04_09_00/job_fall17_WJetsToLNu_MG_HT600to800/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/crab_job_fall17_WJetsToLNu_MG_HT600to800/181015_094632/0000/ggtree_mc_*.root",
        "/eos/cms/store/group/phys_smp/ggNtuples/13TeV/mc/V09_04_09_00/job_fall17_WJetsToLNu_MG_HT600to800/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/crab_job_fall17_WJetsToLNu_MG_HT600to800/181015_094632/0001/ggtree_mc_*.root",
        "/eos/cms/store/group/phys_smp/ggNtuples/13TeV/mc/V09_04_09_00/job_fall17_WJetsToLNu_MG_HT100to200/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/crab_job_fall17_WJetsToLNu_MG_HT100to200/181015_094540/0000/ggtree_mc_*.root",
        "/eos/cms/store/group/phys_smp/ggNtuples/13TeV/mc/V09_04_09_00/job_fall17_WJetsToLNu_MG_HT100to200/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/crab_job_fall17_WJetsToLNu_MG_HT100to200/181015_094540/0001/ggtree_mc_*.root",
        "/eos/cms/store/group/phys_smp/ggNtuples/13TeV/mc/V09_04_09_00/job_fall17_WJetsToLNu_MG_HT100to200/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/crab_job_fall17_WJetsToLNu_MG_HT100to200/181015_094540/0002/ggtree_mc_*.root",
        "/eos/cms/store/group/phys_smp/ggNtuples/13TeV/mc/V09_04_09_00/job_fall17_WJetsToLNu_MG_HT2500toInf/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/crab_job_fall17_WJetsToLNu_MG_HT2500toInf/181015_094722/0000/ggtree_mc_*.root",
        "/eos/cms/store/group/phys_smp/ggNtuples/13TeV/mc/V09_04_09_00/job_fall17_WJetsToLNu_MG_HT2500toInf/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/crab_job_fall17_WJetsToLNu_MG_HT2500toInf/181015_094722/0001/ggtree_mc_*.root",
        "/eos/cms/store/group/phys_smp/ggNtuples/13TeV/mc/V09_04_09_00/job_fall17_WJetsToLNu_MG_HT1200to2500/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/crab_job_fall17_WJetsToLNu_MG_HT1200to2500/181015_094706/0000/ggtree_mc_*.root",
        "/eos/cms/store/group/phys_smp/ggNtuples/13TeV/mc/V09_04_09_00/job_fall17_WJetsToLNu_MG_HT1200to2500/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/crab_job_fall17_WJetsToLNu_MG_HT1200to2500/181015_094706/0001/ggtree_mc_*.root",
        "/eos/cms/store/group/phys_smp/ggNtuples/13TeV/mc/V09_04_09_00/job_fall17_WJetsToLNu_MG_HT200to400/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/crab_job_fall17_WJetsToLNu_MG_HT200to400/181015_094559/0000/ggtree_mc_*.root"
    };

    string outpath[16] =
    {
        "minitree/minitree_Wjets_aMCatNLO_0.root",
        "minitree/minitree_Wjets_aMCatNLO_1.root",
        "minitree/minitree_Wjets_HT400to600_MadGraph_0.root",
        "minitree/minitree_Wjets_HT400to600_MadGraph_1.root",
        "minitree/minitree_Wjets_HT800to1200_MadGraph_0.root",
        "minitree/minitree_Wjets_HT800to1200_MadGraph_1.root",
        "minitree/minitree_Wjets_HT600to800_MadGraph_0.root",
        "minitree/minitree_Wjets_HT600to800_MadGraph_1.root",
        "minitree/minitree_Wjets_HT100to200_MadGraph_0.root",
        "minitree/minitree_Wjets_HT100to200_MadGraph_1.root",
        "minitree/minitree_Wjets_HT100to200_MadGraph_2.root",
        "minitree/minitree_Wjets_HT2500toInf_MadGraph_0.root",
        "minitree/minitree_Wjets_HT2500toInf_MadGraph_1.root",
        "minitree/minitree_Wjets_HT1200to2500_MadGraph_0.root",
        "minitree/minitree_Wjets_HT1200to2500_MadGraph_1.root",
        "minitree/minitree_Wjets_HT200to400_MadGraph_0.root"
    };

    //int Is_aMCatNLO[11] = {0,0,0,0,0,0,0,0,0,0,0};

    float XS[16] = {56000., 56000., 359.7, 359.7, 359.7, 359.7, 12.98, 12.98, 1379., 1379., 1379., 359.7, 359.7, 10.35, 10.35, 402.5};
    for(int i=2;i<16;i++)
    {
        xAna(inpath[i].c_str(), outpath[i].c_str(), 1, XS[i]*1000., false, 2017);
    }
}
