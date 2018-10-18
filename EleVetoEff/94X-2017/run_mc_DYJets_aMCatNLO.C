{
    gSystem->AddIncludePath("-Iexternal");
    gSystem->SetBuildDir("tmpdir", kTRUE);
    gROOT->ProcessLine(".L xAna.C++");

    gStyle->SetOptStat(0);

    string inpath[2] =
    {
        "/data6/ggNtuples/V09_00_00_04/job_fall17_DYJetsToLL_m50_aMCatNLO_ext1/0000/ggtree_mc_*.root",
        "/data6/ggNtuples/V09_00_00_04/job_fall17_DYJetsToLL_m50_aMCatNLO_ext1/0001/ggtree_mc_*.root",
    };

    string outpath[2] =
    {
        "minitree/minitree_DYJetsToLL_aMCatNLO_0.root",
        "minitree/minitree_DYJetsToLL_aMCatNLO_1.root",

    };

    //int Is_aMCatNLO[11] = {0,0,0,0,0,0,0,0,0,0,0};

    for(int i=0;i<2;i++)
    {
        xAna(inpath[i].c_str(), outpath[i].c_str(), 1, 5943.2*1000, false, 2017);
    }
}
