{
    gSystem->AddIncludePath("-Iexternal");
    gSystem->SetBuildDir("tmpdir", kTRUE);
    gROOT->ProcessLine(".L xAna.C++");

    gStyle->SetOptStat(0);

    string inpath[11] =
    {
        // RunB
        "/data1/ggNtuples/V09_00_00_04/job_DoubleMu_Run2017B_MarReminiAOD/DoubleMuon/crab_job_DoubleMu_Run2017B_MarReminiAOD/180817_210042/0000/ggtree_data_*.root",
        // RunC
        "/data1/ggNtuples/V09_00_00_04/job_DoubleMu_Run2017C_MarReminiAOD/DoubleMuon/crab_job_DoubleMu_Run2017C_MarReminiAOD/180817_210350/0000/ggtree_data_*.root",
        "/data1/ggNtuples/V09_00_00_04/job_DoubleMu_Run2017C_MarReminiAOD/DoubleMuon/crab_job_DoubleMu_Run2017C_MarReminiAOD/180817_210350/0001/ggtree_data_*.root",
        "/data1/ggNtuples/V09_00_00_04/job_DoubleMu_Run2017C_MarReminiAOD/DoubleMuon/crab_job_DoubleMu_Run2017C_MarReminiAOD/180817_210350/0002/ggtree_data_*.root",
        // RunD
        "/data1/ggNtuples/V09_00_00_04/job_DoubleMu_Run2017D_MarReminiAOD/DoubleMuon/crab_job_DoubleMu_Run2017D_MarReminiAOD/180817_210444/0000/ggtree_data_*.root",
        "/data1/ggNtuples/V09_00_00_04/job_DoubleMu_Run2017D_MarReminiAOD/DoubleMuon/crab_job_DoubleMu_Run2017D_MarReminiAOD/180817_210444/0001/ggtree_data_*.root",
        // RunE
        "/data1/ggNtuples/V09_00_00_04/job_DoubleMu_Run2017E_MarReminiAOD/DoubleMuon/crab_job_DoubleMu_Run2017E_MarReminiAOD/180817_210540/0000/ggtree_data_*.root",
        "/data1/ggNtuples/V09_00_00_04/job_DoubleMu_Run2017E_MarReminiAOD/DoubleMuon/crab_job_DoubleMu_Run2017E_MarReminiAOD/180817_210540/0001/ggtree_data_*.root",
        // RunF
        "/data1/ggNtuples/V09_00_00_04/job_DoubleMu_Run2017F_MarReminiAOD/DoubleMuon/crab_job_DoubleMu_Run2017F_MarReminiAOD/180817_210629/0000/ggtree_data_*.root",
        "/data1/ggNtuples/V09_00_00_04/job_DoubleMu_Run2017F_MarReminiAOD/DoubleMuon/crab_job_DoubleMu_Run2017F_MarReminiAOD/180817_210629/0001/ggtree_data_*.root",
        "/data1/ggNtuples/V09_00_00_04/job_DoubleMu_Run2017F_MarReminiAOD/DoubleMuon/crab_job_DoubleMu_Run2017F_MarReminiAOD/180817_210629/0002/ggtree_data_*.root"

    };

    string outpath[11] =
    {
        "minitree/minitree_DoubleMu_RunB.root",
        "minitree/minitree_DoubleMu_RunC_0.root",
        "minitree/minitree_DoubleMu_RunC_1.root",
        "minitree/minitree_DoubleMu_RunC_2.root",
        "minitree/minitree_DoubleMu_RunD_0.root",
        "minitree/minitree_DoubleMu_RunD_1.root",
        "minitree/minitree_DoubleMu_RunE_0.root",
        "minitree/minitree_DoubleMu_RunE_1.root",
        "minitree/minitree_DoubleMu_RunF_0.root",
        "minitree/minitree_DoubleMu_RunF_1.root",
        "minitree/minitree_DoubleMu_RunF_2.root",
    };

    //int Is_aMCatNLO[11] = {0,0,0,0,0,0,0,0,0,0,0};

    for(int i=0;i<11;i++)
    {
        xAna(inpath[i].c_str(), outpath[i].c_str(), 0, 1.0, false, 2017);
    }
}
