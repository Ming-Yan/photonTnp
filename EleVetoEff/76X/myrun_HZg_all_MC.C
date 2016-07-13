{

	gSystem->AddIncludePath("-Iexternal");
	gSystem->SetBuildDir("tmpdir", kTRUE);
	gROOT->ProcessLine(".L xAna.cc+");

	TString outpath = "mytry.root";



	const int nfiles = 5; //number of files

	TString inpath[nfiles] = { "/data3/ggNtuples/V07_06_03_00/job_DoubleMu_Run2015C_Dec16_miniAOD.root", "/data3/ggNtuples/V07_06_03_00/job_DoubleMu_Run2015D_Dec16_miniAOD.root", "/data6/ggNtuples/V07_06_03_00/job_fall15_DYJetsToLL_m50_miniAOD.root", "/data6/ggNtuples/V07_06_03_00/job_fall15_WJetsToLNu_aMCatNLO_miniAOD.root", "/data6/ggNtuples/V07_06_03_00/job_fall15_TT_powheg_miniAOD.root" };

	char* outfile[nfiles] = { "dataC.root", "dataD.root", "signal.root", "WgBkg.root", "TTBkg.root"};
	char* type[nfiles] = { "data", "data", "signal", "WgBkg", "TTBkg" };

	for (int i = 0; i < nfiles; i++){

		const char* inpaths[] = { inpath[i].Data() };

		cout << "RUNNING FILE " << inpath[i].Data() << " AND OUTPUT FILE IS " << outfile[i] << endl;

		int qcdchannel = 0; //for photons + jets
		const char* out = outfile[i];

		const char* ftype = type[i];
		xAna(inpaths, 1, out, ftype, 0, -1);
	}//for(int i=0; i<nfiles; i++)



}
