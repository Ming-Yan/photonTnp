#include "plugins/tdrstyle.C"
#include "plugins/Utilities.h"

bool IsPreliminary = true;

float mcwei_DYJetsToLL_aMCatNLO = (5943200.*42.5)/(112669192.+10915332.);
float mcwei_ttbarTo2L2Nu_powheg = (72100.*42.5)/8634992.;
float mcwei_DYJetsToLL_MadGraph = (14420.*1000.*42.5)/(48632630.+49082157.);
float mcwei_Ztomumu_powheg = 1.;
float mcwei_Wjets_aMCatNLO = (56000.*1000.*42.5)/(33043732.+44587448.);

float lumi_2017 = 42.5;
float lumi_2018 = 42.5;

double Binomial_Error(double eff, double N)
{
    double error;
    error = sqrt(eff*(1.-eff)/N);
    return error;
}

double Error_Propagation(double f, double sigmaA, double A, double sigmaB, double B)
{
    double error;
    error = f * sqrt((sigmaA/A)*(sigmaA/A)+(sigmaB/B)*(sigmaB/B));
    return error;
}

void Draw_1DEff(vector<TH1F*> h_den, vector<TH1F*> h_num, int Year, int MCset, int IDtype, int EleVetoSet, int CatNum, const char* puweiset, const char* XaxisName, float y_down, float y_up, const char* outname)
{
    gStyle->SetOptStat(0);

    TString EleVetoType, IDname, MCname, Catname, PUset;
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

    if(MCset==11)
        MCname="MG DY+jets";
    else if(MCset==12)
        MCname="MG DY+jets & powheg t#bar{t}";
    else if(MCset==13)
        MCname="MG DY+jets & aMC@NLO W+jets";
    else if(MCset==21)
        MCname="aMC@NLO DY+jets";
    else if(MCset==31)
        MCname="powheg Z#rightarrow#mu#mu";

    if(CatNum==1)
        Catname="EB Inclusive";
    else if(CatNum==2)
        Catname="EE Inclusive";
    else if(CatNum==3)
        Catname="EB high R_{9}";
    else if(CatNum==4)
        Catname="EB low R_{9}";
    else if(CatNum==5)
        Catname="EE high R_{9}";
    else if(CatNum==6)
        Catname="EE low R_{9}";
    else
        Catname="EB Inclusive";

    if(strcoll(puweiset,"Nominal")==0)
        PUset="PU weight - Nominal";
    else if(strcoll(puweiset,"up")==0)
        PUset="PU weight - Up";
    else if(strcoll(puweiset,"down")==0)
        PUset="PU weight - Down";
    else
        PUset="PU weight - Nominal";

    TCanvas* c = new TCanvas("c","",800,700);
    c->cd();
    TPad *Plot_Pad1;
    TPad *Plot_Pad2;
    Plot_Pad1 = new TPad("pad1","", 0, 0.30, 1, 1);
    Plot_Pad1->SetRightMargin(0.05);
    Plot_Pad1->SetTopMargin(0.08);
    Plot_Pad1->SetLeftMargin(0.13);
    Plot_Pad1->SetBottomMargin(0.03);
    Plot_Pad1->Draw();
    Plot_Pad1->cd();
    TH1F *Eff_data;
    Eff_data = (TH1F*) h_num[0]->Clone();
    Eff_data->Divide(h_den[0]);
    TH1F *Eff_mc;
    if(h_den.size()==2)
    {
        Eff_mc = (TH1F*) h_num[1]->Clone();
        Eff_mc->Divide(h_den[1]);
    }
    if(h_den.size()>2)
    {
        for(unsigned int i=2;i<h_den.size();i++)
        {
            h_den[1]->Add(h_den[i]);
            h_num[1]->Add(h_num[i]);
        }
        Eff_mc = (TH1F*) h_num[1]->Clone();
        Eff_mc->Divide(h_den[1]);
    }

    TGraphAsymmErrors *efferr_data = new TGraphAsymmErrors();
    efferr_data->BayesDivide(h_num[0],h_den[0]);
    TGraphAsymmErrors *efferr_mc = new TGraphAsymmErrors();
    efferr_mc->BayesDivide(h_num[1],h_den[1]);
    efferr_data->GetYaxis()->SetTitle("Efficiency");
    double ymin_data, ymax_data, ymin_mc, ymax_mc;
    Eff_data->GetMinimumAndMaximum(ymin_data,ymax_data);
    Eff_mc->GetMinimumAndMaximum(ymin_mc,ymax_mc);
    //efferr_data->GetYaxis()->SetRangeUser((ymin_data<ymin_mc) ? ymin_data-y_down : ymin_mc-y_down, (ymax_data>ymax_mc) ? ymax_data+y_up : ymax_mc+y_up);
    efferr_data->GetYaxis()->SetRangeUser(0.15, 1.3);
    efferr_data->GetXaxis()->SetRangeUser(Eff_data->GetBinLowEdge(1),Eff_data->GetBinCenter(Eff_data->GetNbinsX())+(Eff_data->GetBinCenter(Eff_data->GetNbinsX())-Eff_data->GetBinLowEdge(Eff_data->GetNbinsX())));
    efferr_data->GetYaxis()->SetTickSize(0.03);
    efferr_data->GetYaxis()->SetTitleSize(0.06);
    efferr_data->GetYaxis()->SetLabelSize(0.05);
    efferr_data->GetYaxis()->SetTitleOffset(1.0);
    efferr_data->GetXaxis()->SetTickSize(0.03);
    efferr_data->GetXaxis()->SetTitleSize(0.0);
    efferr_data->GetXaxis()->SetLabelSize(0.0);
    efferr_data->SetMarkerColor(TColor::GetColor("#233142"));
    efferr_data->SetMarkerSize(1.5);
    efferr_data->SetMarkerStyle(20);
    efferr_data->SetLineColor(TColor::GetColor("#233142"));
    efferr_data->SetLineWidth(2);
    efferr_data->Draw("AP");
    efferr_mc->SetMarkerColor(TColor::GetColor("#f95959"));
    efferr_mc->SetMarkerSize(1.5);
    efferr_mc->SetMarkerStyle(20);
    efferr_mc->SetLineColor(TColor::GetColor("#f95959"));
    efferr_mc->SetLineWidth(2);
    efferr_mc->Draw("Psame");
    TLatex* ltx = new TLatex();
    ltx->SetNDC();
    ltx->SetTextFont(61);
    ltx->SetTextSize(0.07);
    ltx->DrawLatex(0.13,0.93,"CMS");
    ltx->SetTextFont(52);
    ltx->SetTextSize(0.05);
    if(IsPreliminary==true) ltx->DrawLatex(0.24,0.93,"Preliminary");
    ltx->SetTextFont(42);
    ltx->SetTextSize(0.05);
    if(Year==2017)
        ltx->DrawLatex(0.68,0.93,Form("%d %.1f fb^{-1} (13TeV)", Year, lumi_2017));
    else if(Year==2018)
        ltx->DrawLatex(0.68,0.93,Form("%d %.1f fb^{-1} (13TeV)", Year, lumi_2018));
    else
        ltx->DrawLatex(0.68,0.93,Form("%d %.1f fb^{-1} (13TeV)", Year, lumi_2017));
    float binpos1 = Eff_data->GetBinContent(Eff_data->GetNbinsX()-1);
    float binpos2 = Eff_mc->GetBinContent(Eff_data->GetNbinsX()-1);
    float binpos = (binpos1>binpos2) ? binpos1 : binpos2;
    TLegend *l = new TLegend(0.18, 0.71, 0.77, 0.89);
    l->SetHeader(Catname+", "+EleVetoType+", "+IDname+" ID","L");
    l->SetNColumns(2);
    l->AddEntry(efferr_data, "Data","lep");
    l->AddEntry(efferr_mc, "Simulation","lep");
    l->SetFillColor(0); //Set the background to be white
    l->SetLineColor(1);
    l->Draw("same");
    TLatex* ltx2 = new TLatex();
    ltx2->SetNDC();
    ltx2->SetTextFont(42);
    ltx2->SetTextSize(0.04);
    //ltx2->DrawLatex(0.65,0.83,EleVetoType+", "+IDname+" ID");
    ltx2->DrawLatex(0.71,0.81,MCname);
    ltx2->DrawLatex(0.71,0.76,PUset);
    c->cd();

    Plot_Pad2 = new TPad("pad2", "", 0, 0, 1, 0.27);
    Plot_Pad2->SetRightMargin(0.05);
    Plot_Pad2->SetLeftMargin(0.13);
    Plot_Pad2->SetTopMargin(0.03);
    Plot_Pad2->SetBottomMargin(0.35);
    Plot_Pad2->Draw();
    Plot_Pad2->cd();
    Plot_Pad2->SetGridy();
    TH1F *h_ratio = (TH1F*) Eff_data->Clone();
    h_ratio->Divide(Eff_mc);
    int Nbins = h_ratio->GetNbinsX();
    double x[Nbins], y[Nbins], ex[Nbins], ey[Nbins];
    for(int i=0; i<Nbins; i++)
    {
        x[i] = h_ratio->GetBinCenter(i+1);
        y[i] = h_ratio->GetBinContent(i+1);
        ex[i] = fabs(h_ratio->GetBinCenter(i+1) - h_ratio->GetBinLowEdge(i+1));
        ey[i] = Error_Propagation(h_ratio->GetBinContent(i+1),
                                    Binomial_Error(Eff_data->GetBinContent(i+1),h_den[0]->GetBinContent(i+1)), Eff_data->GetBinContent(i+1),
                                    Binomial_Error(Eff_mc->GetBinContent(i+1),h_den[1]->GetBinContent(i+1)), Eff_mc->GetBinContent(i+1));
    }
    TGraphErrors *Err_Ratio = new TGraphErrors(Nbins,x,y,ex,ey);
    Err_Ratio->GetYaxis()->SetTitle("Scale factor");
    Err_Ratio->GetXaxis()->SetTitle(XaxisName);
    Err_Ratio->GetYaxis()->SetTitleSize(0.14);
    Err_Ratio->GetYaxis()->SetTitleOffset(0.3);
    Err_Ratio->GetYaxis()->SetLabelSize(0.11);
    Err_Ratio->GetYaxis()->SetRangeUser(0.8,1.2);
    Err_Ratio->GetXaxis()->SetRangeUser(Eff_data->GetBinLowEdge(1),Eff_data->GetBinCenter(Eff_data->GetNbinsX())+(Eff_data->GetBinCenter(Eff_data->GetNbinsX())-Eff_data->GetBinLowEdge(Eff_data->GetNbinsX())));
    Err_Ratio->GetYaxis()->SetNdivisions(502);
    Err_Ratio->GetXaxis()->SetTitleSize(0.16);
    Err_Ratio->GetXaxis()->SetTitleOffset(1.0);
    Err_Ratio->GetXaxis()->SetLabelSize(0.13);
    Err_Ratio->SetMarkerColor(1);
    Err_Ratio->SetMarkerSize(1.5);
    Err_Ratio->SetMarkerStyle(20);
    Err_Ratio->SetLineColor(1);
    Err_Ratio->SetLineWidth(2);
    Err_Ratio->Draw("AP");
    c->SaveAs(Form("plots/MCset%d/%s_EleVetoSet%d_IDSet%d_MCset%d_CatSet%d_PU%s.png",MCset,outname,EleVetoSet,IDtype,MCset,CatNum,puweiset));
    c->SaveAs(Form("plots/MCset%d/%sEleVetoSet%d_IDSet%d_MCset%d_CatSet%d_PU%s.pdf",MCset,outname
    ,EleVetoSet,IDtype,MCset,CatNum,puweiset));

    TFile* fout = new TFile(Form("histfiles/%s_EleVetoSet%d_IDSet%d_MCset%d_CatSet%d_PU%s.root",outname,EleVetoSet,IDtype,MCset,CatNum,puweiset),"RECREATE");
    fout->cd();
    Eff_data->SetName("Eff_data");
    Eff_data->Write();
    Eff_mc->SetName("Eff_mc");
    Eff_mc->Write();
    efferr_data->SetName("efferr_data");
    efferr_data->Write();
    efferr_mc->SetName("efferr_mc");
    efferr_mc->Write();
    h_ratio->SetName("h_ratio");
    h_ratio->Write();
    Err_Ratio->SetName("Err_Ratio");
    Err_Ratio->Write();
    fout->Close("R");
    fout->Delete("*;*");
}

