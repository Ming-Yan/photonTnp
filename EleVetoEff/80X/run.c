void run(){

  gROOT->LoadMacro("xHistosCombine.C");

  TString fname[4] = { "Loose", "Medium", "Tight", "MVA" };
  TString region[2] = { "EB", "EE" };
  TString hname[5] = { "hMuug", "hMuu", "Ptg", "Etag", "phoMVA"/*, "MuugMuu"*/ };
  TString xname[5] = { "M_{#mu#mu#gamma}", "M_{#mu#mu}", "P_{T}^{#gamma}", "#eta^{#gamma}", "photon MVA"/*, "M_{#mu#mu#gamma}" */};
  Int_t legStyle[5] = { 0, 0, 0, 0, 0 };
  Int_t logx[5] = { 0, 0, 0, 0, 0 };
  Int_t logy[5] = { 0, 0, 1, 0, 0 };

  for (int i = 0; i < 4; i++){
    for (int j = 0; j < 2; j++){
      for (int k = 0; k < 5; k++){

	xHistosCombine(fname[i], region[j], hname[k], xname[k], legStyle[k], logy[k], logx[k]);
      }
    }
  }
}
