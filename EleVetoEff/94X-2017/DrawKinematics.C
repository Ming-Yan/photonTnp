#include "plugins/tdrstyle.C"
#include "plugins/Utilities.h"

float mcwei_DYJetsToLL_aMCatNLO = (5943200.*42.5)/(112669192.+10915332.);
float mcwei_ttbarTo2L2Nu_powheg = (72100.*42.5)/8634992.;
float mcwei_DYJetsToLL_MadGraph = (14420000.*42.5)/(48632630.+49082157.);
float mcwei_Ztomumu_powheg = 1.;
float mcwei_Wjets_aMCatNLO = (56000.*1000.*42.5)/(33043732.+44587448.);

float lumi_2017 = 42.5;
float lumi_2018 = 42.5;

void DrawStack(vector<TH1F*> vhist, vector<TString> vLegend, bool DoRatio, bool LogY, TString LegPos, int Year, TString XaxisName, TString YaxisName, TString outname)
{
    TH1F *hM_TotalMC;
    hM_TotalMC = (TH1F*) vhist[1]->Clone();
    for(unsigned int ihist=2;ihist<vhist.size();ihist++)
    {
        hM_TotalMC->Add(vhist[ihist],1);
    }
    TH1F* hM_ratio;
    hM_ratio = (TH1F*) vhist[0]->Clone();
    hM_ratio->Divide(hM_TotalMC);

    TString Colorname[] = {"#00a8b5","#774898","#e62a76","#fbb901"};
    vector<TString> vColor(Colorname, Colorname + sizeof Colorname / sizeof Colorname[0]);

    THStack *hs = new THStack("hs","hs");
    for(unsigned int ihist=0;ihist<vhist.size()-1;ihist++)
    {
        vhist[ihist+1]->SetFillColor(TColor::GetColor(vColor[ihist]));
        vhist[ihist+1]->SetLineColor(TColor::GetColor(vColor[ihist]));
        hs->Add(vhist[ihist+1]);
        cout << vhist[ihist+1]->Integral(-1,-1) << endl;
    }

    setTDRStyle();
    TCanvas* c = new TCanvas("c1","",800,700);
    c->cd();
    TPad *Plot_Pad1;
    TPad *Plot_Pad2;
    if(DoRatio==true)
        Plot_Pad1 = new TPad("pad1","", 0, 0.3, 1, 1);
    else
        Plot_Pad1 = new TPad("pad1","", 0, 0, 1, 1);
    Plot_Pad1->SetRightMargin(0.05);
    Plot_Pad1->SetTopMargin(0.08);
    Plot_Pad1->SetLeftMargin(0.14);
    if(DoRatio==true) Plot_Pad1->SetBottomMargin(0.01);
    Plot_Pad1->Draw();
    Plot_Pad1->cd();
    if(LogY==true) Plot_Pad1->SetLogy();
    hs->Draw("hist");
    if(DoRatio==false)
        hs->GetXaxis()->SetTitle(XaxisName);
    hs->GetXaxis()->SetTitleSize(0.06);
    hs->GetYaxis()->SetTitle(YaxisName);
    hs->GetYaxis()->SetTitleSize(0.06);
    hs->GetXaxis()->SetTickSize(0.03);
    hs->GetYaxis()->SetTickSize(0.03);
    hs->GetXaxis()->SetLabelSize(0.05);
    hs->GetYaxis()->SetLabelSize(0.05);
    hs->GetXaxis()->SetTitleOffset(1.);
    hs->GetYaxis()->SetTitleOffset(1.1);
    hs->SetMinimum(5);
    if(LogY==true)
        hs->SetMaximum(vhist[0]->GetMaximum()*10.);
    else
        hs->SetMaximum(vhist[0]->GetMaximum()*2.);
    vhist[0]->SetMarkerStyle(20);
    vhist[0]->SetMarkerSize(2);
    vhist[0]->SetLineWidth(2);
    vhist[0]->SetLineColor(1);
    vhist[0]->SetMarkerColor(1);
    c->Modified();
    vhist[0]->Draw("pe1same");
    TLegend *l;
    if(LegPos.EqualTo("right"))
        l = new TLegend(0.7, 0.6, 0.89, 0.89);
    else if(LegPos.EqualTo("left"))
        l = new TLegend(0.2, 0.6, 0.39, 0.89);
    for(unsigned int ileg=0;ileg<vLegend.size();ileg++)
    {
        if(ileg==0)
            l->AddEntry(vhist[ileg],vLegend[ileg],"lep");
        else
            l->AddEntry(vhist[ileg],vLegend[ileg],"lf");
    }
    l->SetFillColor(0); //Set the background to be white
    l->SetLineColor(1);
    l->Draw("same");

    if(DoRatio==true)
    {
        c->cd();
        Plot_Pad2 = new TPad("pad2", "", 0, 0, 1, 0.28);
        Plot_Pad2->SetRightMargin(0.05);
        Plot_Pad2->SetLeftMargin(0.14);
        Plot_Pad2->SetTopMargin(0.03);
        Plot_Pad2->SetBottomMargin(0.35);
        Plot_Pad2->Draw();
        Plot_Pad2->cd();
        //Plot_Pad2->SetLogy();
        Plot_Pad2->SetGridy();
        hM_ratio->GetYaxis()->SetTitle("Data / MC");
        hM_ratio->GetXaxis()->SetTitle(XaxisName);
        hM_ratio->GetYaxis()->SetTitleSize(0.13);
        hM_ratio->GetYaxis()->SetTitleOffset(0.5);
        hM_ratio->GetYaxis()->SetLabelSize(0.11);
        hM_ratio->GetYaxis()->SetRangeUser(0,2);
        hM_ratio->GetYaxis()->SetNdivisions(103);
        hM_ratio->GetXaxis()->SetTitleSize(0.15);
        hM_ratio->GetXaxis()->SetTitleOffset(1);
        hM_ratio->GetXaxis()->SetLabelSize(0.13);
        hM_ratio->SetMarkerColor(1);
        hM_ratio->SetMarkerSize(2);
        hM_ratio->SetMarkerStyle(20);
        hM_ratio->SetLineColor(1);
        hM_ratio->SetLineWidth(2);
        hM_ratio->Draw("pe1");
    }
    c->SaveAs("Kinematics/"+outname+".png");
    c->SaveAs("Kinematics/"+outname+".pdf");
}

