{

	gSystem->AddIncludePath("-Iexternal");
	gSystem->SetBuildDir("tmpdir", kTRUE);
	//gROOT->LoadMacro("xAna.cc+");
	gROOT->ProcessLine(".L xAna.cc+");

	TString outpath = "mytry.root";



	const int nfiles = 4; //number of files

	TString inpath[nfiles] = { "/data3/ggNtuples/V08_00_10_00/job_DoubleMu_Run2016B_PRv2.root", "/data6/ggNtuples/V08_00_10_00/job_spring16_DYJetsToLL_m50_aMCatNLO_miniAOD.root", "/data6/ggNtuples/V08_00_10_00/job_spring16_WJetsToLNu_aMCatNLO.root", "/data6/ggNtuples/V08_00_10_00/job_spring16_TT_powheg_ext3.root"};

	// char* outfile[nfiles] = {"DYJets.root","data.root", "DYJets_mad.root"};
	char* outfile[nfiles] = { "data.root", "signal.root", "WgBkg.root", "TTBkg.root" };
	// char* type[nfiles] = {"signal","data", "signal"};
	char* type[nfiles] = { "data", "signal", "WgBkg", "TTBkg" };

	for (int i = 0; i < nfiles; i++){

		const char* inpaths[] = { inpath[i].Data() };

		cout << "RUNNIGN FILE " << inpath[i].Data() << " AND OUTPUT FILE IS " << outfile[i] << endl;

		int qcdchannel = 0; //for photons + jets
		const char* out = outfile[i];

		const char* ftype = type[i];
		xAna(inpaths, 1, out, ftype, 0, -1/*, 1, qcdchannel*/);
	}//for(int i=0; i<nfiles; i++)



}
