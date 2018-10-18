#include <vector>
#include <iostream>
#include <fstream>
#include <Riostream.h>
#include <stdlib.h>
#include <algorithm>
#include <ctime>
#include <TRandom.h>
#include <TLorentzVector.h>
#include <TROOT.h>
#include <TTree.h>
#include <TH2F.h>
#include <TGraph.h>
#include <TSystem.h>
#include "plugins/untuplizer_v08.h"
#include "plugins/Utilities.h"
#include "plugins/puweicalc.h"
#include "plugins/MuonSelection.h"
#include "plugins/GenMatch.h"

using namespace std;
using namespace ROOT;

void xAna(const char* Inpath, TString outpath, int aMCatNLO, float XS, bool DoMatching, int year)
{
    TreeReader data(Inpath);

    PUWeightCalculator puCalc[3];
    puCalc[0].Init("plugins/PUref/PU_histo_13TeV_2017_GoldenJSON_69200nb.root"); //nominal
    puCalc[1].Init("plugins/PUref/PU_histo_13TeV_2017_GoldenJSON_72383nb.root"); // up
    puCalc[2].Init("plugins/PUref/PU_histo_13TeV_2017_GoldenJSON_66016nb.root"); // down

    double puwei, puwei_up, puwei_down, genwei, mcwei, totalwei;

    float TotalLumi;
    if(year==2017)
        TotalLumi = 42.5;
    else if(year==2018)
        TotalLumi = 42.5;
    else
        TotalLumi = 42.5;

    Long64_t totalEvents = 0;
    if (data.HasMC())
    {
        for (Long64_t ev = 0; ev < data.GetEntriesFast(); ev++)
        {
            data.GetEntry(ev);
            float genWeight = data.GetFloat("genWeight");
            if (genWeight > 0)
                totalEvents++;
            else
                totalEvents--;
        }
        mcwei = (totalEvents != 0) ? XS * TotalLumi / totalEvents : 1;
    }

    TFile* fo = TFile::Open(outpath.Data(), "RECREATE");
    if (!fo || fo->IsZombie())
        FATAL("TFile::Open() failed");
    fo->cd();

    TTree *outTree = new TTree("outTree", "outTree");
    int run, lumis, nVtx ;
    Long64_t event ;
    float mcmatchedPt_mu1, mcmatchedPt_mu2, mcmatchedEta_mu1, mcmatchedEta_mu2, mcmatchedPhi_mu1, mcmatchedPhi_mu2, mcmatchedPt_pho, mcmatchedEta_pho, mcmatchedPhi_pho, mcmatched_Mmumu, mcmatchedPt_mumu, mcmatchedEta_mumu, mcmatchedPhi_mumu, mcmatched_Mmmg, mcmatchedPt_mmg, mcmatchedEta_mmg, mcmatchedPhi_mmg, mcmu1Vtx, mcmu2Vtx, mcmu1Vty, mcmu2Vty, mcmu1Vtz, mcmu2Vtz;
    int mcmatchedPID_mu1, mcmatchedPID_mu2, mcmatchedPID_pho, mcmatchedMomPID_mu1, mcmatchedMomPID_mu2, mcmatchedGMomPID_mu1, mcmatchedGMomPID_mu2, mcmatchedMomPID_pho, mcmatchedGMomPID_pho;
    UShort_t mcStatusFlag_mu1, mcStatusFlag_mu2, mcStatusFlag_pho;
    float mcMomMass_mu1, mcMomMass_mu2, mcMomMass_pho;
    float mu1Pt, mu2Pt, mu1Eta, mu2Eta, mu1Phi, mu2Phi;
    float phoE_, phoEt_, phoCalibEt_, phoEta_, phoPhi_, phoSCEta_, phoIDMVA_, phoR9_, m_mumu, pT_mumu, m_mmg, vtx, vty, vtz;
    int phoEleVeto_, phoHasPix_, looseID_, medID_, tightID_, passMVA_, presel_;
    if(data.HasMC() && DoMatching==true) outTree->Branch("mcmatchedPt_mu1",     &mcmatchedPt_mu1,     "mcmatchedPt_mu1/F");
    if(data.HasMC() && DoMatching==true) outTree->Branch("mcmatchedPt_mu2",     &mcmatchedPt_mu2,     "mcmatchedPt_mu2/F");
    if(data.HasMC() && DoMatching==true) outTree->Branch("mcmatchedEta_mu1",    &mcmatchedEta_mu1,    "mcmatchedEta_mu1/F");
    if(data.HasMC() && DoMatching==true) outTree->Branch("mcmatchedEta_mu2",    &mcmatchedEta_mu2,    "mcmatchedEta_mu2/F");
    if(data.HasMC() && DoMatching==true) outTree->Branch("mcmatchedPhi_mu1",    &mcmatchedPhi_mu1,    "mcmatchedPhi_mu1/F");
    if(data.HasMC() && DoMatching==true) outTree->Branch("mcmatchedPhi_mu2",    &mcmatchedPhi_mu2,    "mcmatchedPhi_mu2/F");
    if(data.HasMC() && DoMatching==true) outTree->Branch("mcmatchedPt_pho",     &mcmatchedPt_pho,     "mcmatchedPt_pho/F");
    if(data.HasMC() && DoMatching==true) outTree->Branch("mcmatchedEta_pho",    &mcmatchedEta_pho,    "mcmatchedEta_pho/F");
    if(data.HasMC() && DoMatching==true) outTree->Branch("mcmatchedPhi_pho",    &mcmatchedPhi_pho,    "mcmatchedPhi_pho/F");
    if(data.HasMC() && DoMatching==true) outTree->Branch("mcmatched_Mmumu",    &mcmatched_Mmumu,    "mcmatched_Mmumu/F");
    if(data.HasMC() && DoMatching==true) outTree->Branch("mcmatchedPt_mumu",    &mcmatchedPt_mumu,    "mcmatchedPt_mumu/F");
    if(data.HasMC() && DoMatching==true) outTree->Branch("mcmatchedEta_mumu",    &mcmatchedEta_mumu,    "mcmatchedEta_mumu/F");
    if(data.HasMC() && DoMatching==true) outTree->Branch("mcmatchedPhi_mumu",    &mcmatchedPhi_mumu,    "mcmatchedPhi_mumu/F");
    if(data.HasMC() && DoMatching==true) outTree->Branch("mcmatched_Mmmg",    &mcmatched_Mmmg,    "mcmatched_Mmmg/F");
    if(data.HasMC() && DoMatching==true) outTree->Branch("mcmatchedPt_mmg",    &mcmatchedPt_mmg,    "mcmatchedPt_mmg/F");
    if(data.HasMC() && DoMatching==true) outTree->Branch("mcmatchedEta_mmg",    &mcmatchedEta_mmg,    "mcmatchedEta_mmg/F");
    if(data.HasMC() && DoMatching==true) outTree->Branch("mcmatchedPhi_mmg",    &mcmatchedPhi_mmg,    "mcmatchedPhi_mmg/F");
    if(data.HasMC() && DoMatching==true) outTree->Branch("mcmatchedPID_mu1",    &mcmatchedPID_mu1,    "mcmatchedPID_mu1/I");
    if(data.HasMC() && DoMatching==true) outTree->Branch("mcmatchedPID_mu2",    &mcmatchedPID_mu2,    "mcmatchedPID_mu2/I");
    if(data.HasMC() && DoMatching==true) outTree->Branch("mcMomMass_mu1",    &mcMomMass_mu1,    "mcMomMass_mu1/F");
    if(data.HasMC() && DoMatching==true) outTree->Branch("mcMomMass_mu2",    &mcMomMass_mu2,    "mcMomMass_mu2/F");
    if(data.HasMC() && DoMatching==true) outTree->Branch("mcMomMass_pho",    &mcMomMass_pho,    "mcMomMass_pho/F");
    if(data.HasMC() && DoMatching==true) outTree->Branch("mcmatchedMomPID_mu1",    &mcmatchedMomPID_mu1,    "mcmatchedMomPID_mu1/I");
    if(data.HasMC() && DoMatching==true) outTree->Branch("mcmatchedMomPID_mu2",    &mcmatchedMomPID_mu2,    "mcmatchedMomPID_mu2/I");
    if(data.HasMC() && DoMatching==true) outTree->Branch("mcmatchedGMomPID_mu1",    &mcmatchedGMomPID_mu1,    "mcmatchedGMomPID_mu1/I");
    if(data.HasMC() && DoMatching==true) outTree->Branch("mcmatchedGMomPID_mu2",    &mcmatchedGMomPID_mu2,    "mcmatchedGMomPID_mu2/I");
    if(data.HasMC() && DoMatching==true) outTree->Branch("mcmatchedPID_pho",    &mcmatchedPID_pho,    "mcmatchedPID_pho/I");
    if(data.HasMC() && DoMatching==true) outTree->Branch("mcmatchedMomPID_pho",    &mcmatchedMomPID_pho,    "mcmatchedMomPID_pho/I");
    if(data.HasMC() && DoMatching==true) outTree->Branch("mcmatchedGMomPID_pho",    &mcmatchedGMomPID_pho,    "mcmatchedGMomPID_pho/I");
    if(data.HasMC() && DoMatching==true) outTree->Branch("mcStatusFlag_mu1",    &mcStatusFlag_mu1,    "mcStatusFlag_mu1/s");
    if(data.HasMC() && DoMatching==true) outTree->Branch("mcStatusFlag_mu2",    &mcStatusFlag_mu2,    "mcStatusFlag_mu2/s");
    if(data.HasMC() && DoMatching==true) outTree->Branch("mcStatusFlag_pho",    &mcStatusFlag_pho,    "mcStatusFlag_pho/s");
    if(data.HasMC() && DoMatching==true) outTree->Branch("mcmu1Vtx",     &mcmu1Vtx,     "mcmu1Vtx/F");
    if(data.HasMC() && DoMatching==true) outTree->Branch("mcmu2Vtx",     &mcmu2Vtx,     "mcmu2Vtx/F");
    if(data.HasMC() && DoMatching==true) outTree->Branch("mcmu1Vty",     &mcmu1Vty,     "mcmu1Vty/F");
    if(data.HasMC() && DoMatching==true) outTree->Branch("mcmu2Vty",     &mcmu2Vty,     "mcmu2Vty/F");
    if(data.HasMC() && DoMatching==true) outTree->Branch("mcmu1Vtz",     &mcmu1Vtz,     "mcmu1Vtz/F");
    if(data.HasMC() && DoMatching==true) outTree->Branch("mcmu2Vtz",     &mcmu2Vtz,     "mcmu2Vtz/F");
    if(data.HasMC()) outTree->Branch("puwei",     &puwei,     "puwei/D");
    if(data.HasMC()) outTree->Branch("puwei_up",     &puwei_up,     "puwei_up/D");
    if(data.HasMC()) outTree->Branch("puwei_down",     &puwei_down,     "puwei_down/D");
    if(data.HasMC()) outTree->Branch("mcwei",     &mcwei,     "mcwei/D");
    if(data.HasMC()) outTree->Branch("genwei", &genwei, "genwei/D");
    outTree->Branch("TotalLumi",       &TotalLumi,       "TotalLumi/F");
    outTree->Branch("XS", &XS, "XS/F");
    outTree->Branch("totalEvents", &totalEvents, "totalEvents/L");
    outTree->Branch("run",       &run,       "run/I");
    outTree->Branch("lumis",     &lumis,     "lumis/I");
    outTree->Branch("event",     &event,     "event/L");
    outTree->Branch("nVtx",      &nVtx,      "nVtx/I");
    // muon
    outTree->Branch("mu1Pt",           &mu1Pt,             "mu1Pt/F");
    outTree->Branch("mu2Pt",           &mu2Pt,             "mu2Pt/F");
    outTree->Branch("mu1Eta",          &mu1Eta,            "mu1Eta/F");
    outTree->Branch("mu2Eta",          &mu2Eta,            "mu2Eta/F");
    outTree->Branch("mu1Phi",          &mu1Phi,            "mu1Phi/F");
    outTree->Branch("mu2Phi",          &mu2Phi,            "mu2Phi/F");
    outTree->Branch("phoE",            &phoE_,            "phoE/F");
    outTree->Branch("phoEt",           &phoEt_,           "phoEt/F");
    outTree->Branch("phoCalibEt",      &phoCalibEt_,      "phoCalibEt/F");
    outTree->Branch("phoEta",          &phoEta_,          "phoEta/F");
    outTree->Branch("phoPhi",          &phoPhi_,          "phoPhi/F");
    outTree->Branch("phoSCEta",        &phoSCEta_,        "phoSCEta/F");
    outTree->Branch("phoIDMVA",        &phoIDMVA_,        "phoIDMVA/F");
    outTree->Branch("phoR9",           &phoR9_,            "phoR9/F");
    outTree->Branch("phoEleVeto",      &phoEleVeto_,      "phoEleVeto/I");
    outTree->Branch("phoHasPix",       &phoHasPix_,      "phoHasPix/I");
    outTree->Branch("m_mumu",          &m_mumu,           "m_mumu/F");
    outTree->Branch("pT_mumu",         &pT_mumu,          "pT_mumu/F");
    outTree->Branch("m_mmg",           &m_mmg,              "m_mmg/F");
    outTree->Branch("looseID",         &looseID_, "looseID/I");
    outTree->Branch("medID",           &medID_, "medID/I");
    outTree->Branch("tightID",         &tightID_, "tightID/I");
    outTree->Branch("passMVA_",        &passMVA_, "passMVA/I");
    outTree->Branch("presel",          &presel_, "presel/I");

    for (Long64_t ev = 0; ev < data.GetEntriesFast(); ev++)
    {
        data.GetEntry(ev);

        run   = data.GetInt("run");
        lumis = data.GetInt("lumis");
        event = data.GetLong64("event");
        nVtx = data.GetInt("nVtx");

        // PU reweighting
        if (data.HasMC())
        {
            float* puTrue = data.GetPtrFloat("puTrue");
            puwei = (float) puCalc[0].GetWeight(run, puTrue[0]); // in-time PU
            puwei_up = (float) puCalc[1].GetWeight(run, puTrue[0]); // in-time PU
            puwei_down = (float) puCalc[2].GetWeight(run, puTrue[0]); // in-time PU

            float generatorWeight = data.GetFloat("genWeight");
            genwei = (generatorWeight > 0) ? 1. : -1.;
            //if(genwei == -1.) cout << ev << " genwei=" << genwei << endl;
        }

        if(ev == 0) cout << "Total events" << " " << data.GetEntriesFast() << endl;
        if(ev % 1000000 == 0) cout << "ev" << " " << ev << endl;

        ULong64_t   HLTEleMuX  = (ULong64_t)data.GetLong64("HLTEleMuX");
        ULong64_t   HLTEleMuXIsPrescaled  = (ULong64_t)data.GetLong64("HLTEleMuXIsPrescaled");
        if( ((HLTEleMuX >> 14) & 1) != 1 && ((HLTEleMuX >> 15) & 1) != 1 && ((HLTEleMuX >> 41) & 1) != 1 && ((HLTEleMuX >> 42) & 1) != 1)
            continue;

        ////Photon branches
        Int_t  nPho       = data.GetInt("nPho");
        Short_t* phoIDbit = data.GetPtrShort("phoIDbit");
        float* phoE      = data.GetPtrFloat("phoE");
        float* phoEt      = data.GetPtrFloat("phoEt");
        float* phoCalibEt = data.GetPtrFloat("phoCalibEt"); // calibrated photon pT
        float* phoEta     = data.GetPtrFloat("phoEta");
        float* phoPhi     = data.GetPtrFloat("phoPhi");
        float* phoSCEta   = data.GetPtrFloat("phoSCEta");
        float* phoIDMVA   = data.GetPtrFloat("phoIDMVA");
        Int_t* phoEleVeto = data.GetPtrInt("phoEleVeto");
        Int_t* phohasPixelSeed  = data.GetPtrInt("phohasPixelSeed");
        float* phoR9      = data.GetPtrFloat("phoR9");
        float* phoHoverE = data.GetPtrFloat("phoHoverE");
        float* phoSigmaIEtaIEtaFull5x5 = data.GetPtrFloat("phoSigmaIEtaIEtaFull5x5");
		float* phoPFPhoIso = data.GetPtrFloat("phoPFPhoIso");
        float* phoPFNeuIso = data.GetPtrFloat("phoPFNeuIso");
		float* phoPFChIso = data.GetPtrFloat("phoPFChIso");
		float* phoPFChWorstIso = data.GetPtrFloat("phoPFChWorstIso");
        float  rho = data.GetFloat("rho");
        ////Muon branches
		Int_t  nMu = data.GetInt("nMu");
		float* muPt = data.GetPtrFloat("muPt");
		float* muEta = data.GetPtrFloat("muEta");
		float* muPhi = data.GetPtrFloat("muPhi");
		int* muCharge = data.GetPtrInt("muCharge");
        ////
        vtx              = data.GetFloat("vtx");
        vty              = data.GetFloat("vty");
        vtz              = data.GetFloat("vtz");

        // Muon Selection
        vector<int> iSelmu; //index of selected mu
        iSelmu.clear();
		for (int imu = 0; imu<nMu; imu++){

			if (muPt[imu] < 10.) continue;
			bool id = select_muons(data, imu);
			if (!id) continue;
			iSelmu.push_back(imu);
		}
		if (iSelmu.size() < 2) continue;

        TLorentzVector mu1, mu2;
        mu1.SetPtEtaPhiM(muPt[iSelmu[0]], muEta[iSelmu[0]], muPhi[iSelmu[0]], 105.7*0.001);
        mu2.SetPtEtaPhiM(muPt[iSelmu[1]], muEta[iSelmu[1]], muPhi[iSelmu[1]], 105.7*0.001);

        vector<int> iSelpho;
        iSelpho.clear();
        //int iSelpho[100]; //select 100 photons
        //int nSelpho = 0;

        if(nPho<1) continue;
        for(int i = 0; i < nPho; i++)
        {
            if (phoCalibEt[i] < 10) continue;
            if ((fabs(phoSCEta[i]) > 1.4442) && (fabs(phoSCEta[i]) < 1.566)) continue; //gap region
            if (fabs(phoSCEta[i]) > 2.5) continue;

            TLorentzVector pho;
            pho.SetPtEtaPhiM(phoCalibEt[i], phoEta[i], phoPhi[i], 0.00);
            double dr1 = deltaR(phoEta[i],phoPhi[i],mu1.Eta(),mu1.Phi());
            double dr2 = deltaR(phoEta[i],phoPhi[i],mu2.Eta(),mu2.Phi());
            double Muu = (mu1 + mu2).M();
            double Muug = (mu1 + mu2 + pho).M();

            if (!(dr1<0.8) && !(dr2<0.8)) continue; //reject the event that neither of the muons emitted the photon (dR < 0.8)
            if ((dr1<0.1) || (dr2<0.1)) continue; //photon picked up track from one of the muons
            if ((Muu + Muug) > 180.) continue; //reject isr photons (muug of isr is higher)
            if (Muug<60 || Muug>120) continue; //three body mass must be close to Z mass

            iSelpho.push_back(i);
        }//photon loop

        if (iSelpho.size() < 1) continue;

        int finipho = -99;
        if(iSelpho.size() > 1)
        {
            double mindiff = 999;

            for (unsigned int ipho = 0; ipho < iSelpho.size(); ipho++)
            { //loop over selected photons
                int indpho = iSelpho[ipho];

                TLorentzVector pho;
                pho.SetPtEtaPhiM(phoCalibEt[iSelpho[ipho]], phoEta[iSelpho[ipho]], phoPhi[iSelpho[ipho]], 0.00);
                double Muu = (mu1 + mu2).M();
                double Muug = (mu1 + mu2 + pho).M();
                double diff = fabs(91.18 - Muug); //must be close to Z mass

                if (mindiff > diff)
                { //take photon which gives closest Z mass value
                    mindiff = diff;
                    finipho = iSelpho[ipho];
                }
            }//selected photons loop
            iSelpho.clear();
            iSelpho.push_back(finipho);
        }
        if(iSelpho.size() != 1)
        {
            cout << "There is more than 1 photon!! This is not right!!" << endl;
            continue;
        }

        int inonFsrMu = -99; //index of mu which does not have fsr photon
        TLorentzVector pho;
        pho.SetPtEtaPhiM(phoCalibEt[iSelpho[0]], phoEta[iSelpho[0]], phoPhi[iSelpho[0]], 0.00);
        double dr1 = deltaR(phoEta[iSelpho[0]],phoPhi[iSelpho[0]],mu1.Eta(),mu1.Phi());
        double dr2 = deltaR(phoEta[iSelpho[0]],phoPhi[iSelpho[0]],mu2.Eta(),mu2.Phi());
        if (dr1>dr2)
            inonFsrMu = iSelmu[0]; //find fsr mu
        else
        inonFsrMu = iSelmu[1];

        if (muPt[inonFsrMu]<20.) continue; //Pt cut on non-fsr mu

        double Muu = (mu1 + mu2).M();
		double Muug = (mu1 + mu2 + pho).M();

        //int looseID_, medID_, tightID_, passMVA_, presel_;
        mu1Pt       = muPt[iSelmu[0]];
        mu2Pt       = muPt[iSelmu[1]];
        mu1Eta      = muEta[iSelmu[0]];
        mu2Eta      = muEta[iSelmu[1]];
        mu1Phi      = muPhi[iSelmu[0]];
        mu2Phi      = muPhi[iSelmu[1]];
        phoE_       = phoE[iSelpho[0]];
        phoEt_      = phoEt[iSelpho[0]];
        phoCalibEt_ = phoCalibEt[iSelpho[0]];
        phoEta_     = phoEta[iSelpho[0]];
        phoPhi_     = phoPhi[iSelpho[0]];
        phoSCEta_   = phoSCEta[iSelpho[0]];
        phoIDMVA_   = phoIDMVA[iSelpho[0]];
        phoEleVeto_ = phoEleVeto[iSelpho[0]];
        phoR9_      = phoR9[iSelpho[0]];
        phoHasPix_ = phohasPixelSeed[iSelpho[0]];
        m_mumu = (mu1 + mu2).M();
        pT_mumu = (mu1 + mu2).Pt();
        m_mmg = (mu1 + mu2 + pho).M();
        looseID_ = phoIDbit[iSelpho[0]] >> 0 & 1;
		medID_ = phoIDbit[iSelpho[0]] >> 1 & 1;
		tightID_ = phoIDbit[iSelpho[0]] >> 2 & 1;
        float phoMVAcut_EB, phoMVAcut_EE;
        if(year==2017)
        {
            phoMVAcut_EB = 0.27;
            phoMVAcut_EE = 0.14;
        }
        else if(year==2018)
        {
            phoMVAcut_EB = -0.02;
            phoMVAcut_EE = -0.26;
        }
        else // Use the default 2017 version
        {
            phoMVAcut_EB = 0.27;
            phoMVAcut_EE = 0.14;
        }
		passMVA_ = ((fabs(phoSCEta[iSelpho[0]]) <= 1.4442 && phoIDMVA[iSelpho[0]] > phoMVAcut_EB) || (fabs(phoSCEta[iSelpho[0]]) >= 1.566 && phoIDMVA[iSelpho[0]] > phoMVAcut_EE));

        //// Check photon pre-selection
        float cut_sie = 0.01015;
        float cut_HoverE = 0.02197;
        float cut_chIso = 1.051;
		if (fabs(phoSCEta[iSelpho[0]])<1.4442)
        {
            cut_sie = 0.01015;//barrel
            cut_HoverE = 0.02197;
        }
		else
        {
            cut_sie = 0.0272;//endcaps
            cut_HoverE = 0.0326;
        }
		int bin;
		if (fabs(phoSCEta[iSelpho[0]]) < 1.0) bin = 0;
		else if (fabs(phoSCEta[iSelpho[0]]) >= 1.0 && fabs(phoSCEta[iSelpho[0]]) < 1.479) bin = 1;
		else if (fabs(phoSCEta[iSelpho[0]]) >= 1.479 && fabs(phoSCEta[iSelpho[0]]) < 2.0) bin = 2;
		else if (fabs(phoSCEta[iSelpho[0]]) >= 2.0 && fabs(phoSCEta[iSelpho[0]]) < 2.2) bin = 3;
		else if (fabs(phoSCEta[iSelpho[0]]) >= 2.2 && fabs(phoSCEta[iSelpho[0]]) < 2.3) bin = 4;
		else if (fabs(phoSCEta[iSelpho[0]]) >= 2.3 && fabs(phoSCEta[iSelpho[0]]) < 2.4) bin = 5;
		else bin = 6; // fabs(phoSCEta[iSelpho[0]]) >= 2.4

        double chEA[] = { 0.0112, 0.0108, 0.0106, 0.01002, 0.0098, 0.0089, 0.0087};
        double corrchIso = TMath::Max(phoPFChIso[iSelpho[0]] - chEA[bin] * rho, 0.);
        // rho-corrected PF neutral hadron isolation
        double neuEA[] = {0.0668, 0.1054, 0.0786, 0.0233, 0.0078, 0.0028, 0.0137};
        double corrneIso = TMath::Max(phoPFNeuIso[iSelpho[0]] - neuEA[bin] * rho,0.);
        // rho-corrected PF photon isolation
        double phoEA[] = {0.1113, 0.0953, 0.0619, 0.0837, 0.1070, 0.1212, 0.1466};
        double corrpfIso = TMath::Max(phoPFPhoIso[iSelpho[0]] - phoEA[bin] * rho,0.);

		presel_ = 0;
		if (phoHoverE[iSelpho[0]] < cut_HoverE && phoSigmaIEtaIEtaFull5x5[iSelpho[0]] < cut_sie && corrchIso < cut_chIso)
			presel_ = 1;
        //
		if (data.HasMC() && DoMatching==true)
        { //match reco muon to MC
            Int_t nMC = data.GetInt("nMC");
    		Int_t *mcPID = data.GetPtrInt("mcPID");
    		Int_t *mcMomPID = data.GetPtrInt("mcMomPID");
    		Int_t *mcGMomPID = data.GetPtrInt("mcGMomPID");
    		float *mcMomMass = data.GetPtrFloat("mcMomMass");
    		float *mcPt = data.GetPtrFloat("mcPt");
    		float *mcEta = data.GetPtrFloat("mcEta");
    		float *mcPhi = data.GetPtrFloat("mcPhi");
    		float *mcMass = data.GetPtrFloat("mcMass");
            UShort_t* mcStatusFlag   = (UShort_t*)data.GetPtrShort("mcStatusFlag");
            float* mcVtx    = data.GetPtrFloat("mcVtx");
            float* mcVty    = data.GetPtrFloat("mcVty");
            float* mcVtz    = data.GetPtrFloat("mcVtz");

			// bool matchmu1 = mcMatchMu(iSelmu[0], data);
			// bool matchmu2 = mcMatchMu(iSelmu[1], data);
			// bool matchpho = mcMatchPho(iSelpho[0], data);
            //double ngenFSR = 0.;
			//if (matchmu1 && matchmu2 && matchpho) ngenFSR = weight + ngenFSR;

            vector<int> GenMuIdx; GenMuIdx.clear();
            vector<int> GenPhoIdx; GenPhoIdx.clear();
            GenMatchPID(data, iSelmu, iSelpho, GenMuIdx, GenPhoIdx);

            mcmatchedPt_mu1 = mcPt[GenMuIdx[0]];
            mcmatchedEta_mu1 = mcEta[GenMuIdx[0]];
            mcmatchedPhi_mu1 = mcPhi[GenMuIdx[0]];
            mcmatchedPID_mu1 = GenMuIdx[0];
            mcmatchedMomPID_mu1 = mcMomPID[GenMuIdx[0]];
            mcmatchedGMomPID_mu1 = mcGMomPID[GenMuIdx[0]];
            mcMomMass_mu1 = mcMomMass[GenMuIdx[0]];
            mcStatusFlag_mu1 = mcStatusFlag[GenMuIdx[0]];
            mcmu1Vtx = mcVtx[GenMuIdx[0]];
            mcmu1Vty = mcVty[GenMuIdx[0]];
            mcmu1Vtz = mcVtz[GenMuIdx[0]];
            mcmatchedPt_mu2 = mcPt[GenMuIdx[1]];
            mcmatchedEta_mu2 = mcEta[GenMuIdx[1]];
            mcmatchedPhi_mu2 = mcPhi[GenMuIdx[1]];
            mcmatchedPID_mu2 = GenMuIdx[1];
            mcmatchedMomPID_mu2 =mcMomPID[GenMuIdx[1]];
            mcmatchedGMomPID_mu2 = mcGMomPID[GenMuIdx[1]];
            mcMomMass_mu2 = mcMomMass[GenMuIdx[1]];
            mcStatusFlag_mu2 = mcStatusFlag[GenMuIdx[1]];
            mcmu2Vtx = mcVtx[GenMuIdx[1]];
            mcmu2Vty = mcVty[GenMuIdx[1]];
            mcmu2Vtz = mcVtz[GenMuIdx[1]];
            mcmatchedPt_pho = mcPt[GenPhoIdx[0]];
            mcmatchedEta_pho = mcEta[GenPhoIdx[0]];
            mcmatchedPhi_pho = mcPhi[GenPhoIdx[0]];
            mcmatchedPID_pho = GenPhoIdx[0];
            mcmatchedMomPID_pho = mcMomPID[GenPhoIdx[0]];
            mcmatchedGMomPID_pho = mcGMomPID[GenPhoIdx[0]];
            mcMomMass_pho = mcMomMass[GenPhoIdx[0]];
            mcStatusFlag_pho = mcStatusFlag[GenPhoIdx[0]];

            TLorentzVector mu1_gen, mu2_gen, pho_gen, mumu_gen, mmg_gen;
            mu1_gen.SetPtEtaPhiM(mcmatchedPt_mu1, mcmatchedEta_mu1, mcmatchedPhi_mu1, 0.1057);
            mu2_gen.SetPtEtaPhiM(mcmatchedPt_mu2, mcmatchedEta_mu2, mcmatchedPhi_mu2, 0.1057);
            pho_gen.SetPtEtaPhiM(mcmatchedPt_pho, mcmatchedEta_pho, mcmatchedPhi_pho, 0);
            mumu_gen = mu1_gen + mu2_gen;
            mmg_gen = mumu_gen + pho_gen;

            mcmatched_Mmumu = mumu_gen.M();
            mcmatchedPt_mumu = mumu_gen.Pt();
            mcmatchedEta_mumu = mumu_gen.Eta();
            mcmatchedPhi_mumu = mumu_gen.Phi();
            mcmatched_Mmmg = mmg_gen.M();
            mcmatchedPt_mmg = mmg_gen.Pt();
            mcmatchedEta_mmg = mmg_gen.Eta();
            mcmatchedPhi_mmg = mmg_gen.Phi();
		}
        outTree->Fill();
    }
    outTree->Write("", TObject::kOverwrite);
    fo->Close();
}
