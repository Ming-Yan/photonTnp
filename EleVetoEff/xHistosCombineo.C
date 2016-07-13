#include "tdrstyle.C"
#include "CMS_lumi.C"

void xHistosCombineo(TString fname="Loose", TString region="EB", TString hname="Muu", TString xname = "x", Int_t legStyle=0, Int_t logy=0, Int_t logx=0) {
	//TString hname = "Muug"; TString yname = "Events"; TString xname = "M_{#mu#mu#gamma}"; Int_t legStyle = 0; Int_t logy = 0; Int_t logx = 0;
	TString yname = "Events";
	//if (hname == "MuugMuu") yname = "M_{#mu#mu}";
	setTDRStyle();

	TFile *f = new TFile("../plots" + fname + region + ".root");

	TH1F  *hs, *hd;
	TString shname = "s" + hname;
	//TH1F  *hMC = new TH1F();
	hs = (TH1F*)f->Get(shname);
	hd = (TH1F*)f->Get(hname);

	hd->Sumw2();
	hs->Sumw2();

	double L = (17731437.060 + 2672070967.096) / (1000. * 1000. * 1000.);
	hs->Scale((6025.2 * 1000.)*L / 19259725.);

	//hs->Scale(1. / hs->Integral(-1, -1));
	//hd->Scale(1. / hd->Integral(-1, -1));
	TH1F *hRatio = (TH1F*)hd->Clone();
	hRatio->SetDirectory(0);
	//hRatio->Scale(1. / hRatio->Integral(-1, -1));
	hRatio->Divide(hs);
	//hRatio->Sumw2();

	TCanvas *c = new TCanvas("c", "c", 750, 750);

	TPad *pad1 = new TPad("pad1", "pad1", 0, 0.25, 1, 1.0);
	pad1->SetTopMargin(0.07);
	pad1->SetBottomMargin(0.01);
	pad1->Draw();
	pad1->cd();
	pad1->SetLogx(logx);
	pad1->SetLogy(logy);
	hs->GetYaxis()->SetTitleOffset(1.2);
	hs->GetYaxis()->SetTitle(yname);
	//hs->SetMinimum(0.0001);
	//hd->SetMinimum(0.0001);
	hd->GetXaxis()->SetLabelSize(0);
	hd->GetYaxis()->SetTitleOffset(1.2);
	hd->GetYaxis()->SetTitle(yname);
	hd->SetMarkerStyle(20);
	hd->SetMarkerSize(1);
	hd->SetMarkerColor(1);
	hd->SetLineColor(1);
	hd->Draw();
	if (hs->GetMaximum() > hd->GetMaximum()){
		hs->Draw("hist");
		hd->Draw("psame");
	}
	else {
		hd->Draw("p");
		hs->Draw("histsame");
	}
	TLegend *leg;
	if (legStyle == 0) leg = new TLegend(0.3, 0.7, 0.5, 0.9);
	if (legStyle == 1) leg = new TLegend(0.75, 0.5, 0.9, 0.9);
	if (legStyle == 2) leg = new TLegend(0.75, 0.7, 0.9, 0.85);
	leg->AddEntry(hd, "Data", "pl");
	leg->AddEntry(hs, "MC", "f");
	leg->SetBorderSize(0);
	leg->SetFillColor(0);
	leg->Draw();

	c->cd();
	TPad *pad2 = new TPad("pad2", "pad2", 0, 0.0, 1, 0.25);
	pad2->SetTopMargin(0.0);
	pad2->SetBottomMargin(0.35);
	pad2->SetGridy();
	pad2->Draw();
	pad2->cd();
	pad2->SetLogx(logx);
	hRatio->SetMaximum(2);
 	hRatio->SetMinimum(0);
	hRatio->SetTitle("");
	hRatio->GetXaxis()->SetTitle(xname);
	hRatio->GetYaxis()->SetTitle("Data/MC");
	hRatio->GetYaxis()->SetNdivisions(505);
	hRatio->GetXaxis()->SetTickLength(0.05);
	hRatio->GetXaxis()->SetTitleSize(0.06 * 2.6);
	hRatio->GetYaxis()->SetTitleSize(0.06 * 2.6);
	hRatio->GetXaxis()->SetLabelSize(0.05 * 2.6);
	hRatio->GetYaxis()->SetLabelSize(0.03 * 2.6);
	hRatio->GetXaxis()->SetTitleOffset(1.0);
	hRatio->GetYaxis()->SetTitleOffset(1.1 / 2.5);
	hRatio->SetMarkerStyle(20);
	hRatio->Draw("pe");

	CMS_lumi(pad1, 4, 0);

	pad1->Update();
	pad1->RedrawAxis();
	pad1->GetFrame()->Draw();

	c->Print("../kplots/hist" + hname + fname + region + ".pdf");
	c->Print("../kplots/hist" + hname + fname + region + ".png");
}
