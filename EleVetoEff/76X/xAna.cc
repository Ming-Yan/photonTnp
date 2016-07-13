#include "untuplizer.h"
#include <TLorentzVector.h>
#include <vector>
#include "puweicalc.h"
#include "Utilities.h"
#include <TMVA/Reader.h>
#include <TH2F.h>
#include <TH1F.h>

using namespace std;

//float PhotonIDCutBasedRunII(int iWP, TreeReader &data, int i);
//float PhotonIDMVA(TreeReader &data, int i);
bool select_muons(TreeReader &data, int i);
bool mcMatchMu(int i, TreeReader &data);
bool mcMatchPho(int i, TreeReader &data);

void xAna(const char** input, int npaths, const char* output = "preminitree.root",
	const char* type = "signal", Long64_t ev1 = 0, Long64_t ev2 = -1){

	int count = 0;
	Double_t wCounter = 0;

	float L = (17731437.060 + 2672070967.096) / (1000. * 1000. * 1000.);
	float mcwei = 1.;

	TString stype = type;

	if (stype == "signal") mcwei = (6025.2 * 1000.)*L / 19259725.;
	if (stype == "WgBkg") mcwei = (60290 * 1000.)*L / 16521036.;
	if (stype == "TTBkg") mcwei = (730 * 1000.)*L / 97994442.;
	if (stype == "signal50120") mcwei = (1975 * 1000.)*L / 2972000.;
	if (stype == "signal120200") mcwei = (19.32 * 1000.)*L / 100000.;

	map<string, TH1F*> hist;
	map<string, TH2F*> hist2;

	hist["Muu"] = new TH1F("Muu", "M_{#mu#mu}", 35, 20, 90);
	hist["Muug"] = new TH1F("Muug", "M_{#mu#mu#gamma}", 40, 70, 110);
	hist["Ptg"] = new TH1F("Ptg", "P_{T}^{#gamma}", 20, 0, 100);
	hist["Etag"] = new TH1F("Etag", "#eta^{#gamma}", 20, -2.5, 2.5);
	hist["phoMVAEE"] = new TH1F("phoMVAEE", "Photon ID MVA EE", 10, -1, 1);
	hist["phoMVAEB"] = new TH1F("phoMVAEB", "Photon ID MVA EB", 10, -1, 1);
	//hist["nVtx_norew"] = new TH1F("nVtx_norew", "Number of Vertices without reweighting", 50, 0, 50);
	//hist["nVtx"] = new TH1F("nVtx", "Number of Vertices", 50, 0, 50); //use puwei_
	hist2["MuugMuu"] = new TH2F("MuugMuu", "M_{#mu#mu#gamma} Vs. M_{#mu#mu}", 100, 70, 140, 100, 70, 100);
	//hist2["EffPt"] = new TH2F("EffPt", "Efficiency Vs. P_{T}^{#gamma}", 100, 0, 100, 100, 0, 5);
	//hist2["EffEta"] = new TH2F("EffEta", "Efficiency Vs. #eta^{#gamma}", 100, 0, 100, 100, 0, 5);

	TreeReader data(input, npaths);
	//TreeReader data(input);

	TFile *fout_ = new TFile(output, "recreate");

	TLorentzVector selLep[2], selPho;

	TTree *outtree_ = new TTree("t", "mini tree");

	Int_t run;

	//TREE VARIABLES
	int EleVeto_, HasPix_;
	int looseID_, medID_, tightID_, bMVA_, presel_;
	float MVA_, SCEta_;
	float genWeight_, mcwei_, Pt_, Eta_, Mass_, R9_;
	float Muu_;
	int run_;
	//ADDED
	int nVtx_norew_;

	//weights
	Float_t puwei_ = 1., puweiup_ = 1., puweidown_ = 1., pu71_ = 1.;

	mcwei_ = mcwei;

	outtree_->Branch("puwei", &puwei_, "puwei/F");

	outtree_->Branch("puweidown", &puweidown_, "puweidown/F");
	outtree_->Branch("puweiup", &puweiup_, "puweiup/F");
	outtree_->Branch("pu71", &pu71_, "pu71/F");

	outtree_->Branch("genWeight", &genWeight_, "genWeight/F");
	outtree_->Branch("Pt", &Pt_, "Pt/F");
	outtree_->Branch("Eta", &Eta_, "Eta/F");
	outtree_->Branch("EleVeto", &EleVeto_, "EleVeto/I"); //1 means pass
	outtree_->Branch("HasPix", &HasPix_, "HasPix/I"); //1 means fail
	outtree_->Branch("Mass", &Mass_, "Mass/F");
	outtree_->Branch("Muu", &Muu_, "Muu/F");
	outtree_->Branch("R9", &R9_, "R9/F");
	outtree_->Branch("SCEta", &SCEta_, "SCEta/F");

	outtree_->Branch("looseID", &looseID_, "looseID/I");
	outtree_->Branch("medID", &medID_, "medID/I");
	outtree_->Branch("tightID", &tightID_, "tightID/I");
	outtree_->Branch("MVA", &MVA_, "MVA/F");
	outtree_->Branch("bMVA", &bMVA_, "bMVA/I");
	outtree_->Branch("presel", &presel_, "presel/I");//photon preselection for plots
	outtree_->Branch("run", &run_, "run/I");
	outtree_->Branch("mcwei", &mcwei_, "mcwei/F");
	//ADDED
	outtree_->Branch("nVtx_norew", &nVtx_norew_, "nVtx_norew/I");

	double nFSR = 0;
	double ngenFSR = 0;

	double nFSRerr = 0;

	// pileup reweighting for MC

	PUWeightCalculator puCalc;
	PUWeightCalculator puCalc_up;
	PUWeightCalculator puCalc_down;
	PUWeightCalculator puCalc_71;

	if (data.HasMC()) {//initialize using reference files
		puCalc.Init("PU_histo_13TeV_SilverJSON_69000nb.root");
		puCalc_71.Init("PU_histo_13TeV_SilverJSON_71000nb.root");
		puCalc_up.Init("PU_histo_13TeV_SilverJSON_74550nb.root");
		puCalc_down.Init("PU_histo_13TeV_SilverJSON_67450nb.root");
	}

	// update upper boundary of the region of events to process, if necessary
	if (ev2 < 0) ev2 = data.GetEntriesFast(); //set deafult value of ev2; if not changed, run on all events; if changed, run up to ev2) events
	if (ev2 > data.GetEntriesFast()) ev2 = data.GetEntriesFast();

	cout << "Nevents : " << ev2 << endl;

	//EVENT LOOP
	for (Long64_t ev = ev1; ev < ev2; ev++) { //ev1 = 0, ev2 = -1 by deafult; ev1 -> lower limit; ev2 -> Nevents
		if ((ev - ev1) % 100000 == 0){
			fprintf(stderr, "processing event %lli of %lli\n", ev + 1, data.GetEntriesFast());
			//cout.precision(17);
			//cout << wCounter << endl;
		}

		data.GetEntry(ev);

		bool HLTgam = true;
		if (!data.HasMC()) { //TRIGGER
			ULong64_t hlt = data.GetLong64("HLTEleMuX"); //HLT for 25 ns
			HLTgam = hlt >> 21 & 1; //HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v - 25 ns
		}

		nVtx_norew_ = data.GetInt("nVtx");

		//PU Reweighting
		if (data.HasMC()) {

			run = data.GetInt("run");
			float* puTrue = data.GetPtrFloat("puTrue");
			puwei_ = (float)puCalc.GetWeight(run, puTrue[1]);
			pu71_ = (float)puCalc_71.GetWeight(run, puTrue[1]);// in-time PU
			puweiup_ = (float)puCalc_up.GetWeight(run, puTrue[1]); // in-time PU
			puweidown_ = (float)puCalc_down.GetWeight(run, puTrue[1]); // in-time PU
		}

		genWeight_ = 1.; //for data
		if (data.HasMC()) genWeight_ = data.GetFloat("genWeight"); //genWeight for MC

		double weight = 1.;
		if (data.HasMC()) weight = genWeight_;

		weight = (weight > 0) ? 1. : -1.;
		//cout << weight << " " << pu71_ << endl;
		wCounter += weight;
		weight = weight*pu71_;//puwei_ for 69mb; pu71_ for 71mb

		if (!HLTgam) continue; //TRIGGER

		Int_t  nPho = data.GetInt("nPho");

		//Photon SC branches
		float* phoSCEta = data.GetPtrFloat("phoSCEta");
	//	float* scPhi = data.GetPtrFloat("phoSCPhi");
	//	float* scEn = data.GetPtrFloat("phoSCE");
	//	float* scRawEn = data.GetPtrFloat("phoSCRawE");
	//	float* scEtaw = data.GetPtrFloat("phoSCEtaWidth");
	//	float* scPhiw = data.GetPtrFloat("phoSCPhiWidth");
	//	float* scBrem = data.GetPtrFloat("phoSCBrem");
		//Preshower
	//	float* esEn = data.GetPtrFloat("phoESEn");
	//	float* phoESEffSigmaRR_x = data.GetPtrFloat("phoESEffSigmaRR");
		//Now photon variables
		Int_t* eleVeto = data.GetPtrInt("phoEleVeto");

		Int_t* pixSeed = data.GetPtrInt("phohasPixelSeed");

		float* phoPt = data.GetPtrFloat("phoCalibEt");
		float* phoEta = data.GetPtrFloat("phoEta");
		float* phoPhi = data.GetPtrFloat("phoPhi");
		float* R9 = data.GetPtrFloat("phoR9");
		float* phoHoverE = data.GetPtrFloat("phoHoverE");
		Float_t* phoIDMVA = data.GetPtrFloat("phoIDMVA");

		float* sie_2012 = data.GetPtrFloat("phoSigmaIEtaIEtaFull5x5");
	//	float* siphi_2012 = data.GetPtrFloat("phoSigmaIPhiIPhiFull5x5");
	//	float* sietaiphi_2012 = data.GetPtrFloat("phoSigmaIEtaIPhiFull5x5");

	//	float* sie = data.GetPtrFloat("phoSigmaIEtaIEta");
	//	float* siphi = data.GetPtrFloat("phoSigmaIPhiIPhi");
	//	float* sietaiphi = data.GetPtrFloat("phoSigmaIEtaIPhiFull5x5");

	//	float* phoE1x3_2012 = data.GetPtrFloat("phoE1x3Full5x5");
	//	float* phoE2x2_2012 = data.GetPtrFloat("phoE2x2Full5x5");
	//	float* phoE5x5_2012 = data.GetPtrFloat("phoE5x5Full5x5");
	//	float* phoE2x5Max_2012 = data.GetPtrFloat("phoE2x5MaxFull5x5");
	//	float* phoE1x3 = data.GetPtrFloat("phoE1x3");
	//	float* phoE2x2 = data.GetPtrFloat("phoE2x2");
	//	float* phoE5x5 = data.GetPtrFloat("phoE5x5");
	//	float* phoE2x5Max = data.GetPtrFloat("phoE2x5Max");

		float  rho2012 = data.GetFloat("rho");
		float* phoPFPhoIso = data.GetPtrFloat("phoPFPhoIso");
		float* phoPFChIso = data.GetPtrFloat("phoPFChIso");
		float* phoPFChWorstIso = data.GetPtrFloat("phoPFChWorstIso");
	//	float* phoPFNeuIso = data.GetPtrFloat("phoPFNeuIso");
	//	float* ecalIso = data.GetPtrFloat("phoEcalRecHitSumEtConeDR03");
	//	float* hcalIso = data.GetPtrFloat("phohcalTowerSumEtConeDR03");

	//	float* hcalIso1 = data.GetPtrFloat("phohcalDepth1TowerSumEtConeDR03");
	//	float* hcalIso2 = data.GetPtrFloat("phohcalDepth2TowerSumEtConeDR03");
	//	float* trkIso = data.GetPtrFloat("photrkSumPtHollowConeDR03");

		////Muon branches
		// load necessary tree branches
		Int_t  nMu = data.GetInt("nMu");
		float* muPt = data.GetPtrFloat("muPt");
		float* muEta = data.GetPtrFloat("muEta");
	//	Int_t* muType = data.GetPtrInt("muType");
	//	float* muChi2NDF = data.GetPtrFloat("muChi2NDF");
	//	Int_t* muStations = data.GetPtrInt("muStations");
	//	float* muD0 = data.GetPtrFloat("muD0");
	//	float* muDz = data.GetPtrFloat("muDz");

	//	Int_t* muNumberOfValidMuonHits = data.GetPtrInt("muMuonHits");
	//	Int_t* muNumberOfValidPixelHits = data.GetPtrInt("muPixelHits");
	//	Int_t* muNumberOfValidTrkLayers = data.GetPtrInt("muTrkLayers");

	//	float* muPFIsoR04_CH = data.GetPtrFloat("muPFChIso");
	//	float* muPFIsoR04_NH = data.GetPtrFloat("muPFNeuIso");
	//	float* muPFIsoR04_Pho = data.GetPtrFloat("muPFPhoIso");
	//	float* muPFIsoR04_PU = data.GetPtrFloat("muPFPUIso");

		// for the energy scale correction
	//	Int_t  run = data.GetInt("run");
		float* muPhi = data.GetPtrFloat("muPhi");
	//	Int_t* muCharge = data.GetPtrInt("muCharge");

	//	float* muInnerPt = data.GetPtrFloat("muBestTrkPt");
	//	float* muInnerPtErr = data.GetPtrFloat("muBestTrkPtError");


		Short_t* phoid = data.GetPtrShort("phoIDbit");

		vector<int> iSelmu; //index of selected mu
		int nSelmu = 0; //number of selected mu

		/// Select 2 good muons 
		for (int imu = 0; imu<nMu; imu++){

			if (muPt[imu] < 10) continue;

			bool id = select_muons(data, imu);
			if (!id) continue;

			iSelmu.push_back(imu);
			nSelmu++;

		}
		if (nSelmu < 2) continue;

		int ileadmu = iSelmu[0];
		int itrailmu = iSelmu[1];

		/*if (muPt[ileadmu] <  muPt[itrailmu]){ 
			cout << "WARNING!!!! Muons not pt ordered" << endl;
		}*/

		TLorentzVector mu1, mu2;

		mu1.SetPtEtaPhiM(muPt[ileadmu], muEta[ileadmu], muPhi[ileadmu], 105.7*0.001);
		mu2.SetPtEtaPhiM(muPt[itrailmu], muEta[itrailmu], muPhi[itrailmu], 105.7*0.001);

		int iSelpho[100]; //select 100 photons
		int nSelpho = 0; //number of photons

		for (Int_t i = 0; i < nPho; i++) {

			float absEta = fabs(phoSCEta[i]);

			if (phoPt[i] < 10) continue; //phopt cut at 10; move to 15?

			if ((absEta > 1.4442) && (absEta < 1.566)) continue; //gap region

			//bool phoID = phoid[i]>>0&1;
			//if(!phoID) continue;

			if (absEta > 2.5) continue;

			//photon preselection
			/*if (phoHoverE[i] > 0.05) continue;

			double cut_sie = 0.011;
			if (absEta<1.4442) cut_sie = 0.011;//barrel
			else cut_sie = 0.031;//endcaps
			if (sie_2012[i] > cut_sie) continue; //cut on phoSigmaIEtaIEtaFull5x5

			if (corrchIso > 3.) continue;*/


			TLorentzVector pho;
			pho.SetPtEtaPhiM(phoPt[i], phoEta[i], phoPhi[i], 0.00);

			double dr1 = pho.DeltaR(mu1);
			double dr2 = pho.DeltaR(mu2);

			double Muu = (mu1 + mu2).M();
			double Muug = (mu1 + mu2 + pho).M();


			//if( !(dr1>0.2&&dr1<0.8) && !(dr2>0.2&&dr2<0.8) ) continue;
			if (!(dr1<0.8) && !(dr2<0.8)) continue; //neither of the muons emitted the photon (dR < 0.8)

			if ((dr1<0.1) || (dr2<0.1)) continue; //photon picked up track from one of the muons

			if ((Muu + Muug) > 180.) continue; //reject isr photons (muug of isr is higher)
			//if( Muu < 35. ) continue;
			//if( Muug<70 || Muug>110 ) continue;
			if (Muug<60 || Muug>120) continue; //Z mass range


			iSelpho[nSelpho] = i; //save index of selected photon
			nSelpho++;

		}//photon loop

		if (nSelpho < 1) continue;

		double mindiff = 999;
		int finipho = -99;
		float phoMVA = -99;

		for (int ipho = 0; ipho < nSelpho; ipho++){ //loop over selected photons

			int indpho = iSelpho[ipho];

			TLorentzVector pho;
			pho.SetPtEtaPhiM(phoPt[indpho], phoEta[indpho], phoPhi[indpho], 0.00);

			double Muu = (mu1 + mu2).M();
			double Muug = (mu1 + mu2 + pho).M();

			double diff = fabs(91.2 - Muug); //must be close to Z mass

			if (mindiff > diff){ //take photon which gives closest Z mass value

				mindiff = diff;
				finipho = indpho;
			}

		}//selected photons loop

		int inonFsrMu = -99; //index of mu which does not have fsr photon
		TLorentzVector pho;
		pho.SetPtEtaPhiM(phoPt[finipho], phoEta[finipho], phoPhi[finipho], 0.00);

		double dr1 = pho.DeltaR(mu1);
		double dr2 = pho.DeltaR(mu2);

		if (dr1>dr2) inonFsrMu = ileadmu; //find fsr mu
		else inonFsrMu = itrailmu;

		if (muPt[inonFsrMu]<20) continue; //Pt cut on non-fsr mu

		double Muu = (mu1 + mu2).M();
		double Muug = (mu1 + mu2 + pho).M();

		if (data.HasMC()){ //match reco muon to MC
			bool matchmu1 = mcMatchMu(ileadmu, data);
			bool matchmu2 = mcMatchMu(itrailmu, data);
			bool matchpho = mcMatchPho(finipho, data);

			if (matchmu1 && matchmu2 && matchpho) ngenFSR = weight + ngenFSR;
		}
		
		run_ = data.GetInt("run");
		phoMVA = phoIDMVA[finipho];
		Pt_ = pho.Pt();
		Eta_ = pho.Eta();
		EleVeto_ = eleVeto[finipho];
		HasPix_ = pixSeed[finipho];
		Mass_ = Muug;
		R9_ = R9[finipho];
		looseID_ = phoid[finipho] >> 0 & 1;
		medID_ = phoid[finipho] >> 1 & 1;
		tightID_ = phoid[finipho] >> 2 & 1;
		MVA_ = phoMVA;
		Muu_ = Muu;
		SCEta_ = phoSCEta[finipho];
		bMVA_ = ((fabs(phoSCEta[finipho]) <= 1.4442 && phoMVA > 0.374) || (fabs(phoSCEta[finipho]) >= 1.566 && phoMVA > 0.336));//EB || EE

		/*if (EleVeto_ == 1 &&
			((fabs(SCEta_) <= 1.4442 && phoHoverE[finipho] < 0.08) || (fabs(SCEta_) >= 1.566 && phoHoverE[finipho] < 0.05)) &&
			phoPFPhoIso[finipho] < 15 &&
			((sie_2012[finipho] < 0.012 && fabs(SCEta_) <= 1.4442) || (sie_2012[finipho] < 0.027 && fabs(SCEta_) >= 1.566)) && 
			phoPFChWorstIso[finipho] < 15 &&
			((R9_ > 0.85 && fabs(SCEta_) >= 1.566) || fabs(SCEta_) <= 1.4442)){*/
		float absEta = fabs(phoSCEta[finipho]);

		double cut_sie = 0.011;
		if (absEta<1.4442) cut_sie = 0.011;//barrel
		else cut_sie = 0.031;//endcaps

		int bin;
		if (absEta < 1.0) bin = 0;
		else if (absEta >= 1.0 && absEta < 1.479) bin = 1;
		else if (absEta >= 1.479 && absEta < 2.0) bin = 2;
		else if (absEta >= 2.0 && absEta < 2.2) bin = 3;
		else if (absEta >= 2.2 && absEta < 2.3) bin = 4;
		else if (absEta >= 2.3 && absEta < 2.4) bin = 5;
		else bin = 6; // absEta >= 2.4

		double chEA[] = { 0.0234, 0.0189, 0.0171, 0.0129, 0.0110, 0.0074, 0.0035 };
		double corrchIso = max(phoPFChIso[finipho] - chEA[bin] * rho2012, 0.);

		presel_ = 0;

		if (phoHoverE[finipho] < 0.05 &&
			sie_2012[finipho] < cut_sie &&
			corrchIso < 3.){

			//histograms
			hist["Muug"]->Fill(Muug, weight);
			hist["Muu"]->Fill(Muu, weight);
			hist["Ptg"]->Fill(pho.Pt(), weight);
			hist["Etag"]->Fill(pho.Eta(), weight);
			if (fabs(SCEta_) <= 1.4442) hist["phoMVAEB"]->Fill(phoMVA, weight);
			if (fabs(SCEta_) >= 1.566) hist["phoMVAEE"]->Fill(phoMVA, weight);
			hist2["MuugMuu"]->Fill(Muug, Muu, weight);

			presel_ = 1;
		}

		count++;
		outtree_->Fill();

	}//EVENT LOOP
	fout_->cd();
	outtree_->Write();

	for (map<string, TH1F*>::iterator it = hist.begin(); it != hist.end(); ++it) {
		hist[it->first]->Write();
	}
	hist2["MuugMuu"]->Write();
	cout << "count" << count << endl;
	cout.precision(17);
	cout << "genWeight count: " << wCounter << endl;
	fout_->Close();
}

