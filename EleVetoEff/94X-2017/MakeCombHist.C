#include "plugins/tdrstyle.C"
#include "plugins/Utilities.h"

float mcwei_DYJetsToLL_aMCatNLO = (5943200.*42.5)/(112669192.+10915332.);
float mcwei_ttbarTo2L2Nu_powheg = (72100.*42.5)/8634992.;
float mcwei_DYJetsToLL_MadGraph = (14420000.*42.5)/(48632630.+49082157.);
float mcwei_Ztomumu_powheg = 1.;
float mcwei_Wjets_aMCatNLO = (56000.*1000.*42.5)/(33043732.+44587448.);

// float mcwei_DYJetsToLL_aMCatNLO = 1.;
// float mcwei_ttbarTo2L2Nu_powheg = 1.;
// float mcwei_DYJetsToLL_MadGraph = 1.;
// float mcwei_Ztomumu_powheg = 1.;
// float mcwei_Wjets_aMCatNLO = 1.;

float lumi_2017 = 42.5;
float lumi_2018 = 42.5;

bool IsPreliminary = true;

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

void DrawHist(int Year, int EleVetoSet, vector<TH1F*> vHist, vector<TH1F*> vHist_ratio, vector<TString> vLegEntry)
{
    setTDRStyle();

    TString ColorCode[6] = {"#00a8b5", "#f07b3f", "#e62a76", "#774898","#851e52","#521168"};
    TString VetoHeaderText[2] = {"Pixel seed veto", "Conversion safe veto"};
    TString VetoOutText[2] = {"PixelSeed","CSEV"};

    float RangeLow_SF, RangeHigh_SF, RangeLow_Ratio, RangeHigh_Ratio;
    if(EleVetoSet==1)
    {
        RangeLow_SF = 0.86;
        RangeHigh_SF = 1.05;
        RangeLow_Ratio = 0.99;
        RangeHigh_Ratio = 1.01;
    }
    else
    {
        RangeLow_SF = 0.86;
        RangeHigh_SF = 1.05;
        RangeLow_Ratio = 0.99;
        RangeHigh_Ratio = 1.01;
    }

    TCanvas *c = new TCanvas("c","",1000,900);
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
    vHist[0]->GetYaxis()->SetRangeUser(RangeLow_SF, RangeHigh_SF);
    vHist[0]->GetYaxis()->SetTitle("Scale factor");
    vHist[0]->GetYaxis()->SetTickSize(0.03);
    vHist[0]->GetYaxis()->SetTitleSize(0.06);
    vHist[0]->GetYaxis()->SetLabelSize(0.05);
    vHist[0]->GetYaxis()->SetTitleOffset(1.0);
    vHist[0]->GetXaxis()->SetTickSize(0.03);
    vHist[0]->GetXaxis()->SetTitleSize(0.0);
    vHist[0]->GetXaxis()->SetLabelSize(0.0);
    vHist[0]->SetMarkerColor(TColor::GetColor(ColorCode[0].Data()));
    vHist[0]->SetMarkerSize(2.5);
    vHist[0]->SetMarkerStyle(20);
    vHist[0]->SetLineColor(TColor::GetColor(ColorCode[0].Data()));
    vHist[0]->SetLineWidth(4);
    vHist[0]->Draw("PE1X0");
    for(unsigned int i=1;i<vHist.size();i++)
    {
        vHist[i]->SetMarkerColor(TColor::GetColor(ColorCode[i].Data()));
        vHist[i]->SetMarkerSize(2.5);
        vHist[i]->SetMarkerStyle(20);
        vHist[i]->SetLineColor(TColor::GetColor(ColorCode[i].Data()));
        vHist[i]->SetLineWidth(4);
        vHist[i]->Draw("PE1X0same");
    }
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
        ltx->DrawLatex(0.67,0.93,Form("%d %.1f fb^{-1} (13TeV)", Year, lumi_2017));
    else if(Year==2018)
        ltx->DrawLatex(0.67,0.93,Form("%d %.1f fb^{-1} (13TeV)", Year, lumi_2018));
    else
        ltx->DrawLatex(0.67,0.93,Form("%d %.1f fb^{-1} (13TeV)", Year, lumi_2017));
    TLegend *l = new TLegend(0.47, 0.68, 0.89, 0.89);
    l->SetHeader(VetoHeaderText[EleVetoSet-1],"L");
    l->SetNColumns(2);
    for(unsigned int i=0;i<vHist.size();i++)
    {
        l->AddEntry(vHist[i], vLegEntry[i],"lep");
    }
    l->SetFillColor(0); //Set the background to be white
    l->SetLineColor(1);
    l->Draw("same");
    c->cd();

    Plot_Pad2 = new TPad("pad2", "", 0, 0, 1, 0.26);
    Plot_Pad2->SetRightMargin(0.05);
    Plot_Pad2->SetLeftMargin(0.13);
    Plot_Pad2->SetTopMargin(0.03);
    Plot_Pad2->SetBottomMargin(0.35);
    Plot_Pad2->Draw();
    Plot_Pad2->cd();
    Plot_Pad2->SetGridy();
    vHist_ratio[0]->GetYaxis()->SetTitle("Cut-based/MVA");
    vHist_ratio[0]->GetXaxis()->CenterTitle();
    //vHist_ratio[0]->GetXaxis()->SetTitle(XaxisName);
    vHist_ratio[0]->GetYaxis()->SetTitleSize(0.12);
    vHist_ratio[0]->GetYaxis()->SetTitleOffset(0.5);
    vHist_ratio[0]->GetYaxis()->SetLabelSize(0.13);
    vHist_ratio[0]->GetYaxis()->SetRangeUser(RangeLow_Ratio,RangeHigh_Ratio);
    vHist_ratio[0]->GetYaxis()->SetNdivisions(502);
    vHist_ratio[0]->GetXaxis()->SetTitleSize(0.16);
    vHist_ratio[0]->GetXaxis()->SetTitleOffset(1.0);
    vHist_ratio[0]->GetXaxis()->SetLabelSize(0.17);
    vHist_ratio[0]->SetMarkerColor(TColor::GetColor(ColorCode[0].Data()));
    vHist_ratio[0]->SetMarkerSize(1.5);
    vHist_ratio[0]->SetMarkerStyle(20);
    vHist_ratio[0]->SetLineColor(TColor::GetColor(ColorCode[0].Data()));
    vHist_ratio[0]->SetLineWidth(2);
    vHist_ratio[0]->Draw("Phist");
    for(unsigned int i=0; i<vHist_ratio.size(); i++)
    {
        vHist_ratio[i]->SetMarkerColor(TColor::GetColor(ColorCode[i].Data()));
        vHist_ratio[i]->SetMarkerSize(1.5);
        vHist_ratio[i]->SetMarkerStyle(20);
        vHist_ratio[i]->SetLineColor(TColor::GetColor(ColorCode[i].Data()));
        vHist_ratio[i]->SetLineWidth(2);
        vHist_ratio[i]->Draw("Phistsame");
    }

    c->SaveAs("plots/CombHist_"+VetoOutText[EleVetoSet-1]+".png");
    c->SaveAs("plots/CombHist_"+VetoOutText[EleVetoSet-1]+".pdf");

    for(unsigned int i=1;i<vHist.size();i++)
    {
        vHist[i]->Add(vHist[0],-1);
        vHist[i]->Scale(100.);
    }
    TCanvas *c1 = new TCanvas("c1","",1000,900);
    gStyle->SetErrorX(0);
    // gStyle->SetErrorY(0);
    c1->cd();
    c1->SetRightMargin(0.05);
    c1->SetTopMargin(0.08);
    c1->SetLeftMargin(0.13);
    c1->SetBottomMargin(0.1);
    vHist[1]->GetYaxis()->SetRangeUser(-1,1);
    vHist[1]->GetYaxis()->SetTitle("Difference w.r.t loose ID (%)");
    vHist[1]->GetYaxis()->SetTickSize(0.03);
    vHist[1]->GetYaxis()->SetTitleSize(0.05);
    vHist[1]->GetYaxis()->SetLabelSize(0.04);
    vHist[1]->GetYaxis()->SetTitleOffset(1.2);
    vHist[1]->GetXaxis()->SetTickSize(0.03);
    vHist[1]->GetXaxis()->SetLabelSize(0.05);
    vHist[1]->SetMarkerColor(TColor::GetColor(ColorCode[1].Data()));
    vHist[1]->SetMarkerSize(2.5);
    vHist[1]->SetMarkerStyle(20);
    vHist[1]->Draw("histP");
    for(unsigned int i=2;i<vHist.size();i++)
    {
        vHist[i]->SetMarkerColor(TColor::GetColor(ColorCode[i].Data()));
        vHist[i]->SetMarkerSize(2.5);
        vHist[i]->SetMarkerStyle(20);
        vHist[i]->Draw("histPsame");
    }
    TLegend *l2 = new TLegend(0.47, 0.68, 0.89, 0.89);
    l2->SetHeader(VetoHeaderText[EleVetoSet-1],"L");
    l2->SetNColumns(2);
    for(unsigned int i=1;i<vHist.size();i++)
    {
        l2->AddEntry(vHist[i], vLegEntry[i],"p");
    }
    l2->SetFillColor(0); //Set the background to be white
    l2->SetLineColor(1);
    l2->Draw("same");
    TLatex* ltx2 = new TLatex();
    ltx2->SetNDC();
    ltx2->SetTextFont(61);
    ltx2->SetTextSize(0.05);
    ltx2->DrawLatex(0.13,0.93,"CMS");
    ltx2->SetTextFont(52);
    ltx2->SetTextSize(0.04);
    if(IsPreliminary==true) ltx2->DrawLatex(0.24,0.93,"Preliminary");
    ltx2->SetTextFont(42);
    ltx2->SetTextSize(0.04);
    if(Year==2017)
        ltx2->DrawLatex(0.63,0.93,Form("%d %.1f fb^{-1} (13TeV)", Year, lumi_2017));
    else if(Year==2018)
        ltx2->DrawLatex(0.63,0.93,Form("%d %.1f fb^{-1} (13TeV)", Year, lumi_2018));
    else
        ltx2->DrawLatex(0.63,0.93,Form("%d %.1f fb^{-1} (13TeV)", Year, lumi_2017));
    c1->SaveAs("plots/CombHist_DiffLooseID_"+VetoOutText[EleVetoSet-1]+".png");
    c1->SaveAs("plots/CombHist_DiffLooseID_"+VetoOutText[EleVetoSet-1]+".pdf");
}

