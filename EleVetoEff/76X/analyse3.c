//#define analyse_cxx
//#include "analyse.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <TH1.h>

#include <iostream>
#include <TLegend.h>
#include <fstream>
#include <vector>
#include <TRandom.h>
#include <TCanvas.h>
/*#include <TStyle.h>
#include <TColor.h>
#include <TLegend.h>
#include <TAxis.h>
#include <TSystem.h>
#include "untuplizer.h"
#include <TLorentzVector.h>
#include <vector>
#include "Utilities.h"
#include <TH2F.h>
#include <TH1F.h>
#include <TGraphAsymmErrors.h>
#include <fstream>*/

using namespace std;

double err(double n, double d, double err_n, double err_d);

void analyse3(TString &IDtype, TString &CutType, TString &R9Type, TString &region, Int_t &puType, double *hdval, double *hsval, double *hsfval, double *defferrp, double *sefferrp, double *sferrp){

	TFile *f1 = new TFile("data.root");
	TFile *f2 = new TFile("signal.root");

	TTree *t1 = (TTree*)f1->Get("t");
	TTree *t2 = (TTree*)f2->Get("t");

	TFile *fout_ = new TFile("plots" + IDtype + region + ".root", "recreate");
	fout_->cd();
	//PLOTS
	TH1F *hMuu = new TH1F("hMuu", "M_{#mu#mu}", 35, 20, 90);
	TH1F *hMuug = new TH1F("hMuug", "M_{#mu#mu#gamma}", 40, 70, 100);
	TH1F *Ptg = new TH1F("Ptg", "P_{T}^{#gamma}", 20, 0, 100);
	TH1F *Etag = new TH1F("Etag", "#eta^{#gamma}", 20, -2.5, 2.5);
	TH1F *phoMVA = new TH1F("phoMVA", "Photon ID MVA", 10, -1, 1);
	TH2F* MuugMuu = new TH2F("MuugMuu", "M_{#mu#mu#gamma} Vs. M_{#mu#mu}", 100, 70, 140, 100, 70, 100);

	TH1F *shMuu = new TH1F("shMuu", "M_{#mu#mu}", 35, 20, 90);
	TH1F *shMuug = new TH1F("shMuug", "M_{#mu#mu#gamma}", 40, 70, 100);
	TH1F *sPtg = new TH1F("sPtg", "P_{T}^{#gamma}", 20, 0, 100);
	TH1F *sEtag = new TH1F("sEtag", "#eta^{#gamma}", 20, -2.5, 2.5);
	TH1F *sphoMVA = new TH1F("sphoMVA", "Photon ID MVA", 10, -1, 1);
	TH2F *sMuugMuu = new TH2F("sMuugMuu", "M_{#mu#mu#gamma} Vs. M_{#mu#mu}", 100, 70, 140, 100, 70, 100);

	double etabin[2] = { 0.0, 2.5 };
	double ptbin[2] = { 10, 200 };

	int bID, bIDs;
	int bCut, bCuts;
	int presel;
	//int looseID, medID, tightID, HasPix, EleVeto;
	float R9, Pt, Eta, genWeight, puwei, puweiup, puweidown, SCEta, pu71;
	//for plots
	float Muug, Muu, MVA;

	t1->SetBranchAddress("R9", &R9);
	t1->SetBranchAddress("Pt", &Pt);
	t1->SetBranchAddress("Eta", &Eta);
	t1->SetBranchAddress("genWeight", &genWeight);
	//t1->SetBranchAddress("puwei", &puwei);
	//t1->SetBranchAddress("puweiup", &puweiup);
	//t1->SetBranchAddress("puweidown", &puweidown);
	t1->SetBranchAddress("MVA", &MVA);
	t1->SetBranchAddress("SCEta", &SCEta);
	t1->SetBranchAddress("Mass", &Muug);
	t1->SetBranchAddress("Muu", &Muu);
	t1->SetBranchAddress("presel", &presel);

	if (IDtype == "Loose") t1->SetBranchAddress("looseID", &bID);
	if (IDtype == "Medium") t1->SetBranchAddress("medID", &bID);
	if (IDtype == "Tight") t1->SetBranchAddress("tightID", &bID);
	if (IDtype == "MVA") t1->SetBranchAddress("bMVA", &bID);

	if (CutType == "HasPix") t1->SetBranchAddress("HasPix", &bCut);
	if (CutType == "CSEV") t1->SetBranchAddress("EleVeto", &bCut);

	if (IDtype == "Loose") t2->SetBranchAddress("looseID", &bIDs);
	if (IDtype == "Medium") t2->SetBranchAddress("medID", &bIDs);
	if (IDtype == "Tight") t2->SetBranchAddress("tightID", &bIDs);
	if (IDtype == "MVA") t2->SetBranchAddress("bMVA", &bIDs);

	if (CutType == "HasPix") t2->SetBranchAddress("HasPix", &bCuts);
	if (CutType == "CSEV") t2->SetBranchAddress("EleVeto", &bCuts);

	//hmap[Form("hdmass_%s_%s_%s", IDtype[i], CutType[j], R9Type[k])] = new TH1F(Form("hdmass_%s_%s_%s", IDtype[i], CutType[j], R9Type[k]), "", nbins, xmin, xmax);

	//NUMERATORS
	TH1F* hs = new TH1F("hs", "signal_" + IDtype + "_" + CutType + "_" + R9Type + " " + region, 1, etabin);
	TH1F* hd = new TH1F("hd", "data_" + IDtype + "_" + CutType + "_" + R9Type + " " + region, 1, etabin);

	//DENOMINATORS
	TH1F* dhs = new TH1F("dhs", "den_signal_" + IDtype + "_" + CutType + "_" + R9Type + " " + region, 1, etabin);
	TH1F* dhd = new TH1F("dhd", "den_data_" + IDtype + "_" + CutType + "_" + R9Type + " " + region, 1, etabin);

	//SF (eff data/eff signal)
	TH1F* hsf = new TH1F("hsf", "SF_" + IDtype + "_" + CutType + "_" + R9Type + " " + region, 1, etabin);

	//2D
	//NUMERATORS
	TH2F* hs2 = new TH2F("hs2", "signal_" + IDtype + "_" + CutType + "_" + R9Type + " " + region, 1, etabin, 1, ptbin);
	TH2F* hd2 = new TH2F("hd2", "data_" + IDtype + "_" + CutType + "_" + R9Type + " " + region, 1, etabin, 1, ptbin);

	//DENOMINATORS
	TH2F* dhs2 = new TH2F("dhs2", "den_signal_" + IDtype + "_" + CutType + "_" + R9Type + " " + region, 1, etabin, 1, ptbin);
	TH2F* dhd2 = new TH2F("dhd2", "den_data_" + IDtype + "_" + CutType + "_" + R9Type + " " + region, 1, etabin, 1, ptbin);

	//SF (eff data/eff signal)
	TH2F* hsf2 = new TH2F("hsf2", "SF_" + IDtype + "_" + CutType + "_" + R9Type + " " + region, 1, etabin, 1, ptbin);

	Long64_t nentries = t1->GetEntries();

	Long64_t nbytes = 0;
	for (Long64_t i = 0; i < nentries; i++) {
		nbytes += t1->GetEntry(i);

		if (Pt[i] > 200)continue;

		float weight;
		weight = (genWeight[i] > 0) ? 1. : -1.;

		if (!bID[i]) continue;
		if (region == "EB" && fabs(SCEta[i]) > 1.4442) continue;
		if (region == "EE" && fabs(SCEta[i]) < 1.566) continue;

		if (presel[i]){//useless after ID cut
			hMuug->Fill(Muug);
			hMuu->Fill(Muu);
			Ptg->Fill(Pt);
			Etag->Fill(Eta);
			MuugMuu->Fill(Muug, Muu);
			phoMVA->Fill(MVA);
		}

		if (R9Type == "GT" && R9[i] < 0.94) continue;
		if (R9Type == "LT" && R9[i] >= 0.94) continue;

		dhd->Fill(fabs(SCEta)[i], weight);
		dhd2->Fill(fabs(SCEta)[i], Pt[i], weight);

		if (CutType == "CSEV" && !bCut[i]) continue;
		if (CutType == "HasPix" && bCut[i]) continue;
		//if (CutType == "MVA" && region == "EB" && MVA[i] < 0.374) continue;
		//if (CutType == "MVA" && region == "EE" && MVA[i] < 0.336) continue;

		hd->Fill(fabs(SCEta[i]), weight);
		hd2->Fill(fabs(SCEta[i]), Pt[i], weight);

	}

	t2->SetBranchAddress("R9", &R9);
	t2->SetBranchAddress("Pt", &Pt);
	t2->SetBranchAddress("Eta", &Eta);
	t2->SetBranchAddress("genWeight", &genWeight);
	t2->SetBranchAddress("puwei", &puwei);//puwei for 69mb; pu71 for 71mb
	t2->SetBranchAddress("pu71", &pu71);
	t2->SetBranchAddress("puweiup", &puweiup);
	t2->SetBranchAddress("puweidown", &puweidown);
	t2->SetBranchAddress("MVA", &MVA);
	t2->SetBranchAddress("SCEta", &SCEta);
	t2->SetBranchAddress("Mass", &Muug);
	t2->SetBranchAddress("Muu", &Muu);
	t2->SetBranchAddress("presel", &presel);

	Long64_t snentries = t2->GetEntries();

	Long64_t snbytes = 0;
	for (Long64_t si = 0; si < snentries; si++) {
		snbytes += t2->GetEntry(si);

		if (Pt[si] > 200)continue;

		float weight = 1.;
		weight = (genWeight[si] > 0) ? 1. : -1.;

		if (puType == 0) weight = weight*pu71; //for Data, puwei is set to 1
		if (puType == 1) weight = weight*puweiup;
		if (puType == 2) weight = weight*puweidown;

		if (!bIDs[si]) continue;
		if (region == "EB" && fabs(SCEta[si]) > 1.4442) continue;
		if (region == "EE" && fabs(SCEta[si]) < 1.566) continue;

		if (presel[si]){
			shMuug->Fill(Muug, weight);
			shMuu->Fill(Muu, weight);
			sPtg->Fill(Pt, weight);
			sEtag->Fill(Eta, weight);
			sphoMVA->Fill(MVA, weight);
			sMuugMuu->Fill(Muug, Muu, weight);
		}

		if (R9Type == "GT" && R9[si] < 0.94) continue;
		if (R9Type == "LT" && R9[si] >= 0.94) continue;

		dhs->Fill(fabs(SCEta)[si], weight);
		dhs2->Fill(fabs(SCEta)[si], Pt[si], weight);

		if (CutType == "CSEV" && !bCuts[si]) continue;
		if (CutType == "HasPix" && bCuts[si]) continue;
		//if (CutType == "MVA" && region == "EB" && MVA[si] < 0.374) continue;
		//if (CutType == "MVA" && region == "EE" && MVA[si] < 0.336) continue;

		hs->Fill(fabs(SCEta[si]), weight);
		hs2->Fill(fabs(SCEta[si]), Pt[si], weight);

	}

	/*	hs->Sumw2();
		dhs->Sumw2();
		hd->Sumw2();
		dhd->Sumw2();*/

	TGraphAsymmErrors *seff = new TGraphAsymmErrors();
	TGraphAsymmErrors *deff = new TGraphAsymmErrors();

	seff->BayesDivide(hs, dhs);
	deff->BayesDivide(hd, dhd);

	//cout << IDtype << " " << CutType << " " << R9Type << " data Npass EB " << hd->GetBinContent(1) << " data Ntotal EB " << dhd->GetBinContent(1) <<
	//" MC Npass EB " << hs->GetBinContent(1) << " MC Ntotal EB " << dhs->GetBinContent(1) << endl;

	hs->Divide(hs, dhs);
	hd->Divide(hd, dhd);

	hs2->Divide(hs2, dhs2);
	hd2->Divide(hd2, dhd2);

	double sefferr = TMath::Max(seff->GetErrorYhigh(0), seff->GetErrorYlow(0));
	double defferr = TMath::Max(deff->GetErrorYhigh(0), deff->GetErrorYlow(0));

	//cout << IDtype << " " << CutType << " " << R9Type << " " << region << " " << seff->GetErrorYhigh(0) << endl;

	hd2->SetBinError(1, 1, defferr);
	hs2->SetBinError(1, 1, sefferr);

	double den = hs->GetBinContent(1);//signal denominator
	double num = hd->GetBinContent(1);

	//sferr = err(num, den, defferr, sefferr); //SF ERROR
	double sferr = (num / den)*sqrt(pow(defferr / num, 2) + pow(sefferr / den, 2));

	//if (region == "EB") cout << IDtype << " " << CutType << " " << R9Type << " data error EB " << defferr << " MC error EB " << sefferr << endl;
	//if (region == "EE") cout << IDtype << " " << CutType << " " << R9Type << " data error EE " << defferr << " MC error EE " << sefferr << endl;

	*sefferrp = sefferr;
	*defferrp = defferr;
	*sferrp = sferr;

	hsf->Divide(hd, hs); //SF
	hsf2->Divide(hd2, hs2);

	hsf->SetBinError(1, sferr);
	hsf2->SetBinError(1, 1, sferr);

	*hsval = hs->GetBinContent(1);
	*hdval = hd->GetBinContent(1);
	*hsfval = hsf->GetBinContent(1);

	fout_->Write();
	fout_->Close();

	//cout << IDtype << " " << CutType << " " << R9Type  << " " << region << " SF error " << hsf->GetBinError(1) << " SF " << hsf->GetBinContent(1) << endl;;

	/*
	gStyle->SetOptStat(0);
	
	TCanvas *c = new TCanvas("c", "c", 900, 600);
	c->cd();
	hs2->SetMarkerSize(2.5);
	hs2->Draw("colztexte");
	c->Print("plots/signal_" + IDtype + "_" + CutType + "_" + R9Type + " " + region + ".png");

	TCanvas *d = new TCanvas("d", "d", 900, 600);
	d->cd();
	hd2->SetMarkerSize(2.5);
	hd2->Draw("colztexte");
	d->Print("plots/data_" + IDtype + "_" + CutType + "_" + R9Type + " " + region + ".png");

	TCanvas *e = new TCanvas("e", "e", 900, 600);
	d->cd();
	hsf2->SetMarkerSize(2.5);
	hsf2->Draw("colztexte");
	d->Print("plots/SF_" + IDtype + "_" + CutType + "_" + R9Type + " " + region + ".png");
	*/
}

/*double err(double n, double d, double err_n, double err_d){//error computation

double efferr = (n / d)*sqrt(pow(err_n / n, 2) + pow(err_d / d, 2));

return efferr;

}*/