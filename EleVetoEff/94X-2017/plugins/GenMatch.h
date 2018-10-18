void GenMatchPID(TreeReader data, vector<int> RecoMu, vector<int> RecoPho, vector<int> &GenmatchMuIdx, vector<int> &GenmatchPhoIdx)
{
    float* muPt = data.GetPtrFloat("muPt");
    float* muEta = data.GetPtrFloat("muEta");
    float* muPhi = data.GetPtrFloat("muPhi");
    float* phoCalibEt = data.GetPtrFloat("phoCalibEt"); // calibrated photon pT
    float* phoEta     = data.GetPtrFloat("phoEta");
    float* phoPhi     = data.GetPtrFloat("phoPhi");
    int nMC         = data.GetInt("nMC"); // MC
    int* mcPID      = data.GetPtrInt("mcPID");
    int* mcMomPID      = data.GetPtrInt("mcMomPID");
    int* mcGMomPID      = data.GetPtrInt("mcGMomPID");
    float* mcPt     = data.GetPtrFloat("mcPt");
    float* mcEta    = data.GetPtrFloat("mcEta");
    float* mcPhi    = data.GetPtrFloat("mcPhi");
    float* mcVtx    = data.GetPtrFloat("mcVtx");
    float* mcVty    = data.GetPtrFloat("mcVty");
    float* mcVtz    = data.GetPtrFloat("mcVtz");

    // MC matching (to check the M_mmg resolution)
    GenmatchMuIdx.clear();
    GenmatchPhoIdx.clear();
    int temp_index=-1;
    float temp_ptratio=999.;
    for(int n=0; n<2; n++)
    {
        temp_ptratio=999.;
        temp_index=-1;
        for(int i = 0; i<nMC; i++)
        {
            if(deltaR(muEta[RecoMu[n]], muPhi[RecoMu[n]], mcEta[i], mcPhi[i]) > 0.1) continue;

            if(fabs((mcPt[i]/muPt[RecoMu[n]]) - 1.) < temp_ptratio)
            {
                temp_ptratio = fabs((mcPt[i]/muPt[RecoMu[n]]) - 1.);
                temp_index = i;
                continue;
            }
            else
            continue;
        }
        GenmatchMuIdx.push_back(temp_index);
    }
    cout << GenmatchMuIdx[0] << " " << GenmatchMuIdx[1] << endl;
    temp_ptratio=999.;
    temp_index=-1;
    for(int i = 0; i<nMC; i++)
    {
        if(deltaR(phoEta[RecoPho[0]], phoPhi[RecoPho[0]], mcEta[i], mcPhi[i]) > 0.1) continue;
        if(fabs((mcPt[i]/phoCalibEt[RecoPho[0]]) - 1.) < temp_ptratio)
        {
            temp_ptratio = fabs((mcPt[i]/phoCalibEt[RecoPho[0]]) - 1.);
            temp_index = i;
            continue;
        }
        else
        continue;
    }
    GenmatchPhoIdx.push_back(temp_index);
    cout << GenmatchPhoIdx[0] << endl; 
}

bool mcMatchMu(int i, TreeReader &data)
{ //match reco muon to MC
		bool isRecomu = false;

		float* muPt = data.GetPtrFloat("muPt");
		float* muEta = data.GetPtrFloat("muEta");
		float* muPhi = data.GetPtrFloat("muPhi");


		TLorentzVector *mu = new TLorentzVector();
		mu->SetPtEtaPhiM(muPt[i], muEta[i], muPhi[i], 105.7*0.001);


		Int_t nMC = data.GetInt("nMC");
		Int_t *mcPID = data.GetPtrInt("mcPID");
		Int_t *mcMomPID = data.GetPtrInt("mcMomPID");
		Int_t *mcGMomPID = data.GetPtrInt("mcGMomPID");
		float *mcMomMass = data.GetPtrFloat("mcMomMass");
		//Int_t *mcDecayType = data.GetPtrInt("mcDecayType");
		float *mcPt = data.GetPtrFloat("mcPt");
		float *mcEta = data.GetPtrFloat("mcEta");
		float *mcPhi = data.GetPtrFloat("mcPhi");
		float *mcMass = data.GetPtrFloat("mcMass");


		for (int imc = 0; imc < nMC; imc++){

			TLorentzVector *gen = new TLorentzVector();
			gen->SetPtEtaPhiM(mcPt[imc], mcEta[imc], mcPhi[imc], mcMass[imc]);

			///FSR muon only
			bool isgenMu = fabs(mcPID[imc]) == 13 && abs(mcMomPID[imc]) == 23 && gen->DeltaR(*mu) < 0.1;

			if (isgenMu) {
				isRecomu = true;
				break;
			}

		}//for(int imc=0; imc<nMC; imc++)

		return isRecomu;
}

bool mcMatchPho(int i, TreeReader &data)
{//photon matching
        bool isRecopho = false;

        float* phoPt = data.GetPtrFloat("phoEt");
        float* phoEta = data.GetPtrFloat("phoEta");
        float* phoPhi = data.GetPtrFloat("phoPhi");

        TLorentzVector *pho = new TLorentzVector();
        pho->SetPtEtaPhiM(phoPt[i], phoEta[i], phoPhi[i], 0.);


        Int_t nMC = data.GetInt("nMC");
        Int_t *mcPID = data.GetPtrInt("mcPID");
        Int_t *mcMomPID = data.GetPtrInt("mcMomPID");
        Int_t *mcGMomPID = data.GetPtrInt("mcGMomPID");
        float *mcMomMass = data.GetPtrFloat("mcMomMass");
        //Int_t *mcDecayType = data.GetPtrInt("mcDecayType");
        float *mcPt = data.GetPtrFloat("mcPt");
        float *mcEta = data.GetPtrFloat("mcEta");
        float *mcPhi = data.GetPtrFloat("mcPhi");
        float *mcMass = data.GetPtrFloat("mcMass");


        for (int imc = 0; imc<nMC; imc++){

            TLorentzVector *gen = new TLorentzVector();
            gen->SetPtEtaPhiM(mcPt[imc], mcEta[imc], mcPhi[imc], mcMass[imc]);

            ///FSR photon only
            bool isgenPho = mcPID[imc] == 22 && abs(mcMomPID[imc]) == 13 && abs(mcGMomPID[imc]) == 23 && gen->DeltaR(*pho) < 0.1;

            if (isgenPho) {
                isRecopho = true;
                break;
            }

        }//for(int imc=0; imc<nMC; imc++)

        return isRecopho;

}//photon matching