void getHist(int Year, int MCset, int IDtype, int EleVetoSet, int CatNum, const char* puweiset)
{
    setTDRStyle();

    int EleVeto_cut;
    if(EleVetoSet==1)
        EleVeto_cut = 0;
    else
        EleVeto_cut = 1;

    vector<float> vmcwei; vmcwei.clear();
    vector<TFile*> vFile; vFile.clear();
    vFile.push_back(new TFile("minitree/minitree_DoubleMu_AllRuns.root"));
    vmcwei.push_back(1.);
    if(MCset == 11)
    {
        vFile.push_back(new TFile("minitree/minitree_DYJetsToLL_MadGraph.root"));
        vmcwei.push_back(mcwei_DYJetsToLL_MadGraph);
    }
    else if(MCset == 12)
    {
        vFile.push_back(new TFile("minitree/minitree_DYJetsToLL_MadGraph.root"));
        vmcwei.push_back(mcwei_DYJetsToLL_MadGraph);
        vFile.push_back(new TFile("minitree/minitree_TTTo2L2Nu_powheg.root"));
        vmcwei.push_back(mcwei_ttbarTo2L2Nu_powheg);
    }
    else if(MCset == 13)
    {
        vFile.push_back(new TFile("minitree/minitree_DYJetsToLL_MadGraph.root"));
        vmcwei.push_back(mcwei_DYJetsToLL_MadGraph);
        vFile.push_back(new TFile("minitree/minitree_Wjets_aMCatNLO.root"));
        vmcwei.push_back(mcwei_Wjets_aMCatNLO);
    }
    else if(MCset == 21)
    {
        vFile.push_back(new TFile("minitree/minitree_DYJetsToLL_aMCatNLO.root"));
        vmcwei.push_back(mcwei_DYJetsToLL_aMCatNLO);
    }
    else if(MCset == 31)
    {
        vFile.push_back(new TFile("minitree/minitree_ZTomumu_powheg.root"));
        vmcwei.push_back(mcwei_Ztomumu_powheg);
    }
    else // Use Nominal one
    {
        vFile.push_back(new TFile("minitree/minitree_DYJetsToLL_MadGraph.root"));
        vmcwei.push_back(mcwei_DYJetsToLL_MadGraph);
    }

    vector<TH1F*> hM_phoEt_den; hM_phoEt_den.clear();
    vector<TH1F*> hM_phoEt_num; hM_phoEt_num.clear();
    vector<TH1F*> hM_nVtx_den; hM_nVtx_den.clear();
    vector<TH1F*> hM_nVtx_num; hM_nVtx_num.clear();

    float phoEt_bin[6] = {10,15,25,40,60,100};
    float nVtx_bin[11] = {0,10,15,20,25,30,35,40,50,65,100};

    for(unsigned int iFile=0;iFile<vFile.size();iFile++)
    {
        hM_phoEt_den.push_back(new TH1F("hM_phoEt_den","",5,phoEt_bin));
        hM_phoEt_num.push_back(new TH1F("hM_phoEt_num","",5,phoEt_bin));
        hM_nVtx_den.push_back(new TH1F("hM_nVtx_den","",10,nVtx_bin));
        hM_nVtx_num.push_back(new TH1F("hM_nVtx_num","",10,nVtx_bin));

        TTree *Tree  = (TTree*) vFile[iFile]->Get("outTree");
        float phoCalibEt, phoSCEta, phoR9, m_mmg;
        int nVtx;
        int presel;
        int passVeto, passID;
        double puwei, puwei_up, puwei_down;
        Tree->SetBranchAddress("phoCalibEt", &phoCalibEt);
        Tree->SetBranchAddress("phoSCEta", &phoSCEta);
        Tree->SetBranchAddress("phoR9", &phoR9);
        Tree->SetBranchAddress("m_mmg", &m_mmg);
        Tree->SetBranchAddress("nVtx", &nVtx);
        Tree->SetBranchAddress("presel", &presel);

        if(EleVetoSet==1)
            Tree->SetBranchAddress("phoHasPix", &passVeto);
        else if(EleVetoSet==2)
            Tree->SetBranchAddress("phoEleVeto", &passVeto);
        else
        {
            cout << "No such EleVeto set!! Please check!!" << endl
                << "Use the default : HasPix !!" << endl;
            Tree->SetBranchAddress("phoHasPix", &passVeto);
        }

        if(IDtype==1)
            Tree->SetBranchAddress("looseID", &passID);
        else if(IDtype==2)
            Tree->SetBranchAddress("medID", &passID);
        else if(IDtype==3)
            Tree->SetBranchAddress("tightID", &passID);
        else if(IDtype==4)
            Tree->SetBranchAddress("passMVA_", &passID);
        else
        {
            cout << "No such photon ID set!! Please check!!" << endl
                << "Use the default : Loose ID !!" << endl;
            Tree->SetBranchAddress("looseID", &passID);
        }

        if(iFile==0)
            puwei=1.;
        else
        {
            if(strcoll(puweiset,"Nominal")==0)
                Tree->SetBranchAddress("puwei", &puwei);
            else if(strcoll(puweiset,"up")==0)
                Tree->SetBranchAddress("puwei_up", &puwei);
            else if(strcoll(puweiset,"down")==0)
                Tree->SetBranchAddress("puwei_down", &puwei);
            else
                Tree->SetBranchAddress("puwei", &puwei);
        }

        for(Long64_t ev=0; ev<Tree->GetEntriesFast(); ev++)
        {
            Tree->GetEntry(ev);

            // All the events should pass photon preselection (medium WP)
            if(presel != 1) continue;

            if(CatNum == 1) // EB Inclusive
            {
                if(fabs(phoSCEta)>1.4442) continue;
            }
            else if(CatNum == 2) // EE Inclusive
            {
                if(fabs(phoSCEta)<1.566 || fabs(phoSCEta)>2.5) continue;
            }
            else if(CatNum == 3) // EB HR9
            {
                if(fabs(phoSCEta)>1.4442 || phoR9<0.94) continue;
            }
            else if(CatNum == 4) // EB LR9
            {
                if(fabs(phoSCEta)>1.444 || phoR9>0.94) continue;
            }
            else if(CatNum == 5) // EE HR9
            {
                if(fabs(phoSCEta)<1.566 || fabs(phoSCEta)>2.5 || phoR9<0.94) continue;
            }
            else if(CatNum == 6) // EE LR9
            {
                if(fabs(phoSCEta)<1.566 || fabs(phoSCEta)>2.5 || phoR9>0.94) continue;
            }
            else
            {
                cout << "No Such category!! Please check!!" << endl
                    << "Use default category : EB Inclusive !!" << endl;
                if(fabs(phoSCEta)>1.4442) continue;
            }

            if(passID==1)
            {
                hM_phoEt_den[iFile]->Fill(phoCalibEt,vmcwei[iFile]*puwei);
                hM_nVtx_den[iFile]->Fill(nVtx,vmcwei[iFile]*puwei);
                if(passVeto==EleVeto_cut)
                {
                    hM_phoEt_num[iFile]->Fill(phoCalibEt,vmcwei[iFile]*puwei);
                    hM_nVtx_num[iFile]->Fill(nVtx,vmcwei[iFile]*puwei);
                }
            }
            else
                continue;
        }
    }
    Draw_1DEff(hM_phoEt_den, hM_phoEt_num, Year, MCset, IDtype, EleVetoSet, CatNum, puweiset, "Photon p_{T} (GeV)", 0.25, 0.3, "EffphoEt");
    Draw_1DEff(hM_nVtx_den, hM_nVtx_num, Year, MCset, IDtype, EleVetoSet, CatNum, puweiset, "Number of vertices", 0.23, 0.25, "EffnVtx");

    for(unsigned int ifile=0;ifile<vFile.size();ifile++)
    {
        vFile[ifile]->Close("R");
        vFile[ifile]->Delete("*;*");
    }
    vFile.clear();
}

