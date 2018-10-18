#include "plugins/tdrstyle.C"
#include "plugins/Utilities.h"

float mcwei_DYJetsToLL_aMCatNLO = (5943200.*42.5)/(112669192.+10915332.);
float mcwei_ttbarTo2L2Nu_powheg = (72100.*42.5)/8634992.;
float mcwei_DYJetsToLL_MadGraph = (14420000.*42.5)/(48632630.+49082157.);
float mcwei_Ztomumu_powheg = 1.;
float mcwei_Wjets_aMCatNLO = (56000.*1000.*42.5)/(33043732.+44587448.);

float lumi_2017 = 42.5;
float lumi_2018 = 42.5;

bool IsPreliminary = true;

void Draw2DEffHist(vector<TH2F*> vhist, int putype, int IDtype, int EleVetoSet, int Year, TString XaxisName, TString YaxisName, TString outname)
{
    TString EleVetoType, IDname, PUset;
    if(EleVetoSet==1)
        EleVetoType="HasPix";
    else if(EleVetoSet==2)
        EleVetoType="CSEV";
    else
        EleVetoType="HasPix";

    if(IDtype==1)
        IDname="Loose";
    else if(IDtype==2)
        IDname="Medium";
    else if(IDtype==3)
        IDname="Tight";
    else if(IDtype==4)
        IDname="MVA";
    else
        IDname="Loose";

    if(putype==1)
        PUset="PU Nominal";
    else if(putype==2)
        PUset="PU Up";
    else if(putype==3)
        PUset="PU Down";
    else
        PUset="PU Nominal";

    gStyle->SetOptStat(0);

    TCanvas* c = new TCanvas("c1","",800,700);
    c->cd();
    gPad->SetRightMargin(0.13);
    gPad->SetTopMargin(0.08);
    gPad->SetLeftMargin(0.13);
    vhist[1]->Divide(vhist[0]);
    vhist[1]->GetXaxis()->SetTitle(XaxisName);
    vhist[1]->GetYaxis()->SetTitle(YaxisName);
    vhist[1]->GetZaxis()->SetRangeUser(0.6,1.0);
    vhist[1]->GetXaxis()->SetTickSize(0.03);
    vhist[1]->GetYaxis()->SetTickSize(0.03);
    vhist[1]->GetXaxis()->SetTitleSize(0.05);
    vhist[1]->GetYaxis()->SetTitleSize(0.05);
    vhist[1]->GetXaxis()->SetLabelSize(0.04);
    vhist[1]->GetYaxis()->SetLabelSize(0.04);
    vhist[1]->GetXaxis()->SetTitleOffset(1);
    vhist[1]->GetYaxis()->SetTitleOffset(1);
    // vhist[1]->GetZaxis()->SetLabelSize(0.025);
    vhist[1]->SetContour(2000);
    vhist[1]->Draw("COLZ");
    // TLegend *l = new TLegend(0.66, 0.75, 0.85, 0.89);
    // l->AddEntry(vhist[0], proc_ltx[0],"lep");
    // l->AddEntry(vhist[1], Form("%s signal",proc_ltx[1]),"f");
    // l->AddEntry(vhist[2], Form("%s background",proc_ltx[2]),"f");
    // l->SetFillColor(0); //Set the background to be white
    // l->SetLineColor(1);
    // l->Draw("same");
    TLatex* ltx = new TLatex();
    ltx->SetNDC();
    ltx->SetTextFont(61);
    ltx->SetTextSize(0.05);
    ltx->DrawLatex(0.13,0.93,"CMS");
    ltx->SetTextFont(52);
    ltx->SetTextSize(0.04);
    if(IsPreliminary==true) ltx->DrawLatex(0.24,0.93,"Preliminary");
    ltx->SetTextFont(42);
    ltx->SetTextSize(0.04);
    if(Year==2017)
        ltx->DrawLatex(0.565,0.93,Form("%d %.1f fb^{-1} (13TeV)", Year, lumi_2017));
    else if(Year==2018)
        ltx->DrawLatex(0.565,0.93,Form("%d %.1f fb^{-1} (13TeV)", Year, lumi_2018));
    else
        ltx->DrawLatex(0.565,0.93,Form("%d %.1f fb^{-1} (13TeV)", Year, lumi_2017));

    TLatex* ltx2 = new TLatex();
    ltx2->SetNDC();
    ltx2->SetTextFont(42);
    ltx2->SetTextSize(0.04);
    ltx2->DrawLatex(0.68,0.82,PUset);
    ltx2->DrawLatex(0.68,0.77,IDname+" ID");
    ltx2->DrawLatex(0.68,0.72,EleVetoType);
    system("mkdir -p PUcheck");
    c->SaveAs("PUcheck/"+outname+".png");
    c->SaveAs("PUcheck/"+outname+".pdf");

}

