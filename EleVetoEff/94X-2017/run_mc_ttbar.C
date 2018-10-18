{
    gSystem->AddIncludePath("-Iexternal");
    gSystem->SetBuildDir("tmpdir", kTRUE);
    gROOT->ProcessLine(".L xAna.C++");

    gStyle->SetOptStat(0);

    string inpath[1] =
    {
        "/eos/cms/store/group/phys_smp/ggNtuples/13TeV/mc/V09_04_09_00/job_fall17_TTTo2L2Nu_powheg/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/crab_job_fall17_TTTo2L2Nu_powheg/180821_113923/0000/ggtree_mc_*.root"
    };

    string outpath[1] =
    {
        "minitree/minitree_TTTo2L2Nu_powheg.root"
    };

    //int Is_aMCatNLO[11] = {0,0,0,0,0,0,0,0,0,0,0};

    for(int i=0;i<1;i++)
    {
        xAna(inpath[i].c_str(), outpath[i].c_str(), 0, 72.1*1000, false, 2017);
    }
}