void MakeSimpleHist(int year=2017)
{
    // MC set number
    // 11 : MG DY+jets & no background (Nominal)
    // 12 : MG DY+jets & powheg TT (Syst. Uncer.)
    // 13 : MG DY+jets & aMC@NLO W + jets (Syst. Uncer.)
    // 21 : aMC@NLO DY+jets (Syst. Uncer.)
    // 31 : powheg Z->μμ (Syst. Uncer.)

    // IDtype
    // 1 : loose
    // 2 : medium
    // 3 : tight
    // 4 : MVA ID

    // EleVeto set number
    // 1 : pixel seed
    // 2 : CSEV

    // Category number
    // 1 : EB Inclusive
    // 2 : EE Inclusive
    // 3 : EB HR9
    // 4 : EB LR9
    // 5 : EE HR9
    // 6 : EE LR9

    int MCsetArr[5] = {11,12,13,21,31};
    //getHist(int MCset, int IDtype, int EleVetoSet, int CatNum, const char* puweiset)
    for(int iMC=0;iMC<4;iMC++)
    {
        for(int iID=0;iID<4;iID++)
        {
            for(int iEleVeto=0;iEleVeto<2;iEleVeto++)
            {
                for(int iCat=0;iCat<6;iCat++)
                {
                    getHist(year, MCsetArr[iMC], iID+1, iEleVeto+1, iCat+1, "Nominal");
                    getHist(year, MCsetArr[iMC], iID+1, iEleVeto+1, iCat+1, "up");
                    getHist(year, MCsetArr[iMC], iID+1, iEleVeto+1, iCat+1, "down");
                }
            }
        }
    }
}