void DrawStack(vector<TH1F*> vhist, vector<TString> vLegend, int IDtype, int EleVetoSet, bool DoRatio, bool LogY, TString LegPos, int Year, TString XaxisName, TString YaxisName, TString outname)
{
    TString EleVetoType, IDname;
    if(EleVetoSet==1)
        EleVetoType="HasPix";
    else if(EleVetoSet==2)
        EleVetoType="CSEV";
    else
        EleVetoType="HasPix";

    if(IDtype==1)
        IDname="Loose";
    else if(IDtype==2)
        IDname="Medium";
    else if(IDtype==3)
        IDname="Tight";
    else if(IDtype==4)
        IDname="MVA";
    else
        IDname="Loose";

    setTDRStyle();

    TString Colorname[] = {"#700961","#e03e36","#ff7c38","#b80d57"};
    vector<TString> vColor(Colorname, Colorname + sizeof Colorname / sizeof Colorname[0]);

    TCanvas* c = new TCanvas("c1","",800,700);
    c->cd();
    TPad *Plot_Pad1;
    TPad *Plot_Pad2;
    if(DoRatio==true)
        Plot_Pad1 = new TPad("pad1","", 0, 0.38, 1, 1);
    else
        Plot_Pad1 = new TPad("pad1","", 0, 0, 1, 1);
    Plot_Pad1->SetRightMargin(0.05);
    Plot_Pad1->SetTopMargin(0.08);
    Plot_Pad1->SetLeftMargin(0.14);
    if(DoRatio==true) Plot_Pad1->SetBottomMargin(0.01);
    Plot_Pad1->Draw();
    Plot_Pad1->cd();
    if(LogY==true) Plot_Pad1->SetLogy();
    vhist[0]->Draw("PE1X0");
    if(DoRatio==false)
        vhist[0]->GetXaxis()->SetTitle(XaxisName);
    vhist[0]->GetXaxis()->SetTitleSize(0.06);
    vhist[0]->GetYaxis()->SetTitle(YaxisName);
    vhist[0]->GetYaxis()->SetTitleSize(0.06);
    vhist[0]->GetXaxis()->SetTickSize(0.03);
    vhist[0]->GetYaxis()->SetTickSize(0.03);
    vhist[0]->GetXaxis()->SetLabelSize(0.05);
    vhist[0]->GetYaxis()->SetLabelSize(0.05);
    vhist[0]->GetXaxis()->SetTitleOffset(1.);
    vhist[0]->GetYaxis()->SetTitleOffset(1.1);
    vhist[0]->SetMarkerStyle(20);
    vhist[0]->SetMarkerSize(0.5);
    vhist[0]->SetLineWidth(2);
    vhist[0]->SetLineColor(1);
    vhist[0]->SetMarkerColor(1);
    if(LogY==true)
        vhist[0]->GetYaxis()->SetRangeUser(0.5,vhist[0]->GetMaximum()*25.);
    else
        vhist[0]->GetYaxis()->SetRangeUser(0.,vhist[0]->GetMaximum()*2.);

    for(unsigned int i=1;i<vhist.size();i++)
    {
        //vhist[i]->SetFillColor(TColor::GetColor(vColor[i-1]));
        vhist[i]->SetLineColor(TColor::GetColor(vColor[i-1]));
        vhist[i]->SetLineWidth(2);
        vhist[i]->Draw("histsame");
    }
    TLatex* ltx = new TLatex();
    ltx->SetNDC();
    ltx->SetTextFont(61);
    ltx->SetTextSize(0.07);
    ltx->DrawLatex(0.14,0.93,"CMS");
    ltx->SetTextFont(52);
    ltx->SetTextSize(0.05);
    if(IsPreliminary==true) ltx->DrawLatex(0.24,0.93,"Preliminary");
    ltx->SetTextFont(42);
    ltx->SetTextSize(0.05);
    if(Year==2017)
        ltx->DrawLatex(0.71,0.93,Form("%d %.1f fb^{-1} (13TeV)", Year, lumi_2017));
    else if(Year==2018)
        ltx->DrawLatex(0.71,0.93,Form("%d %.1f fb^{-1} (13TeV)", Year, lumi_2018));
    else
        ltx->DrawLatex(0.71,0.93,Form("%d %.1f fb^{-1} (13TeV)", Year, lumi_2017));

    TLegend *l;
    if(LegPos.EqualTo("right"))
        l = new TLegend(0.65, 0.6, 0.89, 0.89);
    else if(LegPos.EqualTo("left"))
        l = new TLegend(0.2, 0.6, 0.44, 0.89);
    else
        l = new TLegend(0.65, 0.6, 0.89, 0.89);
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
    TLatex* ltx2 = new TLatex();
    ltx2->SetNDC();
    ltx2->SetTextFont(42);
    ltx2->SetTextSize(0.05);
    //ltx2->DrawLatex(0.65,0.83,EleVetoType+", "+IDname+" ID");
    if(LegPos.EqualTo("right"))
    {
        ltx2->DrawLatex(0.21,0.81,IDname+" ID");
        ltx2->DrawLatex(0.21,0.74,EleVetoType);
    }
    else if(LegPos.EqualTo("left"))
    {
        ltx2->DrawLatex(0.71,0.81,IDname+" ID");
        ltx2->DrawLatex(0.71,0.74,EleVetoType);
    }
    else
    {
        ltx2->DrawLatex(0.21,0.81,IDname+" ID");
        ltx2->DrawLatex(0.21,0.74,EleVetoType);
    }

    if(DoRatio==true)
    {
        vector<TH1F*> vhistratio; vhistratio.clear();
        for(unsigned int i=2;i<vhist.size();i++)
        {
            TH1F* tmphm;
            tmphm = (TH1F*) vhist[1]->Clone();
            tmphm->Add(vhist[i],-1);
            vhistratio.push_back(tmphm);
        }
        c->cd();
        Plot_Pad2 = new TPad("pad2", "", 0, 0, 1, 0.35);
        Plot_Pad2->SetRightMargin(0.05);
        Plot_Pad2->SetLeftMargin(0.14);
        Plot_Pad2->SetTopMargin(0.03);
        Plot_Pad2->SetBottomMargin(0.35);
        Plot_Pad2->Draw();
        Plot_Pad2->cd();
        //Plot_Pad2->SetLogy();
        Plot_Pad2->SetGridy();
        vhistratio[0]->GetYaxis()->SetTitle("Difference");
        vhistratio[0]->GetXaxis()->SetTitle(XaxisName);
        vhistratio[0]->GetYaxis()->SetTitleSize(0.13);
        vhistratio[0]->GetYaxis()->SetTitleOffset(0.5);
        vhistratio[0]->GetYaxis()->SetLabelSize(0.08);
        vhistratio[0]->GetYaxis()->SetRangeUser(-1000,1000);
        //vhistratio[0]->GetYaxis()->SetNdivisions(102);
        vhistratio[0]->GetXaxis()->SetTitleSize(0.15);
        vhistratio[0]->GetXaxis()->SetTitleOffset(1);
        vhistratio[0]->GetXaxis()->SetLabelSize(0.11);
        for(unsigned int i=0;i<vhistratio.size();i++)
        {
            vhistratio[i]->SetMarkerColor(TColor::GetColor(vColor[i+1]));
            //vhistratio[i]->SetMarkerSize(1.3);
            //vhistratio[i]->SetMarkerStyle(20);
            vhistratio[i]->SetLineColor(TColor::GetColor(vColor[i+1]));
            vhistratio[i]->SetLineWidth(3);
            if(i==0)
                vhistratio[i]->Draw("hist");
            else
                vhistratio[i]->Draw("histsame");
        }
        TLatex* ltx3 = new TLatex();
        ltx3->SetNDC();
        ltx3->SetTextFont(42);
        ltx3->SetTextSize(0.1);
        ltx3->DrawLatex(0.18,0.81,"Difference w.r.t PU-nominal");
    }
    system("mkdir -p PUcheck");
    c->SaveAs("PUcheck/"+outname+".png");
    c->SaveAs("PUcheck/"+outname+".pdf");
}

