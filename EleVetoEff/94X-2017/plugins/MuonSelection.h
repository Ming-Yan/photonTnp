bool select_muons(TreeReader &data, int i)
{
	Int_t  run = data.GetInt("run");
	Int_t  nMu = data.GetInt("nMu");
	float* muPt = data.GetPtrFloat("muPt");
	float* muEta = data.GetPtrFloat("muEta");
	float* muPhi = data.GetPtrFloat("muPhi");
	Int_t* muIDbit = data.GetPtrInt("muIDbit");

	bool IsGoodMuon = false;
	if(muPt[i] > 10. && fabs(muEta[i]) < 2.4 && (((muIDbit[i] >> 2) & 1) == 1) ) IsGoodMuon = true;
	return IsGoodMuon;
}