bool select_muons(TreeReader &data, int i)
{
	/* Identification, isolation and energy scale correction for muons (for 2012).
	*
	* NOTE: the energy scale correction is applied to muPt and muInnerPtErr
	* branches only. Other energy-related branches (e.g muPz) are not corrected!
	*
	* NOTE: for multi-muon analysis, the loose muon ID should be complemented
	* with DeltaR > 0.02 cut between the muon pairs in order to suppress
	* contribution from split tracks.
	*
	* Documentation on the muon ID and isolation:
	* https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideMuonId?rev=49
	*
	* Documentation on the muon energy correction:
	* https://twiki.cern.ch/twiki/bin/viewauth/CMS/RochcorMuon?rev=2
	*
	* data = handle providing access to an input event;
	* accepted = array to fill with indices of accepted muons;
	* idLoose, idTight = arrays to fill synchronously with results of cut-based
	*   loose and tight identification criteria (0=not passed, 1=passed).
	*/

	// load necessary tree branches
	Int_t  nMu = data.GetInt("nMu");
	float* muPt = data.GetPtrFloat("muPt");
	float* muEta = data.GetPtrFloat("muEta");
	Int_t* muType = data.GetPtrInt("muType");
	float* muChi2NDF = data.GetPtrFloat("muChi2NDF");
	Int_t* muStations = data.GetPtrInt("muStations");
	float* muD0 = data.GetPtrFloat("muD0");
	float* muDz = data.GetPtrFloat("muDz");

	Int_t* muNumberOfValidMuonHits = data.GetPtrInt("muMuonHits");
	Int_t* muNumberOfValidPixelHits = data.GetPtrInt("muPixelHits");
	Int_t* muNumberOfValidTrkLayers = data.GetPtrInt("muTrkLayers");

	float* muPFIsoR04_CH = data.GetPtrFloat("muPFChIso");
	float* muPFIsoR04_NH = data.GetPtrFloat("muPFNeuIso");
	float* muPFIsoR04_Pho = data.GetPtrFloat("muPFPhoIso");
	float* muPFIsoR04_PU = data.GetPtrFloat("muPFPUIso");


	// for the energy scale correction
	Int_t  run = data.GetInt("run");
	float* muPhi = data.GetPtrFloat("muPhi");
	Int_t* muCharge = data.GetPtrInt("muCharge");

	float* muInnerPt = data.GetPtrFloat("muBestTrkPt");
	float* muInnerPtErr = data.GetPtrFloat("muBestTrkPtError");

	if (muPt[i] < 8) return false;

	// NOTE: applied at a primary vertex, not at the location of muon stations
	//also make sure that it lies in the eta region of interest
	//if (fabs(muEta[i])>1.4442 && fabs(muEta[i])<1.566) return false;

	if (fabs(muEta[i]) > 2.4) return false;

	//if (fabs(muEta[i]) > 2.4) continue;

	bool isLoose = false;
	bool isTight = false;

	// cut-based loose ID for 2012
	//
	// muon types are defined here: CMSSW/DataFormats/MuonReco/interface/Muon.h
	// namely: GlobalMuon     = 1<<1
	//         TrackerMuon    = 1<<2
	//         StandAloneMuon = 1<<3
	//         CaloMuon       = 1<<4
	//         PFMuon         = 1<<5
	//         RPCMuon        = 1<<6
	if ((muType[i] & 1 << 5) != 0 && // PFMuon && (GlobalMuon || TrackerMuon)
		((muType[i] & 1 << 1) != 0 || (muType[i] & 1 << 2) != 0))
		isLoose = true;

	bool tmp = false;
	// cut-based tight ID for 2012
	if ((muType[i] & 1 << 1) != 0 && // GlobalMuon && PFMuon
		(muType[i] & 1 << 5) != 0 &&
		muChi2NDF[i] < 10 &&
		muNumberOfValidMuonHits[i] > 0 &&
		muStations[i] > 1 &&
		///SJ
		//fabs(muInnerD0GV[i]) < 0.2 && // FIXME: GV is used historically,
		//fabs(muInnerDzGV[i]) < 0.5 && // inconsistent with vtx used for photons
		fabs(muD0[i]) < 0.2 && // FIXME: GV is used historically,
		fabs(muDz[i]) < 0.5 && // inconsistent with vtx used for photons
		muNumberOfValidPixelHits[i] > 0 &&
		muNumberOfValidTrkLayers[i] > 5) tmp = true;

	// isolation for 2012
	/*if ( ((muPFIsoR04_CH[i] + max(0., muPFIsoR04_NH[i] + muPFIsoR04_Pho[i]
	- 0.5 * muPFIsoR04_PU[i])) / muPt[i] < 0.4) && tmp ){

	isTight = true;
	}*/
	isTight = tmp;

	return isTight;

}//vector<float> &idLoose, vector<float> &idTight