vector<vector<float>> GetSF(int Year, int IDtype, int EleVetoSet)
{
    setTDRStyle();

    int EleVeto_cut;
    if(EleVetoSet==1)
        EleVeto_cut = 0;
    else
        EleVeto_cut = 1;

    TString CatName[6] = {"EB Inclusive", "EB high R9", "EB low R9", "EE Inclusive", "EE high R9", "EE low R9"};

    float count_EBInc[2][5][3] = {0.};
    float count_EEInc[2][5][3] = {0.};
    float count_EBHR9[2][5][3] = {0.};
    float count_EBLR9[2][5][3] = {0.};
    float count_EEHR9[2][5][3] = {0.};
    float count_EELR9[2][5][3] = {0.};

    vector<float> SF_central; SF_central.clear();
    vector<float> uncer_pileup; uncer_pileup.clear();
    vector<float> uncer_stat; uncer_stat.clear();
    vector<float> uncer_generator; uncer_generator.clear();
    vector<float> uncer_background; uncer_background.clear();

    vector<TFile*> vFile; vFile.clear();
    vFile.push_back(new TFile("minitree/minitree_DoubleMu_AllRuns.root","READ"));
    vFile.push_back(new TFile("minitree/minitree_DYJetsToLL_MadGraph.root","READ"));
    vFile.push_back(new TFile("minitree/minitree_DYJetsToLL_aMCatNLO.root","READ"));
    vFile.push_back(new TFile("minitree/minitree_Wjets_aMCatNLO.root","READ"));
    vFile.push_back(new TFile("minitree/minitree_TTTo2L2Nu_powheg.root","READ"));
    vector<float> vmcwei; vmcwei.clear();
    vmcwei.push_back(1.);
    vmcwei.push_back(mcwei_DYJetsToLL_MadGraph);
    vmcwei.push_back(mcwei_DYJetsToLL_aMCatNLO);
    vmcwei.push_back(mcwei_Wjets_aMCatNLO);
    vmcwei.push_back(mcwei_ttbarTo2L2Nu_powheg);

    for(unsigned int iFile=0;iFile<vFile.size();iFile++)
    {
        TTree *Tree  = (TTree*) vFile[iFile]->Get("outTree");
        float phoSCEta, phoR9;
        int presel;
        int passVeto, passID;
        double puwei, puwei_up, puwei_down;
        Tree->SetBranchAddress("phoSCEta", &phoSCEta);
        Tree->SetBranchAddress("phoR9", &phoR9);
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
        {
            puwei=1.;
            puwei_up=1.;
            puwei_down=1.;
        }
        else
        {
            Tree->SetBranchAddress("puwei", &puwei);
            Tree->SetBranchAddress("puwei_up", &puwei_up);
            Tree->SetBranchAddress("puwei_down", &puwei_down);
        }

        for(Long64_t ev=0; ev<Tree->GetEntriesFast(); ev++)
        {
            Tree->GetEntry(ev);

            // All the events should pass photon preselection (medium WP)
            if(presel != 1) continue;
            if(passID!=1) continue;

            if(fabs(phoSCEta)<1.4442)
            {
                count_EBInc[0][iFile][0] = count_EBInc[0][iFile][0] + 1.*puwei*vmcwei[iFile];
                count_EBInc[0][iFile][1] = count_EBInc[0][iFile][1] + 1.*puwei_up*vmcwei[iFile];
                count_EBInc[0][iFile][2] = count_EBInc[0][iFile][2] + 1.*puwei_down*vmcwei[iFile];
                if(fabs(phoSCEta)<1.4442 && phoR9>0.94)
                {
                    count_EBHR9[0][iFile][0] = count_EBHR9[0][iFile][0] + 1.*puwei*vmcwei[iFile];
                    count_EBHR9[0][iFile][1] = count_EBHR9[0][iFile][1] + 1.*puwei_up*vmcwei[iFile];
                    count_EBHR9[0][iFile][2] = count_EBHR9[0][iFile][2] + 1.*puwei_down*vmcwei[iFile];
                }
                else
                {
                    count_EBLR9[0][iFile][0] = count_EBLR9[0][iFile][0] + 1.*puwei*vmcwei[iFile];
                    count_EBLR9[0][iFile][1] = count_EBLR9[0][iFile][1] + 1.*puwei_up*vmcwei[iFile];
                    count_EBLR9[0][iFile][2] = count_EBLR9[0][iFile][2] + 1.*puwei_down*vmcwei[iFile];
                }
            }
            else if(fabs(phoSCEta)>1.566 && fabs(phoSCEta)<2.5)
            {
                count_EEInc[0][iFile][0] = count_EEInc[0][iFile][0] + 1.*puwei*vmcwei[iFile];
                count_EEInc[0][iFile][1] = count_EEInc[0][iFile][1] + 1.*puwei_up*vmcwei[iFile];
                count_EEInc[0][iFile][2] = count_EEInc[0][iFile][2] + 1.*puwei_down*vmcwei[iFile];
                if(fabs(phoSCEta)>1.566 && fabs(phoSCEta)<2.5 && phoR9>0.94)
                {
                    count_EEHR9[0][iFile][0] = count_EEHR9[0][iFile][0] + 1.*puwei*vmcwei[iFile];
                    count_EEHR9[0][iFile][1] = count_EEHR9[0][iFile][1] + 1.*puwei_up*vmcwei[iFile];
                    count_EEHR9[0][iFile][2] = count_EEHR9[0][iFile][2] + 1.*puwei_down*vmcwei[iFile];
                }
                else
                {
                    count_EELR9[0][iFile][0] = count_EELR9[0][iFile][0] + 1.*puwei*vmcwei[iFile];
                    count_EELR9[0][iFile][1] = count_EELR9[0][iFile][1] + 1.*puwei_up*vmcwei[iFile];
                    count_EELR9[0][iFile][2] = count_EELR9[0][iFile][2] + 1.*puwei_down*vmcwei[iFile];
                }
            }
            else
                continue;

            if(passVeto!=EleVeto_cut) continue;

            if(fabs(phoSCEta)<1.4442)
            {
                count_EBInc[1][iFile][0] = count_EBInc[1][iFile][0] + 1.*puwei*vmcwei[iFile];
                count_EBInc[1][iFile][1] = count_EBInc[1][iFile][1] + 1.*puwei_up*vmcwei[iFile];
                count_EBInc[1][iFile][2] = count_EBInc[1][iFile][2] + 1.*puwei_down*vmcwei[iFile];
                if(fabs(phoSCEta)<1.4442 && phoR9>0.94)
                {
                    count_EBHR9[1][iFile][0] = count_EBHR9[1][iFile][0] + 1.*puwei*vmcwei[iFile];
                    count_EBHR9[1][iFile][1] = count_EBHR9[1][iFile][1] + 1.*puwei_up*vmcwei[iFile];
                    count_EBHR9[1][iFile][2] = count_EBHR9[1][iFile][2] + 1.*puwei_down*vmcwei[iFile];
                }
                else
                {
                    count_EBLR9[1][iFile][0] = count_EBLR9[1][iFile][0] + 1.*puwei*vmcwei[iFile];
                    count_EBLR9[1][iFile][1] = count_EBLR9[1][iFile][1] + 1.*puwei_up*vmcwei[iFile];
                    count_EBLR9[1][iFile][2] = count_EBLR9[1][iFile][2] + 1.*puwei_down*vmcwei[iFile];
                }
            }
            else if(fabs(phoSCEta)>1.566 && fabs(phoSCEta)<2.5)
            {
                count_EEInc[1][iFile][0] = count_EEInc[1][iFile][0] + 1.*puwei*vmcwei[iFile];
                count_EEInc[1][iFile][1] = count_EEInc[1][iFile][1] + 1.*puwei_up*vmcwei[iFile];
                count_EEInc[1][iFile][2] = count_EEInc[1][iFile][2] + 1.*puwei_down*vmcwei[iFile];
                if(fabs(phoSCEta)>1.566 && fabs(phoSCEta)<2.5 && phoR9>0.94)
                {
                    count_EEHR9[1][iFile][0] = count_EEHR9[1][iFile][0] + 1.*puwei*vmcwei[iFile];
                    count_EEHR9[1][iFile][1] = count_EEHR9[1][iFile][1] + 1.*puwei_up*vmcwei[iFile];
                    count_EEHR9[1][iFile][2] = count_EEHR9[1][iFile][2] + 1.*puwei_down*vmcwei[iFile];
                }
                else
                {
                    count_EELR9[1][iFile][0] = count_EELR9[1][iFile][0] + 1.*puwei*vmcwei[iFile];
                    count_EELR9[1][iFile][1] = count_EELR9[1][iFile][1] + 1.*puwei_up*vmcwei[iFile];
                    count_EELR9[1][iFile][2] = count_EELR9[1][iFile][2] + 1.*puwei_down*vmcwei[iFile];
                }
            }
            else
                continue;
        }

        for(int ipu=0; ipu<3; ipu++)
        {
            // if(ipu==0)
            // {
            //     cout << iFile << endl;
            //     cout << count_EBInc[0][iFile][ipu] << " " << count_EBInc[1][iFile][ipu] << " " << endl
            //         << count_EEInc[0][iFile][ipu] << " " << count_EEInc[1][iFile][ipu] << " " << endl
            //         << count_EBHR9[0][iFile][ipu] << " " << count_EBHR9[1][iFile][ipu] << " " << endl
            //         << count_EBLR9[0][iFile][ipu] << " " << count_EBLR9[1][iFile][ipu] << " " << endl
            //         << count_EEHR9[0][iFile][ipu] << " " << count_EEHR9[1][iFile][ipu] << " " << endl
            //         << count_EELR9[0][iFile][ipu] << " " << count_EELR9[1][iFile][ipu] << " " << endl;
            // }

            if(ipu==0)
            {
                //Binomial_Error(double eff, double N)
                uncer_stat.push_back((float) Binomial_Error((double) count_EBInc[1][iFile][ipu]/count_EBInc[0][iFile][ipu], (double) count_EBInc[0][iFile][ipu]));
                uncer_stat.push_back((float) Binomial_Error((double) count_EBHR9[1][iFile][ipu]/count_EBHR9[0][iFile][ipu], (double) count_EBHR9[0][iFile][ipu]));
                uncer_stat.push_back((float) Binomial_Error((double) count_EBLR9[1][iFile][ipu]/count_EBLR9[0][iFile][ipu], (double) count_EBLR9[0][iFile][ipu]));
                uncer_stat.push_back((float) Binomial_Error((double) count_EEInc[1][iFile][ipu]/count_EEInc[0][iFile][ipu], (double) count_EEInc[0][iFile][ipu]));
                uncer_stat.push_back((float) Binomial_Error((double) count_EEHR9[1][iFile][ipu]/count_EEHR9[0][iFile][ipu], (double) count_EEHR9[0][iFile][ipu]));
                uncer_stat.push_back((float) Binomial_Error((double) count_EELR9[1][iFile][ipu]/count_EELR9[0][iFile][ipu], (double) count_EELR9[0][iFile][ipu]));

                if(iFile==3 || iFile==4)
                {
                    for(int i=0;i<2;i++)
                    {
                        count_EBInc[i][iFile][ipu] = count_EBInc[i][iFile][ipu] + count_EBInc[i][2][ipu];
                        count_EEInc[i][iFile][ipu] = count_EEInc[i][iFile][ipu] + count_EEInc[i][2][ipu];
                        count_EBHR9[i][iFile][ipu] = count_EBHR9[i][iFile][ipu] + count_EBHR9[i][2][ipu];
                        count_EBLR9[i][iFile][ipu] = count_EBLR9[i][iFile][ipu] + count_EBLR9[i][2][ipu];
                        count_EEHR9[i][iFile][ipu] = count_EEHR9[i][iFile][ipu] + count_EEHR9[i][2][ipu];
                        count_EELR9[i][iFile][ipu] = count_EELR9[i][iFile][ipu] + count_EELR9[i][2][ipu];
                    }
                }
            }
        }
    }

    for(unsigned int iFile=0;iFile<vFile.size();iFile++)
    {
        for(int ipu=0;ipu<3;ipu++)
        {
            count_EBInc[0][iFile][ipu] = count_EBInc[1][iFile][ipu]/count_EBInc[0][iFile][ipu];
            count_EEInc[0][iFile][ipu] = count_EEInc[1][iFile][ipu]/count_EEInc[0][iFile][ipu];
            count_EBHR9[0][iFile][ipu] = count_EBHR9[1][iFile][ipu]/count_EBHR9[0][iFile][ipu];
            count_EBLR9[0][iFile][ipu] = count_EBLR9[1][iFile][ipu]/count_EBLR9[0][iFile][ipu];
            count_EEHR9[0][iFile][ipu] = count_EEHR9[1][iFile][ipu]/count_EEHR9[0][iFile][ipu];
            count_EELR9[0][iFile][ipu] = count_EELR9[1][iFile][ipu]/count_EELR9[0][iFile][ipu];
        }
    }

    //Error_Propagation(double f, double sigmaA, double A, double sigmaB, double B)
    uncer_stat[0] = (float) Error_Propagation((double) count_EBInc[0][0][0]/count_EBInc[0][1][0], (double) uncer_stat[0], (double) count_EBInc[0][0][0], (double) uncer_stat[6], (double) count_EBInc[0][1][0]);
    uncer_stat[1] = (float) Error_Propagation((double) count_EBHR9[0][0][0]/count_EBHR9[0][1][0], (double) uncer_stat[1], (double) count_EBHR9[0][0][0], (double) uncer_stat[7], (double) count_EBHR9[0][1][0]);
    uncer_stat[2] = (float) Error_Propagation((double) count_EBLR9[0][0][0]/count_EBLR9[0][1][0], (double) uncer_stat[2], (double) count_EBLR9[0][0][0], (double) uncer_stat[8], (double) count_EBLR9[0][1][0]);
    uncer_stat[3] = (float) Error_Propagation((double) count_EEInc[0][0][0]/count_EEInc[0][1][0], (double) uncer_stat[3], (double) count_EEInc[0][0][0], (double) uncer_stat[9], (double) count_EEInc[0][1][0]);
    uncer_stat[4] = (float) Error_Propagation((double) count_EEHR9[0][0][0]/count_EEHR9[0][1][0], (double) uncer_stat[4], (double) count_EEHR9[0][0][0], (double) uncer_stat[10], (double) count_EEHR9[0][1][0]);
    uncer_stat[5] = (float) Error_Propagation((double) count_EELR9[0][0][0]/count_EELR9[0][1][0], (double) uncer_stat[5], (double) count_EELR9[0][0][0], (double) uncer_stat[11], (double) count_EELR9[0][1][0]);

    for(int i=2;i<5;i++)
    {
        count_EBInc[0][i][0] = count_EBInc[0][0][0]/count_EBInc[0][i][0];
        count_EEInc[0][i][0] = count_EEInc[0][0][0]/count_EEInc[0][i][0];
        count_EBHR9[0][i][0] = count_EBHR9[0][0][0]/count_EBHR9[0][i][0];
        count_EBLR9[0][i][0] = count_EBLR9[0][0][0]/count_EBLR9[0][i][0];
        count_EEHR9[0][i][0] = count_EEHR9[0][0][0]/count_EEHR9[0][i][0];
        count_EELR9[0][i][0] = count_EELR9[0][0][0]/count_EELR9[0][i][0];
    }

    // for(int i=0;i<5;i++) cout << count_EBInc[0][i][0] << " " << endl;
    // cout << endl;

    for(int ipu=0; ipu<3; ipu++)
    {
        count_EBInc[0][0][ipu] = count_EBInc[0][0][ipu]/count_EBInc[0][1][ipu];
        count_EEInc[0][0][ipu] = count_EEInc[0][0][ipu]/count_EEInc[0][1][ipu]; //cout << count_EBInc[0][0][ipu] << " ";
        count_EBHR9[0][0][ipu] = count_EBHR9[0][0][ipu]/count_EBHR9[0][1][ipu]; //cout << count_EBInc[0][0][ipu] << " ";
        count_EBLR9[0][0][ipu] = count_EBLR9[0][0][ipu]/count_EBLR9[0][1][ipu]; //cout << count_EBInc[0][0][ipu] << " ";
        count_EEHR9[0][0][ipu] = count_EEHR9[0][0][ipu]/count_EEHR9[0][1][ipu]; //cout << count_EBInc[0][0][ipu] << " ";
        count_EELR9[0][0][ipu] = count_EELR9[0][0][ipu]/count_EELR9[0][1][ipu]; //cout << count_EBInc[0][0][ipu] << " " << endl;
        if(ipu==0)
        {
            SF_central.push_back(count_EBInc[0][0][ipu]);
            SF_central.push_back(count_EBHR9[0][0][ipu]);
            SF_central.push_back(count_EBLR9[0][0][ipu]);
            SF_central.push_back(count_EEInc[0][0][ipu]);
            SF_central.push_back(count_EEHR9[0][0][ipu]);
            SF_central.push_back(count_EELR9[0][0][ipu]);
        }
    }

    // for(int i=0;i<5;i++) cout << count_EBInc[0][i][0] << " " << endl;
    // cout << endl;

    for(int i=0;i<6;i++)
    {
        uncer_stat[i] = uncer_stat[i] / SF_central[i];
    }

    uncer_pileup.push_back((fabs(count_EBInc[0][0][1]-count_EBInc[0][0][0])>fabs(count_EBInc[0][0][2]-count_EBInc[0][0][0])) ? fabs(count_EBInc[0][0][1]-count_EBInc[0][0][0])/SF_central[0] : fabs(count_EBInc[0][0][2]-count_EBInc[0][0][0])/SF_central[0]);
    uncer_pileup.push_back((fabs(count_EBHR9[0][0][1]-count_EBHR9[0][0][0])>fabs(count_EBHR9[0][0][2]-count_EBHR9[0][0][0])) ? fabs(count_EBHR9[0][0][1]-count_EBHR9[0][0][0])/SF_central[1] : fabs(count_EBHR9[0][0][2]-count_EBHR9[0][0][0])/SF_central[1]);
    uncer_pileup.push_back((fabs(count_EBLR9[0][0][1]-count_EBLR9[0][0][0])>fabs(count_EBLR9[0][0][2]-count_EBLR9[0][0][0])) ? fabs(count_EBLR9[0][0][1]-count_EBLR9[0][0][0])/SF_central[2] : fabs(count_EBLR9[0][0][2]-count_EBLR9[0][0][0])/SF_central[2]);
    uncer_pileup.push_back((fabs(count_EEInc[0][0][1]-count_EEInc[0][0][0])>fabs(count_EEInc[0][0][2]-count_EEInc[0][0][0])) ? fabs(count_EEInc[0][0][1]-count_EEInc[0][0][0])/SF_central[3] : fabs(count_EEInc[0][0][2]-count_EEInc[0][0][0])/SF_central[3]);
    uncer_pileup.push_back((fabs(count_EEHR9[0][0][1]-count_EEHR9[0][0][0])>fabs(count_EEHR9[0][0][2]-count_EEHR9[0][0][0])) ? fabs(count_EEHR9[0][0][1]-count_EEHR9[0][0][0])/SF_central[4] : fabs(count_EEHR9[0][0][2]-count_EEHR9[0][0][0])/SF_central[4]);
    uncer_pileup.push_back((fabs(count_EELR9[0][0][1]-count_EELR9[0][0][0])>fabs(count_EELR9[0][0][2]-count_EELR9[0][0][0])) ? fabs(count_EELR9[0][0][1]-count_EELR9[0][0][0])/SF_central[5] : fabs(count_EELR9[0][0][2]-count_EELR9[0][0][0])/SF_central[5]);

    uncer_generator.push_back(fabs(count_EBInc[0][2][0]-count_EBInc[0][0][0])/SF_central[0]);
    uncer_generator.push_back(fabs(count_EBHR9[0][2][0]-count_EBHR9[0][0][0])/SF_central[1]);
    uncer_generator.push_back(fabs(count_EBLR9[0][2][0]-count_EBLR9[0][0][0])/SF_central[2]);
    uncer_generator.push_back(fabs(count_EEInc[0][2][0]-count_EEInc[0][0][0])/SF_central[3]);
    uncer_generator.push_back(fabs(count_EEHR9[0][2][0]-count_EEHR9[0][0][0])/SF_central[4]);
    uncer_generator.push_back(fabs(count_EELR9[0][2][0]-count_EELR9[0][0][0])/SF_central[5]);

    uncer_background.push_back((fabs(count_EBInc[0][3][0]-count_EBInc[0][0][0])>fabs(count_EBInc[0][4][0]-count_EBInc[0][0][0])) ? fabs(count_EBInc[0][3][0]-count_EBInc[0][0][0])/SF_central[0] : fabs(count_EBInc[0][4][0]-count_EBInc[0][0][0])/SF_central[0]);
    uncer_background.push_back((fabs(count_EBHR9[0][3][0]-count_EBHR9[0][0][0])>fabs(count_EBHR9[0][4][0]-count_EBHR9[0][0][0])) ? fabs(count_EBHR9[0][3][0]-count_EBHR9[0][0][0])/SF_central[1] : fabs(count_EBHR9[0][4][0]-count_EBHR9[0][0][0])/SF_central[1]);
    uncer_background.push_back((fabs(count_EBLR9[0][3][0]-count_EBLR9[0][0][0])>fabs(count_EBLR9[0][4][0]-count_EBLR9[0][0][0])) ? fabs(count_EBLR9[0][3][0]-count_EBLR9[0][0][0])/SF_central[2] : fabs(count_EBLR9[0][4][0]-count_EBLR9[0][0][0])/SF_central[2]);
    uncer_background.push_back((fabs(count_EEInc[0][3][0]-count_EEInc[0][0][0])>fabs(count_EEInc[0][4][0]-count_EEInc[0][0][0])) ? fabs(count_EEInc[0][3][0]-count_EEInc[0][0][0])/SF_central[3] : fabs(count_EEInc[0][4][0]-count_EEInc[0][0][0])/SF_central[3]);
    uncer_background.push_back((fabs(count_EEHR9[0][3][0]-count_EEHR9[0][0][0])>fabs(count_EEHR9[0][4][0]-count_EEHR9[0][0][0])) ? fabs(count_EEHR9[0][3][0]-count_EEHR9[0][0][0])/SF_central[4] : fabs(count_EEHR9[0][4][0]-count_EEHR9[0][0][0])/SF_central[4]);
    uncer_background.push_back((fabs(count_EELR9[0][3][0]-count_EELR9[0][0][0])>fabs(count_EELR9[0][4][0]-count_EELR9[0][0][0])) ? fabs(count_EELR9[0][3][0]-count_EELR9[0][0][0])/SF_central[5] : fabs(count_EELR9[0][4][0]-count_EELR9[0][0][0])/SF_central[5]);

    ofstream of;
    of.open(Form("table/SFtable_VetoType%d_IDType%d.txt",EleVetoSet,IDtype));
    for(unsigned int i=0;i<SF_central.size();i++)
    {
        of << CatName[i] << endl
        << "Central-value " << "Pile-up " << "Statistical " << "Generator " << "Background " << "Total " << endl
        << SF_central[i] << " " << uncer_pileup[i] << " " << uncer_stat[i] << " " << uncer_generator[i] << " " << uncer_background[i] << " "
        << sqrt(uncer_pileup[i]*uncer_pileup[i]+uncer_stat[i]*uncer_stat[i]+uncer_generator[i]*uncer_generator[i]+uncer_background[i]*uncer_background[i]) << endl;
    }
    of.close();

    vector<vector<float>> rvector; rvector.clear();
    rvector.push_back(SF_central);
    rvector.push_back(uncer_pileup);
    rvector.push_back(uncer_stat);
    rvector.push_back(uncer_generator);
    rvector.push_back(uncer_background);

    SF_central.clear(); uncer_pileup.clear(); uncer_stat.clear(); uncer_generator.clear(); uncer_background.clear();

    return rvector;
}