void DrawKinematics()
{
    const char* fname[] =
    {"minitree/minitree_DoubleMu_AllRuns.root",
    "minitree/minitree_DYJetsToLL_aMCatNLO.root",
    "minitree/minitree_TTTo2L2Nu_powheg.root",
    "minitree/minitree_Wjets_aMCatNLO.root"};
    vector<const char*> vfname(fname, fname + sizeof fname / sizeof fname[0]);
    vector<float> vmcwei; vmcwei.clear();
    vmcwei.push_back(1.);
    vmcwei.push_back(mcwei_DYJetsToLL_aMCatNLO);
    vmcwei.push_back(mcwei_ttbarTo2L2Nu_powheg);
    vmcwei.push_back(mcwei_Wjets_aMCatNLO);

    TString Legendentry[] = {"Data","DY+jets","t#bar{t}","W+jets"};
    vector<TString> vLegEntry(Legendentry, Legendentry + sizeof Legendentry / sizeof Legendentry[0]);

    vector<TFile*> vFile; vFile.clear();
    vector<TH1F*> hM_Mmmg; hM_Mmmg.clear();
    vector<TH1F*> hM_Mmm; hM_Mmm.clear();
    vector<TH1F*> hM_phoEt; hM_phoEt.clear();
    vector<TH1F*> hM_phoMVA; hM_phoMVA.clear();
    vector<TH1F*> hM_phoR9; hM_phoR9.clear();
    vector<TH1F*> hM_nVtx; hM_nVtx.clear();
    for(unsigned int ifile=0;ifile<vfname.size();ifile++)
    {
        cout << fname[ifile] << " " << vmcwei[ifile];
        hM_Mmmg.push_back(new TH1F("hM_Mmmg","",60,60,120));
        hM_Mmm.push_back(new TH1F("hM_Mmm","",60,60,120));
        hM_phoEt.push_back(new TH1F("hM_phoEt","",95,10,200));
        hM_phoMVA.push_back(new TH1F("hM_phoMVA","",50,-1,1));
        hM_phoR9.push_back(new TH1F("hM_phoR9","",50,0,1));
        hM_nVtx.push_back(new TH1F("hM_nVtx","",100,0,100));
        vFile.push_back(new TFile(vfname[ifile],"READ"));
        TTree* Tree = (TTree*) vFile[ifile]->Get("outTree");
        cout << " " << Tree->GetEntries("presel==1") << endl;
        float mu1Pt, mu2Pt, mu1Eta, mu2Eta, mu1Phi, mu2Phi, phoCalibEt, phoSCEta, phoIDMVA, phoR9, m_mumu, pT_mumu, m_mmg;
        int nVtx;
        int presel, passMVA, looseID, medID, tightID;
        int phoEleVeto, phoHasPix;
        double puwei, puwei_up, puwei_down, mcwei, genwei;
        Tree->SetBranchAddress("mu1Pt", &mu1Pt);
        Tree->SetBranchAddress("mu2Pt", &mu2Pt);
        Tree->SetBranchAddress("mu1Eta", &mu1Eta);
        Tree->SetBranchAddress("mu2Eta", &mu2Eta);
        Tree->SetBranchAddress("mu1Phi", &mu1Phi);
        Tree->SetBranchAddress("mu2Phi", &mu2Phi);
        Tree->SetBranchAddress("phoCalibEt", &phoCalibEt);
        Tree->SetBranchAddress("phoSCEta", &phoSCEta);
        Tree->SetBranchAddress("phoIDMVA", &phoIDMVA);
        Tree->SetBranchAddress("phoR9", &phoR9);
        Tree->SetBranchAddress("m_mumu", &m_mumu);
        Tree->SetBranchAddress("pT_mumu", &pT_mumu);
        Tree->SetBranchAddress("m_mmg", &m_mmg);
        Tree->SetBranchAddress("nVtx", &nVtx);
        Tree->SetBranchAddress("presel", &presel);
        Tree->SetBranchAddress("passMVA_", &passMVA);
        Tree->SetBranchAddress("looseID", &looseID);
        Tree->SetBranchAddress("medID", &medID);
        Tree->SetBranchAddress("tightID", &tightID);
        Tree->SetBranchAddress("phoEleVeto", &phoEleVeto);
        Tree->SetBranchAddress("phoHasPix", &phoHasPix);
        if(ifile>0) Tree->SetBranchAddress("puwei", &puwei);
        if(ifile>0) Tree->SetBranchAddress("puwei_up", &puwei_up);
        if(ifile>0) Tree->SetBranchAddress("puwei_down", &puwei_down);
        if(ifile>0) Tree->SetBranchAddress("genwei", &genwei);

        for(Long64_t ev=0; ev<Tree->GetEntriesFast(); ev++)
        {
            Tree->GetEntry(ev);

            if(ifile==0)
            {
                genwei=1.;
                puwei=1.;
            }

            if(presel != 1) continue;
            if(tightID != 1) continue;
            if(phoHasPix != 0) continue;

            hM_Mmmg[ifile]->Fill(m_mmg,puwei*genwei*vmcwei[ifile]);
            hM_Mmm[ifile]->Fill(m_mumu,puwei*genwei*vmcwei[ifile]);
            hM_phoEt[ifile]->Fill(phoCalibEt,puwei*genwei*vmcwei[ifile]);
            hM_phoMVA[ifile]->Fill(phoIDMVA,puwei*genwei*vmcwei[ifile]);
            hM_phoR9[ifile]->Fill(phoR9,puwei*genwei*vmcwei[ifile]);
            hM_nVtx[ifile]->Fill(nVtx,puwei*genwei*vmcwei[ifile]);
        }
    }
    //DrawStack(vector<TH1F*> vhist, vector<TString> vLegend, bool DoRatio, bool LogY, TString LegPos, int Year, TString XaxisName, TString YaxisName, TString outname)
    DrawStack(hM_Mmmg, vLegEntry, true, true, "right", 2017, "M_{#mu#mu#gamma} (GeV)", Form("Events / %.1f GeV",(float) hM_Mmmg[0]->GetBinWidth(5)), "Mmmg");
    DrawStack(hM_Mmm, vLegEntry, false, true, "right", 2017, "M_{#mu#mu} (GeV)", Form("Events / %.1f GeV",(float) hM_Mmm[0]->GetBinWidth(5)), "Mmm");
    DrawStack(hM_phoEt, vLegEntry, false, true, "right", 2017, "p_{T}^{#gamma} (GeV)", Form("Events / %.1f GeV",(float) hM_phoEt[0]->GetBinWidth(5)), "phoEt");
    DrawStack(hM_phoMVA, vLegEntry, false, true, "left", 2017, "Photon MVA", Form("Events / %.2f",(float) hM_phoMVA[0]->GetBinWidth(5)), "phoMVA");
    DrawStack(hM_phoR9, vLegEntry, false, true,"left", 2017, "Photon R_{9}", Form("Events / %.2f",(float) hM_phoR9[0]->GetBinWidth(5)), "phoR9");
    DrawStack(hM_nVtx, vLegEntry, true, true,"right", 2017, "Number of vertex", "Entries", "nVtx");
}