void Draw_PUcheck(int IDtype, int EleVetoSet)
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

    vector<TFile*> vFile; vFile.clear();
    vector<TH1F*> hM_Mmmg; hM_Mmmg.clear();
    vector<TH1F*> hM_Mmmg_PUup; hM_Mmmg_PUup.clear();
    vector<TH1F*> hM_Mmmg_PUdown; hM_Mmmg_PUdown.clear();
    vector<TH1F*> hM_nVtx; hM_nVtx.clear();
    vector<TH1F*> hM_nVtx_PUup; hM_nVtx_PUup.clear();
    vector<TH1F*> hM_nVtx_PUdown; hM_nVtx_PUdown.clear();

    vector<TH2F*> hM_nVtx_puwei; hM_nVtx_puwei.clear();
    vector<TH2F*> hM_nVtx_puweiup; hM_nVtx_puweiup.clear();
    vector<TH2F*> hM_nVtx_puweidown; hM_nVtx_puweidown.clear();

    for(unsigned int ifile=0;ifile<vfname.size();ifile++)
    {
        // cout << fname[ifile] << " " << vmcwei[ifile];
        hM_Mmmg.push_back(new TH1F("hM_Mmmg","",60,60,120));
        hM_Mmmg_PUup.push_back(new TH1F("hM_Mmmg_PUup","",60,60,120));
        hM_Mmmg_PUdown.push_back(new TH1F("hM_Mmmg_PUdown","",60,60,120));
        hM_nVtx.push_back(new TH1F("hM_nVtx","",120,0,120));
        hM_nVtx_PUup.push_back(new TH1F("hM_nVtx_PUup","",120,0,120));
        hM_nVtx_PUdown.push_back(new TH1F("hM_nVtx_PUdown","",120,0,120));

        vFile.push_back(new TFile(vfname[ifile],"READ"));
        TTree* Tree = (TTree*) vFile[ifile]->Get("outTree");
        // cout << " " << Tree->GetEntries("presel==1") << endl;
        float m_mmg;
        int nVtx;
        int presel, passID, passVeto;
        double puwei, puwei_up, puwei_down, mcwei, genwei;
        Tree->SetBranchAddress("m_mmg", &m_mmg);
        Tree->SetBranchAddress("nVtx", &nVtx);
        Tree->SetBranchAddress("presel", &presel);
        if(EleVetoSet==1)
            Tree->SetBranchAddress("phoHasPix", &passVeto);
        else if(EleVetoSet==2)
            Tree->SetBranchAddress("phoEleVeto", &passVeto);
        else
            Tree->SetBranchAddress("phoHasPix", &passVeto);

        if(IDtype==1)
            Tree->SetBranchAddress("looseID", &passID);
        else if(IDtype==2)
            Tree->SetBranchAddress("medID", &passID);
        else if(IDtype==3)
            Tree->SetBranchAddress("tightID", &passID);
        else if(IDtype==4)
            Tree->SetBranchAddress("passMVA_", &passID);
        else
            Tree->SetBranchAddress("looseID", &passID);

        if(ifile>0) Tree->SetBranchAddress("puwei", &puwei);
        if(ifile>0) Tree->SetBranchAddress("puwei_up", &puwei_up);
        if(ifile>0) Tree->SetBranchAddress("puwei_down", &puwei_down);
        if(ifile>0) Tree->SetBranchAddress("genwei", &genwei);

        int EleVeto_cut;
        if(EleVetoSet==1)
            EleVeto_cut = 0;
        else
            EleVeto_cut = 1;

        double evcount_passID_nom = 0., evcount_passVeto_nom = 0.;
        double evcount_passID_up = 0., evcount_passVeto_up = 0.;
        double evcount_passID_down = 0., evcount_passVeto_down = 0.;
        double evcount_DiffBetUpNom_positive = 0.;
        double evcount_DiffBetUpNom_negative = 0.;
        double evcount_DiffBetDownNom_positive = 0.;
        double evcount_DiffBetDownNom_negative = 0.;
        double puweisum = 0.;

        if(ifile==1)
        {
            hM_nVtx_puwei.push_back(new TH2F("hM_nVtx_puwei","",60,0,120,20,0,2));
            hM_nVtx_puweiup.push_back(new TH2F("hM_nVtx_puweiup","",60,0,120,20,0,2));
            hM_nVtx_puweidown.push_back(new TH2F("hM_nVtx_puweidown","",60,0,120,20,0,2));

            hM_nVtx_puwei.push_back(new TH2F("hM_nVtx_puwei","",60,0,120,20,0,2));
            hM_nVtx_puweiup.push_back(new TH2F("hM_nVtx_puweiup","",60,0,120,20,0,2));
            hM_nVtx_puweidown.push_back(new TH2F("hM_nVtx_puweidown","",60,0,120,20,0,2));
        }

        for(Long64_t ev=0; ev<Tree->GetEntriesFast(); ev++)
        {
            Tree->GetEntry(ev);

            if(ifile==0)
            {
                genwei=1.;
                puwei=1.;
                puwei_up = 1.;
                puwei_down = 1.;
            }

            if(presel != 1) continue;

            if(passID==1)
            {
                evcount_passID_nom = evcount_passID_nom + 1.*puwei*genwei*vmcwei[ifile];
                evcount_passID_up = evcount_passID_up + 1.*puwei_up*genwei*vmcwei[ifile];
                evcount_passID_down = evcount_passID_down + 1.*puwei_down*genwei*vmcwei[ifile];

                if(ifile==1)
                {
                    hM_nVtx_puwei[0]->Fill(nVtx,puwei);
                    hM_nVtx_puweiup[0]->Fill(nVtx,puwei_up);
                    hM_nVtx_puweidown[0]->Fill(nVtx,puwei_down);

                }

                if(passVeto==EleVeto_cut)
                {
                    evcount_passVeto_nom = evcount_passVeto_nom + 1.*puwei*genwei*vmcwei[ifile];
                    evcount_passVeto_up = evcount_passVeto_up + 1.*puwei_up*genwei*vmcwei[ifile];
                    evcount_passVeto_down = evcount_passVeto_down + 1.*puwei_down*genwei*vmcwei[ifile];
                    hM_Mmmg[ifile]->Fill(m_mmg,puwei*genwei*vmcwei[ifile]);
                    hM_Mmmg_PUup[ifile]->Fill(m_mmg,puwei_up*genwei*vmcwei[ifile]);
                    hM_Mmmg_PUdown[ifile]->Fill(m_mmg,puwei_down*genwei*vmcwei[ifile]);
                    hM_nVtx[ifile]->Fill(nVtx,puwei*genwei*vmcwei[ifile]);
                    hM_nVtx_PUup[ifile]->Fill(nVtx,puwei_up*genwei*vmcwei[ifile]);
                    hM_nVtx_PUdown[ifile]->Fill(nVtx,puwei_down*genwei*vmcwei[ifile]);

                    if(ifile==1)
                    {
                        hM_nVtx_puwei[1]->Fill(nVtx,puwei);
                        hM_nVtx_puweiup[1]->Fill(nVtx,puwei_up);
                        hM_nVtx_puweidown[1]->Fill(nVtx,puwei_down);

                        puweisum = puweisum + puwei;
                        if(puwei_up-puwei > 0)
                            evcount_DiffBetUpNom_positive = evcount_DiffBetUpNom_positive + (puwei_up-puwei);
                        else
                            evcount_DiffBetUpNom_negative = evcount_DiffBetUpNom_negative + (puwei_up-puwei);

                        if(puwei_down-puwei > 0)
                            evcount_DiffBetDownNom_positive = evcount_DiffBetDownNom_positive + (puwei_down-puwei);
                        else
                            evcount_DiffBetDownNom_negative = evcount_DiffBetDownNom_negative + (puwei_down-puwei);
                    }
                }
            }
            else
                continue;
        }
        if(ifile==0 || ifile==1)
        {
            std::cout << std::setprecision(6) << std::fixed;
            cout << "ID type = " << IDtype << " Veto type = " << EleVetoSet << endl
            << "(Nominal) # of evets passing ID = " << evcount_passID_nom << "; # of evets passing Veto = " << evcount_passVeto_nom << "; Effciency = " << (double) evcount_passVeto_nom/evcount_passID_nom * 100. << endl
            << "(Up) # of evets passing ID = " << evcount_passID_up << "; # of evets passing Veto = " << evcount_passVeto_up << "; Effciency = " << (double) evcount_passVeto_up/evcount_passID_up * 100. << endl
            << "(Down) # of evets passing ID = " << evcount_passID_down << "; # of evets passing Veto = " << evcount_passVeto_down << "; Effciency = " << (double) evcount_passVeto_down/evcount_passID_down * 100. << endl
            <<endl;

            if(ifile==1)
            {
                cout << "nominal puweisum = " << puweisum << endl
                << "evcount_DiffBetUpNom_positive = " << evcount_DiffBetUpNom_positive << endl
                << "evcount_DiffBetUpNom_negative = " << evcount_DiffBetUpNom_negative << endl
                << "evcount_DiffBetDownNom_positive = " << evcount_DiffBetDownNom_positive << endl
                << "evcount_DiffBetDownNom_negative = " << evcount_DiffBetDownNom_negative << endl
                << endl;
            }
        }
    }

    // for(unsigned int i=2;i<vfname.size();i++)
    // {
    //     hM_Mmmg[1]->Add(hM_Mmmg[i]);
    //     hM_Mmmg_PUup[1]->Add(hM_Mmmg_PUup[i]);
    //     hM_Mmmg_PUdown[1]->Add(hM_Mmmg_PUdown[i]);
    // }

    vector<TH1F*> vHistToDraw; vHistToDraw.clear();
    vHistToDraw.push_back(hM_Mmmg[0]);
    vHistToDraw.push_back(hM_Mmmg[1]);
    vHistToDraw.push_back(hM_Mmmg_PUup[1]);
    vHistToDraw.push_back(hM_Mmmg_PUdown[1]);

    TString Legendentry[] = {"Data","MC (PU nominal)","MC (PU up)","MC (PU down)"};
    vector<TString> vLegEntry(Legendentry, Legendentry + sizeof Legendentry / sizeof Legendentry[0]);

    //DrawStack(vector<TH1F*> vhist, vector<TString> vLegend, int IDtype, int EleVetoSet, bool DoRatio, bool LogY, TString LegPos, int Year, TString XaxisName, TString YaxisName, TString outname)
    DrawStack(vHistToDraw, vLegEntry, IDtype, EleVetoSet, true, true, "right", 2017, "M_{#mu#mu#gamma} (GeV)", Form("Events / %.1f GeV",(float) hM_Mmmg[0]->GetBinWidth(5)), Form("Mmmg_PUcheck_IDtype%d_EleVetoSet%d",IDtype,EleVetoSet));

    vHistToDraw.clear();
    vHistToDraw.push_back(hM_nVtx[0]);
    vHistToDraw.push_back(hM_nVtx[1]);
    vHistToDraw.push_back(hM_nVtx_PUup[1]);
    vHistToDraw.push_back(hM_nVtx_PUdown[1]);
    DrawStack(vHistToDraw, vLegEntry, IDtype, EleVetoSet, true, true, "right", 2017, "Number of vertices", "Entries", Form("nVtx_PUcheck_IDtype%d_EleVetoSet%d",IDtype,EleVetoSet));

    //Draw2DEffHist(vector<TH2F*> vhist, int putype, int IDtype, int EleVetoSet, int Year, const char* XaxisName, const char* YaxisName, const char* outname)
    Draw2DEffHist(hM_nVtx_puwei, 1, IDtype, EleVetoSet, 2017, "Number of vertices", "Pile-up weight (Nominal)", Form("nVtxPUwei2D_Nominal_IDtype%d_EleVetoSet%d",IDtype,EleVetoSet));
    Draw2DEffHist(hM_nVtx_puweiup, 2, IDtype, EleVetoSet, 2017, "Number of vertices", "Pile-up weight (Up)", Form("nVtxPUwei2D_Up_IDtype%d_EleVetoSet%d",IDtype,EleVetoSet));
    Draw2DEffHist(hM_nVtx_puweidown, 3, IDtype, EleVetoSet, 2017, "Number of vertices", "Pile-up weight (Down)", Form("nVtxPUwei2D_Down_IDtype%d_EleVetoSet%d",IDtype,EleVetoSet));
}