bool mcMatchMu(int i, TreeReader &data){ //match reco muon to MC


	if (data.HasMC()){

		bool isRecomu = false;

		float* muPt = data.GetPtrFloat("muPt");
		float* muEta = data.GetPtrFloat("muEta");
		float* muPhi = data.GetPtrFloat("muPhi");


		TLorentzVector *mu = new TLorentzVector();
		mu->SetPtEtaPhiM(muPt[i], muEta[i], muPhi[i], 105.7*0.001);


		Int_t nMC = data.GetInt("nMC");
		Int_t *mcIndex = data.GetPtrInt("mcIndex");
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
	}//if data.HasMC()

	else{

		cout << "This is data ... so no MC match" << endl;
	}
}//bool mcMatch(int i, TreeReader &data)

bool mcMatchPho(int i, TreeReader &data){//photon matching


	if (data.HasMC()) {

		bool isRecopho = false;

		float* phoPt = data.GetPtrFloat("phoEt");
		float* phoEta = data.GetPtrFloat("phoEta");
		float* phoPhi = data.GetPtrFloat("phoPhi");

		TLorentzVector *pho = new TLorentzVector();
		pho->SetPtEtaPhiM(phoPt[i], phoEta[i], phoPhi[i], 0.);


		Int_t nMC = data.GetInt("nMC");
		Int_t *mcIndex = data.GetPtrInt("mcIndex");
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

	}//if (data.HasMC())


	else{

		cout << "This is data ... so no MC match" << endl;
	}
}//photon matching


