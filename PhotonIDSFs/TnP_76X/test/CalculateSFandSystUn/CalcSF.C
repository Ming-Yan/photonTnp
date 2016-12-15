double err( double n, double d, double err_n, double err_d){

  double err = (n/d)*sqrt( pow(err_n/n,2) + pow(err_d/d, 2) );

  return err;

}

double Sqr(double in){
  return in*in;
}

float Sqr(float in){
  return in*in;
}

double Max(double in1, double in2){
  if (in1>in2) return in1;
  if (in1<=in2) return in2;
}


void Calc(double SF[32], double SF_err[32], int IDtype=0, int type=0){

  string ID;
  string ty_Data, ty_MC;

  if (IDtype == 0) ID = "Loose";
  if (IDtype == 1) ID = "Medium";
  if (IDtype == 2) ID = "Tight";
  if (IDtype == 3) ID = "MVA";

  if (type == 0) ty_Data = ""; // baseline
  if (type == 1) ty_Data = "_35pTCut"; // 35pTCut
  if (type == 2) ty_Data = "_BGSys"; // BG fit function
  if (type == 3) ty_Data = "_Signal"; // Signal fit function
  if (type == 4) ty_Data = "_fitRange"; // fitting Range
  if (type == 5) ty_Data = "_MG"; //madgraph
  if (type == 6) ty_Data = "_PU72450"; // PU
  if (type == 7) ty_Data = "_PU65550"; // PU

  if (type == 0) ty_MC = ""; // baseline
  if (type == 1) ty_MC = "_35pTCut"; // 35pTCut
  if (type == 2) ty_MC = ""; // BG fit function
  if (type == 3) ty_MC = ""; // Signal fit function
  if (type == 4) ty_MC = ""; // fitting Range
  if (type == 5) ty_MC = "_MG"; //madgraph
  if (type == 6) ty_MC = "_PU72450"; // PU
  if (type == 7) ty_MC = "_PU65550"; // PU

  ifstream datafile;
  datafile.open("passing"+ID+ty_Data+".txt");

  ifstream mcfile;
  mcfile.open("passing"+ID+"_MC"+ty_MC+".txt");


  for(int i=0 ; i< 32 ; ++i){

    double detamin, detamax, dptmin, dptmax, deff, derr;
    double mcetamin, mcetamax, mcptmin, mcptmax, mceff, mcerr;

    //datafile>>detamin>>detamax>>dptmin>>dptmax>>deff>>derr;                                                                               
    datafile>>dptmin>>dptmax>>detamin>>detamax>>deff>>derr;
    //cout<<"DATA === "<<detamin<<"  "<<detamax<<"  "<<dptmin<<"  "<<dptmax<<"  "<<deff<<"  "<<derr<<endl;

    //mcfile>>mcetamin>>mcetamax>>mcptmin>>mcptmax>>mceff>>mcerr;                                                                           
    mcfile>>mcptmin>>mcptmax>>mcetamin>>mcetamax>>mceff>>mcerr;
    //cout<<"MC===="<<mcetamin<<"  "<<mcetamax<<"  "<<mcptmin<<"  "<<mcptmax<<"  "<<mceff<<"  "<<mcerr<<endl;

    SF[i] = deff/mceff;
    SF_err[i] = err(deff, mceff, derr, mcerr);
  }


} // end of function

