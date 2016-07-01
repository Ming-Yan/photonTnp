double err( double n, double d, double err_n, double err_d){

  //double err = (n/d)*sqrt( pow(err_n/n,2) + pow(err_d/d, 2) );

  //double err = (d/(n+d))*sqrt( pow(err_n/n,2) + pow(err_d/d, 2) );
  double err = (d/(n+d))*err_d/d;


  return err;

}

#include "TGraphAsymmErrors.h"
#include <math.h>

void getMCeff( string mcFname="templatesLoose_test.root", string effType="loose"){
//void getMCeff( string mcFname="templatesMedium_PU72450.root", string effType="medium"){
//void getMCeff( string mcFname="templatesTight_PU72450.root", string effType="tight"){
//void getMCeff( string mcFname="templatesMVA_PU72450.root", string effType="mva"){
    
  //50.0  200.0   -1.5660   -1.4442  0.0000   0.0000
  //hMass_30.0To40.0_-1.4442To-1.0_Pass


  ifstream outfile;
  //outfile.open( "passing"+effType+".txt");



  const int nPtbins = 4;

  const int nEtabins = 8;

  double ptbins[nPtbins+1] = {20, 30, 40, 50, 200};
  string sptbins[nPtbins] = {"20.0To30.0",
			     "30.0To40.0",
			     "40.0To50.0",
			     "50.0To200.0",
  };

  double etabins[nEtabins+1] = {-2.5, -1.566, -1.4442, -1.0, 0.0, 1.0, 1.4442, 1.566, 2.5};
  
  string setabins[nEtabins] = {
    "-2.5To-1.566",
    "-1.566To-1.4442",
    "-1.4442To-1.0",
    "-1.0To0.0",
    "0.0To1.0",
    "1.0To1.4442",
    "1.4442To1.566",
    "1.566To2.5"

    //    "-1.4442To-1.0"
			      

  };


  TH1F *hpass[nPtbins][nEtabins];
  TH1F *hfail[nPtbins][nEtabins];
  
  TFile *f = TFile::Open( mcFname.c_str() );
  

  double eff[nPtbins][nEtabins];

  Int_t BinNum=0;

  TH1F* h_Npass = new TH1F("h_Npass", "h_Npass", 36, 0, 36);
  TH1F* h_Ntot = new TH1F("h_Ntot", "h_Ntot", 36, 0, 36);

  for(int ipt=0; ipt<nPtbins; ipt++){

    for(int ieta=0; ieta<nEtabins; ieta++){
  
      hpass[ipt][ieta] = (TH1F*)f->Get( ("hMass_"+sptbins[ipt]+"_"+setabins[ieta]+"_Pass").c_str() );
      hfail[ipt][ieta] = (TH1F*)f->Get( ("hMass_"+sptbins[ipt]+"_"+setabins[ieta]+"_Fail").c_str() );

      double npass = hpass[ipt][ieta]->Integral();
      double nfail = hfail[ipt][ieta]->Integral();
      double ntot = nfail+npass;
      BinNum++;

      h_Npass->SetBinContent(BinNum, npass);
      h_Ntot->SetBinContent(BinNum, nfail+ntot);

      eff[ipt][ieta] = npass/ntot;
      //double efferr = err( npass , nfail, sqrt(npass), sqrt(nfail) );
      
      //cout<<fixed<<setprecision(4)
      // <<ptbins[ipt]<<"  "<<ptbins[ipt+1]<<"  "<<etabins[ieta]<<"  "<<etabins[ieta+1]<<"  "<<eff[ipt][ieta]<<"  "<<efferr<<endl;
      
    }
    
  }

  TGraphAsymmErrors* effResult = new TGraphAsymmErrors();
  effResult->BayesDivide(h_Npass, h_Ntot);

  double efferr, erryhigh, errylow;
  BinNum=0;

  for(int ipt=0; ipt<nPtbins; ipt++){
    for(int ieta=0; ieta<nEtabins; ieta++){
      efferr=0;
      erryhigh=effResult->GetErrorYhigh(BinNum);
      errylow=effResult->GetErrorYlow(BinNum);
      efferr=max(erryhigh, errylow);
      BinNum++;
     
	cout<<fixed<<setprecision(4)
          <<ptbins[ipt]<<"  "<<ptbins[ipt+1]<<"  "<<etabins[ieta]<<"  "<<etabins[ieta+1]<<"  "<<eff[ipt][ieta]<<"  "<<efferr<<endl;
    }
  }

  //outfile.close();  
}