void MakeCombHist()
{
    vector<TString> IDName{"Loose ID", "Medium ID", "Tight ID", "MVA ID"};
    vector<TString> VetoName{"Pixel seed veto", "CSEV"};
    vector<TString> BinLabel{"EB Inc.", "EB high R_{9}", "EB low R_{9}", "EE Inc.", "EE high R_{9}", "EE low R_{9}"};
    vector<TH1F*> hM_SF; hM_SF.clear();
    vector<TH1F*> hM_MVAratio; hM_MVAratio.clear();

    for(unsigned int iVeto=0; iVeto<VetoName.size(); iVeto++)
    {
        hM_SF.clear();
        hM_MVAratio.clear();
        for(unsigned int iID=0; iID<IDName.size(); iID++)
        {
            //vector<vector<float>> GetSF(int Year, int IDtype, int EleVetoSet)
            vector<vector<float>> tmpvec; tmpvec.clear();
            tmpvec = GetSF(2017,iID+1,iVeto+1);

            hM_SF.push_back(new TH1F("hM_SF","",(int) BinLabel.size(),0, (int) BinLabel.size()));
            for(unsigned int iBin=0; iBin<BinLabel.size();iBin++)
            {
                hM_SF[iID]->SetBinContent(iBin+1, (double) tmpvec[0][iBin]);
                hM_SF[iID]->SetBinError(iBin+1, (double) sqrt(tmpvec[1][iBin]*tmpvec[1][iBin]+tmpvec[2][iBin]*tmpvec[2][iBin]+tmpvec[3][iBin]*tmpvec[3][iBin]+tmpvec[4][iBin]*tmpvec[4][iBin]));
                hM_SF[iID]->GetXaxis()->SetBinLabel(iBin+1, BinLabel[iBin]);
            }
            tmpvec.clear();
        }

        for(int i=0;i<3;i++)
        {
            TH1F* hM_ratio;
            hM_ratio = (TH1F*) hM_SF[i]->Clone();
            hM_ratio->Divide(hM_SF[3]);
            for(unsigned int iBin=0; iBin<BinLabel.size();iBin++)
            {
                //Error_Propagation(double f, double sigmaA, double A, double sigmaB, double B)
                hM_ratio->SetBinError(iBin+1, Error_Propagation(hM_ratio->GetBinContent(iBin+1),hM_SF[i]->GetBinError(iBin+1),hM_SF[i]->GetBinContent(iBin+1),hM_SF[3]->GetBinError(iBin+1),hM_SF[3]->GetBinContent(iBin+1)));
            }
            hM_MVAratio.push_back(hM_ratio);
        }
        //DrawHist(int Year, int EleVetoSet, vector<TH1F*> vHist, vector<TH1F*> vHist_ratio, vector<TString> vLegEntry, TString outname)
        DrawHist(2017, iVeto+1, hM_SF, hM_MVAratio, IDName);
    }
}