void CalcSF(){


  Double_t SF_Loose_baseline[32], SF_Loose_baseline_err[32];
  Calc(SF_Loose_baseline, SF_Loose_baseline_err, 0, 0);
  Double_t SF_Medium_baseline[32], SF_Medium_baseline_err[32];
  Calc(SF_Medium_baseline, SF_Medium_baseline_err, 1, 0);
  Double_t SF_Tight_baseline[32], SF_Tight_baseline_err[32];
  Calc(SF_Tight_baseline, SF_Tight_baseline_err, 2, 0);
  Double_t SF_MVA_baseline[32], SF_MVA_baseline_err[32];
  Calc(SF_MVA_baseline, SF_MVA_baseline_err, 3, 0);

  Double_t SF_Loose_35pTCut[32], SF_Loose_35pTCut_err[32];
  Calc(SF_Loose_35pTCut, SF_Loose_35pTCut_err, 0, 1);
  Double_t SF_Medium_35pTCut[32], SF_Medium_35pTCut_err[32];
  Calc(SF_Medium_35pTCut, SF_Medium_35pTCut_err, 1, 1);
  Double_t SF_Tight_35pTCut[32], SF_Tight_35pTCut_err[32];
  Calc(SF_Tight_35pTCut, SF_Tight_35pTCut_err, 2, 1);
  Double_t SF_MVA_35pTCut[32], SF_MVA_35pTCut_err[32];
  Calc(SF_MVA_35pTCut, SF_MVA_35pTCut_err, 3, 1);

  Double_t SF_Loose_BGSys[32], SF_Loose_BGSys_err[32];
  Calc(SF_Loose_BGSys, SF_Loose_BGSys_err, 0, 2);
  Double_t SF_Medium_BGSys[32], SF_Medium_BGSys_err[32];
  Calc(SF_Medium_BGSys, SF_Medium_BGSys_err, 1, 2);
  Double_t SF_Tight_BGSys[32], SF_Tight_BGSys_err[32];
  Calc(SF_Tight_BGSys, SF_Tight_BGSys_err, 2, 2);
  Double_t SF_MVA_BGSys[32], SF_MVA_BGSys_err[32];
  Calc(SF_MVA_BGSys, SF_MVA_BGSys_err, 3, 2);
  
  Double_t SF_Loose_Signal[32], SF_Loose_Signal_err[32];
  Calc(SF_Loose_Signal, SF_Loose_Signal_err, 0, 3);
  Double_t SF_Medium_Signal[32], SF_Medium_Signal_err[32];
  Calc(SF_Medium_Signal, SF_Medium_Signal_err, 1, 3);
  Double_t SF_Tight_Signal[32], SF_Tight_Signal_err[32];
  Calc(SF_Tight_Signal, SF_Tight_Signal_err, 2, 3);
  Double_t SF_MVA_Signal[32], SF_MVA_Signal_err[32];
  Calc(SF_MVA_Signal, SF_MVA_Signal_err, 3, 3);

  Double_t SF_Loose_fitRange[32], SF_Loose_fitRange_err[32];
  Calc(SF_Loose_fitRange, SF_Loose_fitRange_err, 0, 4);
  Double_t SF_Medium_fitRange[32], SF_Medium_fitRange_err[32];
  Calc(SF_Medium_fitRange, SF_Medium_fitRange_err, 1, 4);
  Double_t SF_Tight_fitRange[32], SF_Tight_fitRange_err[32];
  Calc(SF_Tight_fitRange, SF_Tight_fitRange_err, 2, 4);
  Double_t SF_MVA_fitRange[32], SF_MVA_fitRange_err[32];
  Calc(SF_MVA_fitRange, SF_MVA_fitRange_err, 3, 4);

  Double_t SF_Loose_MG[32], SF_Loose_MG_err[32];
  Calc(SF_Loose_MG, SF_Loose_MG_err, 0, 5);
  Double_t SF_Medium_MG[32], SF_Medium_MG_err[32];
  Calc(SF_Medium_MG, SF_Medium_MG_err, 1, 5);
  Double_t SF_Tight_MG[32], SF_Tight_MG_err[32];
  Calc(SF_Tight_MG, SF_Tight_MG_err, 2, 5);
  Double_t SF_MVA_MG[32], SF_MVA_MG_err[32];
  Calc(SF_MVA_MG, SF_MVA_MG_err, 3, 5);

  Double_t SF_Loose_PU65550[32], SF_Loose_PU65550_err[32];
  Calc(SF_Loose_PU65550, SF_Loose_PU65550_err, 0, 6);
  Double_t SF_Medium_PU65550[32], SF_Medium_PU65550_err[32];
  Calc(SF_Medium_PU65550, SF_Medium_PU65550_err, 1, 6);
  Double_t SF_Tight_PU65550[32], SF_Tight_PU65550_err[32];
  Calc(SF_Tight_PU65550, SF_Tight_PU65550_err, 2, 6);
  Double_t SF_MVA_PU65550[32], SF_MVA_PU65550_err[32];
  Calc(SF_MVA_PU65550, SF_MVA_PU65550_err, 3, 6);

  Double_t SF_Loose_PU72450[32], SF_Loose_PU72450_err[32];
  Calc(SF_Loose_PU72450, SF_Loose_PU72450_err, 0, 7);
  Double_t SF_Medium_PU72450[32], SF_Medium_PU72450_err[32];
  Calc(SF_Medium_PU72450, SF_Medium_PU72450_err, 1, 7);
  Double_t SF_Tight_PU72450[32], SF_Tight_PU72450_err[32];
  Calc(SF_Tight_PU72450, SF_Tight_PU72450_err, 2, 7);
  Double_t SF_MVA_PU72450[32], SF_MVA_PU72450_err[32];
  Calc(SF_MVA_PU72450, SF_MVA_PU72450_err, 3, 7);


  Double_t Systematic_Loose[32], Systematic_Medium[32], Systematic_Tight[32], Systematic_MVA[32];
  Double_t SF_Loose_PU[32], SF_Medium_PU[32], SF_Tight_PU[32], SF_MVA_PU[32];

  for(int i=0 ; i<32 ; ++i) {

    SF_Loose_PU[i] = Max(SF_Loose_baseline[i]-SF_Loose_PU65550[i], SF_Loose_baseline[i]-SF_Loose_PU72450[i]);
    SF_Medium_PU[i] = Max(SF_Medium_baseline[i]-SF_Medium_PU65550[i], SF_Medium_baseline[i]-SF_Medium_PU72450[i]);
    SF_Tight_PU[i] = Max(SF_Tight_baseline[i]-SF_Tight_PU65550[i], SF_Tight_baseline[i]-SF_Tight_PU72450[i]);
    SF_MVA_PU[i] = Max(SF_MVA_baseline[i]-SF_MVA_PU65550[i], SF_MVA_baseline[i]-SF_MVA_PU72450[i]);

    Systematic_Loose[i]=sqrt(
			     pow(fabs(SF_Loose_baseline[i]-SF_Loose_35pTCut[i]), 2)+
			     pow(fabs(SF_Loose_baseline[i]-SF_Loose_BGSys[i]), 2)+
			     pow(fabs(SF_Loose_baseline[i]-SF_Loose_Signal[i]), 2)+
			     pow(fabs(SF_Loose_baseline[i]-SF_Loose_fitRange[i]), 2)+
			     pow(fabs(SF_Loose_baseline[i]-SF_Loose_MG[i]), 2)+
			     pow(fabs(SF_Loose_PU[i]), 2)
			     );

    /*
    cout<<endl<<endl;
    cout<<fabs(SF_Loose_baseline[i]-SF_Loose_35pTCut[i])<<endl;
    cout<<fabs(SF_Loose_baseline[i]-SF_Loose_BGSys[i])<<endl;
    cout<<fabs(SF_Loose_baseline[i]-SF_Loose_Signal[i])<<endl;
    cout<<fabs(SF_Loose_baseline[i]-SF_Loose_fitRange[i])<<endl;
    cout<<fabs(SF_Loose_baseline[i]-SF_Loose_MG[i])<<endl;
    cout<<fabs(SF_Loose_PU[i])<<endl;

    cout<<endl<<endl;
    */

    Systematic_Medium[i]=sqrt(
			      Sqr(SF_Medium_baseline[i]-SF_Medium_35pTCut[i])+
			      Sqr(SF_Medium_baseline[i]-SF_Medium_BGSys[i])+
			      Sqr(SF_Medium_baseline[i]-SF_Medium_Signal[i])+
			      Sqr(SF_Medium_baseline[i]-SF_Medium_fitRange[i])+
			      Sqr(SF_Medium_baseline[i]-SF_Medium_MG[i])+
			      Sqr(SF_Medium_PU[i])
			      );
    Systematic_Tight[i]=sqrt(
                             Sqr(SF_Tight_baseline[i]-SF_Tight_35pTCut[i])+
                             Sqr(SF_Tight_baseline[i]-SF_Tight_BGSys[i])+
                             Sqr(SF_Tight_baseline[i]-SF_Tight_Signal[i])+
                             Sqr(SF_Tight_baseline[i]-SF_Tight_fitRange[i])+
                             Sqr(SF_Tight_baseline[i]-SF_Tight_MG[i])+
                             Sqr(SF_Tight_PU[i])
                             );
    Systematic_MVA[i]=sqrt(
			   Sqr(SF_MVA_baseline[i]-SF_MVA_35pTCut[i])+
			   Sqr(SF_MVA_baseline[i]-SF_MVA_BGSys[i])+
			   Sqr(SF_MVA_baseline[i]-SF_MVA_Signal[i])+
			   Sqr(SF_MVA_baseline[i]-SF_MVA_fitRange[i])+
			   Sqr(SF_MVA_baseline[i]-SF_MVA_MG[i])+
			   Sqr(SF_MVA_PU[i])
			   );

  }


  cout<<"Loose ID, Stat error"<<endl;
  for (int i=0 ; i< 32 ; ++i) { if (i==1 || i==6 || i==9 || i==14 || i==17 || i==22 || i==25 || i==30) continue;
    cout<<SF_Loose_baseline_err[i]<<endl;}

  cout<<"Medium ID, Statistic error"<<endl;
  for (int i=0 ; i< 32 ; ++i) {if (i==1 || i==6 || i==9 || i==14 || i==17 || i==22 || i==25 || i==30) continue;
    cout<<SF_Medium_baseline_err[i]<<endl;}

  cout<<"Tight ID, Statistic error"<<endl;
  for (int i=0 ; i< 32 ; ++i) {if (i==1 || i==6 || i==9 || i==14 || i==17 || i==22 || i==25 || i==30) continue;
    cout<<SF_Tight_baseline_err[i]<<endl;}

  cout<<"MVA ID, Statistic error"<<endl;
  for (int i=0 ; i< 32 ; ++i) {if (i==1 || i==6 || i==9 || i==14 || i==17 || i==22 || i==25 || i==30) continue;
    cout<<SF_MVA_baseline_err[i]<<endl;}


  cout<<"Loose ID, Systematic Uncertainty"<<endl;
  for (int i=0 ; i< 32 ; ++i) { if (i==1 || i==6 || i==9 || i==14 || i==17 || i==22 || i==25 || i==30) continue;
    cout<<Systematic_Loose[i]<<endl;}

  cout<<"Medium ID, Systematic Uncertainty"<<endl;
  for (int i=0 ; i< 32 ; ++i) {if (i==1 || i==6 || i==9 || i==14 || i==17 || i==22 || i==25 || i==30) continue;
    cout<<Systematic_Medium[i]<<endl;}

  cout<<"Tight ID, Systematic Uncertainty"<<endl;
  for (int i=0 ; i< 32 ; ++i) {if (i==1 || i==6 || i==9 || i==14 || i==17 || i==22 || i==25 || i==30) continue;
    cout<<Systematic_Tight[i]<<endl;}

  cout<<"MVA ID, Systematic Uncertainty"<<endl;
  for (int i=0 ; i< 32 ; ++i) {if (i==1 || i==6 || i==9 || i==14 || i==17 || i==22 || i==25 || i==30) continue;
    cout<<Systematic_MVA[i]<<endl;}



  cout<<"Loose ID, pT35Cut"<<endl;
  for(int i=0 ; i<32 ; ++i) {if (i==1 || i==6 || i==9 || i==14 || i==17 || i==22 || i==25 || i==30) continue;
    cout<<fabs(SF_Loose_baseline[i]-SF_Loose_35pTCut[i])<<endl;}

  cout<<"Medium ID, pT35Cut"<<endl;
  for(int i=0 ; i<32 ; ++i) {if (i==1 || i==6 || i==9 || i==14 || i==17 || i==22 || i==25 || i==30) continue;
    cout<<fabs(SF_Medium_baseline[i]-SF_Medium_35pTCut[i])<<endl;}

  cout<<"Tight ID, pT35Cut"<<endl;
  for(int i=0 ; i<32 ; ++i) {if (i==1 || i==6 || i==9 || i==14 || i==17 || i==22 || i==25 || i==30) continue;
    cout<<fabs(SF_Tight_baseline[i]-SF_Tight_35pTCut[i])<<endl;}

  cout<<"MVA ID, pT35Cut"<<endl;
  for(int i=0 ; i<32 ; ++i) {if (i==1 || i==6 || i==9 || i==14 || i==17 || i==22 || i==25 || i==30) continue;
    cout<<fabs(SF_MVA_baseline[i]-SF_MVA_35pTCut[i])<<endl;}


  cout<<"Loose ID, BGSys"<<endl;
  for(int i=0 ; i<32 ; ++i) {if (i==1 || i==6 || i==9 || i==14 || i==17 || i==22 || i==25 || i==30) continue;
    cout<<fabs(SF_Loose_baseline[i]-SF_Loose_BGSys[i])<<endl;}

  cout<<"Medium ID, BGSys"<<endl;
  for(int i=0 ; i<32 ; ++i) {if (i==1 || i==6 || i==9 || i==14 || i==17 || i==22 || i==25 || i==30) continue;
    cout<<fabs(SF_Medium_baseline[i]-SF_Medium_BGSys[i])<<endl;}

  cout<<"Tight ID, BGSys"<<endl;
  for(int i=0 ; i<32 ; ++i) {if (i==1 || i==6 || i==9 || i==14 || i==17 || i==22 || i==25 || i==30) continue;
    cout<<fabs(SF_Tight_baseline[i]-SF_Tight_BGSys[i])<<endl;}

  cout<<"MVA ID, BGSys"<<endl;
  for(int i=0 ; i<32 ; ++i) {if (i==1 || i==6 || i==9 || i==14 || i==17 || i==22 || i==25 || i==30) continue;
    cout<<fabs(SF_MVA_baseline[i]-SF_MVA_BGSys[i])<<endl;}



  cout<<"Loose ID, Signal"<<endl;
  for(int i=0 ; i<32 ; ++i) {if (i==1 || i==6 || i==9 || i==14 || i==17 || i==22 || i==25 || i==30) continue;
    cout<<fabs(SF_Loose_baseline[i]-SF_Loose_Signal[i])<<endl;}

  cout<<"Medium ID, Signal"<<endl;
  for(int i=0 ; i<32 ; ++i) {if (i==1 || i==6 || i==9 || i==14 || i==17 || i==22 || i==25 || i==30) continue;
    cout<<fabs(SF_Medium_baseline[i]-SF_Medium_Signal[i])<<endl;}

  cout<<"Tight ID, Signal"<<endl;
  for(int i=0 ; i<32 ; ++i) {if (i==1 || i==6 || i==9 || i==14 || i==17 || i==22 || i==25 || i==30) continue;
    cout<<fabs(SF_Tight_baseline[i]-SF_Tight_Signal[i])<<endl;}

  cout<<"MVA ID, Signal"<<endl;
  for(int i=0 ; i<32 ; ++i) {if (i==1 || i==6 || i==9 || i==14 || i==17 || i==22 || i==25 || i==30) continue;
    cout<<fabs(SF_MVA_baseline[i]-SF_MVA_Signal[i])<<endl;}


  cout<<"Loose ID, fitRange"<<endl;
  for(int i=0 ; i<32 ; ++i) {if (i==1 || i==6 || i==9 || i==14 || i==17 || i==22 || i==25 || i==30) continue;
    cout<<fabs(SF_Loose_baseline[i]-SF_Loose_fitRange[i])<<endl;}

  cout<<"Medium ID, fitRange"<<endl;
  for(int i=0 ; i<32 ; ++i) {if (i==1 || i==6 || i==9 || i==14 || i==17 || i==22 || i==25 || i==30) continue;
    cout<<fabs(SF_Medium_baseline[i]-SF_Medium_fitRange[i])<<endl;}

  cout<<"Tight ID, fitRange"<<endl;
  for(int i=0 ; i<32 ; ++i) {if (i==1 || i==6 || i==9 || i==14 || i==17 || i==22 || i==25 || i==30) continue;
    cout<<fabs(SF_Tight_baseline[i]-SF_Tight_fitRange[i])<<endl;}

  cout<<"MVA ID, fitRange"<<endl;
  for(int i=0 ; i<32 ; ++i) {if (i==1 || i==6 || i==9 || i==14 || i==17 || i==22 || i==25 || i==30) continue;
    cout<<fabs(SF_MVA_baseline[i]-SF_MVA_fitRange[i])<<endl;}


  cout<<"Loose ID, MG"<<endl;
  for(int i=0 ; i<32 ; ++i) {if (i==1 || i==6 || i==9 || i==14 || i==17 || i==22 || i==25 || i==30) continue;
    cout<<fabs(SF_Loose_baseline[i]-SF_Loose_MG[i])<<endl;}

  cout<<"Medium ID, MG"<<endl;
  for(int i=0 ; i<32 ; ++i) {if (i==1 || i==6 || i==9 || i==14 || i==17 || i==22 || i==25 || i==30) continue;
    cout<<fabs(SF_Medium_baseline[i]-SF_Medium_MG[i])<<endl;}

  cout<<"Tight ID, MG"<<endl;
  for(int i=0 ; i<32 ; ++i) {if (i==1 || i==6 || i==9 || i==14 || i==17 || i==22 || i==25 || i==30) continue;
    cout<<fabs(SF_Tight_baseline[i]-SF_Tight_MG[i])<<endl;}

  cout<<"MVA ID, MG"<<endl;
  for(int i=0 ; i<32 ; ++i) {if (i==1 || i==6 || i==9 || i==14 || i==17 || i==22 || i==25 || i==30) continue;
    cout<<fabs(SF_MVA_baseline[i]-SF_MVA_MG[i])<<endl;}



  cout<<"Loose ID, PU"<<endl;
  for(int i=0 ; i<32 ; ++i) {if (i==1 || i==6 || i==9 || i==14 || i==17 || i==22 || i==25 || i==30) continue;
    cout<<fabs(SF_Loose_PU[i])<<endl;}

  cout<<"Medium ID, PU"<<endl;
  for(int i=0 ; i<32 ; ++i) {if (i==1 || i==6 || i==9 || i==14 || i==17 || i==22 || i==25 || i==30) continue;
    cout<<fabs(SF_Medium_PU[i])<<endl;}

  cout<<"Tight ID, PU"<<endl;
  for(int i=0 ; i<32 ; ++i) {if (i==1 || i==6 || i==9 || i==14 || i==17 || i==22 || i==25 || i==30) continue;
    cout<<fabs(SF_Tight_PU[i])<<endl;}

  cout<<"MVA ID, PU"<<endl;
  for(int i=0 ; i<32 ; ++i) {if (i==1 || i==6 || i==9 || i==14 || i==17 || i==22 || i==25 || i==30) continue;
    cout<<fabs(SF_MVA_PU[i])<<endl;}


} // end of macro
