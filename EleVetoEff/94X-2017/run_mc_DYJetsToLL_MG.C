{
    gSystem->AddIncludePath("-Iexternal");
    gSystem->SetBuildDir("tmpdir", kTRUE);
    gROOT->ProcessLine(".L xAna.C++");

    gStyle->SetOptStat(0);

    string inpath[2] =
    {
        "/eos/cms/store/group/phys_smp/ggNtuples/13TeV/mc/V09_04_09_00/job_fall17_DYJetsToLL_m50_MG/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/crab_job_fall17_DYJetsToLL_m50_MG/181012_140347/0000/ggtree_mc_*.root",
        "/eos/cms/store/group/phys_smp/ggNtuples/13TeV/mc/V09_04_09_00/job_fall17_DYJetsToLL_m50_MG_ext1/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/crab_job_fall17_DYJetsToLL_m50_MG_ext1/181012_140403/0000/ggtree_mc_*.root",
    };

    string outpath[2] =
    {
        "minitree/minitree_DYJetsToLL_MadGraph_0.root",
        "minitree/minitree_DYJetsToLL_MadGraph_1.root",

    };

    //int Is_aMCatNLO[11] = {0,0,0,0,0,0,0,0,0,0,0};

    for(int i=0;i<2;i++)
    {
        xAna(inpath[i].c_str(), outpath[i].c_str(), 1, 14420*1000, false, 2017);
    }
}
